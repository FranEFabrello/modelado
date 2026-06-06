from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
import streamlit as st
import sympy as sp
from scipy.integrate import solve_ivp
from scipy.linalg import expm


EXAMPLES = {
    "Ejercicio apunte 1: constante": {
        "A": "0 -1; 0 -9",
        "f1": "1",
        "f2": "9",
        "x0": 2.0,
        "y0": 3.0,
        "t0": 0.0,
        "tf": 8.0,
    },
    "Ejercicio apunte: X(0)=(2,3)": {
        "A": "2 -1; -1 2",
        "f1": "1",
        "f2": "-5",
        "x0": 2.0,
        "y0": 3.0,
        "t0": 0.0,
        "tf": 5.0,
    },
    "Forzamiento periódico": {
        "A": "0 1; -1 0",
        "f1": "0",
        "f2": "sin(t)",
        "x0": 1.0,
        "y0": 0.0,
        "t0": 0.0,
        "tf": 20.0,
    },
    "Ejemplo pizarrón: cos(t)": {
        "A": "-1 0; 0 -2",
        "f1": "cos(t)",
        "f2": "0",
        "x0": 1.0,
        "y0": 1.0,
        "t0": 0.0,
        "tf": 8.0,
    },
    "Ruptura por crecimiento": {
        "A": "-2 0; 0 -3",
        "f1": "exp(t)",
        "f2": "t",
        "x0": 0.0,
        "y0": 0.0,
        "t0": 0.0,
        "tf": 6.0,
    },
}

ALGEBRAIC_EXAMPLES = {
    "Ejercicio apunte: X(0)=(2,3)": {
        "dx": "2*x - y + 1",
        "dy": "-x + 2*y - 5",
        "x0": 2.0,
        "y0": 3.0,
        "t0": 0.0,
        "tf": 5.0,
    },
    "Ejercicio apunte: X(0)=(3,1)": {
        "dx": "-x + 4*y - 2",
        "dy": "x - y - 1",
        "x0": 3.0,
        "y0": 1.0,
        "t0": 0.0,
        "tf": 5.0,
    },
    "Forzamiento periódico": {
        "dx": "y",
        "dy": "-x + sin(t)",
        "x0": 1.0,
        "y0": 0.0,
        "t0": 0.0,
        "tf": 20.0,
    },
    "Ejemplo pizarrón: cos(t)": {
        "dx": "-x + cos(t)",
        "dy": "-2*y",
        "x0": 1.0,
        "y0": 1.0,
        "t0": 0.0,
        "tf": 8.0,
    },
    "Ruptura por crecimiento": {
        "dx": "-2*x + exp(t)",
        "dy": "-3*y + t",
        "x0": 0.0,
        "y0": 0.0,
        "t0": 0.0,
        "tf": 6.0,
    },
}


@dataclass(frozen=True)
class SystemInput:
    matrix: np.ndarray
    f_exprs: tuple[sp.Expr, sp.Expr]
    initial: np.ndarray
    t0: float
    tf: float


def render() -> None:
    st.header("Sistemas lineales no homogéneos")
    st.markdown(
        "Analiza sistemas de la forma **X'(t) = A X(t) + f(t)**, comparando el "
        "comportamiento homogéneo con la perturbación no homogénea."
    )

    with st.expander("Criterio teórico usado", expanded=False):
        st.markdown(
            """
            - El sistema homogéneo asociado es `X'(t)=A X(t)`.
            - Sus autovalores clasifican la dinámica base: nodo, silla, foco, centro, etc.
            - Si `f(t)` es constante o converge, normalmente preserva el tipo cualitativo y desplaza la solución particular.
            - Si `f(t)` crece, por ejemplo `t` o `e^t`, puede romper el comportamiento asintótico del homogéneo.
            - La solución general se interpreta como `X(t)=X_h(t)+X_p(t)`.
            """
        )

    system = read_inputs()
    if system is None:
        return

    show_solution(system)


def read_inputs() -> SystemInput | None:
    input_mode = st.sidebar.radio(
        "Modo de entrada",
        ["Algebraica", "Matricial"],
        help="Algebraica: escribís x' e y'. Matricial: escribís A y f(t).",
    )
    presets = ALGEBRAIC_EXAMPLES if input_mode == "Algebraica" else EXAMPLES
    selected = st.sidebar.selectbox("Ejemplo rápido", list(presets))
    preset = presets[selected]

    st.subheader("Entrada del sistema")
    if input_mode == "Algebraica":
        col_eq, col_i = st.columns([1.4, 0.8])
        with col_eq:
            dx_text = st.text_input("x'(t) =", value=preset["dx"])
            dy_text = st.text_input("y'(t) =", value=preset["dy"])
            st.caption(
                "Usá `x`, `y`, `t` y funciones como `sin(t)`, `cos(t)`, `exp(t)`. "
                "Ejemplo: `2*x - y + 1`."
            )
        with col_i:
            x0, y0, t0, tf = read_initial_values(preset)
        try:
            matrix, f_exprs = parse_algebraic_system(dx_text, dy_text)
        except ValueError as error:
            st.error(str(error))
            return None
        show_detected_matrix(matrix, f_exprs)
    else:
        col_a, col_f, col_i = st.columns([1.1, 1.1, 0.8])
        with col_a:
            matrix_text = st.text_area(
                "Matriz A 2×2",
                value=preset["A"],
                help="Formato: `a b; c d`",
            )
        with col_f:
            f1_text = st.text_input("f₁(t)", value=preset["f1"])
            f2_text = st.text_input("f₂(t)", value=preset["f2"])
            st.caption("Usá expresiones como `1`, `t`, `exp(t)`, `sin(t)`, `cos(t)`.")
        with col_i:
            x0, y0, t0, tf = read_initial_values(preset)
        try:
            matrix = parse_matrix(matrix_text)
            f_exprs = parse_forcing(f1_text, f2_text)
        except ValueError as error:
            st.error(str(error))
            return None

    return SystemInput(
        matrix=matrix,
        f_exprs=f_exprs,
        initial=np.array([x0, y0], dtype=float),
        t0=float(t0),
        tf=float(tf),
    )


def read_initial_values(preset: dict[str, float]) -> tuple[float, float, float, float]:
        x0 = st.number_input("x(0)", value=float(preset["x0"]))
        y0 = st.number_input("y(0)", value=float(preset["y0"]))
        t0 = st.number_input("t inicial", value=float(preset["t0"]))
        tf = st.number_input("t final", value=float(preset["tf"]), min_value=float(t0) + 0.1)
        return float(x0), float(y0), float(t0), float(tf)


def parse_matrix(text: str) -> np.ndarray:
    rows = [row.strip() for row in text.replace(",", " ").split(";") if row.strip()]
    values = [[float(value) for value in row.split()] for row in rows]
    matrix = np.array(values, dtype=float)
    if matrix.shape != (2, 2):
        raise ValueError("La matriz A debe tener exactamente formato 2×2, por ejemplo `0 -1; 0 -9`.")
    return matrix


def parse_forcing(f1_text: str, f2_text: str) -> tuple[sp.Expr, sp.Expr]:
    return tuple(parse_expression(text, include_state=False) for text in (f1_text, f2_text))


def parse_expression(text: str, include_state: bool) -> sp.Expr:
    t = sp.symbols("t")
    x, y = sp.symbols("x y")
    allowed = {
        "t": t,
        "e": sp.E,
        "sin": sp.sin,
        "cos": sp.cos,
        "tan": sp.tan,
        "exp": sp.exp,
        "log": sp.log,
        "ln": sp.log,
        "sqrt": sp.sqrt,
        "pi": sp.pi,
        "E": sp.E,
    }
    if include_state:
        allowed.update({"x": x, "y": y})
    try:
        expression = sp.sympify(text.replace("^", "**"), locals=allowed)
    except (sp.SympifyError, TypeError) as error:
        raise ValueError(f"No pude interpretar la expresión `{text}`: {error}") from error
    allowed_symbols = {t, x, y} if include_state else {t}
    unknown_symbols = expression.free_symbols - allowed_symbols
    if unknown_symbols:
        names = ", ".join(sorted(str(symbol) for symbol in unknown_symbols))
        raise ValueError(
            f"La expresión `{text}` contiene símbolos no permitidos: {names}. "
            "Usá solo `x`, `y`, `t`; para Euler usá `e^t`, `E^t` o `exp(t)`."
        )
    return expression


def parse_algebraic_system(dx_text: str, dy_text: str) -> tuple[np.ndarray, tuple[sp.Expr, sp.Expr]]:
    x, y = sp.symbols("x y")
    expressions = [parse_expression(text, include_state=True).expand() for text in (dx_text, dy_text)]
    matrix_rows: list[list[float]] = []
    forcing_exprs: list[sp.Expr] = []

    for expression in expressions:
        if sp.diff(expression, x, 2) != 0 or sp.diff(expression, y, 2) != 0 or sp.diff(sp.diff(expression, x), y) != 0:
            raise ValueError("El sistema debe ser lineal en `x` e `y`. Ejemplo válido: `2*x - y + sin(t)`.")
        a_x = sp.diff(expression, x)
        a_y = sp.diff(expression, y)
        if a_x.has(x, y) or a_y.has(x, y):
            raise ValueError("Los coeficientes de `x` e `y` no pueden depender de `x` o `y`.")
        if a_x.has(sp.symbols("t")) or a_y.has(sp.symbols("t")):
            raise ValueError("Para este tema, la matriz A debe ser constante. El tiempo solo puede aparecer en f(t).")
        forcing = sp.simplify(expression - a_x * x - a_y * y)
        matrix_rows.append([float(a_x), float(a_y)])
        forcing_exprs.append(forcing)

    return np.array(matrix_rows, dtype=float), (forcing_exprs[0], forcing_exprs[1])


def show_detected_matrix(matrix: np.ndarray, f_exprs: tuple[sp.Expr, sp.Expr]) -> None:
    with st.expander("Conversión detectada a forma matricial", expanded=True):
        st.write("Matriz `A` detectada:")
        st.dataframe(matrix, use_container_width=True)
        st.write(f"`f(t) = ({sp.sstr(f_exprs[0])}, {sp.sstr(f_exprs[1])})`")
        st.latex(r"X'(t)=A\,X(t)+f(t)")


def show_solution(system: SystemInput) -> None:
    eigenvalues, eigenvectors = np.linalg.eig(system.matrix)
    trace = float(np.trace(system.matrix))
    determinant = float(np.linalg.det(system.matrix))
    discriminant = trace**2 - 4 * determinant

    st.subheader("Pasos de resolución")
    steps_col, metrics_col = st.columns([1.4, 0.8])

    with metrics_col:
        st.metric("Traza(A)", format_number(trace))
        st.metric("Det(A)", format_number(determinant))
        st.metric("Discriminante", format_number(discriminant))

    with steps_col:
        st.markdown("**1) Sistema homogéneo asociado**")
        st.latex(r"X_h'(t)=A X_h(t)")
        st.markdown("**2) Autovalores y autovectores**")
        st.write("Autovalores:", [format_complex(value) for value in eigenvalues])
        st.write("Autovectores por columna:")
        st.dataframe(np.round(eigenvectors, 5), use_container_width=True)
        st.markdown("**3) Clasificación del homogéneo**")
        st.info(classify_system(trace, determinant, discriminant, eigenvalues))

    forcing_type = classify_forcing(system.f_exprs)
    st.markdown("**4) Perturbación no homogénea**")
    st.write(f"`f(t) = ({sp.sstr(system.f_exprs[0])}, {sp.sstr(system.f_exprs[1])})`")
    st.warning(forcing_type)

    if is_constant_forcing(system.f_exprs):
        show_constant_particular(system)
    else:
        show_variation_formula(system)

    show_detailed_symbolic_solution(system)

    t_values = np.linspace(system.t0, system.tf, 500)
    try:
        numeric_solution = solve_numeric(system, t_values)
    except ValueError as error:
        st.error(str(error))
        return
    homogeneous_solution = solve_homogeneous(system, t_values)
    vector_field = st.checkbox("Mostrar campo vectorial con f(t₀)", value=True)

    st.subheader("Simulación")
    graph_col_1, graph_col_2 = st.columns(2)
    with graph_col_1:
        st.pyplot(plot_time_series(t_values, numeric_solution, homogeneous_solution))
    with graph_col_2:
        st.pyplot(plot_phase_plane(system, t_values, numeric_solution, homogeneous_solution, vector_field))

    st.subheader("Retrato de fase cualitativo")
    portrait_col, shifted_col = st.columns(2)
    with portrait_col:
        st.plotly_chart(plot_interactive_homogeneous_portrait(system, eigenvalues), use_container_width=True)
    with shifted_col:
        if is_constant_forcing(system.f_exprs):
            st.plotly_chart(plot_interactive_constant_nonhomogeneous_portrait(system, eigenvalues), use_container_width=True)
        else:
            st.info(
                "El retrato autónomo no homogéneo solo existe directamente cuando `f(t)` es constante. "
                "Si `f(t)` depende del tiempo, el campo cambia con `t`; usá el plano de fase temporal."
            )

    with st.expander("Cómo leer los dos retratos", expanded=True):
        st.markdown("**Cómo leer este gráfico**")
        st.markdown(
            """
            - Izquierda: sistema homogéneo `X'=AX`; su equilibrio está en `(0,0)`.
            - Derecha: sistema no homogéneo autónomo `X'=AX+b`, cuando `f(t)=b` es constante.
            - Si `A` es invertible, el equilibrio no homogéneo es `X*=-A^{-1}b`.
            - La forma silla/nodo/foco/centro se preserva, pero el centro del dibujo se traslada.
            - Si `f(t)` depende del tiempo, no hay un único campo fijo en el plano porque el campo cambia con `t`.
            """
        )
        show_equilibrium_note(system)

    with st.expander("Datos de la solución numérica"):
        st.dataframe(
            {
                "t": np.round(t_values, 4),
                "x(t)": np.round(numeric_solution[0], 6),
                "y(t)": np.round(numeric_solution[1], 6),
            },
            use_container_width=True,
        )


def classify_system(trace: float, determinant: float, discriminant: float, eigenvalues: np.ndarray) -> str:
    if determinant < 0:
        return "Punto silla: comportamiento inestable por direcciones de signos opuestos."
    if np.isclose(determinant, 0):
        return "Caso degenerado: al menos un autovalor es cero; requiere análisis adicional."
    if discriminant > 0:
        if trace < 0:
            return "Nodo estable: las trayectorias del homogéneo tienden al equilibrio."
        if trace > 0:
            return "Nodo inestable: las trayectorias se alejan del equilibrio."
        return "Nodo con autovalores reales de suma nula."
    if np.isclose(discriminant, 0):
        if trace < 0:
            return "Nodo impropio estable o estrella estable."
        if trace > 0:
            return "Nodo impropio inestable o estrella inestable."
        return "Caso doble crítico."
    real_part = float(np.real(eigenvalues[0]))
    if np.isclose(real_part, 0):
        return "Centro: oscilaciones cerradas en el homogéneo."
    if real_part < 0:
        return "Foco estable: oscilaciones amortiguadas hacia el equilibrio."
    return "Foco inestable: oscilaciones con amplitud creciente."


def classify_forcing(f_exprs: tuple[sp.Expr, sp.Expr]) -> str:
    t = sp.symbols("t")
    if is_constant_forcing(f_exprs):
        return "f(t) es constante: preserva la dinámica cualitativa y desplaza el equilibrio si A es invertible."
    if all(sp.limit(expr, t, sp.oo).is_finite for expr in f_exprs):
        return "f(t) converge o permanece acotada: suele preservar el comportamiento asintótico base, con solución particular acotada."
    if any(expr.has(sp.exp) or expr.is_polynomial(t) for expr in f_exprs):
        return "f(t) contiene crecimiento polinómico o exponencial: puede romper el comportamiento asintótico del homogéneo."
    return "f(t) no es constante: se resuelve numéricamente y se interpreta comparando con el homogéneo."


def is_constant_forcing(f_exprs: tuple[sp.Expr, sp.Expr]) -> bool:
    t = sp.symbols("t")
    return all(not expr.has(t) for expr in f_exprs)


def show_constant_particular(system: SystemInput) -> None:
    b = np.array([float(system.f_exprs[0]), float(system.f_exprs[1])])
    st.markdown("**5) Solución particular constante**")
    st.latex(r"0=A X_p+b \Rightarrow X_p=-A^{-1}b")
    try:
        particular = -np.linalg.solve(system.matrix, b)
    except np.linalg.LinAlgError:
        st.error("A no es invertible, por eso no hay una única solución particular constante por `-A⁻¹b`.")
        return
    st.write("Solución particular / equilibrio desplazado:", np.round(particular, 6))
    st.latex(r"X(t)=e^{At}\,(X(0)-X_p)+X_p")


def show_variation_formula(system: SystemInput) -> None:
    st.markdown("**5) Fórmula de variación de parámetros**")
    st.latex(r"X(t)=e^{A(t-t_0)}X(t_0)+\int_{t_0}^{t} e^{A(t-s)} f(s)\,ds")
    st.caption("Para forzamientos no constantes, la app simula esta solución mediante integración numérica.")


def show_detailed_symbolic_solution(system: SystemInput) -> None:
    st.subheader("Cálculo paso a paso de la solución")
    try:
        symbolic = build_symbolic_solution(system)
    except Exception as error:
        st.error(f"No pude construir la solución simbólica completa: {error}")
        return

    with st.expander("Ver desarrollo algebraico completo", expanded=True):
        st.markdown("**1) Matriz y vector no homogéneo**")
        st.latex(r"A=" + sp.latex(symbolic["A"]))
        st.latex(r"f(t)=" + sp.latex(symbolic["forcing"]))

        st.markdown("**2) Autovalores y autovectores**")
        st.latex(r"\det(A-\lambda I)=" + sp.latex(symbolic["characteristic_polynomial"]) + r"=0")
        for eigenvalue, multiplicity, eigenvectors in symbolic["eigen_data"]:
            st.latex(
                r"\lambda="
                + sp.latex(eigenvalue)
                + rf",\quad m={multiplicity},\quad v="
                + sp.latex(eigenvectors)
            )
            st.latex(r"(A-\lambda I)v=0")

        st.markdown("**3) Solución homogénea según autovalores/autovectores**")
        st.caption(str(symbolic["homogeneous_method"]))
        st.latex(r"X_h(t)=" + sp.latex(symbolic["homogeneous_professor"]))
        with st.expander("Equivalencia matricial opcional", expanded=False):
            st.latex(r"e^{At}=" + sp.latex(symbolic["matrix_exp_t"]))
            st.latex(r"X_h(t)=e^{At}C")

        if symbolic["constant_forcing"]:
            st.markdown("**4) Solución particular constante**")
            st.latex(r"0=A X_p+b")
            st.latex(r"X_p=-A^{-1}b=" + sp.latex(symbolic["particular"]))
            st.markdown("**5) Solución general no homogénea**")
            st.latex(r"X(t)=X_h(t)+X_p")
            st.latex(r"X(t)=" + sp.latex(symbolic["general_professor"]))
            st.markdown("**6) Aplicando condición inicial**")
            st.latex(r"X(t_0)=" + sp.latex(symbolic["initial"]))
            st.latex(sp.latex(symbolic["constant_equations"]))
            st.latex(r"C=" + sp.latex(symbolic["constants"]))
            st.markdown("**7) Solución final del problema de valor inicial**")
            st.latex(r"X(t)=" + sp.latex(symbolic["ivp_solution"]))
        else:
            if symbolic["particular_method"] == "trig_undetermined":
                st.markdown("**4) Solución particular por coeficientes indeterminados**")
                st.caption("Método como en el pizarrón: si f(t) usa cos(t) y sin(t), se propone una particular con cos(t) y sin(t).")
                st.latex(r"X_p(t)=U\cos(t)+V\sin(t)")
                st.latex(r"U=\begin{pmatrix}a\\c\end{pmatrix},\quad V=\begin{pmatrix}b\\d\end{pmatrix}")
                st.latex(
                    r"X_p(t)=\begin{pmatrix}a\cos(t)+b\sin(t)\\c\cos(t)+d\sin(t)\end{pmatrix}"
                )
                st.latex(r"X_p'(t)=-U\sin(t)+V\cos(t)")
                st.latex(
                    r"X_p'(t)=\begin{pmatrix}-a\sin(t)+b\cos(t)\\-c\sin(t)+d\cos(t)\end{pmatrix}"
                )
                st.latex(r"X_p'=AX_p+f(t)")
                st.latex(r"AX_p+f(t)=" + sp.latex(symbolic["trig_rhs_expanded"]))
                st.latex(r"\cos(t):\quad V=AU+P")
                st.latex(r"\sin(t):\quad -U=AV+Q")
                st.latex(r"P=" + sp.latex(symbolic["trig_P"]) + r",\quad Q=" + sp.latex(symbolic["trig_Q"]))
                st.markdown("**Sistema de ecuaciones para los coeficientes**")
                for equation in symbolic["trig_scalar_equations"]:
                    st.latex(sp.latex(equation))
                st.markdown("**Resolviendo coeficientes**")
                for variable, value in symbolic["trig_coefficients"].items():
                    st.latex(sp.latex(variable) + "=" + sp.latex(value))
                st.latex(r"U=" + sp.latex(symbolic["trig_U"]) + r",\quad V=" + sp.latex(symbolic["trig_V"]))
                st.latex(r"X_p(t)=" + sp.latex(symbolic["particular"]))
                st.markdown("**5) Solución general no homogénea**")
                st.latex(r"X(t)=X_h(t)+X_p(t)")
                st.latex(r"X(t)=" + sp.latex(symbolic["general_professor"]))
                st.markdown("**6) Aplicando condición inicial**")
                st.latex(sp.latex(symbolic["constant_equations"]))
                st.latex(r"C=" + sp.latex(symbolic["constants"]))
                st.markdown("**7) Solución final del problema de valor inicial**")
                st.latex(r"X(t)=" + sp.latex(symbolic["ivp_solution"]))
            else:
                st.markdown("**4) Solución particular por variación de parámetros**")
                st.latex(
                    r"X_p(t)=\int_{t_0}^{t} e^{A(t-s)}f(s)\,ds"
                )
                st.latex(r"X_p(t)=" + sp.latex(symbolic["particular_integral"]))
                st.markdown("**5) Solución general no homogénea**")
                st.latex(r"X(t)=e^{A(t-t_0)}X(t_0)+X_p(t)")
                st.latex(r"X(t)=" + sp.latex(symbolic["ivp_solution"]))

        st.markdown("**Interpretación dinámica**")
        st.write(symbolic["interpretation"])


def build_symbolic_solution(system: SystemInput) -> dict[str, object]:
    t, s = sp.symbols("t s")
    c1, c2 = sp.symbols("C_1 C_2")
    matrix = sp.Matrix(system.matrix).applyfunc(lambda value: sp.nsimplify(value))
    forcing = sp.Matrix(system.f_exprs)
    initial = sp.Matrix([sp.nsimplify(system.initial[0]), sp.nsimplify(system.initial[1])])
    t0 = sp.nsimplify(system.t0)
    constants = sp.Matrix([c1, c2])

    matrix_exp_t = sp.simplify((matrix * t).exp())
    eigen_data = matrix.eigenvects()
    characteristic_polynomial = sp.factor((matrix - sp.symbols("lambda") * sp.eye(2)).det())
    homogeneous_professor, homogeneous_method = build_professor_homogeneous_solution(matrix)

    if is_constant_forcing(system.f_exprs) and matrix.det() != 0:
        particular = sp.simplify(-matrix.inv() * forcing)
        general_professor = sp.simplify(homogeneous_professor + particular)
        constants_value = sp.simplify((matrix * (-t0)).exp() * (initial - particular))
        ivp_solution = sp.simplify((matrix * (t - t0)).exp() * (initial - particular) + particular)
        constant_equations = sp.Eq(general_professor.subs(t, t0), initial)
        return {
            "A": matrix,
            "forcing": forcing,
            "initial": initial,
            "eigen_data": eigen_data,
            "characteristic_polynomial": characteristic_polynomial,
            "matrix_exp_t": matrix_exp_t,
            "homogeneous_professor": homogeneous_professor,
            "homogeneous_method": homogeneous_method,
            "constant_forcing": True,
            "particular_method": "constant",
            "particular": particular,
            "general_professor": general_professor,
            "constant_equations": constant_equations,
            "constants": constants_value,
            "ivp_solution": ivp_solution,
            "interpretation": "Como f(t) es constante, la dinámica del homogéneo se preserva y se traslada al equilibrio Xp.",
        }

    trig_solution = build_trig_undetermined_solution(matrix, forcing, initial, t0, homogeneous_professor)
    if trig_solution is not None:
        return {
            "A": matrix,
            "forcing": forcing,
            "initial": initial,
            "eigen_data": eigen_data,
            "characteristic_polynomial": characteristic_polynomial,
            "matrix_exp_t": matrix_exp_t,
            "homogeneous_professor": homogeneous_professor,
            "homogeneous_method": homogeneous_method,
            "constant_forcing": False,
            "particular_method": "trig_undetermined",
            "interpretation": "Como f(t) es trigonométrica, se usa coeficientes indeterminados: la forma oscilatoria se conserva en la particular.",
            **trig_solution,
        }

    variation_reason = (
        "A es singular: no se puede usar Xp=-A^{-1}b. Se usa variación de parámetros aunque f(t) sea constante."
        if is_constant_forcing(system.f_exprs)
        else "Como f(t) depende del tiempo, la solución particular se calcula por variación de parámetros y puede preservar o romper la dinámica según su crecimiento."
    )
    matrix_exp_t_minus_s = sp.simplify((matrix * (t - s)).exp())
    forcing_s = forcing.subs(t, s)
    integrand = sp.simplify(matrix_exp_t_minus_s * forcing_s)
    particular_integral = sp.Matrix(
        [sp.Integral(sp.simplify(component), (s, t0, t)) for component in integrand]
    )
    try:
        particular_integral = sp.simplify(particular_integral.doit())
    except Exception:
        pass
    ivp_solution = sp.simplify((matrix * (t - t0)).exp() * initial + particular_integral)
    return {
        "A": matrix,
        "forcing": forcing,
        "initial": initial,
        "eigen_data": eigen_data,
        "characteristic_polynomial": characteristic_polynomial,
        "matrix_exp_t": matrix_exp_t,
        "homogeneous_professor": homogeneous_professor,
        "homogeneous_method": homogeneous_method,
        "constant_forcing": False,
        "particular_method": "variation",
        "particular_integral": particular_integral,
        "ivp_solution": ivp_solution,
        "interpretation": variation_reason,
    }


def build_trig_undetermined_solution(
    matrix: sp.Matrix,
    forcing: sp.Matrix,
    initial: sp.Matrix,
    t0: sp.Expr,
    homogeneous_professor: sp.Matrix,
) -> dict[str, object] | None:
    t = sp.symbols("t")
    c1, c2 = sp.symbols("C_1 C_2")
    a, b, c, d = sp.symbols("a b c d")
    cos_t = sp.cos(t)
    sin_t = sp.sin(t)
    expanded_forcing = sp.Matrix([sp.expand_trig(sp.expand(component)) for component in forcing])
    p_vector = sp.Matrix([sp.simplify(component.coeff(cos_t)) for component in expanded_forcing])
    q_vector = sp.Matrix([sp.simplify(component.coeff(sin_t)) for component in expanded_forcing])
    residual = sp.simplify(expanded_forcing - p_vector * cos_t - q_vector * sin_t)

    if any(component != 0 for component in residual):
        return None

    u_symbols = sp.Matrix([a, c])
    v_symbols = sp.Matrix([b, d])
    cos_left = v_symbols
    cos_right = matrix * u_symbols + p_vector
    sin_left = -u_symbols
    sin_right = matrix * v_symbols + q_vector
    rhs_expanded = sp.expand(matrix * (u_symbols * cos_t + v_symbols * sin_t) + forcing)
    equations = list(cos_left - cos_right) + list(sin_left - sin_right)
    scalar_equations = [
        sp.Eq(cos_left[0], cos_right[0]),
        sp.Eq(cos_left[1], cos_right[1]),
        sp.Eq(sin_left[0], sin_right[0]),
        sp.Eq(sin_left[1], sin_right[1]),
    ]
    solution = sp.solve(equations, [a, b, c, d], dict=True)
    if not solution:
        return None

    coefficients = solution[0]
    u_vector = sp.simplify(u_symbols.subs(coefficients))
    v_vector = sp.simplify(v_symbols.subs(coefficients))
    particular = u_vector * cos_t + v_vector * sin_t
    general_professor = homogeneous_professor + particular
    particular_at_t0 = sp.simplify(particular.subs(t, t0))
    constants_value = sp.simplify((matrix * (-t0)).exp() * (initial - particular_at_t0))
    ivp_solution = sp.simplify(
        general_professor.subs({c1: constants_value[0], c2: constants_value[1]})
    )
    constant_equations = sp.Eq(general_professor.subs(t, t0), initial)

    return {
        "trig_U_symbols": u_symbols,
        "trig_V_symbols": v_symbols,
        "trig_P": p_vector,
        "trig_Q": q_vector,
        "trig_equations": sp.Matrix(equations),
        "trig_scalar_equations": scalar_equations,
        "trig_coefficients": coefficients,
        "trig_rhs_expanded": rhs_expanded,
        "trig_U": u_vector,
        "trig_V": v_vector,
        "particular": particular,
        "general_professor": general_professor,
        "constant_equations": constant_equations,
        "constants": constants_value,
        "ivp_solution": ivp_solution,
    }


def build_professor_homogeneous_solution(matrix: sp.Matrix) -> tuple[sp.Matrix, str]:
    t = sp.symbols("t")
    c1, c2 = sp.symbols("C_1 C_2")
    eigen_data = matrix.eigenvects()
    eigen_terms: list[tuple[sp.Expr, sp.Matrix]] = []

    for eigenvalue, _multiplicity, eigenvectors in eigen_data:
        for eigenvector in eigenvectors:
            eigen_terms.append((sp.simplify(eigenvalue), normalize_symbolic_vector(eigenvector)))

    real_terms = [(value, vector) for value, vector in eigen_terms if sp.simplify(sp.im(value)) == 0]
    if len(real_terms) >= 2:
        first_value, first_vector = real_terms[0]
        second_value, second_vector = real_terms[1]
        solution = sp.simplify(
            c1 * sp.exp(first_value * t) * first_vector
            + c2 * sp.exp(second_value * t) * second_vector
        )
        return solution, "Caso del apunte para nodos/sillas: X_h(t)=C1 e^(λ1 t)v1 + C2 e^(λ2 t)v2."

    complex_terms = [(value, vector) for value, vector in eigen_terms if sp.simplify(sp.im(value)) != 0]
    if complex_terms:
        eigenvalue, eigenvector = next(
            ((value, vector) for value, vector in complex_terms if sp.N(sp.im(value)) > 0),
            complex_terms[0],
        )
        alpha = sp.simplify(sp.re(eigenvalue))
        beta = sp.simplify(abs(sp.im(eigenvalue)))
        real_vector = sp.simplify(sp.re(eigenvector))
        imaginary_vector = sp.simplify(sp.im(eigenvector))
        solution = sp.simplify(
            sp.exp(alpha * t)
            * (
                c1 * (real_vector * sp.cos(beta * t) - imaginary_vector * sp.sin(beta * t))
                + c2 * (real_vector * sp.sin(beta * t) + imaginary_vector * sp.cos(beta * t))
            )
        )
        return solution, "Caso del apunte para focos/centros: λ=α±βi, v=a+bi y se usa cos(βt), sin(βt)."

    if len(real_terms) == 1:
        eigenvalue, eigenvector = real_terms[0]
        nullity = len((matrix - eigenvalue * sp.eye(2)).nullspace())
        if nullity == 1:
            generalized = (matrix - eigenvalue * sp.eye(2)).gauss_jordan_solve(eigenvector)[0]
            solution = sp.simplify(
                c1 * sp.exp(eigenvalue * t) * eigenvector
                + c2 * sp.exp(eigenvalue * t) * (t * eigenvector + generalized)
            )
            return solution, "Autovalor doble no diagonalizable: se agrega un vector generalizado."

    fallback = sp.simplify((matrix * t).exp() * sp.Matrix([c1, c2]))
    return fallback, "Caso no cubierto por la forma básica del apunte; se muestra la forma equivalente con e^(At)."


def normalize_symbolic_vector(vector: sp.Matrix) -> sp.Matrix:
    vector = sp.Matrix(vector)
    for component in vector:
        if component != 0:
            return sp.simplify(vector / component)
    return vector


def solve_numeric(system: SystemInput, t_values: np.ndarray) -> np.ndarray:
    forcing = lambdify_forcing(system.f_exprs)

    def rhs(t_value: float, state: np.ndarray) -> np.ndarray:
        return system.matrix @ state + forcing(t_value)

    solution = solve_ivp(
        rhs,
        (system.t0, system.tf),
        system.initial,
        t_eval=t_values,
        rtol=1e-8,
        atol=1e-10,
    )
    if not solution.success:
        st.error(f"La integración numérica falló: {solution.message}")
    return solution.y


def solve_homogeneous(system: SystemInput, t_values: np.ndarray) -> np.ndarray:
    return np.array([expm(system.matrix * (t_value - system.t0)) @ system.initial for t_value in t_values]).T


def lambdify_forcing(f_exprs: tuple[sp.Expr, sp.Expr]) -> Callable[[float], np.ndarray]:
    t = sp.symbols("t")
    functions = [sp.lambdify(t, expr, modules=["numpy"]) for expr in f_exprs]

    def evaluate(t_value: float) -> np.ndarray:
        values: list[float] = []
        for expr, function in zip(f_exprs, functions):
            try:
                values.append(float(function(t_value)))
            except TypeError as error:
                raise ValueError(
                    f"No pude evaluar numéricamente `{sp.sstr(expr)}` en t={t_value}. "
                    "Revisá que f(t) use solo `t` y funciones válidas como `sin`, `cos`, `exp`."
                ) from error
        return np.array(values, dtype=float)

    return evaluate


def plot_time_series(t_values: np.ndarray, numeric_solution: np.ndarray, homogeneous_solution: np.ndarray):
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.plot(t_values, numeric_solution[0], label="x(t) no homogéneo", linewidth=2)
    ax.plot(t_values, numeric_solution[1], label="y(t) no homogéneo", linewidth=2)
    ax.plot(t_values, homogeneous_solution[0], "--", label="x_h(t)", alpha=0.7)
    ax.plot(t_values, homogeneous_solution[1], "--", label="y_h(t)", alpha=0.7)
    ax.set_title("Evolución temporal")
    ax.set_xlabel("t")
    ax.grid(True, alpha=0.25)
    ax.legend()
    return fig


def plot_phase_plane(
    system: SystemInput,
    t_values: np.ndarray,
    numeric_solution: np.ndarray,
    homogeneous_solution: np.ndarray,
    show_field: bool,
):
    fig, ax = plt.subplots(figsize=(7, 4))
    if show_field:
        add_vector_field(ax, system, numeric_solution)
    ax.plot(numeric_solution[0], numeric_solution[1], label="No homogéneo", linewidth=2)
    ax.plot(homogeneous_solution[0], homogeneous_solution[1], "--", label="Homogéneo", alpha=0.8)
    ax.scatter([numeric_solution[0, 0]], [numeric_solution[1, 0]], color="green", label="Inicio")
    ax.scatter([numeric_solution[0, -1]], [numeric_solution[1, -1]], color="red", label="Final")
    mark_constant_equilibrium(ax, system)
    ax.set_title("Plano de fase")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, alpha=0.25)
    ax.legend()
    return fig


def plot_homogeneous_portrait(system: SystemInput, eigenvalues: np.ndarray):
    fig, ax = plt.subplots(figsize=(7, 5))
    radius = max(float(np.linalg.norm(system.initial)) * 1.6, 4.0)
    xs = np.linspace(-radius, radius, 32)
    ys = np.linspace(-radius, radius, 32)
    grid_x, grid_y = np.meshgrid(xs, ys)
    field = system.matrix @ np.vstack([grid_x.ravel(), grid_y.ravel()])
    u = field[0].reshape(grid_x.shape)
    v = field[1].reshape(grid_y.shape)
    speed = np.hypot(u, v)

    ax.streamplot(grid_x, grid_y, u, v, color=speed, cmap="viridis", density=1.1, linewidth=1)
    ax.quiver(grid_x, grid_y, u, v, alpha=0.18)
    ax.scatter([0], [0], color="black", s=60, label="Equilibrio homogéneo")
    add_sample_trajectories(ax, system, radius)
    add_eigen_directions(ax, system, eigenvalues, radius)

    ax.set_title("Retrato de fase del homogéneo")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.25)
    ax.legend(loc="upper right")
    return fig


def plot_interactive_homogeneous_portrait(system: SystemInput, eigenvalues: np.ndarray) -> go.Figure:
    radius = max(float(np.linalg.norm(system.initial)) * 1.6, 4.0)
    starts = sample_initial_conditions(radius)
    fig = go.Figure()

    add_interactive_vector_field(fig, system.matrix, np.zeros(2), radius, np.zeros(2))
    add_interactive_trajectories(fig, system.matrix, np.zeros(2), starts)
    add_interactive_eigen_directions(fig, system.matrix, eigenvalues, radius, np.zeros(2))

    fig.add_trace(
        go.Scatter(
            x=[0],
            y=[0],
            mode="markers",
            marker={"color": "black", "size": 10},
            name="Equilibrio homogéneo",
            hovertemplate="Equilibrio homogéneo<br>x=0<br>y=0<extra></extra>",
        )
    )

    fig.update_layout(
        title="Retrato de fase interactivo del homogéneo X'=AX",
        xaxis_title="x",
        yaxis_title="y",
        height=560,
        hovermode="closest",
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
        margin={"l": 10, "r": 10, "t": 80, "b": 10},
    )
    fig.update_xaxes(range=[-radius, radius], zeroline=True, scaleanchor="y", scaleratio=1)
    fig.update_yaxes(range=[-radius, radius], zeroline=True)
    return fig


def plot_interactive_constant_nonhomogeneous_portrait(system: SystemInput, eigenvalues: np.ndarray) -> go.Figure:
    b = np.array([float(system.f_exprs[0]), float(system.f_exprs[1])], dtype=float)
    try:
        equilibrium = -np.linalg.solve(system.matrix, b)
    except np.linalg.LinAlgError:
        equilibrium = np.zeros(2)
    radius = max(float(np.linalg.norm(system.initial - equilibrium)) * 1.6, 4.0)
    starts = [equilibrium + start for start in sample_initial_conditions(radius)]
    fig = go.Figure()

    add_interactive_vector_field(fig, system.matrix, b, radius, equilibrium)
    add_interactive_trajectories(fig, system.matrix, b, starts)
    add_interactive_eigen_directions(fig, system.matrix, eigenvalues, radius, equilibrium)

    fig.add_trace(
        go.Scatter(
            x=[equilibrium[0]],
            y=[equilibrium[1]],
            mode="markers",
            marker={"color": "purple", "size": 13, "symbol": "star"},
            name="Equilibrio no homogéneo",
            hovertemplate="Equilibrio no homogéneo<br>x=%{x:.4g}<br>y=%{y:.4g}<extra></extra>",
        )
    )
    fig.update_layout(
        title="Retrato no homogéneo X'=AX+b",
        xaxis_title="x",
        yaxis_title="y",
        height=560,
        hovermode="closest",
        legend={"orientation": "h", "yanchor": "bottom", "y": 1.02, "xanchor": "right", "x": 1},
        margin={"l": 10, "r": 10, "t": 80, "b": 10},
    )
    fig.update_xaxes(
        range=[equilibrium[0] - radius, equilibrium[0] + radius],
        zeroline=True,
        scaleanchor="y",
        scaleratio=1,
    )
    fig.update_yaxes(range=[equilibrium[1] - radius, equilibrium[1] + radius], zeroline=True)
    return fig


def add_interactive_vector_field(
    fig: go.Figure,
    matrix: np.ndarray,
    forcing: np.ndarray,
    radius: float,
    center: np.ndarray,
) -> None:
    xs = np.linspace(center[0] - radius, center[0] + radius, 17)
    ys = np.linspace(center[1] - radius, center[1] + radius, 17)
    arrow_x: list[float | None] = []
    arrow_y: list[float | None] = []
    marker_x: list[float] = []
    marker_y: list[float] = []
    hover_text: list[str] = []
    arrow_length = radius * 0.09

    for x_value in xs:
        for y_value in ys:
            vector = matrix @ np.array([x_value, y_value], dtype=float) + forcing
            norm = float(np.linalg.norm(vector))
            if np.isclose(norm, 0):
                continue
            direction = vector / norm
            end_x = x_value + arrow_length * direction[0]
            end_y = y_value + arrow_length * direction[1]
            arrow_x.extend([x_value, end_x, None])
            arrow_y.extend([y_value, end_y, None])
            marker_x.append(end_x)
            marker_y.append(end_y)
            hover_text.append(
                f"x={x_value:.3g}<br>y={y_value:.3g}<br>x'={vector[0]:.3g}<br>y'={vector[1]:.3g}"
            )

    fig.add_trace(
        go.Scatter(
            x=arrow_x,
            y=arrow_y,
            mode="lines",
            line={"color": "rgba(80,80,80,0.35)", "width": 1},
            name="Campo vectorial",
            hoverinfo="skip",
        )
    )
    fig.add_trace(
        go.Scatter(
            x=marker_x,
            y=marker_y,
            mode="markers",
            marker={"symbol": "triangle-up", "size": 6, "color": "rgba(80,80,80,0.45)"},
            name="Dirección del campo",
            text=hover_text,
            hovertemplate="%{text}<extra></extra>",
            showlegend=False,
        )
    )


def add_interactive_trajectories(
    fig: go.Figure,
    matrix: np.ndarray,
    forcing: np.ndarray,
    starts: list[np.ndarray],
) -> None:
    def rhs(_t: float, state: np.ndarray) -> np.ndarray:
        return matrix @ state + forcing

    for index, start in enumerate(starts, start=1):
        forward = solve_ivp(rhs, (0, 5), start, max_step=0.04, rtol=1e-7, atol=1e-9)
        backward = solve_ivp(rhs, (0, -5), start, max_step=0.04, rtol=1e-7, atol=1e-9)
        x_values = np.concatenate([backward.y[0][::-1], forward.y[0]])
        y_values = np.concatenate([backward.y[1][::-1], forward.y[1]])
        fig.add_trace(
            go.Scatter(
                x=x_values,
                y=y_values,
                mode="lines",
                line={"color": "#1f77b4", "width": 2},
                name="Trayectorias típicas" if index == 1 else "Trayectorias típicas",
                showlegend=index == 1,
                hovertemplate="Trayectoria<br>x=%{x:.4g}<br>y=%{y:.4g}<extra></extra>",
            )
        )


def add_interactive_eigen_directions(
    fig: go.Figure,
    matrix: np.ndarray,
    eigenvalues: np.ndarray,
    radius: float,
    center: np.ndarray,
) -> None:
    if not np.allclose(np.imag(eigenvalues), 0):
        return
    _, eigenvectors = np.linalg.eig(matrix)
    for index, eigenvalue in enumerate(eigenvalues):
        direction = np.real(eigenvectors[:, index])
        norm = np.linalg.norm(direction)
        if np.isclose(norm, 0):
            continue
        direction = direction / norm
        fig.add_trace(
            go.Scatter(
                x=[center[0] - radius * direction[0], center[0] + radius * direction[0]],
                y=[center[1] - radius * direction[1], center[1] + radius * direction[1]],
                mode="lines",
                line={"dash": "dash", "width": 2},
                name=f"Dirección λ={format_number(float(np.real(eigenvalue)))}",
                hovertemplate=f"Autodirección<br>λ={format_number(float(np.real(eigenvalue)))}<extra></extra>",
            )
        )


def sample_initial_conditions(radius: float) -> list[np.ndarray]:
    return [
        np.array([radius * sx, radius * sy], dtype=float)
        for sx, sy in [
            (-0.8, -0.8),
            (-0.8, 0.0),
            (-0.8, 0.8),
            (0.0, -0.8),
            (0.0, 0.8),
            (0.8, -0.8),
            (0.8, 0.0),
            (0.8, 0.8),
            (-0.35, 0.55),
            (0.55, -0.35),
        ]
    ]


def add_sample_trajectories(ax, system: SystemInput, radius: float) -> None:
    starts = sample_initial_conditions(radius)

    def rhs(_t: float, state: np.ndarray) -> np.ndarray:
        return system.matrix @ state

    for start in starts:
        solution = solve_ivp(rhs, (0, 5), start, max_step=0.05, rtol=1e-7, atol=1e-9)
        ax.plot(solution.y[0], solution.y[1], color="#1f77b4", alpha=0.55, linewidth=1.2)


def add_eigen_directions(ax, system: SystemInput, eigenvalues: np.ndarray, radius: float) -> None:
    if not np.allclose(np.imag(eigenvalues), 0):
        return
    _, eigenvectors = np.linalg.eig(system.matrix)
    for index, eigenvalue in enumerate(eigenvalues):
        direction = np.real(eigenvectors[:, index])
        norm = np.linalg.norm(direction)
        if np.isclose(norm, 0):
            continue
        direction = direction / norm
        points = np.array([-radius * direction, radius * direction])
        label = f"Dirección λ={format_number(float(np.real(eigenvalue)))}"
        ax.plot(points[:, 0], points[:, 1], "--", linewidth=1.4, label=label)


def mark_constant_equilibrium(ax, system: SystemInput) -> None:
    if not is_constant_forcing(system.f_exprs):
        return
    b = np.array([float(system.f_exprs[0]), float(system.f_exprs[1])])
    try:
        equilibrium = -np.linalg.solve(system.matrix, b)
    except np.linalg.LinAlgError:
        return
    ax.scatter([equilibrium[0]], [equilibrium[1]], color="purple", marker="*", s=130, label="Equilibrio desplazado")


def show_equilibrium_note(system: SystemInput) -> None:
    if not is_constant_forcing(system.f_exprs):
        return
    b = np.array([float(system.f_exprs[0]), float(system.f_exprs[1])])
    try:
        equilibrium = -np.linalg.solve(system.matrix, b)
    except np.linalg.LinAlgError:
        st.caption("A no es invertible: no hay equilibrio desplazado único.")
        return
    st.markdown("**Equilibrio no homogéneo constante**")
    st.write(np.round(equilibrium, 6))


def add_vector_field(ax, system: SystemInput, numeric_solution: np.ndarray) -> None:
    forcing = lambdify_forcing(system.f_exprs)
    x_min, x_max = bounds(numeric_solution[0])
    y_min, y_max = bounds(numeric_solution[1])
    xs = np.linspace(x_min, x_max, 18)
    ys = np.linspace(y_min, y_max, 18)
    grid_x, grid_y = np.meshgrid(xs, ys)
    field = system.matrix @ np.vstack([grid_x.ravel(), grid_y.ravel()]) + forcing(system.t0)[:, None]
    u = field[0].reshape(grid_x.shape)
    v = field[1].reshape(grid_y.shape)
    norm = np.hypot(u, v)
    norm[norm == 0] = 1
    ax.quiver(grid_x, grid_y, u / norm, v / norm, alpha=0.35)


def bounds(values: np.ndarray) -> tuple[float, float]:
    min_value = float(np.min(values))
    max_value = float(np.max(values))
    margin = max((max_value - min_value) * 0.15, 1.0)
    return min_value - margin, max_value + margin


def format_complex(value: complex) -> str:
    if np.isclose(value.imag, 0):
        return format_number(float(value.real))
    sign = "+" if value.imag >= 0 else "-"
    return f"{format_number(float(value.real))} {sign} {format_number(abs(float(value.imag)))}i"


def format_number(value: float) -> str:
    return f"{value:.5g}"
