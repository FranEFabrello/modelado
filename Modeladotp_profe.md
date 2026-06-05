UADE

FUNDAMENTOS DE
MODELADO Y SIMULACIÓN

Omar J. Caceres

DEPARTAMENTO DE CIENCIAS BÁSICAS

Segunda Edición 2026

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Índice

Introducción
Capítulo I
Búsqueda binaria de raíces
Método del punto fijo
Método de aceleración Aitken
Método de Newton Raphson
Polinomio Interpolante de Lagrange
Diferencias finitas
Reglas de Newton Cotes
Regla del Rectángulo medio compuesto
Regla del trapecio
Regla de Simpson
El Método de Monte Carlo
Ecuaciones diferenciales
Método de Euler
Método de Euler mejorado (Heun)
Método de Runge Kutta 4
Bibliografías Capítulo I
Capítulo II Sistemas dinámicos
Conceptos Básicos
Sistemas desacoplados unidimensionalmente
Bifurcaciones
Tipo Hopf
Sistema Lorent
Sistemas dinámicos lineales 2d
Sistemas lineales no homogéneos
Conversión de un sistema (EDO) de orden superior
Sistemas dinámicos no lineales
Análisis cualitativo
Teoremas de existencia y unicidad (Picard -Lindelöf)
Teorema de Harmant-Grobman
Estabilidad de Lyapunuv (directa)
Principio de Invarianza deSalle
Teorema del flujo
Teorema de la variedad estable e inestable
Teorema de la variedad central
Teorema de Poincaré Bendinxson
Teorema de Bendixson-Dulac
Teorema de Invarianza positiva (criterio de la frontera)
Teorema de la Bifurcación Hopf

2

Pg.

4
5
8
11
13
15
20
24
27
27
27
28
36
44
46
48
50
57
58
61
63
71
75
78
79
91
94
95
98
98
98
99
100
101
104
104
104
107
110
110

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Teorema de la estabilidad estructural
Bibliografías Capítulo II
Aplicaciones de sistemas dinámicos
Romeo y Julieta
Modelo Lotka Volterra
Modelos de combate
Sistemas conservativos
Parametrización de sistemas dinámicos
Estructura Orbital
Conjuntos límites
Glosario de términos básicos
Prácticas de Laboratorio
Bibliografía Modelos

110
139
148
148
155
158
164
168
172
173
195
201
211

3

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Introducción

Modelado y simulación es sin dudas una de las materias más prácticas y vigentes en el campo de la ciencia
y la ingeniería. Sin embargo, no es una disciplina nueva ya que desde tiempos remotos la humanidad tuvo
la necesidad de describir fenómenos naturales —como el movimiento planetario, los brotes epidémicos o
los cambios en la economía, el comportamiento del clima, o cómo funcionan los biorritmos humanos, esto
ha impulsado el desarrollo de modelos que permitan comprender, anticipar y, en cierta medida, controlar
el comportamiento de los procesos.

Las primeras civilizaciones trazaron el cielo para predecir las estaciones; más tarde, médicos y filósofos
intentaron explicar la propagación de enfermedades; y con el surgimiento de la economía moderna tratar
de entender los cambios en los mercados, por esto matemáticos y economistas buscaron patrones que
revelaran la evolución de la dinámica comercial.

A lo largo de la historia descubrimos que detrás de la diversidad de fenómenos existen estructuras regulares
que pueden expresarse mediante ecuaciones, algoritmos o reglas lógicas matemáticas. Así nacieron los
primeros modelos: simplificaciones del mundo real que capturan su esencia y permiten razonar sobre ella.
En la era moderna, el modelado y la simulación por computadora se volvieron herramientas indispensables.
La física formalizó leyes que describen desde osciladores hasta sistemas planetarios; la biología desarrolló
modelos poblacionales y epidemiológicos; la ingeniería utiliza representaciones matemáticas para diseñar
estructuras seguras; la computación permite simular sistemas en escenarios imposibles de experimentar
directamente.

todo  modelo  —por  simple  o  complejo  que  sea—  necesita  ser

resuelto.
Sin  embargo,
Y para resolverlo, especialmente cuando la solución analítica no existe o es impracticable, recurrimos a los
métodos  numéricos.  En  este  texto  se  presentan  de  una  manera  resumida  y  sencilla  estos  métodos,  al
menos los más comunes, siendo la primera parte los métodos numéricos mientras que en la parte final
tendremos los sistemas dinámicos.

4

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

CAPÍTULO I MÉTODOS NUMÉRICOS

Los métodos numéricos son un conjunto de técnicas y algoritmos diseñados para aproximar soluciones a
problemas  matemáticos  que  no  pueden  resolverse  de  forma  exacta  o  analítica,  o  cuya  solución  exacta
resulta impráctica y compleja de calcular. Estos métodos se apoyan en procedimientos iterativos, y el uso
de aproximaciones sucesivas donde el cálculo computacional es primordial, por lo que son fundamentales
en ciencias aplicadas e ingeniería.

Conceptos básicos:

a)  Modelo  Matemático  “Se  define,  de  manera  general,  como  una  formulación  o  una  ecuación  que
expresa las características esenciales de un sistema físico o de un proceso en términos matemáticos.
en general, el modelo se representa mediante una relación funcional de la forma: Variable dependiente
= f (variables independientes, parámetros, funciones de fuerza)” Steven Chapra Métodos Numéricos
para ingenieros 5ta Edición, Pg 11.

b) Simular: una vez que se ha creado un modelo, la simulación es el proceso de ejecutarlo para estudiar el
comportamiento del sistema a través del tiempo o bajo diferentes condiciones.

c) Iterar: Significa repetir un proceso con el objetivo de acercarse a un resultado deseado.

𝑥𝑛+1 = 𝑥𝑛
d) Convergencia: Indica como las aproximaciones sucesivas se acercan a la solución 𝑥∗ de una ecuación:
𝑓(𝑥) = 0

Velocidad de convergencia: La rapidez con la que se reduce el error,  𝑒𝑛 = |𝑥𝑛 − 𝑥∗|

e) Orden de Convergencia: Es una medida utilizada en análisis numérico para describir la rapidez con la
que una secuencia iterativa se acerca a su límite o solución. cuando se emplean métodos iterativos para
resolver ecuaciones o sistemas de ecuaciones, es útil conocer el orden de convergencia para determinar la
eficiencia del método.

|𝑋𝑛+1 − 𝑋∗  |
|𝑋𝑛 − 𝑋∗|𝑃 = 𝐶

lim
𝑛→∞

Donde C es una constante, P el orden de aproximación y 𝑋∗ la solución buscada, es decir se basa en cómo
se reduce el error entre aproximaciones sucesivas. Entonces:

Donde C es una constante independiente de n, P el orden de convergencia, 𝑋∗ la solución buscada, 𝑒𝑛 error.

𝑒𝑛 = 𝑥𝑛 − 𝑥∗ , 𝐶 > 0, 𝑝 > 1

|𝑒𝑛+1| = 𝐶|𝑒𝑛|𝑝

5

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Algunos Métodos Iterativos: Existen otros métodos, pero estos son los más conocidos.

Método

Orden de
Convergencia

Ventajas

Desventajas

Newton Raphson

Cuadrática

Muy rápido cerca del
valor real

Necesita derivadas

Bisección

Punto Fijo

Lineal

Lineal

Siempre converge

Lento

Fácil de
implementar

Requiere la
condición|𝑔′

(𝑥0)| < 1

TABLA 1

Cota de error: La cota de error se refiere a una estimación del error máximo que se comete en un proceso
iterativo o aproximación. Garantiza el resultado dentro de una tolerancia aceptable.

Tipos de cota de error: existen varios tipos, acá estudiaremos los dos principales que son; error absoluto y
relativo.

Error Absoluto: Es la diferencia entre el valor exacto 𝑥∗ y la aproximación 𝑥𝑛

Como 𝑥∗ no lo conocemos entonces se puede usar diferencia entre iteraciones

𝐸𝑎𝑏𝑠 = |𝑥∗ − 𝑥𝑛|

𝐸𝑎𝑏𝑠 ≈ |𝑥𝑛+1 − 𝑥𝑛|

Error Relativo: Es  una medida  utilizada para  cuantificar la precisión de una  aproximación o medición en
comparación  con  un  valor  exacto  o  verdadero.  se  expresa  como  una  fracción  o  porcentaje  del  valor
verdadero y es útil para evaluar la significancia del error en términos relativos.

Como 𝑥∗ no lo conocemos entonces se puede usar diferencia entre iteraciones

𝐸𝑟 =

|𝑥∗ − 𝑥𝑛|
|𝑥∗|

𝐸𝑟 ≈

|𝑥𝑛+1 − 𝑥𝑛|
|𝑥𝑛+1|

Criterios de Detención: Son las reglas que definen cuando un método iterativo debe parar, los criterios más
comunes son:

1.  Tolerancia en el error absoluto: |𝑥𝑛+1 − 𝑥𝑛| ≤ 𝜀, 𝜀 Tolerancia permitida

6

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

2.  Tolerancia en el error relativo:

|𝑥𝑛+1−𝑥𝑛|
|𝑥𝑛+1|
3.  Condición sobre el residuo: |𝑓(𝑥)| ≤ 𝜀
4.  Número máximo de iteraciones: 𝑛 > 𝑁𝑚𝑎𝑥

≤ 𝜀

Como 𝑥∗ no lo conocemos entonces se puede usar diferencia entre iteraciones

Conjuntos compactos:

En un espacio métrico, un conjunto k se define compacto si es cerrado (contiene todos los puntos limite),
acotado: (todos los puntos del conjunto están a una distancia finita de algún punto fijo).

Ejemplos de conjuntos compactos:

1. Un disco cerrado en el plano {(𝑥, 𝑦)𝜖ℝ2,  𝑥2 + 𝑦2 ≤ 1}

 es compacto, es un disco de radio 1 centro en el origen, es cerrado porque incluye el borde 𝑥2 + 𝑦2 = 1  y
es acotado

Ejemplos de conjuntos compactos:

2.  Un  segmento  de  recta  en ℝ𝒏 :  la  línea  parametrizada  [a,b]= {𝑋𝜖ℝ2,   𝑥 = 𝑡𝑎 + (1 − 𝑡)𝑏,   0 ≤ 𝑡 ≤ 1} es
compacta.

3.  Un  rectángulo  cerrado  en  ℝ2  el  conjunto  [a,b]x[c,d]  en  ℝ2  es  compacto  en  la  región  rectangular
delimitada por a,b,c,d (cerrado y acotado).

4. El conjunto de funciones continúas acotadas en [0,1] con la topología de la convergencia uniforme, esta
es  una  aplicación  del  teorema  de  Arzelá-Ascolí,  que  afirma  que  un  conjunto  es  compacto  si  es
equicontinuo, acotado y cerrado.

Condición de Lipschitz en conjuntos compactos:

Supongamos  que  tenemos  una  función 𝑔: 𝑘 → ℝ,  definida  en  un  conjunto  compacto  k.  Decimos  que  g
tatisface una condición de Lipschitz contante L, si para todos 𝑥, 𝑦 ∈ 𝑘;  |𝑔(𝑥) − 𝑔(𝑦)| ≤ 𝐿|𝑥 − 𝑦|.

Si  una  función  es  continuamente  diferenciable, (𝑔 ∈  ∁1
derivada acotada, |𝑔′

(𝑥)| < 𝑀, para todo 𝑥 ∈ k y podemos tomar L=M.

(𝑘)) entonces  y  el  conjunto  compacto  tiene  una

La constante L es uniforme en el todo el conjunto compacto, y además da garantía de convergencia si 𝐿 < 1
en 𝑥𝑛+1=𝑔(𝑥𝑛).

Propiedades de un conjunto compacto:

Existencia de un punto fijo: El teorema del punto fijo de Banach establece que, si X es un conjunto compacto
completo y compacto en un espacio métrico, y f es una función contractiva, entonces existe un único punto
fijo. 𝑥∗𝜖𝑋 tal que 𝑓(𝑥∗)=𝑋∗

7

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Convergencia  Iterativa:  Partiendo  de  un  punto  arbitrario 𝑥0𝜖𝑋  la  sucesión  generada  la  iteración  de  f:
converge al punto fijo, 𝑥𝑛+1 = 𝑓(𝑥𝑛)

Funciones  Contractivas:  sea  una  𝑓: 𝑋 → 𝑋 ,  Se  dice  contractiva  si  existe  una  constante  𝑘𝜖[0,1) tal  que
𝑑(𝑓(𝑥), 𝑓(𝑦)) ≤ 𝑘𝑑(𝑥, 𝑦),  ∀𝑥,  𝑘𝜖𝑋, donde 𝑑(∙,∙) es una métrica definida en el espacio métrico 𝑋.

En esencia una función contractiva (acerca) los puntos del dominio, ya que la distancia entre las imágenes
de los puntos es estrictamente menor que la distancia entre los puntos originales

Ejemplo Función contractiva: sea 𝑓(𝑥) =

1
2

𝑥, definida en un conjunto compacto 𝑋 = [0,1].

Verificamos la contracción: |𝑓(𝑥) − 𝑓(𝑦)| = |

1
2

𝑥 −

1
2

1
𝑦|=
2

|𝑥 − 𝑦|

En este caso la constante de contracción cumple el requerimiento, entonces, hay un único punto fijo en X.
𝑥 − 𝑥 = 0,  𝑝𝑜𝑟 𝑙𝑜 𝑞𝑢𝑒 𝑥∗ = 0, esto nos dice que, si aplicamos
se calcula 𝑓(𝑥) = 𝑥, ordenando la ecuación:
iteración desde un punto cercano por ejemplo 1, la función converge a 0.

1
2

𝑑(𝑥𝑛, 𝑥∗) ≤ 𝑘𝑛𝑑(𝑥𝟎, 𝑥∗), |𝑓(𝑥) − 𝑓(𝑦)| ≤k|𝑥 − 𝑦|, 0 < 𝑘 < 1

Búsqueda binaria de raíces

También conocida como el método de bisección, es un algoritmo numérico utilizado para encontrar una
raíz de una función continua f(x) en un intervalo dado [a,b], donde f(a) y f(b) tienen signos opuestos f(a)⋅f(b)<
0. este método se basa en el teorema del valor intermedio, que garantiza la existencia de al menos una raíz
en dicho intervalo.

FIGURA 1.

8

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Teorema de Bolzano

sea f(x) una función continua en un intervalo cerrado [a,b]. sí f(a)⋅f(b)<0, es decir, f(a) y f(b) tienen signos
opuestos, entonces existe al menos un punto c∈(a,b) tal que: f(c)=0

El algoritmo consiste en seguir los siguientes pasos:

FIGURA 2

1.  Escoger el intervalo [a, b] donde f(a)⋅f(b)< 0, esto garantiza que haya una raíz en dicho intervalo.
2.  Calcular el punto medio. 𝒄 =
3.  Evaluar c en la función: si 𝑓(𝑐)=0, entonces parar y hemos obtenido la raíz.
4.  𝑆𝑖 𝑓(𝑎) 𝑓(𝑐) < 0,  𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 𝑙𝑎 𝑟𝑎𝑖𝑧 𝑒𝑠𝑡𝑎 𝑒𝑛 [𝑎, 𝑐] 𝒚 actualizamos 𝑏 = 𝑐
5.  𝑆𝑖 𝑓(𝑏) 𝑓(𝑐) < 0,  𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 𝑙𝑎 𝑟𝑎𝑖𝑧 𝑒𝑠𝑡𝑎 𝑒𝑛 [𝑐, 𝑏] 𝑎𝑐𝑡𝑢𝑎𝑙𝑖𝑧𝑎𝑚𝑜𝑠 𝑎 = 𝑐

𝑎+𝑏
2

Código en python

import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
# Método de Bisección
def biseccion(f, a, b, iteraciones=100, tolerancia=1e-6, precision=5):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo [a, b].")
    results = []
    for i in range(iteraciones):
        c = round((a + b) / 2.0, precision)
        fc = round(f(c), precision)
        results.append([i+1, a, b, c, fc])
        print(tabulate(results, headers=["Iteración", "a", "b", "c", "f(c)"], tablefmt="grid"))
        if abs(fc) < tolerancia or (b - a) / 2.0 < tolerancia:
            return c

9

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("El método no convergió o faltan iteraciones.")
def graficar_biseccion(f, a, b, raiz):
    # Graficar la función
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.plot(x, y, label='$f(x)$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate
# Método de Bisección
def biseccion(f, a, b, iteraciones=100, tolerancia=1e-6, precision=5):
    if f(a) * f(b) >= 0:
        raise ValueError("La función debe tener signos opuestos en los extremos del intervalo [a, b].")
    results = []
    for i in range(iteraciones):
        c = round((a + b) / 2.0, precision)
        fc = round(f(c), precision)
        results.append([i+1, a, b, c, fc])
        print(tabulate(results, headers=["Iteración", "a", "b", "c", "f(c)"], tablefmt="grid"))
        if abs(fc) < tolerancia or (b - a) / 2.0 < tolerancia:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    raise ValueError("El método no convergió o faltan iteraciones.")
def graficar_biseccion(f, a, b, raiz):
    # Graficar la función
    x = np.linspace(a - 1, b + 1, 400)
    y = f(x)
    plt.plot(x, y, label='$f(x)$')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

10

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Método del punto fijo

Es un punto donde al evaluarlo en una función se obtiene el mismo punto

Propiedades de un conjunto compacto:

FIGURA 3

Existencia de un punto fijo: El teorema del punto fijo de Banach establece que, si X es un conjunto compacto
completo y compacto en un espacio métrico, y f es una función contractiva, entonces existe un único punto
fijo. 𝑥∗𝜖𝑋 tal que 𝑓(𝑥∗)=𝑋∗

converge a 𝑥∗:

lim
𝑛→∞

𝑥𝑛 = 𝑥∗

Convergencia  Iterativa:  Partiendo  de  un  punto  arbitrario 𝑥0𝜖𝑋  la  sucesión  generada  la  iteración  de  f:
converge al punto fijo, 𝑥𝑛+1 = 𝑓(𝑥𝑛)

𝑆𝑒𝑎 𝑓(𝑥) 𝑙𝑎 𝑓𝑢𝑛𝑐𝑖ó𝑛 𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙,
𝑔(𝑥) 𝑙𝑎 𝑓𝑢𝑛𝑐𝑖ó𝑛 𝑎 𝑖𝑡𝑒𝑟𝑎𝑟

Para aplicar Banach:

•  𝑔: 𝑋 → 𝑋 debe ser contractiva
•  𝑋 debe ser completo
Entonces el punto fijo de 𝑔 es la solución buscada.

11

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Casos

Código en Python
import math
import numpy as np
import matplotlib.pyplot as plt
"""
f(x)=cos(x)
0=cos(x)
x= cos(x)+x
"""

FIGURA 4

FIGURA 5

12

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

def f(x):
    return math.cos(x)
 def g(x):
    return math.cos(x) + x
 def fixed_point_iteration(x0, tol=1e-5, max_iter=100):
    x = x0
    iter_values = [x0]
    for i in range(max_iter):
        x_new = g(x)
        iter_values.append(x_new)
        if abs(x_new - x) < tol:
            print("Tolerance exceeded...")
            break
        x = x_new
    return x_new, iter_values
 x0 = 1.0 # Valor inicial

root, iter_values = fixed_point_iteration(x0)

# Graficar la función original y el proceso de iteración
x_vals = np.linspace(-2 * np.pi, 2 * np.pi, 400)
y_vals = np.cos(x_vals)

plt.plot(x_vals, y_vals, label='$f(x) = cos(x)$')
plt.scatter(iter_values, [f(x) for x in iter_values], color='red', zorder=5)
plt.plot(iter_values, [f(x) for x in iter_values], color='red', linestyle='--', zorder=5)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Método del Punto Fijo para $f(x) = cos(x)$')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.legend()
plt.show()

print(f"La raíz aproximada es: {root}")

Método de aceleración Aitken

Es  una  técnica  numérica  que  se  usa  para  mejorar  la  velocidad  de  convergencia  de  una  secuencia  que
converge lentamente hacia un límite. básicamente, toma tres elementos consecutivos de una secuencia y
calcula un valor "acelerado" que se acerca más rápidamente al valor límite. la fórmula central del método
es:

𝑥∗

𝑛 = 𝑥(𝑛) −

(𝑥𝑛+1 − 𝑥𝑛)2
𝑥𝑛+2 − 2(𝑥𝑥𝑛+1) + 𝑥𝑛

13

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑥(𝑛) 𝑡𝑒𝑟𝑚𝑖𝑛𝑜 𝑑𝑒 𝑠𝑢𝑐𝑒𝑠𝑖ó𝑛 𝑜𝑟𝑖𝑔𝑖𝑛𝑎𝑙
𝑥∗

𝑛 𝑡𝑒𝑟𝑚𝑖𝑛𝑜 𝑑𝑒 𝑠𝑢𝑐𝑒𝑠𝑖ó𝑛 𝑎𝑐𝑒𝑙𝑒𝑟𝑎𝑑𝑜

Se requiere tres términos iterativos consecutivos para poder iniciar la primera extrapolación, y este valor
puede  ser  considerado  el  inicial  de  un  nuevo  proceso  de  aceleración  tras  calcular  los  próximos  dos
términos al mismo

Condiciones de Convergencia

•

Secuencia  Convergente:  La  secuencia  debe  ser  monótona  y  convergente  hacia  un  valor  límite  L.  El
método no es efectivo si la secuencia diverge o si oscila de manera significativa.

•  Disponibilidad de Tres: El denominador de la fórmula de Aitken.
•

Términos  Consecutivos:  Para  aplicar  la  fórmula  de  Aitken,  necesitas  al  menos  tres  términos
consecutivos de la secuencia.

•  Diferencia no Nula en el Denominador.
•  Convergencia  Relativamente  Lenta:  El  método  es especialmente  útil  cuando  la  secuencia  converge
lentamente  al límite, ya que  Aitken  acelera el proceso. Si la  secuencia ya converge rápidamente, la
mejora puede ser mínima.
Estabilidad  Numérica:  Si  la  secuencia  presenta  un  comportamiento  numérico  inestable  o  errores
significativos en los cálculos, los resultados de la aceleración pueden no ser fiables.

•

Código

def punto_fijo_con_aitken_tabla(g, x0, tol=1e-6, max_iter=100):
    """
    Método del punto fijo con aceleración de Aitken que muestra una tabla de iteraciones.
    g: función de iteración (polinomio en este caso).
    x0: aproximación inicial.
    tol: tolerancia para la convergencia.
    max_iter: número máximo de iteraciones.
    """
    x = x0
    print(f"{'Iteración':<10}{'x':<20}{'x1 = g(x)':<20}{'x2 = g(x1)':<20}{'x_acelerado':<20}{'Error':<20}")
    print("-" * 100)
    for i in range(max_iter):
        # Calcular tres puntos consecutivos de la iteración
        x1 = g(x)
        x2 = g(x1)
        # Aplicar la aceleración de Aitken
        denominador = x2 - 2 * x1 + x
        if denominador != 0:
            x_acelerado = x - (x1 - x)**2 / denominador
        else:

            x_acelerado = x2  # Si no se puede aplicar Aitken, continuar con x

# Calcular error relativo

14

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

        error = abs(x_acelerado - x)
        # Mostrar valores en la tabla
        print(f"{i + 1:<10}{x:<20.10f}{x1:<20.10f}{x2:<20.10f}{x_acelerado:<20.10f}{error:<20.10f}")
        # Verificar convergencia
        if error < tol:
            print(f"\nConvergencia alcanzada en la iteración {i + 1}.")
            return x_acelerado
        # Actualizar para la siguiente iteración
        x = x_acelerado
    print("\nEl método no converge después del número máximo de iteraciones.")
    return None
# Ejemplo de uso
def g(x):
    return (2*x-1)**(1/2)  # Polinomio g(x)
x0 = 2  # Aproximación inicial
resultado = punto_fijo_con_aitken_tabla(g, x0)
if resultado is not None:

    print(f"\nLa solución aproximada es: {resultado}")

Método de Newton Raphson

El método de Newton-Raphson es un método iterativo muy eficiente para encontrar raíces de funciones no
lineales f(x)=0. se basa en la aproximación lineal de la función mediante su derivada, y su fórmula iterativa
es:

𝑥𝑛+1 = 𝑥𝑛 −

𝑓 (𝑛)
𝑓′

(𝑛)

FIGURA 6

15

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ventajas:

•  Convergencia rápida si el punto inicial está cerca de la raíz.
•  Simple de implementar.

Limitaciones:

•  Puede fallar o divergir si la derivada es cero o si el punto inicial no está cerca de la raíz.
•  Requiere conocer la derivada de la función.

Código

FIGURA 7

import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from tabulate import tabulate
# Método de Newton-Raphson
def newton_raphson(f, valor_inicial, iteraciones=100, tolerancia=1e-6, precision=5):
    x = valor_inicial
    results = []
    for i in range(iteraciones):
        fx = round(f(x), precision)
        dfx = round(derivative(f, x, dx=tolerancia), precision)
        if dfx == 0:
            raise ValueError("La derivada es cero. El método no puede continuar.")
        x_new = round(x - fx / dfx, precision)
        results.append([i+1, x, fx, dfx, x_new])
        print(tabulate(results, headers=["Iteración", "x", "f(x)", "f'(x)", "Resultado"], tablefmt="grid"))
        if abs(x_new - x) < tolerancia:
            return x_new
        x = x_new
    raise ValueError("El método no convergió o faltan iteraciones.").
def graficar(f, raiz):

16

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

    # Graficar la función
    x = np.linspace(0, 3, 400)
    y = f(x)
    plt.plot(x, y, label='$f(x)$')
    plt.axhline(0, color='black',linewidth=0.5)
    plt.axvline(0, color='black',linewidth=0.5)
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
     # Marcar la raíz encontrada
    plt.plot(raiz, f(raiz), 'ro', label=f'Raíz: x = {raiz:.5f}')
      # Añadir leyenda y mostrar la gráfica
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfica de la función y su raíz')
    plt.show()
# Definir la función para la cual quieres encontrar la raíz
def f(x):
    return x**3 - x-4
# Valor inicial
valor_inicial = 1.0
# Encontrar la raíz utilizando el método de Newton-Raphson
raiz = newton_raphson(f, valor_inicial)
# Imprimir la raíz encontrada
print(f"La raíz encontrada es: {raiz}")
# Graficar la función y la raíz
graficar(f, raiz)

Búsqueda Binaria de raíces (Bisección)

Ejercicios búsqueda de raíces

1.   Para  cada  una  de  las  funciones  halle  un  intervalo  [𝑎, 𝑏] ,  de  manera  que  𝑓(𝑎)𝑦 𝑓(𝑏)  tengan  signo
contrario.

a)  𝑓(𝑥)=𝑒 𝑥 − 2 − 𝑥
b)  𝑓(𝑥)=cos(𝑥) + 𝑥
c)  𝑓(𝑥) = ln(𝑥) − 5 − 𝑥
d)  𝑓(𝑥) = 𝑥2 − 10𝑥 + 23

2.  Sea 𝑓(𝑥) = 3(𝑥 + 1) (𝑥 −

1
2

) (𝑥 − 1) aplique el método de búsqueda binaria de raíces en los siguientes

intervalos:
a)
[-1, 1.5]
b)
[-1.25, 2.5]

17

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

3.  Aplique el método de bisección para encontrar una solución aproximada con tolerancia de 10−3, para
las siguientes funciones en sus intervalos:
a)  √𝑥 − cos(𝑥) = 0, para 0 ≤ 𝑥 ≤ 1
b)  𝑥 − 2−𝑥 = 0, para 0 ≤ 𝑥 ≤ 1
c)  𝑒 𝑥 − 𝑥2 + 3𝑥 − 2 = 0. para 0 ≤ 𝑥 ≤ 1
d)  2𝑥 cos(𝑥) − (𝑥 + 1)2 = 0, para − 3 ≤ 𝑥 ≤ −2, para − 1 ≤ 𝑥 ≤ 0
e)  𝑥 cos(𝑥) − 2𝑥2 + 3𝑥 − 1 = 0, para 0.2 ≤ 𝑥 ≤ 0.3, para 1.2 ≤ 𝑥 ≤ 1.3

4.  Aplique el método de bisección para encontrar todas las raíces del polinomio dentro de 10−2, para 𝑥4 −
2𝑥3 − 4𝑥2 + 4𝑥 + 4, en:

a)
b)
c)
d)

[-2, -1]
[0,2]
[2,3]
[-1, 0]

5  sea  𝑓(𝑥) = (𝑥 + 2)(𝑥 + 1)(𝑥 − 1)3(𝑥 − 2) ,  ¿a  cuál  cero  la  función  converge,  estudie  los  siguientes
intervalos?

a)
b)
c)
d)

[-3, 2.5]
[-2.5, 3]
[-1.75, 1.5]
[-1.5, 1.75]

Use el método del punto fijo para

− 5𝑥,  𝑥∗𝜖 [0, 1],  𝑥0 = 0

1.  𝑓(𝑥) = 2𝑒 𝑥2
2.  𝑓(𝑥) = cos(𝑥),  𝑥∗𝜖 [1, 2],  𝑥0 = 1
3.  𝑓(𝑥) = 𝑒−𝑥 − 𝑥,  𝑥∗𝜖 [0, 1],  𝑥0 = 0
4.  𝑓(𝑥) = 𝑥3 − 𝑥 − 1,  𝑥∗𝜖 [1, 2],  𝑥0 = 1
𝑥
5.  𝑓(𝑥) = 𝜋 + 0.5 sin (
2

) − 𝑥,  𝑥∗𝜖 [0, 2𝜋],  𝑥0 = 0

6.  Use  manejo  algebraico  para  demostrar  que  las  siguientes  funciones  tienen  un  punto  fijo  en    𝑝,

exactamente cuando 𝑓(𝑝) = 0, donde 𝑓(𝑥)=𝑥4 + 2𝑥2 − 𝑥 − 3:

a.  𝑔(𝑥) = (3 + 𝑥 − 2𝑥2)

1
4

b.  𝑔(𝑥) = (

𝑥+3−𝑥4
2

1
2
)

7.  Demuestre que la función iterativa 𝑔(𝑥) = 2−𝑥 tiene un punto fijo en [

1
3

, 1]

8.  Use el método de punto fijo para convertir la expresión √3,  con exactitud de 10−4

18

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

9.  ¿En qué intervalo [a,b] convergerá la iteración del punto fijo con exactitud de 10−3? Para 𝑥 =
10. Hallar el intervalo [a, b] donde 𝑔(𝑥) = √𝑒𝑥

  Tiene un punto fijo.

3

5
𝑥2 + 2

Use el método de Aceleración Aitken

1.  𝑓(𝑥) =

𝜋
2

𝑥2 − 𝑥 − 2,  𝑥0 = 1.4 (halle 𝑔(𝑥))

2.  𝑓(𝑥) = cos(𝑥) − 𝑥,  𝑥0 = 0.5 (halle 𝑔(𝑥))

3
3.  𝑔(𝑥) = √3𝑥2 − 4𝑥 + 1
4.  𝑔(𝑥) = 𝑒−𝑥,  𝑥0 = 1

,  𝑥0 = 0.3

5.  𝑔(𝑥) = √3𝑥 − 2,  𝑥0 = 2

6.  𝑔(𝑥) = 𝐿𝑛(𝑥 + 1),  𝑥0 = 0.5
7.  𝑔(𝑥) = 1 − 𝑥3,  𝑥0 = 0.5

8.  𝑔(𝑥) =

1
2

(𝑥2 − 3),  𝑥0 = 0.5

9.  𝑔(𝑥) =

sin(𝑥)+5
𝑥2

,  𝑥0 = 2

10.  𝑔(𝑥) = 𝑥2,  𝑥0 = 0.4,   𝑥0 = 0.9,, 𝑥0 = 1.5

11.  𝑔(𝑥) =

3
2

𝑥 +

1
𝑥2,  𝑥0 = 0.25

 Ejercicios Newton-Raphson

1.  𝑓(𝑥) = (𝑥 − 1)2,  𝑥0 = 0
2.  𝑓(𝑥) = 𝑥3 − 2𝑥 − 5, 𝑥0 =  1.5
3.  𝑓(𝑥) = 𝑥5 − 𝑥 − 1, 𝑥0 = 1

4.  𝐴𝑝𝑟𝑜𝑥𝑖𝑚𝑎𝑟 6√2   (𝑐𝑜𝑛 𝑝𝑟𝑒𝑐𝑖𝑠𝑖ó𝑛 𝑑𝑒 8 𝑐𝑖𝑓𝑟𝑎𝑠)
5.  𝑓(𝑥) = 𝑒 𝑥 + 𝑥2 − 4,   𝑥0 =  0.5
6.  𝑓(𝑥) = 𝑥2 −  3𝑥  −  4, 𝑥0 =  8
7.  𝑓(𝑥) = ln(𝑥) − 1,   𝑥0 = 2
8.  𝑓(𝑥) = 𝑥4 −  16, 𝑥0 =  2
9.  𝑓(𝑥) =   𝑥3 −  2𝑥  +  1, 𝑥0 =   −1.5
10.  𝑓(𝑥) =   𝑒{3𝑥} −  4, 𝑥0 =  0
11.  𝑓(𝑥) = 𝑥2 −  2𝑥  +  1, 𝑥0 =  0
12.  (𝑥) =  𝑥𝑒−𝑥, 𝑥0 = −1

19

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Polinomio Interpolante de Lagrange

El  polinomio  interpolante  de  Lagrange  es  una  técnica  matemática  utilizada  para  aproximar  funciones
basándose en un conjunto de puntos dados. este método construye un polinomio que pasa exactamente
por esos puntos.

𝑛
𝑃(𝑥) = ∑ 𝑦𝑖𝐿𝑖(𝑥)
𝑖=0

,    𝐿𝑖(𝑥) = ∏

𝑛
𝑗=0
𝑖≠𝑗

𝑥−𝑥𝑗
𝑥𝑖−𝑥𝑗

Existencia y unicidad

FIGURA 8

Siempre  es  posible  construir  un  polinomio  de  interpolación  de  Lagrange  para  un  conjunto  de  puntos
distintos (𝑥𝑖, 𝑦𝑖), como 𝑃(𝑥).

Unicidad

𝑛
𝑃(𝑥) = ∑ 𝑦𝑖𝐿𝑖(𝑥)
𝑖=0

Dado un conjunto  (n+1) puntos distintos (𝑥𝑖, 𝑦𝑖), existe un polinomio  grado n que pasa exactamente por
todos esos puntos. Esto se garantiza por el teorema fundamental de la interpolación.

20

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 9

Básicamente lo que se busca es: conseguir un polinomio que según su grado sea similar a la función original
que está en estudio, o en todo caso si tenemos un paquete de datos discretos construir un polinomio que
permita interpolar valores en un dominio dado con cierto nivel de presión, un error local y global pequeño.
En  la  siguiente  figura  vemos  como  parte  de  la  función  tangente  se  compara  con  un  polinomio  que  la
interpola.

Errores locales y Globales

FIGURA 10

El  error  de  interpolación:  el  error  entre 𝑓(𝑥) y  el  polinomio 𝑃(𝑥),  donde 𝑥0 < 𝜉 < 𝑥𝑛 ,  es  un  número  en  el
intervalo de los puntos.

𝑓(𝑥) − 𝑃(𝑥) =

𝑓(𝑛+1)(𝜉)
(𝑛 + 1)!

𝑛
∏(𝑥 − 𝑥𝑖)
𝑖=0

21

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Aproximación de Taylor

la serie de Taylor es una herramienta matemática que permite aproximar funciones mediante una suma
infinita de términos polinómicos. cada término se calcula utilizando las derivadas de la función en un punto
específico.

FIGURA 11

Cálculo de errores

1.  Construir un polinomio interpolante de Lagrange.

𝑛
𝑃(𝑥) = ∑ 𝑦𝑖𝐿𝑖(𝑥)
𝑖=0

𝑛
𝐿𝑖(𝑥) = ∏
𝑗=0
𝑖≠𝑗

𝑥 − 𝑥𝑗
𝑥𝑖 − 𝑥𝑗

2.  Calcular las bases de Lagrange

3.  Determinar el valor máximo en la derivada

4.

Aplicar la cota

𝑀𝑛+1 = 𝑚𝑎𝑥|𝑓(𝑛+1)(𝜉)|

|𝐸(𝑥)| ≤

𝑀𝑛+1
(𝑛 + 1)!

𝑛

|∏(𝑥 − 𝑥𝑖)
|
𝑖=0

22

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

5. Verificar con el valor real (error local)

|𝐸(𝑥)| = |𝑓(𝑥) − 𝑃(𝑥)|

Código

import numpy as np
import matplotlib.pyplot as plt
def polinomio_lagrange(x, x_puntos, y_puntos):
    n = len(x_puntos)
    L = 0
    for i in range(n):
        # Calcular el polinomio base de Lagrange
        li = 1
        for j in range(n):
            if i != j:
                li *= (x - x_puntos[j]) / (x_puntos[i] - x_puntos[j])
        L += y_puntos[i] * li
    return L
def reconstruccion_lagrange(x_puntos, y_puntos):
    n = len(x_puntos)
    coeficientes = np.zeros(n)
    for i in range(n):
        # Calcular el polinomio base de Lagrange
        li = np.poly1d([1])
        for j in range(n):
            if i != j:
                li *= np.poly1d([1, -x_puntos[j]]) / (x_puntos[i] - x_puntos[j])
        coeficientes += y_puntos[i] * li.coefficients

    return coeficientes

# Definir los puntos dados
x_puntos = np.array([0,1,2, 3,4])
y_puntos = np.array([1,2,0, 2,3])
# Crear un conjunto de valores x para graficar
x = np.linspace(min(x_puntos) - 1, max(x_puntos) + 1, 400)
y = [polinomio_lagrange(xi, x_puntos, y_puntos) for xi in x]
# Graficar los puntos dados
plt.scatter(x_puntos, y_puntos, color='red', label='Puntos dados')
# Graficar el polinomio de Lagrange
plt.plot(x, y, label='Polinomio de Lagrange')
# Añadir leyenda y mostrar la gráfica
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

23

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

plt.title('Interpolación de Lagrange')
plt.grid(True)
plt.show()
# Reconstruir el polinomio de Lagrange
coeficientes = reconstruccion_lagrange(x_puntos, y_puntos)
polinomio = np.poly1d(coeficientes)
# Imprimir el polinomio reconstruido
print(f"El polinomio de Lagrange es:\n{polinomio}")

Diferencias finitas progresivas

𝑓′

(𝑥𝑖) =

𝑓(𝑥𝑖+1)−𝑓(𝑥𝑖)
ℎ

,   𝑓′′

(𝑥𝑖) =

𝑓(𝑥𝑖+2)−2𝑓(𝑥𝑖+1)+𝑓(𝑥𝑖)
ℎ2

Diferencias divididas Regresivas

𝑓′

(𝑥𝑖) =

𝑓(𝑥𝑖)−𝑓(𝑥𝑖−1)
ℎ

,   𝑓′′

(𝑥𝑖) =

𝑓(𝑥𝑖)−2𝑓(𝑥𝑖−1)+𝑓(𝑥𝑖−2)
ℎ2

Diferencias finitas Centrales

𝑓′

(𝑥𝑖) =

𝑓(𝑥𝑖+1)−𝑓(𝑥𝑖−1)
2ℎ

,  𝑓′′

(𝑥𝑖) =

𝑓(𝑥𝑖+1)−2𝑓(𝑥𝑖)+𝑓(𝑥𝑖−1)
ℎ2

En este gráfico se resume los tres casos posibles

FIGURA 12

24

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Código

# Definir la funcion
def f(x):
return x**3 - 2*x + 1
# Punto y paso
x = 2
h = 0.1

# Diferencias finitas centradas para la primera derivada
def primera_derivada(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Diferencias finitas centradas para la segunda derivada
def segunda_derivada(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)

# Calcular las derivadas
primera = primera_derivada(f, x, h)
segunda = segunda_derivada(f, x, h)

# Imprimir los resultados
print(f"Primera derivada en x = {x}: {primera}")

print(f"Segunda derivada en x = {x}: {segunda}")

Ejercicios polinomios interpolantes y derivación numérica

Para los siguientes construir un polinomio interpolante de Lagrange, para los casos donde haya una función
a la que comparar, calcule los errores globales y locales, y grafique la función y su polinomio interpolante:

1.  Hallar el polinomio que pasa por los puntos (1,1), (2,4), (3,9)
2.  Reconstruir la función que pasa por los puntos (0,1), (1,3), (2,2), (3,5)
3.  Dado el siguiente el siguiente conjunto de puntos, hallar el valor de (𝑏): : 𝑥 = [0,1,2,3,4], 𝑦 = [1,2, 𝑏, 2,3]
4.  Hallar el polinomio interpolante de Lagrange para: 𝑥 = [0,1,2,3,4], 𝑓(𝑥) = [1,2,0,2,3]
5.  Hallar el polinomio interpolante de Lagrange para: [0,1,2], 𝑦 = [1,3,0]
6.  Hallar el polinomio de segundo grado que pase por: 𝑥 = [1,2,3], 𝑦 = [10,15,80]
7.  Construir un polinomio con los datos: 𝑥 = [2,4,5], 𝑓(𝑥) = [5,6,3]
8.  Construir un polinomio que interpole: 𝑥 = [−2,0,2], 𝑓(𝑥) = [0,1,0]
9.  Aproximar 𝑓(𝑥) = 𝑠𝑖𝑛(𝑥), con , 𝑥 ∈ [0, 𝜋], use un polinomio de Lagrange de 2 grado
10.  Construir el polinomio interpolante de Lagrange para: 𝑥 = [0,1,2], 𝑓(𝑥) = [1,2,7]
11.  Usar los nodos 𝑥0 =  2, 𝑥1 =  2.5, 𝑥2 =  4.5, para construir el polinomio  interpolante de Lagrange que
aproxime 𝑓(𝑥) =

1
𝑥

25

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

), use los nodos 𝑥0 =  1, 𝑥1 =  2, 𝑥2 =  3, use interpolación de Lagrange de grado 2

12.  Sea 𝑓(𝑥) = 2sin (
para aproximar:

𝜋𝑥
6

a)  𝑓(4)
b)  𝑓(1.5)

13.  Use los siguientes nodos 𝑥0 =  0, 𝑥1 =  0.6, 𝑥2 = 0.9, construir que aproxime 𝑓(0.45)
a)  𝑓(𝑥) = co s(𝑥)
b)  𝑓(𝑥) =   √𝑥 + 1
c)  𝑓(𝑥) = 𝑙𝑛(𝑥  +  1)

Ejercicios de Diferencia Finitas

1.  Use diferencias finitas centrales para hallar la derivada aproximada de 𝑓(𝑥) = sin(𝑥), en cada punto

de 𝑥 = [0, 0.1, 0.2, 0.3, 0.4, 0.5], con ℎ = 0.1

2.  Hallar la derivada de 𝑓(𝑥) = 𝑒 𝑥 en cada punto 𝑥 = [0, 0.1, 0.2, 0.3, 0.4, 0.5], con ℎ = 0.1
3.  Sea 𝑓(𝑥) = 𝑥3 − 𝑥, calcular la derivada primera y segunda en 𝑥 = 1, con ℎ = 0.1
4.  Sea 𝑓(𝑥) = 𝑒 𝑥 sin(𝑥),
a)  Halle 𝑓′(1) usando diferencias finitas centrales y un paso de  ℎ = 0.01
b)  Halle el error absoluto
c)  Halle  𝑓′′(1) usando diferencia finitas centrales
5.  Comparar la aproximación por diferencias finitas de segundo orden exactas hacia adelante, atrás y

centrales   de  𝑓(𝑥) = 𝑒−2𝑥 − 𝑥, para 𝑥 = 2

6 calcule la velocidad y la aceleración en cada punto usando el método de diferencias finitas centrales
salvo en los extremos donde pueda usar progresiva o regresiva. Completar la tabla de valores

0
0

t(seg)

𝑥(𝑚)
𝑣(𝑚 𝑠⁄ )
𝑎(𝑚 𝑠2⁄ )

7.  Igual al anterior

0
0

t(seg)

𝑥(𝑚)
𝑣(𝑚 𝑠⁄ )
𝑎(𝑚 𝑠2⁄ )

1
1.9

2
4.2

3
7.8

4
12

5
17

6
25

7
32

8
42

TABLA 2

2
0.7

4
2

6
3.5

8
5.4

10
6.5

12
7.5

14
8.5

16
8.5

Analice el comportamiento de la velocidad y la aceleración

TABLA 3

26

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Reglas de Newton Cotes

Las reglas de Newton-Cotes son una familia de métodos de integración numérica utilizadas para aproximar
integrales  definidas.  Se  basan  en  la  interpolación  de  la  función  a  integrar  mediante  polinomios  y  en  la
evaluación de la integral de estos polinomios.

Regla del rectángulo medio compuesta

FIGURA 13

𝑥𝑖−1 + 𝑥𝑖
2

)

𝑏

𝑛

∫ 𝑓(𝑥)𝑑𝑥 ≈ ℎ ∑ 𝑓 (
𝑎

𝑖=1
𝑛−1

𝑏

∫ 𝑓(𝑥)𝑑𝑥 ≈ ℎ ∑ 𝑓(𝑥̅𝑖)
𝑎

𝑖=0

Donde 𝑥̅𝑖= 𝑝𝑢𝑛𝑡𝑜 𝑚𝑒𝑑𝑖𝑜,  ℎ =

(𝑏−𝑎)
𝑛

Existen varias reglas de Newton-Cotes, dependiendo del número de puntos utilizados en la interpolación.

Regla del Trapecio

Regla del trapecio (Newton-Cotes de orden 1): Utiliza dos puntos para aproximar la integral como la suma
de áreas de un trapezoide.

𝑏

∫ 𝑓(𝑥)𝑑𝑥 ≈
𝑎

(𝑏 − 𝑎)
2

[𝑓(𝑎) + 𝑓(𝑏)]

27

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Forma compuesta

Se divide el área de subintervalos para mejorar la precisión, acá se resume la formula:

FIGURA 14

𝑛−1

(𝑓(𝑎) + 2 ∑ 𝑓(𝑎 + 𝑖ℎ) + 𝑓(𝑏)

)

𝑖=1

𝑏

∫ 𝑓(𝑥)𝑑𝑥 ≈
𝑎

ℎ
2

Donde h es el paso, y n el número de subintervalos:

ℎ =

(𝑏 − 𝑎)
𝑛

𝐸𝑇 = −

(𝑏 − 𝑎)3
12𝑛2 𝑓′′

(𝜉)

Error de truncamiento

Regla de Simpson

Regla de Simpson 1/3, (Newton-Cotes)

a)  Usa  tres  puntos y ajusta un  polinomio  cuadrático para mejorar la precisión. Para esta regla  (n) solo
puede ser par

28

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑏

∫ 𝑓(𝑥)𝑑𝑥
𝑎

≈

ℎ
3

(𝑓(𝑎) + 4𝑓 (

𝑎 + 𝑏
2

) + 𝑓(𝑏))

Figura 15

ℎ =

(𝑏 − 𝑎)
2

Error de truncamiento

𝐸 = −

(𝑏 − 𝑎)5
2880

𝑓(4)(𝜉)

𝑑𝑜𝑛𝑑𝑒 𝜉𝜖[𝑎, 𝑏]

𝐸 = −

ℎ5
90

𝑓(4)(𝜉)

Reglas de Simpson 1/3 compuesta

𝑏

∫ 𝑓(𝑥)𝑑𝑥
𝑎

≈

ℎ
3

(𝑓(𝑎) + 4 ∑ 𝑓(𝑎+𝑖ℎ) + 2 ∑ 𝑓(𝑎+𝑖ℎ) + 𝑓(𝑏)

)

𝑖𝑚𝑝𝑎𝑟𝑒𝑠

𝑝𝑎𝑟𝑒𝑠

29

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 16

Error de truncamiento

𝐸𝑐𝑜𝑚𝑝 = −

𝐸𝑐𝑜𝑚𝑝 = −

(𝑏 − 𝑎)5
180𝑛4 𝑓(4)(𝜉)
(𝑏 − 𝑎)
ℎ4𝑓(4)(𝜉)
180

(b − a)
𝑛

ℎ =

{

n es par

Simpson (3/8)

Reglas de Simpson 3/8 y otras de orden superior: Utilizan más puntos y polinomios de mayor grado para
obtener aproximaciones más precisas. Es una extensión de la regla 1/3 pero esta usa 4 puntos. n=3

FIGURA 17
30

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑏

∫ 𝑓(𝑥)𝑑𝑥 ≈
𝑎

3ℎ
8

(𝑓(𝑎) + 3𝑓(𝑥1) + 3𝑓(𝑥2) + 𝑓(𝑏))

Error de truncamiento

ℎ =

(𝑏 − 𝑎)
3

𝐸𝑇 = −

3
80

ℎ5𝑓(4)(𝜉)

Simpson 3/8 compuesta, n debe ser múltiplo de 3

𝑏

∫ 𝑓(𝑥)𝑑𝑥 ≈
𝑎

3ℎ
8

ℎ =

(𝑏 − 𝑎)
3𝑛

(𝑓(𝑎) + 3 ∑ 𝑓(𝑥𝑖)

+ 3 ∑ 𝑓(𝑥𝑗) + 2 ∑ 𝑓(𝑥𝑖)

+ 𝑓(𝑏))

𝑖𝑚𝑝𝑎𝑟𝑒𝑠

𝑝𝑎𝑟𝑒𝑠

𝑚𝑢𝑙𝑡. 3

Error de truncamiento

𝐸 = −

(𝑏 − 𝑎)5
6480

𝑓(4)(𝜉)

Codigo1: regla del rectángulo medio compuesta

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Número de subintervalos
n = 10  # Ajusta según la precisión deseada
# Paso
h = (b - a) / n
# Puntos medios
x_medio = np.linspace(a + h/2, b - h/2, n)
# Aplicamos la regla del rectángulo medio compuesta
integral = h * np.sum(funcion(x_medio))
print(f"Integral aproximada con la regla del rectángulo medio compuesta: {integral:.4f}")

codigo2: regla del trapecio simple

31

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por cualquier otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi/2  # Límite superior
# Evaluamos la función en los extremos
fa = funcion(a)
fb = funcion(b)
# Aplicamos la regla del trapecio simple
integral = (b - a) / 2 * (fa + fb)
print(f"Integral aproximada con la regla del trapecio simple: {integral:.4f}")

codigo 3: regla del trapecio compuesta

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Número de subintervalos
n = 10  # Ajusta según la precisión deseada
# Paso
h = (b - a) / n
# Puntos de evaluación
x = np.linspace(a, b, n + 1)
y = funcion(x)
# Aplicamos la regla del trapecio compuesta
integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[-1])
print(f"Integral aproximada con la regla del trapecio compuesta: {integral:.4f}")

codigo4: regla de Simpson simple

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por cualquier otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Punto medio

32

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

m = (a + b) / 2
# Evaluamos la función en los tres puntos
fa = funcion(a)
fm = funcion(m)
fb = funcion(b)
# Aplicamos la regla de Simpson simple
integral = (b - a) / 6 * (fa + 4 * fm + fb)
print(f"Integral aproximada con Simpson simple: {integral:.4f}")

codigo 5: regla de Simpson compuesta

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por cualquier otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Número de subintervalos (debe ser par)
n = 10  # Ajusta según la precisión deseada
# Paso
h = (b - a) / n
# Puntos
x = np.linspace(a, b, n + 1)
y = funcion(x)
# Aplicamos la regla de Simpson compuesta
S = y[0] + y[-1] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2])
integral = (h / 3) * S
print(f"Integral aproximada con Simpson compuesta: {integral:.4f}")

codigo 6: regla de Simpson 3/8 simple

import numpy as np
# Definimos la función a integrar
def funcion(x):
return np.sin(x)  # Puedes cambiarla por otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Paso
h = (b - a) / 3
# Puntos de evaluación
x1 = a + h
x2 = a + 2*h
# Evaluamos la función en los puntos
fa = funcion(a)

33

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

fx1 = funcion(x1)
fx2 = funcion(x2)
fb = funcion(b)
# Aplicamos la regla de Simpson 3/8 simple
integral = (3 * h / 8) * (fa + 3 * fx1 + 3 * fx2 + fb)

print(f"Integral aproximada con Simpson 3/8 simple: {integral:.4f}")

codigo 7: la regla de Simpson 3/8 compuesta

import numpy as np
# Definimos la función a integrar
def funcion(x):
    return np.sin(x)  # Puedes cambiarla por otra función
# Límites de integración
a = 0  # Límite inferior
b = np.pi  # Límite superior
# Número de subintervalos (debe ser múltiplo de 3)
n = 9  # Ajusta según la precisión deseada
# Paso
h = (b - a) / n
# Puntos de evaluación
x = np.linspace(a, b, n + 1)
y = funcion(x)
# Aplicamos la regla de Simpson 3/8 compuesta
S = y[0] + y[-1] + 3 * np.sum(y[1:n:3]) + 3 * np.sum(y[2:n:3]) + 2 * np.sum(y[3:n-1:3])
integral = (3 * h / 8) * S

print(f"Integral aproximada con la regla de Simpson 3/8: {integral:.4f}")

Ejericicios

1.  Sea ∫ (6 + 3 cos(𝑥)

)𝑑𝑥:

𝜋
2
0

a)  Use la regla del trapecio para aproximar la solucion con 𝑛 = 2, 𝑛 = 4
b)  Use la regla de Simpson (1/3) con 𝑛 = 4
c)  Use la regla de Simpson (3/8) con 𝑛 = 3, 𝑦 𝑛 = 6

2.  Sea ∫ (𝑥 +

2
1

3
)

2
𝑥

𝑑𝑥

a)  Use la solucion analitica para calcular los errores ralativos porcentuales para la regla del trapacio.
3.  Sea ∫ (4𝑥 − 3)3 𝑑𝑥

3
−3

34

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

a)  Integre de forma analitica y use la regla de Simpson con 𝑛 = 3, 𝑦 𝑛 = 6 para comparar la aproximacion
(use 3/8)

3
4.  Sea ∫ (𝑥2𝑒 𝑥)
0

𝑑𝑥:

a)  Integre de forma analitica y numerica, emplee la regla del trapecio con 𝑛 = 4
b)  Use la regla de Simpson (1/3) con 𝑛 = 4
c)  Calcules los errores de truncamiento

4
0

5.  Sea ∫ (1 − 𝑒−2𝑥) 𝑑𝑥
:
a)  Integre con la regla del trapecio con 𝑛 = 4
b)  Integre usando la regla de Simpdon (1/3) con 𝑛 = 4

𝜋
6.  Sea ∫ (sin(𝑥)) 𝑑𝑥
0

a)   Integre con la regla del trapecio con 𝑛 = 10
b)  Integre usando la regla de Simpdon (1/3) con 𝑛 = 4

7.  Sea ∫ 𝑒 𝑥2

1
0

𝑑𝑥

a)  Integre con la regla de Simpson (1/3) con, 𝑛 = 4, 𝑛 = 10
b)  Integre usando la regla del rectángulo con 𝑛 = 5

2
8.  Sea ∫ 𝑥2𝑑𝑥
0

a)  Integre con la regla del rectángulo punto medio  con, 𝑛 = 4

2
9.  Sea ∫ √1 + 𝑥2
0

4

𝑑𝑥

a)  Integre usando la regla del rectángulo izquierdo   con, 𝑛 = 8

6
10.  Sea ∫
1

𝑥2
6

𝑑𝑥

a)  Integre usando la regla del trapecio   con, 𝑛 = 5

11.  Sea ∫ 𝑒 𝑥4

1
−1

𝑑𝑥

a)  Integre usando la regla del trapecio   con, 𝑛 = 5
2
12.  Sea ∫
1

1
𝑥2 𝑑𝑥

a)  Integre usando la regla del trapecio   con, 𝑛 = 5

35

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

El método de Monte Carlo

El  método  de  Monte  Carlo  es  una  técnica  matemática  utilizada  para  aproximar  soluciones numéricas  a
problemas  complejos  mediante  el  uso  de  muestreo  aleatorio  y  probabilidad.  Su  nombre  proviene  del
famoso casino de Monte Carlo, debido al enorme papel del azar en este método.

Cómo funciona

FIGURA 18

El método de Montecarlo utiliza simulaciones repetitivas basadas en números aleatorios para aproximar
soluciones a problemas complejos. Se suele emplear en situaciones donde es difícil o imposible obtener
una solución analítica exacta. Su procedimiento básico sigue estos pasos:

1.  Definir el problema y el dominio de posibles valores.
2.  Generar valores aleatorios dentro del dominio.
3.  Evaluar cada valor en la función del problema.
4.  Calcular la estimación basada en los resultados obtenidos.

Características Principales

1.  Se basa en repeticiones aleatorias (simulaciones) para estimar resultados.
2.  Es útil cuando el problema es demasiado complicado para resolverse analíticamente.
3.  Se aplica en áreas como física, finanzas, ingeniería, inteligencia artificial y mas.

36

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Método gráfico para integracion numérica

En  estos  casos  se  busca  inscribir  el  area  de  interes  en  un  cuadrado  o  rectangulo,  generamos  numeros
aleatorios de tan manera que se pueda comparar los numeros que quedan bajo la curva que se llamaran
puntos de exitos con el total de los puntos generados.

Supongamos que quieres estimar el área de una región R en el plano. La idea es:

1.  Encerrar la región R en una caja rectangular que sea fácil de describir. Por ejemplo, que tenga límites

[𝑥𝑚𝑖𝑛, 𝑥𝑚𝑎𝑥]×[𝑦𝑚𝑖𝑛, 𝑦𝑚𝑎𝑥],  [𝑦_{𝑚𝑖𝑛}, 𝑦_{𝑚𝑎𝑥}].

2.  Generar muchos puntos aleatorios uniformemente distribuidos dentro del rectángulo.
3.  Contar qué fracción de puntos cae dentro de R.
4.  Calcular el área estimada como:

Á𝑟𝑒𝑎(𝑅) ≈ Á𝑟𝑒𝑎 𝑟𝑒𝑐𝑡á𝑛𝑔𝑢𝑙𝑜 ×

𝑛ú𝑚𝑒𝑟𝑜 𝑑𝑒 𝑝𝑢𝑛𝑡𝑜𝑠 𝑑𝑒𝑛𝑡𝑟𝑜 𝑑𝑒 𝑅
𝑛ú𝑚𝑒𝑟𝑜 𝑡𝑜𝑡𝑎𝑙 𝑑𝑒 𝑝𝑢𝑛𝑡𝑜𝑠

FIGURA 19

Este ejemplo se estimo con el uso de 500 puntos aleatorios, basicamente usando un código que los genere
y  cuente  cuando  quedan  debajo  de  la  curva  y  con  esa  informacion  establecemos  la  relación,  ahora  si
queremos más precisión es necesario aumente el número de muestras generadas.

Ejemplo clásico estimar π (pi).
El objetivo es estimar pi usando aleatoriedad.
Algunos pasos:

1.  Dibuja un cuadrado de lado 2 y un circulo inscrito de radio 1 (área del circulo = π).

37

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

2. Genera puntos aleatorios dentro del cuadrado.
3. Cuenta los puntos que caen dentro del circulo (puntos de éxito), la distancia al centro <= 1

𝜋 ≈ 4 (

𝑝𝑢𝑛𝑡𝑜𝑠 𝑑𝑒𝑛𝑡𝑟𝑜 𝑑𝑒𝑙 𝑐𝑖𝑟𝑐𝑢𝑙𝑜
𝑡𝑜𝑡𝑎𝑙 𝑑𝑒 𝑝𝑢𝑛𝑡𝑜𝑠

)

Código python

import random
# Número de puntos aleatorios
num_puntos = 1000000
puntos_dentro = 0  # Contador de puntos dentro del círculo
# Generamos los puntos aleatorios
for _ in range(num_puntos):
    x = random.uniform(-1, 1)  # Coordenada x aleatoria en [-1,1]
    y = random.uniform(-1, 1)  # Coordenada y aleatoria en [-1,1]

    # Si el punto cae dentro del círculo unitario, sumamos al contador
    if x**2 + y**2 <= 1:
        puntos_dentro += 1
# Estimación de pi usando la relación entre área del círculo y cuadrado
pi_estimado = (puntos_dentro / num_puntos) * 4
print(f"Estimación de π usando Montecarlo: {pi_estimado}")

Herramientas estadisticas necesarias (Distribucion Normal)

FIGURA 20

38

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Formulas:

𝜎 = √

1
(𝑛 − 1)

(𝑓(𝑥𝑖) − 𝑥̅)2

𝐸𝐸 =

𝜎

√𝑛

𝜎
[𝐼̂ − 𝑧𝛼 2⁄
√𝑛
(Intervalo de confianza)

,  𝐼̂ + 𝑧𝛼 2⁄

𝜎
√𝑛

]

𝜎 = 𝑑𝑒𝑠𝑣𝑖𝑎𝑐𝑖ó𝑛 𝑒𝑠𝑡á𝑛𝑑𝑎𝑟

𝐸𝐸 = 𝐸𝑟𝑟𝑟𝑜𝑟 𝑒𝑠𝑡á𝑛𝑑𝑎𝑟

𝐼̂ = 𝐼𝑛𝑡𝑒𝑔𝑟𝑎𝑙 𝑒𝑠𝑡𝑖𝑚𝑎𝑑𝑎

𝐼̂ ± 𝑧𝛼 2⁄

𝜎
√𝑛

 (para calcular lo límites)

𝑏
𝐼̂ =   ∫ 𝑓(𝑥)𝑑𝑥
𝑎

= (𝑏 − 𝑎)

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

IC

𝑧𝛼 2⁄

90

1.645

95

1.96

TABLA 4

99

2.576

Métodos para generar números con distribución uniforme y los generadores más comunes en programación
incluyen:

❖  en Python: ranom.uniform(a,b) Devuelve un número aleatorio en el intervalo ([a, b]).

import random
# Generar 5 números aleatorios uniformes en el rango [0, 1]
for _ in range(10):
    print(random.uniform(0, 1))

Primera ejecución

Segunda ejecución

0.5415297812161269
0.08528259751738321
0.978464626756584
0.6283191030955314

0.5415297812161269
0.08528259751738321
0.978464626756584
0.6283191030955314

Los valores cambia para cada ejecucion del codigo

39

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

❖  en Python: ranom.seed(42) Devuelve un número aleatorio en el intervalo ([a, b]). Con semilla en 42

y siempre va devolver el mismo resultado

import random
random.seed(42)  # Establece la semilla para la generación de números aleatorios
# Generar 10 números aleatorios uniformes en el rango [0, 1]
for _ in range(5):
    print(random.uniform(0, 1))

Todas las ejecuciones del codigo repiten la misma salida (util para reproducibilidad de esperimentos)

0.6394267984578837
0.025010755222666936
0.27502931836911926
0.22321073814882275
0.7364712141640124

❖  Aplicación (cálculo de área)

Método Integración Montecarlo usando  la media

La  media  ( 𝑥̅ )  de  las  muestras  se  utiliza  como  estimador  del  valor  de  la  integral  porque  bajo  ciertas
condiciones converge al valor esperado de la función que estamos integrando. Esto se basa en la ley de los
grandes números (LGN) y en propiedades estadísticas de los estimadores.

1.  Fundamento  matemático:  La
multidimensional.
Si adaptamos el problema para muestrea 𝑥 uniformemente, podemos expresar la integral como un valor
esperado.

integral  como  valor  esperado  𝐼 = ∫ 𝑓(𝑥) 𝑑𝑥 ,  sobre  un  dominio

𝐼 = 𝑉𝑜𝑙𝑢𝑚𝑒𝑛(

).  𝐸|𝑓(𝑥)|

𝐸|𝑓(𝑥)| es el valor esperado de 𝑓(𝑥) cuando 𝑥 se distribuye uniformemente

Estimación  Montecarlo  por  promedio  muestral  tomando  n=  muestral  𝑥1, 𝑥2, … , 𝑥𝑛    Uniformemente
distribuidos. Entonces calculamos el promedio de las evaluaciones de 𝑓 en estas muestras

𝐼̂= Es la estimación de la integral

𝑥̅ =

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

𝐼̂ = 𝑉𝑜𝑙𝑢𝑚𝑒𝑛(

40

)

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Convergencia por la ley de los grandes números

Esta ley establece que si las muestras son independientes e idénticamente distribuidas, entonces:

lim
𝑛→∞

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

= 𝐸|𝑓(𝑥)|

𝐼̂= Es la estimación de la integral converge al valor verdadero 𝐼 cuando 𝑛 → ∞
Casi 1: integral de una variable 1D, en el intervalo [𝑎, 𝑏] :

Integral con dominio no estandarizado

𝑏
𝐼 =   ∫ 𝑓(𝑥)𝑑𝑥
𝑎

= (𝑏 − 𝑎)

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

𝑏
𝐼 =   ∫ 𝑓(𝑥)𝑑𝑥
𝑎

= (𝑏 − 𝑎)

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖)
𝑖=1

𝐼̂= Es la estimación de la integral converge al valor verdadero 𝐼 cuando 𝑛 → ∞
𝑣𝑜𝑙𝑢𝑚𝑒𝑛 (𝑏 − 𝑎) ≠ 1
𝑀𝑢𝑒𝑠𝑡𝑟𝑎 𝑥𝑖~𝑢𝑛𝑖𝑓𝑜𝑟𝑚𝑒 (𝑎, 𝑏)
𝑥𝑖 = 𝑎 + (𝑏 − 𝑎)𝑢𝑖
𝑢𝑖 ∈ (0,1)

Caso 2: Integrales múltiples:

𝑏

𝑑

𝐼 = ∫ ∫ 𝑓(𝑥, 𝑦)𝑑𝑦𝑑𝑥

𝑎

𝑐

𝐼̂ = (𝑏 − 𝑎)(𝑐 − 𝑑)

1
𝑛

𝑛
∑ 𝑓(𝑥𝑖
𝑖=1

, 𝑦𝑖)

𝑣𝑜𝑙𝑢𝑚𝑒𝑛 (𝑏 − 𝑎)(𝑑 − 𝑐) 𝑎𝑟𝑒𝑎 𝑑𝑒𝑙 𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑢𝑙𝑜
{
𝑀𝑢𝑒𝑠𝑡𝑟𝑎 𝑥𝑖~𝑢𝑛𝑖𝑓𝑜𝑟𝑚𝑒 𝑒𝑛 [𝑎, 𝑏]. [𝑐, 𝑑]

Código

import numpy as np
def monte_carlo_with_ci(f, a, b, N):
    x = np.random.uniform(a, b, N)
    f_x = f(x)
    mean_f = np.mean(f_x)
    s = np.std(f_x, ddof=1)  # Usando N-1

41

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

        z = 1.96  # Para confianza del 95%
    SE = s / np.sqrt(N)
    margin_error = z * SE
    IC = ((b-a)*mean_f - margin_error, (b-a)*mean_f + margin_error)

    return (b - a) * mean_f, IC

# Ejemplo:
integral, IC = monte_carlo_with_ci(lambda x: np.exp(-x**2), 0, 1, 10000)
print(f"Estimación: {integral:.6f}")
print(f"IC 95%: [{IC[0]:.6f}, {IC[1]:.6f}]")

import numpy as np
def monte_carlo_with_ci(f, a, b, N):
    x = np.random.uniform(a, b, N)
    f_x = f(x)
    mean_f = np.mean(f_x)
    s = np.std(f_x, ddof=1)  # Usando N-1

    z = 1.96  # Para confianza del 95%
    SE = s / np.sqrt(N)
    margin_error = z * SE
    IC = ((b-a)*mean_f - margin_error, (b-a)*mean_f + margin_error)

    return (b - a) * mean_f, IC

# Ejemplo:
integral, IC = monte_carlo_with_ci(lambda x: np.exp(-x**2), 0, 1, 10000)
print(f"Estimación: {integral:.6f}")
print(f"IC 95%: [{IC[0]:.6f}, {IC[1]:.6f}]")

42

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios de Montecarlo

1.  Cree un modelo matemático que aproxime 𝜋 usando un código para generar 𝑛 = 10000 números aleatorios
para simular un modelo Montecarlo. (muestreo por rechazo), puntos de éxito dentro de un cuadrado de lado
2.

2.  Use  Estimación  por muestreo  aleatorio (Random  Sampling  Estimation),  para  aproximar la  integral; 𝐼 =

1
∫ 𝑒−𝑥2
0

𝑑𝑥

 con un intervalo de confianza del 99,7% y un máximo de error de 1

.
100⁄

3.  Estimar la integral 𝐼 = ∫ 𝐿𝑛(𝑥) 𝑑𝑥

, usando Montecarlo con un intervalo de confianza del 95% y un error

máximo permitido de 0,01.

5
2

4.  Estimar 𝐼 = ∫ √𝑥 𝑑𝑥

4
1

, con una muestra de 𝑛 = 5000.

a)  Calcule la desviación y error estándar.
b)  Calcule el intervalo de confianza para 99%, use 𝑧0.05 = 2,576.

5.  Estimar la integral, ∫ sin 𝑥 𝑑𝑥
intervalo de confianza del 95%.

𝜋
0

, usando Montecarlo con una muestra uniforme de 𝑛 = 10000, y un

6.  Estimar la integral doble 𝐼 = ∫ ∫ 𝑒 𝑥+𝑦 𝑑𝑦 𝑑𝑥

2
0
intervalo de confianza del 90%.

3
1

,

 usando Montecarlo con una muestra de 𝑛 = 50000 y un

7.  Estimar la integral doble 𝐼 = ∫ ∫ 𝑥2 + 𝑦2

𝑑𝑦 𝑑𝑥

, usando Montecarlo con 𝑛 = 100000 y un intervalo de

1
0

1
0

confianza del 95%.

1
8.  Estimar la integral 𝐼 = ∫
0

para 95%.

1
𝑥2+1

𝑑𝑥

, usando una muestra de 𝑛 = 5000, calculo los intervalos de confianza

𝜋
9.  Estimar 𝐼 = ∫
0

sin 𝑥
𝑥

𝑑𝑥

, use una muestra de 𝑛 = 10000, intervalo de confianza 95%.

10.  Use un método grafico para modelar el rechazo por muestreo para Montecarlo que permita aproximar el

área contenida en las curvas: 𝑓(𝑥) = 𝑥2, 𝑔(𝑥) = √𝑥, en el intervalo 𝑥 ∈ [0,1].

11. Escriba un código para un simulador en Python para estimar mediante Monte Carlo la probabilidad
de éxito de una inserción orbital tras un burn impulsivo con incertidumbres en la magnitud del Δv
producido por el motor y en el tiempo de encendido.  Además, calcula el margen adicional de Δv
requerido para alcanzar un 99% de probabilidad de éxito.

12. Escriba un código para un simulador en Python que estime el precio de una call europea vía Monte
Carlo (validando contra la fórmula de Black–Scholes) y calcula el Value at Risk (VaR) a 99% a 1 día
para una cartera simple formada por una acción y la opción.

43

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ecuaciones diferenciales
Métodos de Runge Kutta

Son un conjunto de métodos iterativos para aproximar ecuaciones diferenciales ordinarias basados en el
problema  de  valor  inicial  (Cauchy)  en  el  cual  se  predice  una  nueva  pendiente  proyectada  a  un  paso  de
distancia (constante) y lo que diferencia los diversos métodos es el como se calcula  la pendiente. Antes
del  siglo  XX,  la  resolución  de  EDO  se  apoyaba  principalmente  en:  Métodos  analíticos  (separación  de
variables, ecuaciones exactas, etc.). o Métodos numéricos simples, como el método de Euler (siglo XVIII).
que era fácil de implementar, pero: Tenía baja precisión, era inestable para muchos problemas físicos. El
matemático alemán Carl David Tolmé Runge (1856–1927), profesor en la Universidad de Gotinga, fue uno
de los primeros en sistematizar métodos numéricos de mayor orden para EDO. A fines del siglo XIX (≈ 1895),
Runge propuso métodos que: Evaluaban la pendiente en varios puntos dentro del intervalo. Combinaban
estas pendientes para obtener una mejor aproximación. Su idea central fue superar la aproximación lineal
de Euler usando información intermedia. Esto sentó las bases de los métodos que hoy llevan su nombre.
(Burden & Faires,  2011). El  avance decisivo lo dio Martin Wilhelm Kutta, también alemán, discípulo del
entorno  académico  de  Gotinga.  En  1901,  Kutta  publicó  un  trabajo  fundamental  donde:  Generalizó  y
formalizó  los  métodos  propuestos  por  Runge.  Clasificó  los  métodos  según  su  orden  de  precisión  e
Introdujo esquemas sistemáticos para construir métodos de orden superior.

Ecuacion diferencial ordinaria

Método Numérico

FIGURA 21

𝑑𝑦
𝑑𝑥

= 𝑓(𝑥𝑛, 𝑦𝑛)

𝑦𝑛+1 = 𝑦𝑛 + ℎ∅
44

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Donde:
𝑦𝑛+1 = El valor de la función en el siguiente paso
𝑦𝑛 = El valor de la función en el paso actual
ℎ = El tamaño del paso
∅ = 𝑓(𝑥𝑛, 𝑦𝑛) = Derivada de la función en el paso actual

Problema de valor inicial
El problema del valor inicial (Cauchy)

El problema de Cauchy es un concepto fundamental en ecuaciones diferenciales. Se trata de encontrar la
solución de una ecuación diferencial que cumple con ciertas condiciones iniciales o de frontera

𝑑𝑦
𝑑𝑥

= 𝑓(𝑥𝑛, 𝑦𝑛)

Ecuación diferencial ordinaria

Caso polinómico por ejemplo
𝑦 = 𝐹(𝑥) + 𝑐

FIGURA 22

Error de trunzamiebto

𝑅𝑛 =

𝑦(𝑛+1)(𝜉)
(𝑛 + 1)!

ℎ(𝑛+1)

El efecto del tamaño del paso, así como también como se calcule la pendiente según el método escogido
determinará la precisión de la aproximación así como el error es como se muestra en la grafica siguiente

45

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 23

Método de Euler

Es un procedimiento numérico para encontrar aproximaciones de soluciones de ecuaciones diferenciales
ordinarias. Especialmente útil cuando no se puede encontrar la solución exacta.

Formula de Euler

𝑦𝑛+1 = 𝑦𝑛 + ℎ𝑓(𝑥𝑛, 𝑦𝑛)

Donde:
𝑦𝑛+1 = 𝑦𝑛 + ℎ𝑓(𝑥𝑛, 𝑦𝑛)
𝑦𝑛 = El valor de la función en el paso actual
ℎ = El tamaño del paso
𝑓(𝑥𝑛, 𝑦𝑛) = Derivada de la función en el paso actual

1. Se utiliza la pendiente de la función en el punto inicial para hacer una predicción del siguiente valor. Esta
pendiente se calcula como: 𝑓(𝑥𝑛, 𝑦𝑛) donde f es la derivada de la función.
2. Segmento de línea recta: La predicción se realiza moviéndose a lo largo de un segmento de línea recta
que  sigue  la  pendiente  inicial.  Este  segmento  se  extiende  desde  el  punto  inicial (𝑥𝑛, 𝑦𝑛) hasta  el  punto
predicho (𝑥𝑛+1, 𝑦𝑛+1).
3. El nuevo punto: (𝑥𝑛+1, 𝑦𝑛+1) se calcula utilizando la formula de Euler 𝑦𝑛+1 = 𝑦𝑛 + ℎ𝑓(𝑥𝑛, 𝑦𝑛), donde ℎ es
el tamaño del paso

46

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 24

Código

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def euler(f, y0, t0, tf, h):
    t_values = np.arange(t0, tf + h, h)
    y_values = np.zeros(len(t_values))
    y_values[0] = y0
    for i in range(1, len(t_values)):
        y_values[i] = y_values[i - 1] + h * f(t_values[i - 1], y_values[i - 1])
    return t_values, y_values

 def f(t, y):
    return t+y

def solucion_particular(t):
    return -t-1+2*np.exp(t)

47

Modelado y Simulación – 3.1.025

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

 # Condiciones iniciales y parámetros
y0, t0, tf, h = 1, 0, 1, 0.1
# Soluciones
t_euler, y_euler = euler(f, y0, t0, tf, h)
y_real = solucion_particular(t_euler)

# Crear DataFrame
resultados = pd.DataFrame({
    'Tiempo': t_euler,
    'Euler': y_euler,
        'Solución Real': y_real
})

print(resultados)

# Graficar resultados
plt.plot(t_euler, y_euler, label='Euler')
plt.plot(t_euler, y_real, label='Solución Real')
plt.xlabel('Tiempo')
plt.ylabel('Valor de y')
plt.legend()
plt.title('Métodos de Euler, Euler Mejorado y Solución Real')
plt.show()

Método de Euler Mejorado (Heun)

Se basa en la idea de mejorar la aproximación inicial obtenida con el método de Euler. Geométricamente,
esto se puede entender como una corrección de la pendiente inicial.

1.  Predicción  inicial:  En  el  método  de  Euler,  se  utiliza  la  pendiente  del  punto  inicial  para  hacer  una
predicción de la siguiente posición. Esto se representa como una línea recta que sigue la pendiente inicial.

2.  Corrección:  En el método de Heun, se calcula una segunda pendiente en el punto predicho. Luego, se
toma el promedio de la pendiente inicial y la pendiente predicha para obtener una mejor aproximación de
la pendiente real en el intervalo.

𝑦𝑛+1 = 𝑦𝑛 +

ℎ
2

(𝑓(𝑥𝑛, 𝑦𝑛) + 𝑓(𝑥𝑛+1, 𝑦∗))

𝑦∗ = Es el valor predicho usando Euler → 𝑦∗ = 𝑦𝑛 + ℎ𝑓(𝑥𝑛, 𝑦𝑛)

Método de Euler mejorado (Heun) Interpretación geométrica.

48

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 25

Código
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
def euler_mejorado(f, y0, t0, tf, h):
    """ Método de Euler mejorado (Heun). """
    t = np.arange(t0, tf + h, h)
    y = np.zeros_like(t)
    y[0] = y0
    for i in range(len(t) - 1):
        y_pred = y[i] + h * f(t[i], y[i])  # Predicción con Euler
        y[i + 1] = y[i] + h * (f(t[i], y[i]) + f(t[i] + h, y_pred)) / 2
  # Corrección
    return t, y
# Ecuación diferencial: dy/dt = y*sin(t)
def f(t, y):
    return 0.4 * t * y
# Solución exacta
def sol_exacta(y0, t):
    return (1 / np.exp(0.2)) * np.exp(0.2 * t**2)
# Parámetros
y0 , t0, tf, h= 1, 1, 2, 0.1     # Condiciones iniciales
# Cálculo de soluciones
t, y_eul_mej = euler_mejorado(f, y0, t0, tf, h)
y_real = sol_exacta(y0, t)
# Crear tabla resumen
tabla = pd.DataFrame({
    'Tiempo': t,

49

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

    'Exacta': y_real,
    'Euler Mejorado': y_eul_mej
})
print(tabla)
# Graficar resultados
plt.figure(figsize=(8, 5))
plt.plot(t, y_real, label="Solución Exacta", color="blue", linestyle="-", linewidth=2)
plt.plot(t,  y_eul_mej,  label="Euler  Mejorado",  color="green",  linestyle="dashdot",  linewidth=2,
marker="d")
plt.xlabel("Tiempo")
plt.ylabel("Solución y")
plt.title("Comparación de Métodos Numéricos para EDO")
plt.legend()
plt.grid()
plt.show()

Método de Runge Kutta 4

La  interpretación  geométrica  del  método  de  Runge-Kutta  de  cuarto  orden  (RK4)  se  basa  en  la  idea  de
aproximar la solución de una ecuación diferencial mediante una serie de estimaciones de la pendiente en
distintos puntos. En términos visuales, el método busca mejorar la precisión de la trayectoria de la solución
al  considerar  varias  pendientes  intermedias  en  cada  paso.  Imagina  que  quieres  seguir  una  curva  en  un
gráfico, pero solo puedes avanzar en pequeños pasos. En cada paso:

Algunos pasos son:

1. Pendiente inicial 𝑘1: Se calcula la pendiente en el punto actual.
2. Primera corrección 𝑘2: Se estima la pendiente en un punto intermedio, avanzando la mitad del paso.
3. Segunda corrección 𝑘3: Se vuelve a estimar la pendiente en otro punto intermedio.
4. Corrección final 𝑘4: Se calcula la pendiente en el punto final del paso.

Cálculos de las pendientes:

ℎ,  𝑦𝑛 +

𝑘2 = 𝑓 (𝑥𝑛 +

𝑘1 = 𝑓(𝑥𝑛, 𝑦𝑛)
1
2
1
2
𝑘4 = 𝑓(𝑥𝑛 + ℎ,   𝑦𝑛 + 𝑘3ℎ)
ℎ
6

𝑘3 = 𝑓 (𝑥𝑛 +

𝑦𝑛+1 = 𝑦𝑛 +

ℎ,  𝑦𝑛 +

1
2
1
2

𝑘1ℎ)

𝑘2ℎ)

(𝑘1 + 2𝑘2 + 2𝑘3 + 𝑘4)

A continuación se presenta la interpretación geometrica:

50

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 26

Código
import numpy as np
from tabulate import tabulate

# Definimos la EDO: dy/dx = x + y
def f(x, y):
    return x + y

# Solución exacta para dy/dx = x + y, y(0)=1
def solucion_exacta(x):
    return 2*np.exp(x) - x - 1

# RK4 Modificado (h/2 dentro)
def rk4_modificado(f, x0, y0, h, pasos):
    x, y = x0, y0
   solucion = [(x, y)]
    for _ in range(pasos):
        k1 = f(x, y)
        k2 = f(x + h/2, y + (h/2)*k1)
        k3 = f(x + h/2, y + (h/2)*k2)
        k4 = f(x + h, y + h*k3)

51

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

        y += h * (k1 + 2*k2 + 2*k3 + k4) / 6
        x += h
        solucion.append((x, y))
    return solucion
 # Parámetros
x0, y0, h, pasos = 0.0, 1.0, 0.1, 10
# Calculamos todas las soluciones
sol_rk4_mod = rk4_modificado(f, x0, y0, h, pasos)
sol_exacta = [(x, solucion_exacta(x)) for x in np.arange(x0, x0 + (pasos+1)*h, h)]

# Preparamos datos para la tabla comparativa
tabla_comparativa = []
headers = ["x", "Exacta", "RK4 Modificado"]

for i in range(pasos + 1):
    x = x0 + i*h
    y_rk4m = sol_rk4_mod[i][1]
    y_exacta = sol_exacta[i][1]
           tabla_comparativa.append([
        f"{x:.1f}",
        f"{y_rk4m:.6f}",
        f"{y_exacta:.6f}"
       ])
 # Imprimimos tabla
print(tabulate(tabla_comparativa, headers=headers, tablefmt="grid"))

dy/dx=x+y

n
0
1
2
3
4
5
6
7
8
9
10

Euler
1.0000
1.1000

x
0.0000
0.1000
0.2000       1.2200
0.3000       1.3620
0.4000       1.5282
0.5000       1.7210
0.6000       1.9431
0.7000       2.1974
0.8000       2.4872
0.9000       2.8159
1.0000       3.1875

Exacta
1.0000
1.1103
1.2428
1.3997
1.5282
1.7974
2.0442
2.3275
2.6511
3.0192
3.4366

Error
0.0000
0.0103
0.0028
0.0377
0.00554
0.0764
0.1011
0.1301
0.1639
0.2033
0.2491

TABLA 5

52

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

N

0

1

2

3

4

5

6

7

8

9

10

X

0.0

0.1

0.2

0.3

0.4

0.5

0.6

0.7

0.8

0.9

1.0

FIGURA 27

Sol Exacta

Euler

Euler mejorado

Runge Kutta 4

1.000000

1.000000

1.000000

1.000000

1.110342

1.100000

1.110000

1.110342

1.242806

1.220000

1.242050

1.242805

1.399718

1.362000

1.398465

1.399717

1.583649

1.528200

1.581804

1.583648

1.797443

1.721020

1.794894

1.797441

2.044238

1.943122

2.040857

2.044236

2.327505

2.197434

2.323147

2.327503

2.651082

2.487178

2.645578

2.651079

3.019206

2.815895

3.012364

3.019203

3.436564

3.187485

3.428162

3.436559

TABLA 6

53

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

N
0
1
2
3
4
5
6
7
8
9
10

Exacta
1.000000
3.436564
11.77000
36.17000
104.1900
290.8200
799.8500
2185.260
5952.910
16196.16
4401.930

Euler
1.00000
2.00000
6.00000
12.0000
27.0000
58.0000
121.000
248.000
503.000
1014.00
2037.00

FIGURA 28

Heun
1.0000
3.0000
9.0000
26.000
70.000
181.00
460.00
1159,0
2908,0
7282.0
1819.0

TABLA 7

Runge Kutta 4
1.0000000
3.0000000
10.000000
31.000000
89.000000
248.00000
680.00000
1852.0000
5028,0000
13631.000
36933.000

Resumen de la tabla comparativa (Exacta vs métodos numéricos)

La tabla muestra la evolución de una solución exacta y sus aproximaciones numéricas usando los métodos
de Euler, Heun y Runge–Kutta de orden 4 (RK4) a medida que aumenta el número de pasos 𝑁. A medida que
el sistema evoluciona y la solución crece rápidamente:

RK4   >   Heun   >   Euler

A continuación, lo simulamos en python:

54

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 29

Ejercicios Ecuaciones diferenciales Ordinarias

Dadas las siguientes ecuaciones diferenciales de valores iniciales:

a)  resolver analíticamente si es posible.
b)  Simular la solución exacta usando un código Python
c)  Simular las soluciones aproximadas por los métodos de Euler, Heun y runge Kutta 4. Y compararlas

con la solución particular exacta (presentar tabla resumen de las iteraciones y gráficos)

d)  Dibujar los campos directores (use el método de las isoclinas)

   Ecuación Diferencial

Condiciones Iniciales

Intervalo

Paso

1.

2.

3.

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑡

= 𝑦 + 𝑡2

= 𝑦 sin(𝑡)

= 2𝑡 + 3𝑦

 𝑦(0)=1

 𝑦(0)=2

 𝑦(0)=0

0 ≤ 𝑡 ≤ 1

ℎ = 0.1

0 ≤ 𝑡 ≤ 𝜋

ℎ = 𝜋/10

0 ≤ 𝑡 ≤ 1

ℎ = 0.2

55

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

= 𝑡 − 𝑦2

= 𝑒−𝑡 − 𝑦

=

1

1+𝑡2 − 𝑦

=

𝑥2−1
𝑦2

 𝑦(0)=1

 𝑦(0)=0

 𝑦(0)=1

 𝑦(0)=2

0 ≤ 𝑡 ≤ 2

ℎ = 0.2

0 ≤ 𝑡 ≤ 1

ℎ = 0.1

0 ≤ 𝑡 ≤ 2

ℎ = 0.5

0 ≤ 𝑥 ≤ 2

ℎ = 0.5

= 𝑦 − 𝑡2 + 1

 𝑦(0)=0.5

0 ≤ 𝑡 ≤ 1

ℎ = 0.2

4.

5.

6.

7.

8.

9.

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑥

𝑑𝑦

𝑑𝑡

𝑑𝑦

𝑑𝑥

= 𝑦 + 𝑥

10.  𝑑𝑦
𝑑𝑥

= 𝑦 − 𝑥

 𝑦(0)=1

 𝑦(0)=0.5

11.  𝑑𝑦

𝑑𝑥

= 0.1√𝑦 + 0.4𝑥2

 𝑦(2)=2

12.  𝑑𝑦

𝑑𝑥

= 0.4𝑥𝑦

 𝑦(1)=1

0 ≤ 𝑥 ≤ 1

ℎ = 0.2

𝑦(1)

𝑦(2.5)

𝑦(2)

ℎ = 0.1

𝑛 = 10

ℎ = 0.1

A continuación, se presentan algunas ecuaciones diferenciales ordinarias de valor inicial:

a)  Resolver analíticamente
b)  Dibujar sus campos directores
c)  Resolver usando el modelo de Runge kutta4 (presente los cálculos para cada pendiente y todas las

iteraciones.

 Ecuación Diferencial

Condiciones Iniciales

Intervalo

Paso

1.

2.

3.

𝑑𝑦

𝑑𝑥

𝑑𝑦

𝑑𝑥

𝑑𝑦

𝑑𝑥

= 𝑥𝑦

= 2𝑥𝑦

= 2𝑥√𝑦

 𝑦(1)=1

 𝑦(1)=1

 𝑦(1)=3

1 ≤ 𝑥 ≤ 1.2

ℎ = 0.1

1 ≤ 𝑥 ≤ 1.5

ℎ = 0.1

1 ≤ 𝑥 ≤ 1.2

ℎ = 0.1

56

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

BIBLIOGRAFIAS CAPÍTULO I

Burden, R.L., & Faires, J.D. (2011). Numerical Analysis (9th ed.). Brooks/Cole.
Chapra, S.C., & Canale, R.P. (2015). Métodos numéricos para ingenieros (7ª ed.). McGraw-Hill.
Atkinson, K.E. (1989). An Introduction to Numerical Analysis. Wiley.
Sauer, T. (2012). Numerical Analysis (2nd ed.). Pearson.
Quarteroni, A., Sacco, R., & Saleri, F. (2007). Numerical Mathematics (2nd ed.). Springer.n
Kroese, D.P., Brereton, T., Taimre, T., & Botev, Z.I. (2014)
Why the Monte Carlo Method is So Important Today
Wiley Interdisciplinary Reviews: Computational Statistics.

57

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Capítulo II
Sistemas Dinámicos

Son modelos matemáticos que describen cómo cambia el estado de un sistema a lo largo del tiempo. Estos
sistemas pueden ser de tiempo continuo o discreto y se utilizan en diversas disciplinas como la física, la
biología, la economía y la ingeniería.

El estudio de los sistemas dinámicos constituye uno de los pilares fundamentales para la comprensión y el
modelado  de  fenómenos  que  evolucionan  en  el  tiempo.  Desde  los  desarrollos  clásicos  de  la  mecánica
newtoniana hasta las aplicaciones modernas en ingeniería, física, biología y ciencias computacionales, los
sistemas dinámicos proporcionan un marco matemático  unificador para describir, analizar y predecir el
comportamiento de sistemas naturales y tecnológicos (Hirsch, Smale & Devaney, 2013; Strogatz, 2015).

En términos generales, un sistema dinámico se define como una ley que determina la evolución temporal
del estado de un sistema a partir de una condición inicial. Dicha ley se expresa habitualmente mediante
ecuaciones  diferenciales  o  ecuaciones  en  diferencias,  según  se  modele  el  tiempo  como  una  variable
continua o discreta (Teschl, 2012). A través de esta formulación es posible representar desde dinámicas
simples, como el crecimiento o decaimiento exponencial, hasta comportamientos complejos que incluyen
oscilaciones, transiciones de régimen, bifurcaciones y caos determinista (Wiggins, 2003).

Un  ejemplo  clásico  y  altamente  ilustrativo  es  el  modelo  de  decaimiento  radiactivo,  que  describe  la
disminución  en  el  tiempo  del  número  de  núcleos  inestables  de  una  sustancia.  Este  proceso  se  modela
mediante la ecuación diferencial

𝑁̇ (𝑡) = −𝜆𝑁(𝑡),

donde 𝑁(𝑡)representa  la  cantidad  de  núcleos  radiactivos  presentes  y 𝜆 es  la  constante  de  decaimiento
característica del material. A pesar de su simplicidad, este modelo introduce de manera intuitiva conceptos
fundamentales como estabilidad, soluciones analíticas y dependencia paramétrica (Tipler & Mosca, 2008).
Una  aplicación  directa  de  este  sistema  dinámico  es  la  datación  por  carbono-14,  técnica  ampliamente
utilizada  en  arqueología,  geología  y  ciencias  forenses  para  estimar  la  antigüedad  de  restos  orgánicos,
evidenciando cómo un modelo dinámico elemental puede tener un impacto científico significativo (Zeidler,
2011).

En  física,  los  sistemas  dinámicos  aparecen  de  forma  natural  en  la  descripción  del  movimiento  y  la
evolución  de  sistemas  mecánicos  y  electromagnéticos.  El  oscilador  armónico,  por  ejemplo,  modela
fenómenos tan  diversos como el movimiento de un resorte, las vibraciones estructurales o  los circuitos
eléctricos RLC (Boylestad & Nashelsky, 2015). De manera más compleja, los sistemas dinámicos permiten
analizar la dinámica orbital de planetas y satélites, la estabilidad de trayectorias en mecánica celeste y la
aparición de comportamientos caóticos en sistemas atmosféricos, como ocurre en el modelo de Lorenz
para la predicción meteorológica (Strogatz, 2015).

58

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

En el ámbito de la ingeniería, los sistemas dinámicos constituyen la base del análisis y diseño de sistemas
de  control.  La  dinámica  de  un  vehículo,  un  robot  industrial  o  un  dron  puede  describirse  mediante
ecuaciones  diferenciales  que  relacionan  posiciones,  velocidades  y  fuerzas  actuantes.  A  partir  de  estos
modelos,  es  posible  estudiar  la  estabilidad  del  sistema,  diseñar  estrategias  de  control  y  garantizar  un
comportamiento  seguro  y  eficiente  (Ogata,  2010;  Khalil,  2002).  Un  ejemplo  intuitivo  es  el  control  de
temperatura en un proceso industrial, donde el sistema dinámico permite regular la variable alrededor de
un valor deseado frente a perturbaciones externas.

En  ciencia  aplicada  y  biología,  los  sistemas  dinámicos  se  emplean  para  modelar  la  evolución  de
poblaciones, la propagación de epidemias y la interacción entre especies. El modelo depredador–presa de
Lotka–Volterra  describe  de  manera  sencilla  cómo  dos  poblaciones  interactúan  y  oscilan  en  el  tiempo,
proporcionando una interpretación cualitativa clara del equilibrio ecológico y sus posibles perturbaciones
(Lotka, 1925; Brauer, Castillo-Chávez & Feng, 2019).

Un aspecto central de la teoría de sistemas dinámicos es el análisis cualitativo, que permite caracterizar
el comportamiento global del sistema sin recurrir necesariamente a soluciones explícitas. Conceptos como
puntos de equilibrio, estabilidad, conjuntos invariantes y estructura del espacio de fases ofrecen una visión
profunda del sistema, especialmente relevante en contextos donde las soluciones analíticas no existen o
son difíciles de obtener (Hirsch et al., 2013).

El desarrollo de métodos numéricos y herramientas computacionales ha reforzado aún más la importancia
de los sistemas dinámicos en la práctica científica y tecnológica. Algoritmos de integración temporal, como
los métodos de Runge–Kutta, permiten simular la evolución de sistemas complejos y analizar escenarios
realistas  en  los  que  intervienen  múltiples  variables  y  parámetros  (Strogatz,  2015;  Teschl,  2012).  Esta
interacción entre teoría, simulación y aplicación convierte a los sistemas dinámicos en una herramienta
esencial para la investigación moderna.

También podemos mencionar El sistema logístico como modelo dinámico fundamental, ampliamente
utilizado para describir procesos de crecimiento limitado en biología, ecología, economía e ingeniería. A
diferencia del crecimiento exponencial, el sistema logístico incorpora de manera explícita la existencia de
restricciones naturales o tecnológicas que impiden un crecimiento indefinido.

El modelo se describe mediante la ecuación diferencial no lineal

𝑥̇(𝑡) = 𝑟 𝑥(𝑡) (1−

𝑥(𝑡)
𝐾

) ,

donde 𝑥(𝑡) representa el tamaño de la población o magnitud de interés en el instante 𝑡, 𝑟 > 0 es la tasa de
crecimiento intrínseca y 𝐾 > 0 es la capacidad de carga del sistema, es decir, el valor máximo sostenible
por el entorno (Strogatz, 2015).

Desde  un punto  de vista  intuitivo,  cuando 𝑥(𝑡) es pequeño  en  comparación  con 𝐾,  el  término (1−

𝑥
𝐾

) es

cercano a uno y el sistema se comporta aproximadamente como un crecimiento exponencial. Sin embargo,

59

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

a medida que 𝑥(𝑡)se aproxima a 𝐾, el crecimiento se ralentiza progresivamente hasta detenerse, reflejando
la influencia de recursos limitados, competencia o restricciones externas.

El  análisis  cualitativo  del  sistema  logístico  revela  la  presencia  de  dos  puntos  de  equilibrio:  𝑥 = 0,  que
resulta inestable, y 𝑥 = 𝐾, que es asintóticamente estable. Este comportamiento ilustra de manera clara
cómo los sistemas dinámicos no lineales pueden presentar estructuras de estabilidad que no aparecen en
modelos  lineales,  y  constituye  un  ejemplo  paradigmático  para  introducir  conceptos  como  estabilidad,
atractores y dependencia de parámetros (Hirsch et al., 2013).

En  ciencia,  el  modelo  logístico  se  utiliza  para  describir  la  evolución  de  poblaciones  biológicas,  el
crecimiento  bacteriano  y  la  difusión  de  innovaciones  o  epidemias  en  etapas  tempranas.  En  ingeniería,
aparece de forma natural en modelos de saturación de sistemas, crecimiento de demanda, dinámica de
recursos y procesos con límites físicos o energéticos. Incluso en control automático, el comportamiento
logístico  sirve  como  aproximación  para  sistemas  con  actuadores  saturados  o  restricciones  operativas
(Ogata, 2010).

Además, el modelo logístico posee una versión en tiempo discreto:

𝑥𝑛+1 = 𝑟 𝑥𝑛(1 − 𝑥𝑛),

que ha sido ampliamente estudiada por su capacidad de exhibir bifurcaciones y comportamiento caótico
al  variar  el  parámetro 𝑟.  Este  hecho  convierte  al  sistema  logístico  en  un  puente  natural  entre  sistemas
dinámicos  simples  y  dinámicas  complejas,  siendo  un  ejemplo  central  en  la  introducción  al  caos
determinista (Strogatz, 2015; Wiggins, 2003).

La inclusión del sistema logístico junto con modelos como el decaimiento radiactivo y el oscilador armónico
pone de manifiesto cómo ecuaciones relativamente simples pueden capturar comportamientos esenciales
de sistemas reales, reforzando el papel de los sistemas dinámicos como herramienta fundamental para la
modelización científica y el análisis ingeniería

Características de los Sistemas Dinámicos

1.   Evolución  Temporal:  El  estado  del  sistema  cambia  con  el  tiempo,  lo  que  puede  ser  descrito  por
ecuaciones diferenciales (en el caso de sistemas continuos) o por ecuaciones en diferencias (en el caso de
sistemas discretos)

2.   Determinismo:  En  muchos  sistemas  dinámicos,  el  estado  futuro  del  sistema  está  completamente
determinado por su estado actual y las leyes que gobiernan su evolución.

3.   No Linealidad: Muchos sistemas dinámicos son no lineales, lo que significa que las ecuaciones que los
describen no son lineales. Esto puede llevar a comportamientos complejos como el caos.

60

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

La historia de los sistemas dinámicos es fascinante y tiene raíces profundas en la matemática y la física. Su
origen se remonta a la mecánica newtoniana, donde Isaac Newton formuló ecuaciones diferenciales para
describir  el  movimiento  de  los  cuerpos.  A  lo  largo  del  tiempo,  matemáticos  como  Euler  y  Laplace
contribuyeron al desarrollo de la teoría, estableciendo principios fundamentales sobre la evolución de los
sistemas en el tiempo. En el siglo XX, la teoría de los sistemas dinámicos se expandió con el estudio del
caos y la teoría de bifurcaciones, lo que permitió comprender fenómenos complejos en diversas disciplinas,
desde  la  biología  hasta  la  economía.  Hoy  en  día,  los  sistemas  dinámicos  son  esenciales  para  modelar
procesos naturales y sociales, ayudando a predecir comportamientos y optimizar soluciones.

Conceptos Básicos

Desarrollemos algunos de los proncipios a tener en cuenta para el estudio cualitativo de estos sistemas:

Diagramas de Fase: Los diagramas de fase son herramientas visuales que se utilizan para representar el
comportamiento  de  sistemas  dinámicos  en  el  espacio  de  fases.  Estos  diagramas  muestran  todas  las
trayectorias posibles del sistema  a  partir  de  diferentes condiciones iniciales, proporcionando una visión
clara de cómo evoluciona el sistema con el tiempo.

Características de los Diagramas de Fase

❖  Ejes del Espacio de Fases: Los ejes del diagrama representan las variables del sistema. Por ejemplo,
en un sistema de dos dimensiones, los ejes podrían ser la posición y la velocidad.
❖  Trayectorias: Las curvas en el diagrama representan las trayectorias del sistema, mostrando cómo
cambia el estado del sistema a lo largo del tiempo.
❖  Puntos  Críticos:  Los  puntos  donde  las  trayectorias  se  cruzan  o  terminan  pueden  ser  puntos  de
equilibrio, donde el sistema no cambia con el tiempo.

Clasificacion de los puntos de equilibrios

1.  Punto de Silla: Si al menos uno de los valores propios tiene parte real positiva y otro tiene parte real
negativa, el punto de equilibrio es un punto de silla y es inestable.
2.  Nodo Estable: Si todos los valores propios tienen partes reales negativas, el punto de equilibrio es un
nodo estable (atractor).
3.  Nodo Inestable: Si todos los valores propios tienen partes reales positivas, el punto de equilibrio es un
nodo inestable (repulsor).
4.  Centro: Si todos los valores propios son puramente imaginarios (sin parte real), el punto de equilibrio es
un centro y es estable en el sentido de Lyapunov, pero no asintóticamente estable.
5.  Punto  de  Equilibrio  No Hiperbólico:  Si  al menos  uno de  los valores  propios  tiene  parte  real  cero, el
análisis lineal no es concluyente y se requiere un análisis no lineal más detallado.

Análisis de Estabilidad sistemas no lineales 1D

Se evalúa cada punto de equilibrio en la primera derivada:

61

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

 Si 𝑓′(𝑥∗) < 0 (es estable)
Si 𝑓′(𝑥∗) > 0 (es inestable)

Análisis de Estabilidad sistemas no lineales 2D

La estabilidad de un punto de equilibrio se determina observando los valores propios de la matriz Jacobiana
evaluada en ese punto. Aquí hay un resumen de cómo interpretar estos valores propios:

J = ||

𝜕𝑓1
𝜕𝑥
𝜕𝑓2
𝜕𝑥

𝜕𝑓1
𝜕𝑦
𝜕𝑓2
𝜕𝑥

||

Estabilidad Asintótica (teorema de Lyapunov)

La estabilidad asintótica es un concepto fundamental en teoría de sistemas dinámicos que describe como
un sistema  queda acotado  ante pequeñas perturbaciones, sino que además converge al equilibrio en el
tiempo. Un punto de equilibrio 𝑥∗ en un sistema dinámico autónomo de la forma:

𝑑𝑥
𝑑𝑡

= 𝑓( 𝑥)

Cumple dos condiciones:
1.  Para todo 𝜖 > 0,  𝑒𝑥𝑖𝑠𝑡𝑒 𝛿 > 0 𝑡𝑎𝑙 𝑞𝑢𝑒 𝑠𝑖,  ‖𝑥(0) − 𝑥∗‖ <  𝛿,  𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 ‖𝑥(𝑡) − 𝑥∗‖ < 𝜖 𝑝𝑎𝑟𝑎 𝑡𝑜𝑑𝑜 𝑡 ≥ 0
2.  Convergencia al equilibrio, donde:

𝑥(𝑡) =  𝑥∗

lim
𝑡→∞

Básicamente la distancia ‖𝑥(𝑡) − 𝑥∗‖,  tiende a cero cuando  t→ ∞

Estabilidad Asintótica

Según Lyapunov las trayectorias de un sistema dinámico se aproximan arbitrariamente al equilibrio, pero
no necesariamente lo tocan en un tiempo finito. Un punto de equilibrio es asintóticamente estable, si:

𝑥(𝑡) =  𝑥∗

lim
𝑡→∞

Para todas las condiciones iniciales en una vecindad del equilibrio básicamente la distancia
‖𝑥(𝑡) − 𝑥∗‖,  tiende a cero cuando  t→ ∞

Sin embargo, en tiempo finito las trayectorias no necesariamente alcanzan el equilibrio, solo se acercan.

La interpretación física: para la estabilidad simple, una perturbación ligera en el sistema, su nuevo estado
de equilibrio permanece cerca del anterior, pero no vuelve a el.

62

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

En el caso de estabilidad asintótica: el sistema no solo se mantiene sino que vuelve al equilibrio después
de la perturbación.

La interpretación física: para la estabilidad simple, una perturbación ligera en el sistema, su nuevo estado
de equilibrio permanece cerca del anterior, pero no vuelve a el.

En el caso de estabilidad asintótica: el sistema no solo se mantiene sino que vuelve al equilibrio después
de la perturbación.

𝑑𝑥
𝑑𝑡

= 𝑓( 𝑥)

Donde:
𝑥(𝑡) = Es la variable dependiente (estado del sistema)
(𝑡) = Variable independiente
La ecuación 𝑓( 𝑥) no depende de (t)  explícitamente.
Las soluciones pueden analizarse mediante diagramas de fase, donde se estudia los puntos de equilibrio
𝑓(𝑥) = 0,  y su estabilidad.

Sistemas desacoplados unidimensionales

Un sistema desacoplado implica que las ecuaciones que lo componen no interactúan entre si. En el caso
unidimensional esto significa que tenemos una ecuación de la forma:

Ejemplo

𝑑𝑥
𝑑𝑡

= 𝑓( 𝑥)

𝑑𝑥
𝑑𝑡

=   ∫ −𝑘𝑑𝑡

=   − 𝑘𝑥,   (𝑘 > 0)
𝑑𝑥
𝑥
𝑑𝑥
𝑥

=   ∫ −𝑘𝑑𝑡
𝑥(𝑡) = 𝑥0𝑒−𝑘𝑡

∫

∫

Donde 𝑥0: Constante

Sistemas Acoplados unidimensionales

En  realidad,  el  termino  (acoplado)  generalmente  se  aplica  a  sistemas  multidimensionales  (con  varias
variables),  donde  las  ecuaciones  interactúan.  Sin  embargo,  si  consideramos  un  sistema  acoplado
unidimensional a un parámetro externo, podríamos tener:

𝑑𝑥
𝑑𝑡

= 𝑓( 𝑥,  𝜆)

63

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Donde 𝜆 : Parámetro externo, que puede cambiar con el tiempo o depender de una ecuación (esto
implicaría  un sistema de dos variables)

𝑑𝑥
𝑑𝑡

= 𝑓( 𝑥, 𝑦),

𝑑𝑦
𝑑𝑡

= 𝑔( 𝑥, 𝑦)

Volviendo  a
unidimensional desacoplado

los  sistemas  que  estamos  analizando  unidimensionales,  Ejemplo  de  un  sistema

𝑑𝑥
𝑑𝑡

= 𝑥(1 − 𝑥)(𝑥 − 2)

Resolviendo el sistema los equilibrio se comportan dos estable y uno inestable por lo que las
simulaciones respectivas serian las siguientes:

FIGURA 30

En 𝑥 = 0, y en 𝑥 = 2 los equilibrios son estable y en 𝑥 = 1 inestable, esto se puede observar mejor en el
diagrama de soluciones en el tiempo:

Metodología General Un sistema dinámico unidimensional autónomo tiene la forma:

𝑑𝑥
𝑑𝑡

=  𝑓(𝑥) El análisis

cualitativo consiste en los siguientes pasos:

1. Encontrar los puntos de equilibrio (críticos): Resolver 𝑓(𝑥) =  0.
 2. Analizar el signo de 𝑓(𝑥) entre los puntos críticos: Esto indica si 𝑥(𝑡) aumenta o disminuye.
3. Clasificar los puntos críticos según la estabilidad: a). Estable (atractor): las soluciones cercanas tienden
al  punto.  b).  Inestable  (repulsor):  las  soluciones  cercanas  se  alejan.  c).  Semiestable:  comportamiento
distinto a cada lado.
4. Dibujar el diagrama de fase: Eje 𝑥 con flechas indicando la dirección del flujo de 𝑥(𝑡).
 5. Dibujar soluciones en el tiempo para condiciones iniciales: Mostrar cómo varía 𝑥(𝑡) para varios 𝑥0

64

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 31.

Las soluciones tienden a alejarce del 𝑥 = 1, mientras se acercan asintoticamente a 𝑥 = 0 𝑦 𝑎 𝑥 = 2. Para
determinar la naturaleza de  cada punto hay que usar la derivada en el punto. Si en negativa el punto de
equilibrio es estable, por lo contrario el punto seria inestable.

Otro ejemplo

𝑑𝑥
𝑑𝑡

= 𝑥2 − 1

Resolvemo el sistema y simulamos, se obtiene lo siguiente:

FIGURA 32

65

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Código

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
from scipy.integrate import solve_ivp

# Define la función f(x) que describe el sistema autónomo dx/dt = f(x)
def f(x):
    return x ** 2 - 1  # Ejemplo: sistema dx/dt = x^2 - 1

# Encuentra los puntos fijos resolviendo f(x) = 0
def find_fixed_points(f):
    # Intentamos encontrar las raíces en el rango [-2, 2], con una tolerancia mayor para asegurar
exactitud
    fixed_points = fsolve(f, np.linspace(-2, 2, 5))
    # Filtramos para obtener únicamente las raíces únicas, sin valores repetidos
    fixed_points = np.unique(fixed_points)
    # Comprobamos que los puntos encontrados son verdaderas raíces
    true_fixed_points = []
    tolerance = 1e-6  # Tolerancia para considerar que f(x) es efectivamente 0
    for point in fixed_points:
        if np.abs(f(point)) < tolerance:
            true_fixed_points.append(point)
    return np.array(true_fixed_points)

# Analiza la naturaleza de los puntos fijos usando la derivada de f(x)
def stability_analysis(f, fixed_points):
    def f_prime(x):
        return 2 * x  # Derivada de x^2 - 1
    stabilities = {}
    for point in fixed_points:
        derivative = f_prime(point)
        if derivative > 0:
            stabilities[point] = 'Inestable (Fuente)'  # Derivada positiva, punto inestable
        elif derivative < 0:
            stabilities[point] = 'Estable (Pozo)'  # Derivada negativa, punto estable
        else:
            stabilities[point] = 'Indeterminado'
    return stabilities

# Función que describe el sistema autónomo para la resolución numérica
def system(t, x):
    return f(x)

66

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

# Graficar la función f(x) con los puntos fijos marcados, las flechas y el gráfico de soluciones
def plot_function_with_fixes_and_solutions(f):
    fixed_points = find_fixed_points(f)
    stabilities = stability_analysis(f, fixed_points)
    # Rango de x para graficar la función
    x_vals = np.linspace(-2, 2, 400)
    y_vals = f(x_vals)
    # Graficar la función
    plt.figure(figsize=(12, 8))
    # Graficar la función f(x)
    plt.subplot(2, 1, 1)
    plt.plot(x_vals, y_vals, label=r'$f(x) = x^2 - 1$', color='b')
    # Graficar solo los puntos fijos en el eje x, con el color adecuado
    for point in fixed_points:
        if stabilities[point] == 'Estable (Pozo)':
            plt.scatter(point, 0, color='g', zorder=5, s=100)  # Círculo relleno para punto estable (verde)
        else:
            plt.scatter(point, 0, color='white', edgecolor='black', zorder=5,
                        s=100)  # Círculo vacío con borde negro para punto inestable (blanco)
    # Flechas indicando la dirección de la solución sobre el eje x
    for point in fixed_points:
        if stabilities[point] == 'Estable (Pozo)':
            # Flechas hacia el punto fijo (hacia la izquierda y derecha)
            plt.text(point - 0.2, -0.2, '>', fontsize=12, color='green', ha='center', va='center')
            plt.text(point + 0.2, -0.2, '<', fontsize=12, color='green', ha='center', va='center')
        else:
            # Flechas alejándose del punto fijo (hacia la derecha y hacia la izquierda)
            plt.text(point - 0.2, -0.2, '<', fontsize=12, color='red', ha='center', va='center')
            plt.text(point + 0.2, -0.2, '>', fontsize=12, color='red', ha='center', va='center')
    # Ejes
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title('Gráfico de la función f(x) con puntos fijos y dirección de las soluciones')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend(['$f(x)$'])
    # Graficar el gráfico de soluciones en otro subplot
    plt.subplot(2, 1, 2)
    # Condiciones iniciales para las soluciones
    initial_conditions = [-1.5, -0.5, 0.5, 1.5]  # Diferentes condiciones iniciales
    # Tiempo para simular las soluciones
    t_span = (0, 10)  # Simulación de 10 unidades de tiempo
    t_eval = np.linspace(t_span[0], t_span[1], 400)  # Puntos en el tiempo

67

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

    # Graficar las soluciones de las condiciones iniciales
    for x0 in initial_conditions:
        sol = solve_ivp(system, t_span, [x0], t_eval=t_eval, method='RK45')
        plt.plot(sol.t, sol.y[0], label=f'Condición inicial: x0 = {x0}')
    # Graficar las raíces como líneas horizontales
    for point in fixed_points:
        plt.axhline(y=point, color='gray', linestyle='--', label=f'Raíz en x={point:.2f}')
    # Comportamiento hacia las raíces (líneas horizontales que son estables o inestables)
    for point in fixed_points:
        if stabilities[point] == 'Estable (Pozo)':
            plt.text(10, point - 0.2, '>', fontsize=12, color='green', ha='center', va='center')
            plt.text(10, point + 0.2, '<', fontsize=12, color='green', ha='center', va='center')
        else:
            plt.text(10, point - 0.2, '<', fontsize=12, color='red', ha='center', va='center')
            plt.text(10, point + 0.2, '>', fontsize=12, color='red', ha='center', va='center')
    # Acotamos el eje vertical para mayor claridad
    plt.ylim(-2, 2)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.title('Gráfico de Soluciones del Sistema')
    plt.xlabel('t')
    plt.ylabel('x(t)')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
# Ejecutar las funciones
plot_function_with_fixes_and_solutions(f)
# Mostrar los puntos fijos y su naturaleza
fixed_points = find_fixed_points(f)
stabilities = stability_analysis(f, fixed_points)
print("Puntos Fijos:")
for point in fixed_points:
    print(f"x = {point:.2f}, Naturaleza: {stabilities[point]}")

Ejercicios Sistemas Autónomos

Dadas las siguientes ecuaciones diferenciales:

e)  Resolver analíticamente si es posible.
f)  Calcular puntos de equilibrio
g)  Dibujar su diagrama de fase
h)  Gráfico de soluciones

68

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

1.

2.

3.

4.

5.

6.

𝑑𝑥
𝑑𝑡

𝑑𝑥
𝑑𝑡

𝑑𝑥
𝑑𝑡

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

= 2𝑥,

𝑥 ≥ 0

= 𝑥2 − 4

= 3𝑥 − 𝑥2

= 3𝑦 − 9

= 4 − 2𝑦

= 3 − 2𝑦

7.

𝑑𝑦
𝑑𝑥

 = 𝑦 2 − 6𝑦 + 5

8.  𝑥̇ = sin(𝑥)

  9.

10.

𝑑𝑥
𝑑𝑡

𝑑𝑦
𝑑𝑡

= 4𝑥 − 𝑥2

= 3𝑦(𝑦 − 2)

11.

12.

13.

14.

15.

16.

𝑑𝑦
𝑑𝑡

𝑑𝑦
𝑑𝑡

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

= 𝑦2 − 4𝑦 − 12

= 𝑦2 − 𝑦

= (𝑦 − 1)2

= 𝑦(𝑦 + 1)(𝑦 − 2)

= 𝑦 + 2

= 𝑦(4 − 𝑦)

17.  Decaimiento radiactivo básico (1D): Un isótopo radiactivo tiene una constante de decaimiento 𝜆 =
0.1 𝑎ñ𝑜𝑠−1 Inicialmente hay 𝑁0 = 1000 núcleos.

Preguntas: 1) Escribe el sistema dinámico que modela el proceso. 2) Explica con palabras qué significa que
𝑁̇ < 0.  3)  ¿Existe  un  punto  de  equilibrio?  4)  ¿Es  estable  o  inestable?  5)  Describe  la  forma  de  la  gráfica
𝑁(𝑡) sin hacer cálculos.

18. – Vida media e interpretación física: Para el carbono-14 se sabe que la vida media es aproximadamente
5730 años.

Preguntas 1) Explica qué significa “vida media” en términos de sistema dinámico. 2) ¿Qué relación existe
entre la vida media y la constante 𝜆?, 3) Si se mide un fósil con el 25% del carbono-14 original, ¿cuántas
vidas medias han pasado? 4) ¿Por qué este método es confiable para restos orgánicos y no para rocas?

19. Enfriamiento de Newton en estudio forense: Un investigador forense encuentra un cuerpo en una
habitación cerrada. La temperatura ambiente se mantiene constante en:

𝑇𝑎 = 18∘C

A las 22:00 h, la temperatura corporal medida es: 𝑇(22: 00) = 30∘C, Una hora más tarde, a las 23:00 h, se
mide nuevamente y se obtiene: 𝑇(23: 00) = 27∘C Se asume que la temperatura corporal normal es: 𝑇0 =
69

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

37∘C, y que el proceso sigue la ley de enfriamiento de Newton: 𝑇̇ = −𝑘(𝑇 − 𝑇𝑎)

Explica por qué es razonable usar el modelo de Newton en este caso: 1) ¿Qué representa físicamente la
constante 𝑘? 2) Usa las dos mediciones para estimar el valor de 𝑘. 3) Estima el tiempo de muerte.

20. Un servidor procesa solicitudes de usuarios. Según 𝑥(𝑡) el número de solicitudes activas en el servidor
en el tiempo 𝑡. Cuando el servidor está poco cargado, las solicitudes entran rápidamente. Cuando la carga
es alta, el sistema desacelera la admisión o rechaza peticiones.

•  Existe un mecanismo automático de control para evitar la saturación, y el comportamiento se modela
mediante el sistema dinámico:

donde 𝑥(𝑡) se mide en solicitudes activas.

𝑥̇ = 𝑥(100 − 𝑥)

a)  Encuentra los puntos de equilibrio del sistema. Dibuja el diagrama de fases 1D indicando el sentido

del flujo. Clasifica cada equilibrio como estable o inestable.

b)  Describe qué ocurre con la carga del servidor si: 𝑥(0) < 100, 𝑥(0) > 100
c)  Interpreta físicamente cada equilibrio:
d)  ¿Qué representa 𝑥 = 0? ¿Qué representa 𝑥 = 100?
e)  Explica por qué el equilibrio estable es deseable desde el punto de vista del diseño de sistemas.
f)  Supón que se introduce un parámetro de control 𝛼 > 0: 𝑥̇ = 𝛼𝑥(100 − 𝑥); ¿Qué efecto tiene 𝛼 sobre

la estabilidad? ¿Qué efecto tiene sobre la velocidad de convergencia?

g)  Una  plataforma  digital  registra  el  número  de  usuarios  activos  por  día.  Debido  a  límites  de
infraestructura y control automático, el crecimiento no es ilimitado. Sea 𝑥𝑛el número de usuarios
activos el día 𝑛. El crecimiento se modela mediante la ecuación logística discreta:

𝑥𝑛+1 = 𝑟 𝑥𝑛 (1−

𝑥𝑛
𝐾 )

donde: 𝑟 > 0: tasa de crecimiento diario, 𝐾 > 0: capacidad máxima del sistema, 𝑟 = 1.5, 𝐾 = 1000,
𝑥0 = 100

1.  Explica con palabras qué representa cada término del modelo.
2.  ¿Por qué este modelo es más realista que el crecimiento exponencial?
3.  Calcula 𝑥1, 𝑥2y 𝑥3.
4.  ¿El número de usuarios crece o decrece inicialmente?

70

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

BIFURCACIONES

Suponga un sistema de la forma 𝑓(𝑥, 𝜇) donde , 𝜇 es el parametro que controla el comportamiento
del mismo. La bifurcación ocurre en 𝜇 = 𝜇0 si un cambio arbitrariamente pequeño en 𝜇 produce
un cambio cualitativo en el comportamiento del sistema. Las bifurcaciones en sistemas dinámicos
ocurren  cuando  un  pequeño  cambio  en  los  parámetros  provoca  un  cambio  cualitativo  en  su
comportamiento. Como la aparición o desaparición de un punto de equilibro, ciclos limites o cambios en la
estabilidad. Son fundamentales en el estudio de ecuaciones diferenciales y sistemas no lineales.

Por ejemplo en la siguiente figura se muestra como: las curvas de lineas azules continuas representan los
equilibrios estables (soluciones atractoras), mientras que las rojas discontinuas los equilibrios inestables
(rama roja separa las cuencas de atracción).

Tipos

FIGURA 33

•  Bifurcación  tipo  Local: Es  aquella  que puede ser analizada  completamente mediante  cambios en las
propiedades  de  la  estabilidad  local.  Como  puntos  de  equilibrio,  orbitas  locales  u  otros  conjuntos
invariantes. Conforme los parámetros atraviesan umbrales críticos.

Bifurcación Silla Nodo

𝑥̇ = 𝑟 + 𝑥2
𝑥̇ = 𝑓(𝑥, 𝑟) 𝑐𝑜𝑛 𝑥 ∈ 𝑅,  𝑟 ∈ 𝑅

71

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 35

Es  un  fenómeno  en  sistemas  dinámicos  donde  dos  puntos  de  equilibrio  (uno  estable  y  otro  inestable)
colisionan  y  desaparecen  cuando  un  parámetro  varía.  Es  una  de  las  bifurcaciones  más  comunes  en
ecuaciones diferenciales.

Bifurcación Pitchfork

𝑥̇ = μ𝑥 − 𝑥3

•  Supercrítica: Para valores pequeños del parámetro, el sistema tiene un único equilibrio estable.
•  Cuando el  parámetro cruza  un  valor  crítico, aparecen dos  nuevos equilibrios estables  y el  original se
vuelve inestable.

FIGURA 36

72

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Bifurcación Pitchfork

𝑥̇ = 𝑟𝑥 + 𝑥3

2. Subcrítica:
• Similar a la supercrítica solo que ahora 𝑟 < 0
Hay tres equilibrios 𝑥∗ = 0
 que es estable y 𝑥∗ = ±√−𝑟
 que son inestables.
En el momento de la bifurcación cuando los equilibrios inestables colisionan con el origen desaparecen,
mientras que el origen sigue siendo un punto de equilibrio, pero cambia su naturaleza

FIGURA 37

Bifurcación Pitchfork (histeresis)

𝑥̇ = 𝑟𝑥 + 𝑥3- 𝑥5

3. Subcrítica: el sistema muestra como
- 𝑥5 crea una estructura mas rica
En 𝑟 = − 0.25, aparece una ifurcacion silla-nodo, que crea dos puntos fijos; un par estable (rama exterior),
un par inestable (rama interior)
• Para   -0.25 < 𝑟 < 0 , 𝑥∗ = 0
Sigue siendo estable y las ramas inestables
En 𝑟 = 0, el (0) cambia de estable a inestable y las ramas inestables se fusionan en el origen.

73

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

En 𝑟 > 0
 solo persisten las ramas estables exteriores. 𝑥 = 0 es inestable.

Bifurcación Transcrita

FIGURA 38

La bifurcación transcrita es un tipo de bifurcación en sistemas dinámicos donde dos puntos de equilibrio
intercambian estabilidad a medida que un parámetro varía. Es común en modelos ecológicos, económicos
y físicos. En 𝑟  = 0  ocurre una bifurcación, los puntos de equilibrio cambian su naturaleza: 𝑥∗ = 0
Cambia de estable a inestable y para 𝑥 = 𝑟
 cambia de inestable a estable, la dinamica es 𝑥̇ = 𝑟𝑥 − 𝑥2

FIGURA 39

74

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Tipos de bifurcaciones

•  Bifurcación  tipo  Global:  Ocurre  cuando  grandes  conjuntos  invariantes,  como  orbitas  periódicas,
colisionan con equilibrios. Esto causa cambios en la topología de las trayectorias en el espacio fase que no
pueden ser restringidos a un pequeño entorno, como ocurre con las bifurcaciones locales.

{

𝑥̇ = 𝑦
𝑦̇ = 𝑥 − 𝑥2 + 𝜇𝑦

Tipo Hopf

FIGURA 40

Aunque los autovalores son siempre complejos con parte real negativa, el ciclo límite emerge cuando los
términos  no  lineales  provocan  un  cambio  de  comportamiento.  En  este  sistema,  la  bifurcación  de  Hopf
ocurre en 𝑟 = 1

𝑥̇ = 𝑟𝑦 − 𝑥
𝑦̇ = −𝑟𝑥 − 𝑦 + (𝑥2 + 𝑦2)𝑦

{

FIGURA 41

75

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ciclos limites:

Para 𝑟 < 0  Foco estable

𝑥̇ = 𝑦 − 𝑥(𝑟  − 𝑥2 − 𝑦2)
{
𝑦̇ = −𝑥 + 𝑦(𝑟 − 𝑥2 + 𝑦2)

Para 𝑟 = 0  Bifurcación Hopf

FIGURA 42

FIGURA 43

76

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Para 𝑟 > 0  Ciclo limite radio √𝑟

Modelado y Simulación – 3.1.025

Sistema Lorent

FIGURA 44

{

𝑥̇ = 𝜎(𝑦 − 𝑥)
𝑦̇ = 𝑥(𝜌 − 𝑧) − 𝑦
𝑧̇ = 𝑥𝑦 − 𝛽𝑧

𝜌 =  número de Rayleigh (controla el calor, bifurcaciones)
β:  relacionado con la geometría (≈ 8/3)

𝜎 = 𝑛𝑢𝑚𝑒𝑟𝑜 𝑑𝑒 𝑝𝑟𝑎𝑛𝑡  ≈ 10

Para   𝜌 = 10 el sistema es estable, la trayectoria converge al equilibrio
Para   𝜌 = 24.74 se produce la bifurcación Hopf, los puntos de equilibrio pierden estabilidad, aparecen
oscilaciones
Para   𝜌 = 28 El sistema entra en régimen caótico, aparece el atractor raro de Loren en forma de mariposa,
las trayectorias nunca se repiten

77

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 45

Ejercicio de bifurcaciones

Dado los siguientes sistemas unidimensionales:

Encontrar los puntos fijos

i)
j)  Determinar la estabilidad lineal en función del parámetro
k)
l)  Dibujar el diagrama de bifurcación (use un código Python)

Identificar el valor donde ocurre la bifurcación y clasificarla

1.  𝑥̇ = 𝑟 + 𝑥2

2.  𝑥̇ = 𝑟𝑥 − 𝑥2

3.  𝑥̇ = 𝑟𝑥 − 𝑥3

  8.  𝑥̇ = 𝑥3 − 𝑟𝑥

  9.  𝑥̇ = (𝑟 − 1) − (𝑥 − 1)2

10.  𝑥̇ = (𝑟 − 2)𝑥 − 𝑥2

4.  𝑥̇ = 𝑟 + 3𝑥 − 𝑥3

11.  𝑥̇ = (𝑟 − 3)𝑥 − 𝑥3

5.  𝑥̇ = 𝑟 − 𝑒 𝑥

6.  𝑥̇ = 𝑟 − 𝑥2

7.  𝑥̇ = 𝑟𝑥 + 𝑥3

12.  𝑥̇ = 𝑟 − (𝑥 − 2)2

13.  𝑥̇ = (𝑟 − 1)(𝑥 − 1) − (𝑥 − 1)2

14.  𝑥̇ = 𝑟𝑥 (1 −

𝑥
𝑘

) − ℎ

Variables del ejercicio 14:

𝑥 = población, 𝑘= capacidad de carga,
ℎ = 𝑝𝑒𝑠𝑐𝑎, 𝑟= tasa de crecimiento

78

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Sistemas Dinámicos Lineales 2D

La teoría de los sistemas dinámicos 2D se refiere al estudio de cómo evolucionan los sistemas descritos
por ecuaciones diferenciales de primer orden que involucran dos variables independientes. En términos
generales, un sistema dinámico 2D describe cómo el estado de un sistema cambia con el tiempo en función
de dos variables, lo que genera un campo de trayectorias en un plano.

Son modelos matematicos de la forma:

𝑥̇ = 𝑎𝑥 + 𝑏𝑦
{
𝑦̇ = 𝑐𝑥 + 𝑑𝑦

Forma matricial

Donde:

𝐴 = (

𝑎 𝑏
𝑐 𝑑

)

𝑋(𝑡) = (

𝑥(𝑡)
𝑦(𝑡)

)

𝑋̇ = 𝐴𝑋
Estrucctura general

𝑋̇ =

𝑑
𝑑𝑡

(

𝑥
𝑦

) = (

𝑎 𝑏
𝑐 𝑑

) (

𝑥
𝑦

)

𝑥̇ = 𝑓( 𝑥,  𝑦)
{
𝑦̇ = 𝑔( 𝑥,  𝑦)

Donde: 𝑥(𝑡)𝑦 𝑦(𝑡) son variables de estado,
𝑓(𝑥, 𝑦) y 𝑔(𝑥, 𝑦) son funciones que definen la dinámica
𝑥̇ y 𝑦̇  son las derivadas temporales

, y

𝑑𝑥
𝑑𝑡

𝑑𝑦
𝑑𝑡

Conceptos claves:

1. Puntos Fijos (equilibrios): son soluciones constantes donde 𝑥̇ = 0,  𝑦̇ = 0 se encuentran resolviendo el
sistema  𝑓( 𝑥,  𝑦) = 0 𝑦 𝑔( 𝑥,  𝑦) = 0

2. Análisis de Estabilidad sistemas no lineales 2D

79

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝐽( 𝑥,  𝑦) =

𝜕𝑓
𝜕𝑥
𝜕𝑔
𝜕𝑥
[

𝜕𝑓
𝜕𝑦
𝜕𝑔
𝜕𝑦]

⌊( 𝑥∗,  𝑦∗)

Los autovalores de (J) determinan la estabilidad:

•  Reales y negativas diferentes: Nodo estable
•  Reales positivos diferentes: Nodo inestable
•  Complejo parte real positiva: espiral inestable
•  Complejo parte real negativo: espiral estable
•  Complejo puramente imaginario: Centro

1.  Nodos Estable

Si 𝜆1 < 𝜆2 < 0
Diferentes y negativos

𝑋(𝑡) = 𝑐1𝑒 𝜆1𝑡 (𝑣1) + 𝑐2𝑒 𝜆2𝑡(𝑣2),  𝜆1 < 𝜆2 los autovalores de la matriz determinante, es decir det(𝐴 − 𝜆𝐼) =
0, 𝑣1 𝑦  𝑣2 los autovectores asociados a los valores propios, (𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0

FIGURA 46

80

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

1.  Nodos Inestable

Si 𝜆1 > 𝜆2 > 0, Diferentes y positivos, 𝑋(𝑡) = 𝑐1𝑒𝜆1𝑡 (𝑣1) + 𝑐2𝑒𝜆2𝑡(𝑣2), 𝜆1,  𝜆2 los autovalores de la matriz
determinante , det(𝐴 − 𝜆𝐼) = 0, 𝑣1 𝑦  𝑣2 los autovectores asociados a los valores propios (𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0

FIGURA 47

2.  Silla

Si 𝜆1 < 0 < 𝜆2

Un  nodo  silla  de  caballo  (o  simplemente  silla)  es  un  tipo  fundamental  de  punto  crítico  en  los  sistemas
dinámicos 2D. Se refiere a un punto de equilibrio hiperbólico con utovalores reales de signos opuestos, y su
comportamiento es característico: una mezcla de estabilidad e inestabilidad.

𝑋(𝑡) = 𝑐1𝑒 𝜆1𝑡 (𝑣1) + 𝑐2𝑒 𝜆2𝑡(𝑣2), 𝑣1 𝑦  𝑣2 los autovectores asociados a los valores propios
(𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0, det(𝐴 − 𝜆𝐼) = 0, 𝜆1,  𝜆2 los autovalores de la matriz determinante

Comportamiento cualitativo

•  Hay una variedad estable (invariante) asociada al autovalor negativo.
•  Hay una variedad inestable asociada al autovalor positivo.
•
El origen no es ni atractor ni repulsor global: es un punto silla

Las trayectorias se acercan al origen en una dirección (estable) y se alejan en otra (inestable).

81

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 48

4. Focos y Centros

Si 𝜆1, 𝜆2  imaginarios
Para los focos o espirales el complejo conjugado.
Para los centros (orbitas periódicas) el autovalor es un número complejo

𝜆 = 𝛼 ± 𝛽𝑖

𝑒(𝛼±𝛽𝑖)𝑡 = 𝑒𝛼𝑡(cos 𝛽𝑡 ± 𝑖 sin 𝛽𝑡)

) = 𝑅𝑒(𝑣⃗) + 𝐼𝑚(𝑣⃗)i

𝑋(𝑡) = 𝑒𝛼𝑡(𝑐1(a cos 𝛽𝑡 − 𝑏 sin 𝛽𝑡) + 𝑐2(𝑎 sin 𝛽𝑡 + 𝑏 cos 𝛽𝑡))
𝑣⃗ = (𝑣1
𝑣2
𝑎 =  𝑅𝑒(𝑣⃗)
𝑏 =  𝐼𝑚(𝑣⃗)

𝑣1 𝑦  𝑣2 los autovectores asociados a los valores propios
𝜆1,  𝜆2 los autovalores de la matriz determinante
(𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0
det(𝐴 − 𝜆𝐼) = 0

FIGURA 49

82

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Espiral Inestable

Si 𝜆1, 𝜆2  imaginarios
La parte real del autovalor es positivo

𝜆 = 𝛼 ± 𝛽𝑖
𝛼 > 0
𝑋(𝑡) = 𝑒𝛼𝑡(𝑐1(a cos 𝛽𝑡 − 𝑏 sin 𝛽𝑡) + 𝑐2(𝑎 sin 𝛽𝑡 + 𝑏 cos 𝛽𝑡))
𝑣⃗ = (𝑣1
𝑣2
𝑎 =  𝑅𝑒(𝑣⃗)
𝑏 =  𝐼𝑚(𝑣⃗)
(𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0,  det(𝐴 − 𝜆𝐼) = 0

) = 𝑅𝑒(𝑣⃗) + 𝐼𝑚(𝑣⃗)i

Centros

Si 𝜆1, 𝜆2 puramente  imaginarios
La parte real del autovalor es cero
La parte real del autovalor es cero

𝜆 = 𝛼 ± 𝛽𝑖
𝛼 = 0

FIGURA 50

83

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

) = 𝑅𝑒(𝑣⃗) + 𝐼𝑚(𝑣⃗)i

𝜆 = ±𝛽𝑖
𝑋(𝑡) =  𝑒𝛼𝑡(𝑐1(a cos 𝛽𝑡 − 𝑏 sin 𝛽𝑡) + 𝑐2(𝑎 sin 𝛽𝑡 + 𝑏 cos 𝛽𝑡))
𝑋(𝑡) =  𝑐1(a cos 𝛽𝑡 − 𝑏 sin 𝛽𝑡) + 𝑐2(𝑎 sin 𝛽𝑡 + 𝑏 cos 𝛽𝑡)
𝑣⃗ = (𝑣1
𝑣2
𝑎 =  𝑅𝑒(𝑣⃗)
𝑏 =  𝐼𝑚(𝑣⃗)
(𝐴 − 𝜆𝑛𝐼)𝑣⃗ = 0
det(𝐴 − 𝜆𝐼) = 0

FIGURA 51

Comportamiento

•  Las soluciones son órbitas cerradas: circunferencias o elipses alrededor del origen.
•  El origen no es ni atractor ni repulsor.

El sistema es conservativo: no hay disipación de energía.

Nodos degenerados
Caso 1 donde:
Valores propios;  𝜆1 =  𝜆2 < 0
Matriz diagonizable: 2 autovalores linealmente independiente).
Sistema típico:

La solución a este sistema es la siguiente:

𝑑
𝑑𝑡

(

𝑥
𝑦

) = (

𝜆 0
0 𝜆

) (

𝑥
𝑦

)

84

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡 (

1
0

) + 𝑐2𝑒 𝜆𝑡 (

0
1

)

Comportamiento: todas las trayectorias se acercan exponencialmente al origen sin doblarse, el nodo es un
punto atractor simple

FIGURA 52

Nodo degenerado
Caso 2 donde: 𝜆1 =  𝜆2 < 0
Matriz no diagonizable:

𝑑
𝑑𝑡

(

𝑥
𝑦

) = (

𝜆 1
0 𝜆

) (

𝑥
𝑦

)

Como se solo hay una autovector (no dos linealmente independientes), y tenemos una raíz doble, el sistema
no es diagonizable entonces hay que buscar un vector generalizado.

(𝑣)es el único vector asociado al autovalor, entonces 𝑤 es el vector generalizado.

(𝐴 − 𝜆1𝐼)𝑣 = 𝑤

𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡𝑣 + 𝑐2𝑒 𝜆𝑡(𝑡𝑣 + 𝑤)

𝑋(𝑡) = 𝑒 𝜆𝑡 (𝑐1 (

1
0

) + 𝑐2 (𝑡 (

1
0

) + (

0
1

)))

Comportamiento:
las trayectorias se acercan al origen doblándose en formas de (z) por el termino en (t)
Nodo degenerado
Caso 3 donde: 𝜆1 =  𝜆2 > 0

85

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Matriz diagonizable;

Solución General

𝑑
𝑑𝑡

(

𝑥
𝑦

) = (

𝜆 0
0 𝜆

) (

𝑥
𝑦

)

𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡 (

1
0

) + 𝑐2𝑒 𝜆𝑡 (

0
1

)

FIGURA 53

Comportamiento:
las trayectorias se alejan del origen exponencialmente sin dobleces
Nodo degenerado
Caso 4 donde: 𝜆1 =  𝜆2  > 0
Matriz no diagonizable;

𝑑
𝑑𝑡

(

𝑥
𝑦

) = (

𝜆 1
0 𝜆

) (

𝑥
𝑦

)

Como se solo hay una autovector (no dos linealmente independientes), y tenemos una raíz doble, el sistema
no es diagonizable entonces hay que buscar un vector generalizado

(𝐴 − 𝜆1𝐼)𝑣2 = 𝑣1

86

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑣1 es el único vector asociado al autovalor, entonces 𝑣2 es el vector generalizado.

𝑋(𝑡) = 𝑐1𝑒𝜆𝑡𝑣1 + 𝑐2𝑒𝜆𝑡(𝑡𝑣1 + 𝑣2)

𝑋(𝑡) = 𝑒 𝜆𝑡 (𝑐1 (

1
0

) + 𝑐2 (𝑡 (

1
0

) + (

0
1

)))

FIGURA 54

Comportamiento: las trayectorias se alejan del origen doblándose en formas de (z) por el termino en (t)

Nodo degenerado Nulo

Caso 5 donde: 𝜆1 =  𝜆2  = 0
En los sistemas dinámicos lineales en el plano, un nodo degenerado nulo se refiere a un caso particular del
nodo degenerado en el que la única solución del sistema linealizado es el punto crítico, es decir, todas las
trayectorias colapsan hacia un punto y no se mueven. Sin embargo, este término se presta a confusión, así
que vamos a desglosarlo con claridad.

87

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

A= (

𝜆 1
0 𝜆

) , 𝐴 = (

𝑎 𝑏
𝑐 𝑑

)

𝜏= 𝑎 + 𝑑 (traza)

𝜏(𝐴) = 0,    det(𝐴) = 0
𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡𝑣1 + 𝑐2𝑒 𝜆𝑡(𝑡𝑣1 + 𝑤)
(𝐴 − 0𝐼)w = 𝑣1
1
0

𝑋(𝑡) = 𝑐1 (

) + 𝑐2 (𝑡 (

) + (

0
1

1
0

))

𝑣1 es el único vector asociado al autovalor, entonces 𝑤 es el vector generalizado.

                 FIGURA 55

Estabilidad

Este tipo de punto no puede clasificarse directamente como estable o inestable mediante el análisis lineal.
Se requiere un análisis no lineal (p.ej., usando el teorema de Hartman-Grobman o métodos de Lyapunov).

Nodo Estrella
Un nodo estrella aparece cuando: La matriz del sistema tiene un autovalor real doble: λ de multiplicidad
algebraica  2.  Pero  la  matriz  sí  es  diagonalizable,  es  decir,  tiene  dos  autovectores  linealmente
independientes. Entonces, el sistema tiene solución general del tipo:

𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡𝑣1 + 𝑐2𝑒 𝜆𝑡𝑣2

0) + 𝑐2 𝑒 𝜆𝑡 (0
1)

𝑋(𝑡) = 𝑐1𝑒 𝜆𝑡(1
𝜆 0
A= (
0 𝜆

)

88

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Comportamiento del nodo estrella

•  Las trayectorias son líneas rectas (por la estructura de la solución).
•  Todas las trayectorias apuntan directamente hacia o fuera del origen, dependiendo del signo de λ.
•  Las direcciones de movimiento no giran ni se curvan.

FIGURA 56

Ejercicios Sistemas dinámicos lineales 2D

Dadas los siguientes sistemas dimanamos:

m)  Resolver analíticamente si es posible.
n)  Calcular puntos de equilibrio
o)  Calcular los autovalores y autovalores asociados
p)  Dibujar su diagrama de fase manualmente
q)  Graficar de soluciones (use algún software para simular el campo vectorial y algunas soluciones).

1.  {

𝑥̇ = 𝑥
𝑦̇ = 𝑦

2.   {

𝑥̇ = −𝑦
𝑦̇ = 𝑥

3.   {

𝑥̇ = 𝑥
𝑦̇ = −𝑦

7.   {

𝑥̇ = 2𝑦
𝑦̇ = 2𝑥

11.   {

𝑥̇ = 𝑥 − 2𝑦
𝑦̇ = 𝑥 + 𝑦

21.   {

𝑥̇ = 𝑦
𝑦̇ = 6𝑥 + 𝑦

12.   {

𝑥̇ = 𝑥 − 𝑦
𝑦̇ = 3𝑥 + 3𝑦

22.   {

𝑥̇ = 2𝑥 − 2𝑦
𝑦̇ = 4𝑥 − 2𝑦

13.   {

𝑥̇ = −4𝑥 + 3𝑦
𝑦̇ = −6𝑥 + 5𝑦

23.   {

𝑥̇ = 𝑥 + 2𝑦
𝑦̇ = 2𝑥 + 𝑦

17.   {

𝑥̇ = −5𝑥 + 2𝑦
𝑦̇ = −10𝑥 + 3𝑦

27.   {

𝑥̇ = −2𝑥 + 𝑦
𝑦̇ = 𝑥 − 2𝑦

8.   {

𝑥̇ = −𝑦 + 𝑥
𝑦̇ = 𝑥 + 𝑦

18.   {

𝑥̇ = −2𝑥 + 3𝑦
𝑦̇ = −6𝑥 + 4𝑦

28.   {

𝑥̇ = 𝑥 + 3𝑦
𝑦̇ = 𝑥 − 𝑦

89

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

9.   {

𝑥̇ = 𝑥 − 2𝑦
𝑦̇ = −2𝑥 + 𝑦

10. {

𝑥̇ = 𝑥 + 2𝑦
𝑦̇ = 3𝑦 + 4𝑥

19.   {

𝑥̇ = 5𝑥 − 4𝑦
𝑦̇ = 𝑥 + 𝑦

20.   {

𝑥̇ = 3𝑥 + 𝑦
𝑦̇ = 𝑥 + 3𝑦

29.  Ẋ = (

a −2
2    1

) X

29. Hallar a∈ ℝ,  tal que:

a). El sistema tenga un equilibrio silla-nodo

b) Nodo estable

c) Espiral

30.  Sea  el  sistema  Masa-resorte  amortiguado:  𝑥̇ = 𝑦,   𝑦̇ = −𝑘 𝑥 − 𝑐 𝑦,   𝑘 > 0,  𝑐 ≥ 0 ,  se  quiere  analizar
usando
los  posibles
comportamientos del sistema según lo siguiente:

la  matriz  A  y  su  polinomio  característico:  𝜆2 + 𝑐𝜆 + 𝑘 = 0 ,  determinante

Condición Tipo Estabilidad Geometría

a) c2 > 4k Nodo Estable Entradas sin oscilación

b) c2 = 4k Nodo deg. Estable Recta dominante

c) c2 < 4k Foco Estable Espirales

d) c = 0 Centro Estable (no A.E.) Órbitas cerradas

31. Modelo idealizado de rotación rígida en un sistema físico

Un dispositivo experimental consiste en una partícula cargada que se mueve sin fricción en un plano bajo
la  acción de  un campo perpendicular constante. Se observa que la  fuerza ejercida  sobre la  partícula  es
siempre perpendicular a su velocidad y proporcional a su módulo, produciendo un movimiento rotacional
uniforme. Para modelar este fenómeno, se propone el siguiente sistema dinámico lineal bidimensional:

𝑥̇ = −𝜔𝑦, 𝑦̇ = 𝜔𝑥,  𝜔 > 0,

donde 𝑥(𝑡) y 𝑦(𝑡) representan las coordenadas de la partícula en el plano.

a)  Escriba el sistema en forma matricial y determine los autovalores (haga un análisis espectral)
b)  Halle la solución explícita del sistema para una condición inicial arbitraria (𝑥0, 𝑦0).
c)  Dibuje el diagrama de fases

90

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Diagrama de Poincaré

El diagrama de Poincaré clasifica el comportamiento local de un punto fijo (equilibrio o ciclo límite) usando
la traza y el determinante de la matriz linealizada 𝐴.

FIGURA 57

Sistemas lineales no homogéneos: preservación o ruptura de comportamientos

Forma general
Un sistema lineal no homogéneo tiene la forma

donde:

𝑥′(𝑡) = 𝐴𝑥(𝑡) + 𝑓(𝑡)

•  𝐴 𝑒𝑠 𝑢𝑛𝑎 𝑚𝑎𝑡𝑟𝑖𝑧 𝑐𝑜𝑛𝑠𝑡𝑎𝑛𝑡𝑒 𝑑𝑒 2 × 2
•  𝑓(𝑡) 𝑓𝑢𝑛𝑐𝑖ó𝑛 𝑣𝑒𝑐𝑡𝑜𝑟𝑖𝑎𝑙 (𝑛𝑜 𝑛𝑢𝑙𝑎 𝑒𝑛 𝑔𝑒𝑛𝑒𝑟𝑎𝑙)  El  sistema  es  no  homogéneo  El  sistema  es  no

homogéneo porque tiene un término independiente 𝑓(𝑡) ≠ 0

•  El sistema homogéneo asociado es:

𝑥′(𝑡) = 𝐴𝑥(𝑡)

91

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Su comportamiento (nodo, foco, centro, etc.) se determina completamente a partir de los valores propios
de A.

¿Qué ocurre al agregar 𝑓(𝑡)?

Si 𝑓(𝑡) es constante o convergente a un valor fijo: el comportamiento del sistema homogéneo se preserva
asintóticamente, pero la solución se desplaza hacia una nueva solución particular.

Si 𝑓(𝑡) tiene crecimiento (𝑡,  𝑒𝑡 ),  puede romper el comportamiento asintótico del sistema homogéneo.

solución General

Donde:

X(𝑡) = 𝑋ℎ(𝑡) + 𝑋𝑝(𝑡)

𝑥ℎ(𝑡): solución del sistema homogéneo

 𝑥𝑝(𝑡): 𝑠𝑜𝑙𝑢𝑐𝑖ó𝑛 𝑝𝑎𝑟𝑡𝑖𝑐𝑢𝑙𝑎𝑟 𝑑𝑒𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎 𝑛𝑜 ℎ𝑜𝑚𝑜𝑔é𝑛𝑒𝑜.

Ejemplo

𝑥̇ = (

𝑎 𝑏
𝑐 𝑑

) 𝑥 + (

𝑒
𝑓

)

Acá  𝑓(𝑡) =   (𝑒

𝑓) se tiene que platear una solución particular, suponga que son constantes en este caso:

 𝑋𝑝(𝑡)= (𝑥0

𝑦0),  el punto de equilibrio coincide con la solución particular.

Casos

Forma del sistema

𝑥′ =  𝐴𝑥  +  𝑏

𝑥′ =  𝐴𝑥  +   𝑒 𝜆𝑡 · 𝑣

Comportamien
to del sistema
homogéneo

Nodo / foco /
centro / etc.

Depende de
autovalores de
A

Forma de f(t)

Solución particular
xₚ(t)

𝑓(𝑡) =  𝑏

Constante:

𝐴 · 𝑥ₚ  =   −𝑏

𝑓(𝑡) =   𝑒 𝜆𝑡 · 𝑣

∝ tᵏ·e^(λt) (según
multiplicidad)

𝑥′ =  𝐴𝑥  + acos(𝑡) +  𝑏𝑠𝑖𝑛(𝑡)

Centro / foco
(oscilatorio)

𝑓(𝑡)
= acos(𝑡) +  𝑏𝑠𝑖𝑛(𝑡)

Periódica

𝑥′ =  𝐴𝑥  +  𝑝(𝑡)

Nodo / foco

f(t) = p(t) (polinomio)

Polinómica del
mismo grado

92

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Forma del sistema

Comportamien
to del sistema
homogéneo

Forma de f(t)

Solución particular
xₚ(t)

𝑥′ =  𝐴𝑥  +   𝑒−𝛼𝑡 · 𝑣

Nodo estable /
fuente / etc.

𝑓(𝑡) =   𝑒−𝛼𝑡 · 𝑣

Decae
exponencialmente

𝑥′ =  𝐴𝑥  +   𝑒𝑡 + cos(𝑡)

Mixto

𝑓(𝑡) =   𝑒𝑡 + cos(𝑡)

Suma de
soluciones
particulares

Ejercicios de sistemas lineales no homogéneos: preservación o ruptura de comportamientos

a)  Resolver si es posible analíticamente
b)  Hallar autovalores y autovectores
c)  Solución general del sistema en forma matricial
d)  Análisis del cambio o preservación de la dinámica al introducir la perturbación f(t)
e)  Resolver el sistema usando los métodos de coeficientes indeterminados o variación de parámetros
f)  Simular con un software la dinámica de cada sistema

1.  𝑋̇ = (

0 −1
0
−9

) 𝑋 + (1
9)

6.  𝑋̇ = (

−1
0
0 −2

) 𝑋 + (3
5)

2.  𝑋̇ = (

1 2
2 1

) (𝑥

𝑦) + (−5
−7)

7.  𝑋̇ = (

−1
0
0 −2

) 𝑋 + (cos 𝑡

0 )

4 −1
3.  𝑋̇ = (
1
2

) 𝑋 + ( 0

−6)

8.  𝑋̇ = (

−1
0
0 −2

) 𝑋 + (𝑒𝑡

0 )

4.  𝑋̇ = (

−2
1
1 −2

) 𝑋 + (3
2)

1
0
9.  𝑋̇ = (
0 −2

) 𝑋 + (𝑒𝑡

0 )

5.    𝑋̇ = (

−1 2
−1 1

) 𝑋 + (

−8
3

)

1
2
10.  𝑋̇ = (
0 −1

) 𝑋 + ( 𝑡

−𝑡)

Identificar cuales dinámicas cambian bruscamente si comportamiento con la función forzada f(t).

93

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Conversión de un sistema (EDO) de orden superior a un sistema de primer orden

a.  𝑦̈ − 4𝑦 = 2
b.  𝑦̈ + 2𝑦̇ − 3𝑦=6

Deducir  un algoritmo que permita realizar la transformación para este tipo de ecuación diferenciales de
segundo orden:

𝑦̈ + 𝑎1𝑦̇ + 𝑎0𝑦 = 𝑓(𝑡)

⃗⃗⃗⃗⃗
𝑑𝑥
𝑑𝑡

= (

0

1
−𝑎0 −𝑎1

) 𝑥⃗ + 𝑓(𝑡)

Idea clave: reducir a primer orden, todo sistema de orden 𝑛 puede escribirse como un sistema dinámico n
ℝ𝑛. Regla general, si tienes: 𝑥(𝑛) = 𝐹(𝑥, 𝑥̇, … , 𝑥(𝑛−1), 𝑡)

Definimos  nuevas  variables:  𝑥1 = 𝑥,   𝑥2 = 𝑥̇,   𝑥3 = 𝑥̈ ,  𝑥𝑛 = 𝑥𝑛−1 ,  y  obtienes:    𝑥̇1 = 𝑥2, 𝑥̇2 = 𝑥3, … , 𝑥̇𝑛 =
𝐹(𝑥1, … , 𝑥𝑛, 𝑡). Esto ya es un sistema dinámico de primer orden.

Ejemplo: 𝑥̈ + 3𝑥̇ + 2𝑥 = 0

Paso 1: nuevas variables: 𝑥1 = 𝑥,  𝑥2 = 𝑥̇

Paso 2: sistema equivalente:  {

𝑥̇1 = 𝑥2
𝑥̇2 = −3𝑥2 − 2𝑥1

Forma matricial:  𝑋̇ = (

0
1
−2 −3

) 𝑋

Otro ejemplo: Oscilador no lineal

(Van der Pol)

Sistema equivalente:

𝑥̈ + 𝜇(𝑥2 − 1)𝑥̇ + 𝑥 = 0

𝑥̇ = 𝑦
{
𝑦̇ = −𝑥 − 𝜇(𝑥2 − 1)𝑦

94

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Sistemas dinámicos no lineales

Un sistema dinámico no lineal en el plano es un sistema de ecuaciones diferenciales ordinarias de la forma:

𝑥̇ = 𝑓(𝑥, 𝑦)
{
𝑦̇ = 𝑔(𝑥, 𝑦)

donde

al  menos

una

de

las

funciones

𝑓(𝑥, 𝑦)

 o

𝑔(𝑥, 𝑦)

 no

es

lineal

¿cómo se analizan estos sistemas?

Para encontrar los puntos críticos se resuelve el sistema donde 𝑓(𝑥, 𝑦 = 0, y 𝑔(𝑥, 𝑦)=0, y para linealizar el
sistema cerca de estos puntos se usa la matriz jacobiana:

𝐽( 𝑥,  𝑦) =

𝜕𝑓
𝜕𝑥
𝜕𝑔
𝜕𝑥
[

𝜕𝑓
𝜕𝑦
𝜕𝑔
𝜕𝑦]

⌊( 𝑥∗,  𝑦∗)

Evaluar en el equilibrio y analizar los eigenvalores.

Si  el  punto  es  hiperbólico  (eigenvalores  con  parte  real  distinta  de  cero),  se  puede  usar  el  teorema  de
Hartman-Grobman.

 Si la linealización no concluye, usar:

•  Funciones de Lyapunov

•  El teorema de LaSalle

•  El teorema de Poincaré–Bendixson (si estamos en 2D)

•  Análisis global con curvas nulas, simetrías, energía, etc.

 Ejemplos clásicos de sistemas no lineales

1.  Sistema Depredador-Presa (Lotka-Volterra)

𝑥̇ = 𝛼𝑥 − 𝛽𝑥𝑦
{
𝑦̇ = 𝛿𝑥𝑦 − 𝛾𝑦

95

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Donde:  𝑥(𝑡) =presas,  𝑦(𝑡) = depredadores,  y  los  parámetros;  𝛼,   𝛽, 𝛿, 𝛾  son  propios  de  la  dinámica  del
sistema, como tasa de reproducción, mortalidad y otras.

𝛿
•  Este  sistema  tiene  dos  equilibrios  en:  (0,0)  donde  se  extinguen  ambas  especies,  y  en (
𝛾

,

𝛼
𝛽

),  las

soluciones son órbitas cerradas → centro (requiere análisis no lineal).

2.  Oscilador de Van der Pol

𝑥̇ = 𝑦
𝑦̇ = 𝜇(1 − 𝑥2)𝑦 − 𝑥

{

Si  𝜇 > 0, ciclo limite estable (atractor), no se puede deducir con linealización (se usa Lyapunov o análisis
de energía)

3.  Bifurcación tipo Hopf

𝑥̇ = 𝑦 − 𝑥(𝜇  − 𝑥2 − 𝑦2)
𝑦̇ = −𝑥 + 𝑦(𝜇 − 𝑥2 + 𝑦2)

{

Si 𝜇 < 0 estable, si 𝜇 > 0 aparece el ciclo limite

FIGURA 57

Sistema de Rayleigh modificado

𝑥̇ = 𝑦
{
𝑦̇ =   −𝑥 + (1 − 𝑥2)𝑦

Este  sistema  tiene  una  estructura  parecida  al  de  Van  der  Pol,  pero  con  una  forma  más  accesible  para
análisis cualitativo. El único punto de equilibrio (0,0)

𝐽(𝑥, 𝑦) =   [

−1 − 2𝑥𝑦 1 − 𝑥2]

0

1

96

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Es un foco espiral hasta llegar a un ciclo limite
Punto de equilibrio: solo (0,0)
Linealización: foco inestable (espiral que se aleja)
No linealidad: frena las soluciones para ∣ 𝑥 ∣> 1
Resultado global: se forma una órbita cerrada atractor → ciclo límite

FIGURA 58

¿Ciclo límite?

Para determinar si hay un ciclo límite, usamos razonamiento cualitativo:

•  El origen es inestable: las trayectorias se alejan.

•  Pero el término (1 − 𝑥2)𝑦  actúa como amortiguamiento no lineal:

o  𝑆𝑖 𝑥 > 1  𝑜 𝑥 < −1 𝑒𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎 𝑎𝑚𝑜𝑟𝑡𝑖𝑔𝑢𝑎 (𝑝𝑜𝑟𝑞𝑢𝑒 𝑥2 > 1  ⇒  𝑐𝑜𝑒𝑓𝑖𝑐𝑖𝑒𝑛𝑡𝑒 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑜).

o  𝑆𝑖 𝑥 ≈ 0 , 𝑙𝑎 𝑓𝑟𝑖𝑐𝑐𝑖ó𝑛 𝑒𝑠 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑎 (energía entra al sistema).

Esto sugiere que las soluciones no se van al infinito, sino que se estabilizan en una órbita cerrada.

Conclusión: Este sistema tiene un ciclo límite estable que rodea el origen.

97

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Análisis cualitativos

En ocasiones podemos analizar un sistema dinámico sin necesidad de resolverlo, sino en determinar las
estructuras  fundamentales  de  la  dinámica,  para  esto  nos  podemos  apoyar  de  algunos  fundamentos
teóricos  los  cuales  llamaremos  teoremas  fundamentales,  a  continuación,  un  resumen  de  los  más
importantes:

1.  Teorema de Existencia y Unicidad (Picard–Lindelöf)

Dado un sistema de EDO:

𝑥̇ = 𝑓(𝑡, 𝑥)

si  la  función  𝑓(𝑡, 𝑥)  es  continua  en  t  y  Lipschitz  en  x  (es  decir,  existe  una  constante  𝐿 > 0  𝑡𝑎𝑙 𝑞𝑢𝑒  ∥
𝑓(𝑡, 𝑥1) − 𝑓(𝑡, 𝑥2) ∥≤ 𝐿 ∥ 𝑥1 − 𝑥2 ∥, entonces existe una única solución local de la ecuación diferencial que
satisface la condición inicial 𝑥(𝑡0) = 𝑥0

Interpretación:

•  Existencia garantiza que sí hay una solución al sistema.

•  Unicidad garantiza que esa solución es única, es decir, no se bifurca.

Esto es crucial para entender que las trayectorias del sistema no se cruzan en el espacio de fase.

2. Teorema de Hartman–Grobman (Linealización)

FIGURA 59

Enunciado:  Sea  𝑥̇ = 𝑓(𝑥) ,    𝑓 ∈ 𝐶1  un  sistema  no  lineal  con  un  punto  crítico  𝑥0 hiperbólico  (todos  los
eigenvalores de la Jacobiana tienen parte real distinta de cero).  Entonces, cerca de 𝑥0, el sistema no lineal
es topológicamente conjugado a su sistema linealizado:  𝑥̇ ≈ 𝐷𝑓(𝑥0)(𝑥 − 𝑥0)

98

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Interpretación: El comportamiento cualitativo (tipo de punto fijo, direcciones de atracción/repulsión) del
sistema no lineal cerca del equilibrio es igual al del sistema lineal. No aplica si alguno de los eigenvalores
tiene parte real cero (punto no hiperbólico).

Sea 𝑥∗un punto de equilibrio.

3.  Estabilidad de Lyapunov (Directa)

Objetivo: Estudiar la estabilidad sin resolver el sistema explícitamente.

Idea central: Se busca una función escalar 𝑉(𝑥, 𝑦) tal que: 𝑉(𝑥, 𝑦) > 0  para todo (𝑥, 𝑦) ≠ (0,0)

•  𝑉(0,0) = 0

•

y la derivada de V a lo largo de las 𝑡𝑟𝑎𝑦𝑒𝑐𝑡𝑜𝑟𝑖𝑎𝑠 (𝑣̇ = 𝛻𝑉 ⋅ 𝑓) sea:

o  𝑣̇ < 0: el equilibrio es asintóticamente estable.

o  𝑣̇˙≤0: el equilibrio es estable.

o  𝑣̇ > 0: el equilibrio es inestable.

Ventaja: Permite determinar estabilidad sin necesidad de linealizar.

FIGURA 60

Estas imágenes muestran dos conceptos fundamentales en la teoría de estabilidad de Lyapunov, la imagen
de la izquierda muestra la estabilidad asintótica, el punto 𝑥∗ es atractor, y para una condición inicial 𝑥(0),
suficientemente cercana (dentro del radio 𝛿),  la trayectoria del sistema no solo permanece cerca de  𝑥∗,
sino que tiene a 𝑥∗ cuando 𝑡 → ∞, Es decir:

∥ 𝑥(𝑡) − 𝑥∗ ∥→ 0, 𝑐𝑢𝑎𝑛𝑑𝑜 𝑡 → ∞

99

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ahora la figura del lado derecho se conoce como estabilidad de Lyapunov que establece que el punto 𝑥∗, es
estable en el sentido de Lyapunov y toda trayectoria que comienza en la vecindad dentro de un radio 𝛿 de
𝑥∗ permanece dentro de una vecindad mayor de radio 𝜖, para todo tiempo futuro. Es decir:

∀𝜀 > 0,  ∃𝛿 > 0 𝑡𝑎𝑙 𝑞𝑢𝑒 𝑠𝑖  ∥ 𝑥(0) − 𝑥∗ ∥< 𝛿,  𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠  ∥ 𝑥(𝑡) − 𝑥∗ ∥< 𝜀 ∀𝑡 ≥ 0

La solución no se aleja, pero no necesariamente se acerca a 𝑥∗

Ejemplo: queremos estudiar el sistema dinámico si el punto (0,0) es estable usando la función de energía
de Lyapunov

Ejemplo 1

𝑥̇ = −𝑥 + 𝑥𝑦
{
𝑦̇ = −𝑦

Verificamos que (0,0) es un punto de equilibrio:

0 = −𝑥 + 𝑥𝑦
{
0 = −𝑦

𝑥̇ = 0, 𝑦̇ = 0, 𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠

El único punto de equilibrio es (0,0), Probamos la función de energía de Lyapunov

𝑥2 +

1
𝑉(𝑥, 𝑦)=
2
(0,0), entonces es positiva.

1
2

𝑦2, esta función siempre es mayor que cero cuando 𝑥 ≠ 0, o 𝑦 ≠ 0, y vale cero solo en

Calculamos la derivada de 𝑉,

𝑉̇ = 𝑥𝑥̇ + 𝑦𝑦̇, entonces 𝑉̇ = 𝑥(−𝑥 + 𝑥𝑦)
+ 𝑦(−𝑦)=−𝑥2 + 𝑥2𝑦-𝑦2=-𝑥2(1 − 𝑦) − 𝑦2,  si ahora cerca del origen
(𝑦) es pequeño, entonces 1 − 𝑦 > 0, y por tanto la expresión es negativa demostrando que 𝑉̇ < 0 cerca del
origen y 𝑉 > 0. La conclusión que el punto es estable.

4. Principio de invariancia de LaSalle

Teorema (LaSalle). Sea 𝑥̇ = 𝑓(𝑥) con 𝑓 continua. Sea 𝑉: 𝑈 → ℝ una función tal que:

1.  𝑉(𝑥) ≥ 0,

2.  𝑉̇ (𝑥) ≤ 0,

3.  Las trayectorias que parten de 𝑈 son acotadas.

100

̇

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Entonces, toda trayectoria converge al mayor conjunto invariante

𝑀 ⊂ {𝑥 ∈ 𝑈: 𝑉̇ (𝑥) = 0}.

Ejemplo típico en sistemas no lineales

{

𝑥̇ = −𝑥 + 𝑦2
𝑦̇ = −𝑦
1
2

𝑉(𝑥, 𝑦) =

(𝑥2 + 𝑦2)

𝑉̇ = −𝑥2 − 𝑦2 + 𝑥𝑦2 ≤ 0

•  𝑉̇ = 0 solo si 𝑥 = 0, 𝑦 = 0

•  El conjunto invariante es {(0,0)}

El origen es asintóticamente estable por LaSalle.

 Pasos prácticos para aplicar LaSalle

1.  Elegir 𝑉(𝑥)

2.  Calcular 𝑉̇ (𝑥)

3.  Encontrar 𝐸 = {𝑉̇ = 0}

4.  Determinar el mayor conjunto invariante

5.  Concluir el comportamiento asintótico

5. Teorema del flujo

Bajo las hipótesis del teorema de existencia y unicidad, el sistema define una aplicación

𝜑: ℝ × 𝑈 → ℝ𝑛

tal que:

1.  𝜑(0, 𝑥) = 𝑥,

2.  𝜑(𝑡 + 𝑠, 𝑥) = 𝜑(𝑡, 𝜑(𝑠, 𝑥)),

3.  𝜑(𝑡,⋅) es un homeomorfismo local.

101

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

La aplicación 𝜑 se denomina flujo del sistema.

FIGURA 61

El teorema del flujo es uno de los resultados fundamentales en la teoría de sistemas dinámicos, porque
formaliza  la  idea  de  que  un  sistema  de  ecuaciones  diferenciales  genera  un  movimiento  continuo  en  el
espacio de estados.

Como vienes trabajando fuerte con análisis cualitativo, fronteras, invariancia, LaSalle, Poincaré–Bendixson,
lo presento, pero con interpretación geométrica, que es donde realmente se usa.

En cuanto al flujo y trayectorias (órbita), de 𝑥0 es:

𝛾(𝑥0) = {Φ(𝑡, 𝑥0): 𝑡 ∈ ℝ}

Tipos:

•  órbitas abiertas

•  puntos de equilibrio

•  ciclos límite

•  órbitas homoclínicas / heteroclínicas

Todo tu trabajo con Poincaré–Bendixson y Dulac se apoya aquí.

102

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑥0 ∈ 𝑆 ⇒ Φ(𝑡, 𝑥0) ∈ 𝑆∀𝑡 ≥ 0

Φ(𝑡, 𝑥0) ∈ 𝑆 ∀𝑡 ≤ 0

Flujo e invariancia (muy importante)

Un conjunto 𝑆 ⊂ ℝ𝑛 es:

❖   Positivamente invariante si:

❖  Negativamente invariante si:

Esto es exactamente lo que usas en:

•  estudio de fronteras
•  conjuntos atrapantes
•  LaSalle
•  Poincaré–Bendixson

Flujo y campo vectorial

Relación fundamental:

𝑑
𝑑𝑡

Φ(𝑡, 𝑥) = 𝑓(Φ(𝑡, 𝑥))

Es decir:

•  el campo vectorial es el generador infinitesimal del flujo.

 Ejemplo sencillo (lineal)

Flujo explícito:

𝑥̇ = 𝐴𝑥

Φ(𝑡, 𝑥0) = 𝑒 𝐴𝑡𝑥0

Aquí:
•
•

las propiedades del flujo vienen de 𝑒 𝐴𝑡,
lo usas todo el tiempo en nodos, espirales, focos, etc.

 Ejemplo geométrico 2D

Solución:

{

𝑥̇ = −𝑦
𝑦̇ = 𝑥

103

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Φ(𝑡, (𝑥0, 𝑦0)) = (

𝑥0cos  𝑡 − 𝑦0sin  𝑡
𝑥0sin  𝑡 + 𝑦0cos  𝑡

)

Interpretación:

•

•

flujo = rotación

todas las órbitas son círculos

•  conjunto invariante: 𝑥2 + 𝑦2 = 𝑐

6. Teorema de la variedad estable e inestable

Sea 𝑥∗un equilibrio hiperbólico. Entonces existen variedades invariantes:

•  𝑊 𝑠(𝑥∗): variedad estable,

•  𝑊𝑢(𝑥∗): variedad inestable,

tangentes  en 𝑥∗ a  los  subespacios  propios  asociados  a  autovalores  con  parte  real  negativa  y  positiva,
respectivamente.

7. Teorema de la variedad central

Sea 𝑥∗un equilibrio de 𝑥̇ = 𝑓(𝑥), con 𝑓 ∈ 𝐶𝑘. Si existen autovalores con parte real cero, entonces existe una
variedad  central 𝑊𝑐 ,  invariante,  tangente  en  𝑥∗ al  subespacio  central,  tal  que  la  estabilidad  de  𝑥∗ está
determinada por la dinámica restringida a 𝑊𝑐.

8. Teorema de Poincaré–Bendixson

Sea 𝑥̇ = 𝑓(𝑥), 𝑥 ∈ ℝ2, donde 𝑓: ℝ2 → ℝ2es una función continuamente diferenciable (𝐶1).

Sea 𝐶 ⊂ ℝ2un conjunto compacto, cerrado e invariante positivamente para el sistema.
Sea 𝑥(𝑡) una trayectoria contenida en 𝐶.
Si el conjunto límite 𝜔(𝑥)no contiene puntos de equilibrio, entonces:

𝜔(𝑥) es una oˊ rbita perioˊ dica (ciclo lıˊmite).

Gráficamente:

104

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo: usar frontera geométrica para el sistema

FIGURA 62

{

𝑥̇ = 𝑦 − 𝑥
𝑦̇ = −𝑥 − 𝑦 + 𝑥2

Paso 1: Proponer región

Considerar el disco: 𝑅 𝑒𝑠 𝑚á𝑠 𝑔𝑟𝑎𝑛𝑑𝑒 𝑑𝑒 𝑐𝑢𝑎𝑙𝑞𝑢𝑖𝑒𝑟 𝑟 𝑐𝑒𝑟𝑐𝑎

𝐷 = {𝑥2 + 𝑦2 ≤ 𝑅2}

Paso 2: Producto con normal

Normal exterior:

∇𝑔(𝑥, 𝑦) = 𝑛⃗⃗ = (2𝑥, 2𝑦)
𝐹⃗ ⋅ 𝑛⃗⃗ = 2𝑥(𝑦 − 𝑥) + 2𝑦(−𝑥 − 𝑦 + 𝑥2)

Para 𝑅 grande:

Campo entra

𝐹⃗ ⋅ 𝑛⃗⃗ < 0

105

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Paso 3: Equilibrios

Resolver: 𝑦 = 𝑥, −𝑥 − 𝑦 + 𝑥2 = 0 ⇒ 𝑥(𝑥 − 2) = 0

Solo uno dentro → se puede excluir con un anillo

Conclusión: Por Poincaré–Bendixson, existe un ciclo límite

Otro ejemplo: (clásico – existencia de ciclo límite)

Sistema

𝑥̇ = 𝑦 − 𝑥(𝑥2 + 𝑦2 − 1)
{
𝑦̇ = −𝑥 − 𝑦(𝑥2 + 𝑦2 − 1)

𝑟2 = 𝑥2 + 𝑦2

𝑟̇ = 𝑟(1 − 𝑟2),

𝜃̇ = −1

𝐷 = {(𝑥, 𝑦): 𝑟 ≤ 2}

Paso 1: Coordenadas polares

Se obtiene:

Paso 2:  Análisis radial

•  Si 𝑟 < 1: 𝑟̇ > 0→ sale
•  Si 𝑟 > 1: 𝑟̇ < 0→ entra

El círculo 𝑟 = 1  atrae trayectorias

Paso 3: Región invariante

•  Cerrada
•  Acotada
•
•  Sin equilibrios en 0 < 𝑟 < 2

Invariante

Conclusión: por Poincaré–Bendixson, existe un: ciclo lıˊmite estable en 𝑟 = 1
Ejercicio (región anular)

𝑥̇ = 𝑦 + 𝑥(1 − 𝑥2 − 𝑦2)
𝑦̇ = −𝑥 + 𝑦(1 − 𝑥2 − 𝑦2)

{

106

Modelado y Simulación – 3.1.025

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Paso 1. Sistema radial:  𝑟̇ = 𝑟(1 − 𝑟2)

Paso 2. Definir anillo: 𝐷 = {1/2 ≤ 𝑟 ≤ 2}

•  En 𝑟 = 1/2:  𝑟̇ > 0→ entra
•  En 𝑟 = 2:  𝑟̇ < 0→ entra

Paso 3: Sin equilibrios en D
El único equilibrio está en el origen 𝑟 = 0 ∉ 𝐷
Conclusión: Existe al menos una órbita periódica en D, → ciclo límite

9. Teorema de Bendixson–Dulac

Sea 𝑥̇ = 𝑓(𝑥)un sistema plano. Si existe una función 𝐵(𝑥, 𝑦) ∈ 𝐶1 tal que ∇ ⋅ (𝐵𝑓)

no cambia de signo y no se anula en una región simplemente conexa 𝐷, entonces el sistema no posee
ciclos límite contenidos en 𝐷.

El sistema del ejemplo

{

𝑥̇ = 𝑥(1 − 𝑥2 − 𝑦2) − 𝑦
𝑦̇ = 𝑦(1 − 𝑥2 − 𝑦2) + 𝑥

Es un sistema radial + rotacional. De hecho, en coordenadas polares: 𝑟̇ = 𝑟(1 − 𝑟2), 𝛳̇ = 1

Esto ya te dice que existe un ciclo límite estable en 𝑟 = 1.  Es el ejemplo clásico de oscilador con ciclo
límite.

¿Por qué falla Bendixson clásico?

Tomamos 𝐵(𝑥, 𝑦) = 1.

div  𝐹 =

∂𝑃
∂𝑥

+

∂𝑄
∂𝑦

= 2 − 4(𝑥2 + 𝑦2)

•  Es positiva si 𝑥2 + 𝑦2 <

1
2

•  Negativa si 𝑥2 + 𝑦2 >

1
2

 Cambia de signo, Bendixson no concluye nada

 La idea clave de Dulac generaliza Bendixson permitiendo un factor 𝐵(𝑥, 𝑦). Se propone:

107

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Dominio:

 El cálculo crítico (y correcto)
Se calcula:

Resultado (efectivamente):

𝐵(𝑥, 𝑦) =

1
𝑥2 + 𝑦2

𝐷 = ℝ2 ∖ {(0,0)}

∂(𝐵𝑃)
∂𝑥

+

∂(𝐵𝑄)
∂𝑦

= −2

Negativo constante, no cambia de signo, pero cumple las hipótesis del teorema de Dulac en 𝐷.

 ¿Cuál es el error conceptual frecuente?

La lámina dice: no existen ciclos límite en ℝ2 ∖ {0}

Esto es falso si se interpreta literalmente, porque:

•  El ciclo límite 𝑥2 + 𝑦2 = 1

•  Está contenido completamente en ℝ2 ∖ {0}

Contradicción aparente

Teorema de Dulac–Bendixson exige dominio simplemente conexo

Pero:

ℝ2 ∖ {0}

No es simplemente conexo (tiene un “agujero” en el origen).  El ciclo límite rodea el agujero, Dulac no puede
aplicarse globalmente

  El  cálculo  con  𝐵(𝑥, 𝑦) = 1/(𝑥2 + 𝑦2) es  correcto
 Conclusión  correcta  (la  que  deberías  usar):
 La  divergencia  es  negativa  constante,  no  se  puede  concluir
límite
porque  el  dominio  no  es  simplemente  conexo,  de  hecho,  este  ejemplo  se  usa  justamente  para  mostrar
porqué la hipótesis topológica del dominio es esencial.

inexistencia  de  ciclos

108

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Aunque existe un factor de Dulac 𝐵(𝑥, 𝑦) = 1/(𝑥2 + 𝑦2)  tal que ∇ ⋅ (𝐵𝐹) < 0 en ℝ2 ∖ {0}, el dominio no es
simplemente conexo, por lo que el teorema de Dulac–Bendixson no excluye la existencia de ciclos límite.
De hecho, el sistema posee un ciclo límite estable dado por 𝑥2 + 𝑦2 = 1.

{

𝑥̇ = 𝑃(𝑥, 𝑦) = 𝑥(1 − 𝑥2 − 𝑦2) − 𝑦
𝑦̇ = 𝑄(𝑥, 𝑦) = 𝑦(1 − 𝑥2 − 𝑦2) + 𝑥

Elección del factor de Dulac

Elegimos (como en la lámina): 𝐵(𝑥, 𝑦) =

1
𝑥2+𝑦2

Dominio:

𝐷 = ℝ2 ∖ {(0,0)}

Calculamos 𝐵𝑃 y 𝐵𝑄, Producto 𝐵𝑃

𝐵𝑃 =

𝑥(1 − 𝑥2 − 𝑦2) − 𝑦
𝑥2 + 𝑦2

=

𝑥

𝑥2 + 𝑦2 − 𝑥 −

𝑦
𝑥2 + 𝑦2

Producto 𝐵𝑄

𝐵𝑄 =

𝑦(1 − 𝑥2 − 𝑦2) + 𝑥
𝑥2 + 𝑦2

=

𝑦

𝑥2 + 𝑦2 − 𝑦 +

𝑥
𝑥2 + 𝑦2

Derivada parcial de 𝐵 𝑃respecto de 𝑥

Derivamos término a término: Sumamos:

∂(𝐵𝑃)
∂𝑥

=

𝑦2−𝑥2+2𝑥𝑦
(𝑥2

+𝑦2)2 − 1

Derivada parcial de 𝐵𝑄respecto de 𝑦

Sumamos:

∂(𝐵𝑄)
∂𝑦

=

𝑥2−𝑦2−2𝑥𝑦
(𝑥2

+𝑦2)2 − 1

Sumamos las derivadas (Dulac)

∂(𝐵𝑃)
∂𝑥

+

∂(𝐵𝑄)
∂𝑦

Numeradores: (𝑦2 − 𝑥2 + 2𝑥𝑦) + (𝑥2 − 𝑦2 − 2𝑥𝑦) = 0

Entonces:

∂(𝐵𝑃)
∂𝑥

+

∂(𝐵𝑄)
∂𝑦

= −1 − 1 = −2

109

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Resultado final ∇ ⋅ (𝐵𝐹) = −2 < 0 en ℝ2 ∖ {0}

Negativo constante, no cambia de signo y cumple la condición analítica de Dulac

Recordatorio importante (conceptual): Aunque el cálculo es correcto, no elimina el ciclo límite porque ℝ2 ∖
{0} no es simplemente conexo.

De hecho, el sistema sí tiene el ciclo: 𝑥2 + 𝑦2 = 1

10. Teorema de invariancia positiva (criterio de frontera)

Sea 𝑆 ⊂ ℝ𝑛 una región cerrada con frontera suave. Si para todo 𝑥 ∈ ∂𝑆,

𝑓(𝑥) ⋅ 𝑛(𝑥) ≤ 0,

donde 𝑛(𝑥) es la normal al exterior, entonces 𝑆 es positivamente invariante.

11. Teorema de bifurcación de Hopf

Sea 𝑥̇ = 𝑓(𝑥, 𝜇) con 𝑓 ∈ 𝐶𝑘. Supóngase que en 𝜇 = 𝜇0 el Jacobiano tiene un par de autovalores conjugados
que cruzan transversalmente el eje imaginario. Entonces existe un intervalo de valores de 𝜇 donde aparece
(o desaparece) un ciclo límite.

12. Teorema de estabilidad estructural (plano)

Un sistema plano es estructuralmente estable si todos sus equilibrios y ciclos límite son hiperbólicos y no
existen  conexiones  heteroclínicas  delicadas.  En  tal  caso,  pequeñas  perturbaciones  no  alteran  el
comportamiento cualitativo.

Observación final (clave conceptual)

Todos  estos  teoremas  permiten  clasificar  comportamiento  sin  resolver  el  sistema,  y  se  articulan  en  el
siguiente  orden  lógico:  existencia  →  flujo  →  estabilidad  →  invariancia  →  comportamiento  límite  →
bifurcaciones.

Simulamos usando el siguiente código

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# Sistema de ecuaciones

110

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

def system(t, z):
    x, y = z
    dxdt = -x + x * y
    dydt = -y
    return [dxdt, dydt]

# Campo vectorial
x_vals = np.linspace(-2, 2, 20)
y_vals = np.linspace(-2, 2, 20)
X, Y = np.meshgrid(x_vals, y_vals)
DX = -X + X * Y
DY = -Y
M = np.hypot(DX, DY)
M[M == 0] = 1
DX /= M
DY /= M
# Condiciones iniciales
initial_conditions = [
    [2, 2], [-2, 2], [1, -1], [-1, -1], [0.5, 1.5], [1.5, -0.5], [-1.5, 0.5], [0, 1], [1, 0]
]

# Tiempo de simulación
t_span = (0, 10)
t_eval = np.linspace(*t_span, 300)
# Graficar
plt.figure(figsize=(8, 8))
plt.quiver(X, Y, DX, DY, M, pivot='middle', cmap=plt.cm.plasma, alpha=0.3)
# Trayectorias
for z0 in initial_conditions:
    sol = solve_ivp(system, t_span, z0, t_eval=t_eval)
    plt.plot(sol.y[0], sol.y[1], label=f'{z0}')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trayectorias del sistema\ndx/dt = -x + xy, dy/dt = -y')
plt.grid()
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.legend(loc='upper right', fontsize='small')
plt.show()

111

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

La simulación del sistema en Python:

Ejemplo 2:  𝑥̇ = −𝑥3,  𝑦̇ = −𝑦 + 𝑥𝑦2

FIGURA 63

•  El sistema no es linealizable (Jacobiano nulo en el origen)
•  La estabilidad no se puede decidir por autovalores
•  La función de Lyapunov permite concluir estabilidad no lineal

Vamos a estudiar el punto (0,0) y se demuestra que es el único punto de equilibrio, y en su vecindad para
valores pequeños estudiemos la función de energía de Lyapunov

1
2

1
2

𝑥2 +

𝑦2,  calculamos  la  derivada,  entonces: 𝑉̇ = 𝑥𝑥̇ + 𝑦𝑦̇ ,   𝑉̇ = 𝑥(−𝑥3)̇ + 𝑦(−𝑦 + 𝑥𝑦2)=−𝑥4 −
𝑉(𝑥, 𝑦)=
𝑦2 + 𝑥𝑦3,  Analizamos  cada  termino )=−𝑥4 − 𝑦2 ,  siempre  es  negativo  y  como 𝑥𝑦3, puede  ser  positivo  o
negativo pero muy pequeño al estar cerca del origen comparado con el otro termino se puede deducir que
𝑉̇ < 0

112

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 64

Recordemos que según el teorema de Poincaré–Bendixson

Enunciado:

En un sistema dinámico en el plano (ℝ2), si una órbita permanentemente contenida en una región cerrada,
acotada y sin puntos fijos en su interior, entonces su límite 𝜔-límite es:

•  un punto fijo, o

•  una órbita periódica (ciclo límite), o

•  una unión finita de órbitas y puntos fijos conectados por separatrices.

Importancia:

Este teorema descarta el caos en sistemas 2D continuos: no puede haber dinámica caótica en el plano.

A  continuación,  se  muestra  el  diagrama  de  fase  del  sistema  oscilatorio  conocido  como  Va  de  Pol,  La
ecuación original de segundo orden es

𝑥̈ − 𝜇(1 − 𝑥2)𝑥̇ + 𝑥 = 0,

𝜇 ∈ ℝ

Se transforma en un sistema 2D tomando: 𝑥̇ = 𝑦, 𝑦̇ = 𝜇(1 − 𝑥2)𝑦 − 𝑥

113

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

En la siguiente figura #64, se puede obervar la región de captura:

FIGURA 65

FIGURA 66

114

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

También recordemos el teorema de LaSalle (Principio de Invariancia)

Generaliza el método de Lyapunov:

Si:

•  𝑉(𝑥) es una función de Lyapunov tal que 𝑉̇ (x)≤0 en una región invariante D,

•  Entonces las trayectorias de D tienden al conjunto más grande donde 𝑉̇ (𝑥) = 0

Utilidad:

Permite deducir convergencia a conjuntos atractores más generales que un solo punto.

Conclusión

Los sistemas no lineales 2D muestran una enorme variedad de comportamientos que no pueden capturarse
con  sistemas  lineales.  Su  análisis  combina  herramientas  algebraicas  (Jacobiana),  teóricas  (Lyapunov,
Poincaré–Bendixson) y gráficas (diagramas de fase), siendo uno de los campos más ricos y aplicados de las
matemáticas modernas

Pasos para resolver sistemas dinámicos no lineales

1. Encontrar puntos de equilibrio

2. Calcular Jacobiano

3. Autovalores → estabilidad

4. Clasificar tipo de punto

5. Analizar comportamiento no lineal

6. Estudiar bifurcaciones (si hay parámetro)

7. Dibujar retrato de fase

Ejemplo 1

Modelo de Lotka Volterra con competencia

{𝑥′ = 𝑥(1 − 𝑥 − 𝑦),

𝑦′ = 𝑦(2 − 𝑥 − 𝑦)

Encontramos los puntos de equilibrio

115

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

a)  𝐸scribir f(x, y) = 0, g(x, y) =  0

b)  Resolver el sistema de ecuaciones no lineales:

o  Si las funciones tienen factores comunes, factorízalos.

o  Divide en casos según los factores

c)  Analiza cada caso:

o  Sustituye un valor en la otra ecuación para encontrar los pares (x, y)

o  Revisa si hay soluciones repetidas o inconsistentes.

d)  Escribir todos los puntos de equilibrio encontrados.

1.  Puntos de equilibrio: (0,0), (1,0), (0,2)

2.  Jacobiano

𝐽(𝑥, 𝑦) =   [

0
−𝑦 2 − 𝑥 − 2𝑦

−𝑥

]

3.  Evaluamos cada punto de equilibrio y se obtiene que el punto (0,0) es un nodo fuente, el (2,0) es un
punto silla, y el (0,1) un nodo atractor por lo que la dinámica del campo es la siguiente: Como el sistema es
polinómico de grado 2, y los puntos de equilibrio ya están completamente clasificados por el Jacobiano, no
se necesita análisis adicional. No hay ciclos límite.

FIGURA 67
116

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 2

Análisis sin usar coordenadas polares

Consideramos el sistema: 𝑥′ = 𝑦,   𝑦′ = −𝑥 + 𝑥(1 − 𝑥2 − 𝑦2)

4.  Puntos de equilibrio

Resolvemos:

•  𝑦 = 0,
•  0 = −𝑥 + 𝑥(1 − 𝑥2 − 𝑦2)

𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠: resolvemos y el punto es (0,0)

2.  Cálculo del Jacobiano

En

𝐽(0,0) =   [

0 1
0 0

]

3. Autovalores del Jacobiano

𝐽(𝑥, 𝑦) =   [

0

1

−3𝑥2 − 𝑦2 −2𝑥𝑦

]

det(𝐽 − 𝜆𝐼) = |

−𝜆
1
0 −𝜆

| = 𝜆2 = 0,  𝜆 = 𝜆1 = 𝜆2 (doble)

4. Clasificación del punto crítico

•  Tenemos un autovalor doble nulo.

•  No hay información completa con la linealización.

•  Este es un caso degenerado: necesitamos analizar más allá.

Función de energía

1. Función tipo energía (Lyapunov o similar)

Proponemos una función tipo energía (Lyapunov):

𝑉(𝑥, 𝑦) =

1
2

𝑥2 +

1
2

𝑦2,

𝐶𝑎𝑙𝑐𝑢𝑙𝑎𝑚𝑜𝑠 𝑠𝑢 𝑑𝑒𝑟𝑖𝑣𝑎𝑑𝑎 𝑎 𝑙𝑜 𝑙𝑎𝑟𝑔𝑜 𝑑𝑒 𝑙𝑎𝑠 𝑡𝑟𝑎𝑦𝑒𝑐𝑡𝑜𝑟𝑖𝑎𝑠 𝑑𝑒𝑙 𝑠𝑖𝑠𝑡𝑒𝑚𝑎:

117

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑑𝑉
𝑑𝑡

= 𝑥𝑥′ + 𝑦𝑦′˙ = 𝑥𝑦 + 𝑦[−𝑥 + 𝑥(1 − 𝑥2 − 𝑦2)] = 𝑥𝑦 + 𝑦𝑥(−𝑥2 − 𝑦2)

Análisis de la derivada 𝑉′, r𝑒𝑐𝑜𝑟𝑑𝑒𝑚𝑜𝑠 𝑞𝑢𝑒 𝑟2 = 𝑥2 + 𝑦2, e𝑛𝑡𝑜𝑛𝑐𝑒𝑠:

𝑉′ = 𝑥𝑦(1 − 𝑟2),  𝐴ℎ𝑜𝑟𝑎 𝑎𝑛𝑎𝑙𝑖𝑧𝑎𝑚𝑜𝑠:

•  𝑆𝑖 𝑟2 < 1: 𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 1 − 𝑟2 > 0   𝐸𝑙 𝑠𝑖𝑔𝑛𝑜 𝑑𝑒 𝑉˙ 𝑑𝑒𝑝𝑒𝑛𝑑𝑒 𝑑𝑒 𝑥𝑦.
•  𝑆𝑖 𝑟2 > 1:  𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠 1 − 𝑟2 < 0  𝐸𝑙 𝑠𝑖𝑔𝑛𝑜 𝑐𝑎𝑚𝑏𝑖𝑎.
•  𝑆𝑖 𝑥 = 0  𝑜 𝑦 = 0:  𝑉′ = 0

Esto no nos da una función estrictamente decreciente, pero sí indica que en la frontera 𝑟 = 1 ocurre un
cambio importante.

Estudio geométrico del vector

𝑦′ = 𝑥(1 − 𝑥2 − 𝑦2)

La aceleración vertical de 𝑦′cambio de signo cuando, 𝑥2 + 𝑦2 = 1, el circulo de radio 1, Dentro del círculo:
y’  tiene el mismo signo que 𝑥  → repulsivo del origen. Fuera del círculo: y’  tiene el signo contrario a 𝑥  →
atracción hacia el centro. Esto sugiere que las trayectorias que comienzan lejos del origen se acercan a la
frontera del circulo   𝑥2 + 𝑦2 = 1, y las que están dentro se alejan: esto implica un ciclo límite estable.

FIGURA 68

118

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Sistemas varios

Ejemplo 1

𝑥̇ = 𝑥𝑦
{
𝑦̇ = 𝑥2 + 𝑦2 − 1

hay cuatro  puntos críticos: un nodo  inestable, y otro estable, (0,1), (0,-1), y dos puntos silla (1,0), (-1,0).
Todos  los  puntos  son  hiperbólicos  por  lo  que  la  linealización  nos  ofrece  suficiente  información  de  la
naturaleza de la dinámica.

𝐽(𝑥, 𝑦) =   [

𝑥

𝑦
2𝑥 2𝑦]

FIGURA 69

119

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Observaciones visuales:

•  𝐸𝑛 𝑒𝑙 𝑐í𝑟𝑐𝑢𝑙𝑜 𝑢𝑛𝑖𝑑𝑎𝑑 (𝑥2 + 𝑦2 = 1) 𝑠𝑒 𝑜𝑏𝑠𝑒𝑟𝑣𝑎 𝑢𝑛𝑎 𝑡𝑟𝑎𝑛𝑠𝑖𝑐𝑖ó𝑛: 𝑑𝑒𝑛𝑡𝑟𝑜 𝑑𝑒 é𝑙,

= 0, 𝑎𝑠í 𝑞𝑢𝑒 𝑙𝑜𝑠 𝑣𝑒𝑐𝑡𝑜𝑟𝑒𝑠 𝑠𝑜𝑛 𝑣𝑒𝑟𝑡𝑖𝑐𝑎𝑙𝑒𝑠.

= 0, 𝑦 𝑒𝑙 𝑚𝑜𝑣𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑒𝑠 𝑡𝑎𝑚𝑏𝑖é𝑛 𝑣𝑒𝑟𝑡𝑖𝑐𝑎𝑙.

•

𝑑𝑦
𝑑𝑡

< 0;   𝑓𝑢𝑒𝑟𝑎,

𝑑𝑦
𝑑𝑡

> 0

•  𝐴 𝑙𝑜 𝑙𝑎𝑟𝑔𝑜 𝑑𝑒𝑙 𝑒𝑗𝑒 𝑥 = 0,

•  𝐴 𝑙𝑜 𝑙𝑎𝑟𝑔𝑜 𝑑𝑒𝑙 𝑒𝑗𝑒 𝑦 = 0,

𝑑𝑥
𝑑𝑡

𝑑𝑡
𝑑𝑥

Ejemplo 2

𝑥̇ = 𝑥(2 − 𝑥 − 𝑦)
{
𝑦̇ = 𝑦(3 − 2𝑥 − 𝑦)

hay cuatro puntos críticos: (0,0) fuente, (0,3) nodo estable, y (1,1) silla, (2,0) nodo estable. Todos los puntos
son  hiperbólicos  por  lo  que  la  linealización  nos  ofrece  suficiente  información  de  la  naturaleza  de  la
dinámica.

𝐽(𝑥, 𝑦) =   [

2 − 2𝑥
−2𝑦

−𝑥
3 − 2𝑥 − 2𝑦

]

FIGURA 70

120

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 3

𝑥̇ = 𝑦
{
𝑦̇ = 𝑥2 + 𝑦2 − 1

hay dos puntos críticos: (-1,0) es un centro lineal, por lo que la linealización no es suficiente para determinar
su naturaleza necesita un análisis adicional fuente, (1,0) es un punto silla (hiperbólico).

𝐽(𝑥, 𝑦) =   [

0
1
2𝑥 2𝑦

]

Análisis adicional para el punto (-1,0) orbitas circulares (determinar si son cerradas o espirales), para ello
hagamos una transformación a coordenadas polares:

𝑥𝑥̇ +𝑦𝑦̇
𝑟

𝑟̇ =

,      𝜃̇ =

,      𝑥 = 𝑟 cos 𝜃 , 𝑦 = 𝑟 sin 𝜃 ,  𝑥2 + 𝑦2 = 𝑟2 ,  entonces  la  transformación  es  no  da
mucha información así que se prueba dibujando el campo vectorial, No son propiamente orbitas cerradas,
pero se observa las trayectorias circulares

𝑥𝑦̇ −𝑦𝑥̇
𝑟2

FIGURA 71

121

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 4

𝑥̇ = 𝑥𝑦 − 2𝑦
{
𝑦̇ = 𝑥𝑦 − 2𝑥

hay dos puntos críticos: (0,0) es un punto silla, y (2,2) un nodo inestable

𝐽(𝑥, 𝑦) =   [

𝑦
𝑦 − 2

𝑥 − 2
𝑥

]

Este  ejemplo  tiene  dos  puntos  críticos,  un  punto  silla  y  un  nodo  fuente  ambos  hiperbólicos  así  que  la
linealización con el jacobiano es suficiente para predecir su comportamiento en el diagrama de fases.

Análisis con coordenadas polares

𝑟̇ =

𝑥𝑥̇ +𝑦𝑦̇
𝑟

,

𝜃̇ =

𝑥𝑦̇ −𝑦𝑥̇
𝑟2

,

𝑥 = 𝑟 cos 𝜃 , 𝑦 = 𝑟 sin 𝜃,

𝑥2 + 𝑦2 = 𝑟2

FIGURA 72

122

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 5: Analicemos el siguiente sistema:

𝑥̇ = −𝑦 − 𝑥(𝑥2 + 𝑦2)
{
𝑦̇ = 𝑥 − 𝑦(  𝑥2 + 𝑦2)

𝜆 = ±𝑖 (comportamiento lineal pero no concluyente para sistema no lineal)

•  El origen (0,0) es un punto crítico no hiperbólico.

•  Autovalores puramente imaginarios → centro lineal.

•  Pero el sistema es no lineal, por lo que este análisis solo indica que hay movimiento oscilatorio cerca

del origen.

Si realizamos la transformación de coordenadas se obtiene:

{𝑟̇ = −𝑟3
𝜃̇ = 1

Esto significa:

•  Las trayectorias son espirales que giran en sentido antihorario 𝜃 = 1

•  Pero el radio decrece: 𝑟̇ = −𝑟3 ⇒ 𝑟(𝑡)→0

•  Entonces, todas las trayectorias se mueven como espirales hacia el origen.

Ejemplo 6:

{𝑥̇ = −𝑥 + 𝑦 − 𝑥(𝑥2 + 𝑦2),  𝑦̇ = −𝑥 − 𝑦 − 𝑦(𝑥2 + 𝑦2)

{𝑟̇ = −𝑟(1 + 𝑟2),  𝜃̇ = −1

Interpretación

•

𝑟̇ = −𝑟(1 + 𝑟2): el radio siempre decrece ⇒ todas las trayectorias van hacia el origen.

•  𝜃̇=−1: rotación uniforme en sentido horario.

Las soluciones son espirales que giran hacia adentro en sentido horario, convergiendo al origen.

123

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

En la siguiente figura se ve como las trayectorias radiales se puedes representar en un diagrama (𝑥, 𝑦)

FIGURA 73

FIGURA 74

124

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 7

{𝑥̇ = 𝑥(1 − 𝑥2 − 𝑦2) − 𝑦,

𝑦̇ = 𝑦(1 − 𝑥2 − 𝑦2) + 𝑥

Transformación a coordenadas polares

{𝑟̇ = 𝑟(1 − 𝑟2),

𝜃̇ = 1

Simulamos:

FIGURA 75

Aquí puedes ver el comportamiento del sistema no lineal en coordenadas cartesianas:

•  Las trayectorias parten de distintas condiciones iniciales.

•  Tienden hacia la circunferencia de radio 1, como predice la ecuación

•

ṙ = r(1 − r2):  si r < 1, crece;  si r > 1, decrece.

•  𝑈𝑛𝑎 𝑣𝑒𝑧 𝑐𝑒𝑟𝑐𝑎 𝑑𝑒𝑙 𝑐í𝑟𝑐𝑢𝑙𝑜, 𝑔𝑖𝑟𝑎𝑛 𝑎𝑙𝑟𝑒𝑑𝑒𝑑𝑜𝑟 𝑑𝑒𝑙 𝑜𝑟𝑖𝑔𝑒𝑛 𝑐𝑜𝑛 𝑣𝑒𝑙𝑜𝑐𝑖𝑑𝑎𝑑 𝑎𝑛𝑔𝑢𝑙𝑎𝑟 𝑐𝑜𝑛𝑠𝑡𝑎𝑛𝑡𝑒 𝜃̇ = 1

Este  es  un  ejemplo  claro  de  cómo  el  análisis  polar  permite  entender  fácilmente  el  comportamiento:
espirales entrantes hacia una órbita circular estable.

125

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Estudio de Frontera

Para  ampliar  el  análisis  cualitativo  de  los  sistemas  dinámicos  y  en  ocasiones  se  presenta  el  caso  que
tenemos un sistema y queremos que el mismo permanezca en control, o en un rango de parámetros de
estabilidad del sistema al que llamaremos zona segura. Entonces ¿Qué significa “estudiar la frontera”?

Tenemos un sistema dinámico plano:

𝑋̇ = 𝐹(𝑋),

𝑋 = (𝑥, 𝑦) ∈ ℝ2

y un conjunto 𝑆 ⊂ ℝ2.

Estudiar la  frontera  significa  responder:  ¿Qué hace el  campo  vectorial  cuando  una  trayectoria  llega  a  la
frontera de 𝑆?

Tres posibilidades locales en un punto de la frontera:

1.  El campo entra en 𝑆

2.  El campo sale de 𝑆

3.  El campo es tangente a la frontera

De esto depende si 𝑆 es:

•  positivamente invariante

•  negativamente invariante

•  o no invariante

FIGURA 76

126

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Idea geométrica fundamental

Sea 𝑝 ∈ ∂𝑆 (frontera).

•  La frontera tiene una dirección normal

•  El campo vectorial 𝐹(𝑝) tiene una dirección propia

El signo del producto escalar

𝑛(𝑝). 𝐹(𝑝)

Criterio analítico (criterio de Nagumo en 2D)

Sea 𝑝 ∈ ∂𝑆.

Calculamos:

Interpretación:

Signo de 𝑔̇ Significado

<0

Campo entra en 𝑆

> 0

Campo sale de 𝑆

= 0

Campo tangente

Condición de invariancia

Positivamente invariante

 ¿Qué significa “estudiar la frontera”?

Tenemos un sistema dinámico plano:

y un conjunto S ⊂ ℝ2.

Estudiar la frontera significa responder:

𝑔̇(𝑝) = ∇𝑔(𝑝) ⋅ 𝐹(𝑝)

Ẋ = 𝐹(𝑋), 𝑋 = (𝑥, 𝑦) ∈ ℝ2

¿Qué hace el campo vectorial cuando una trayectoria llega a la frontera de S?

Tres posibilidades locales en un punto de la frontera:

1.  El campo entra en S

127

Modelado y Simulación – 3.1.025

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

2.  El campo sale de S

3.  El campo es tangente a la frontera

De esto depende si S es:

•  positivamente invariante

•  negativamente invariante

•  o no invariante

 Cómo describir matemáticamente una frontera

Caso estándar (el más usado)

La frontera se escribe como:

∂S = {(x, y): g(x, y) = 0}

con:

•  g(x, y) < 0 dentro de S

•  g(x, y) > 0 fuera de S

Ejemplos:

•  Rectas

•  Semiplanos

•  Regiones poligonales

•  Elipses, discos, etc.

El vector normal a la frontera

Si

entonces:

es un vector normal a la frontera.

g(x, y) = 0

∇g(x, y) = (

∂g
∂x

, ∂g
∂y

)

128

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Importante:

•  𝛻𝑔 apunta hacia donde 𝑔crece

•  Si  𝑆 = {𝑔 ≤ 0}, entonces 𝛻𝑔es normal exterior

Método paso a paso (algoritmo práctico)

Cuando te dan un conjunto S:

Paso 1 Identificar las fronteras

Descomponer S como intersección de desigualdades:

𝑆 = ⋂  {

𝑔𝑖(𝑥, 𝑦) ≤ 0}

𝑖

Cada 𝑔𝑖 = 0 es una frontera.

Paso 2 Elegir correctamente gi

No es arbitrario:

•  gi < 0 dentro

•  gi > 0 fuera

Esto fija la normal exterior.

Paso 3 Calcular el gradiente

Paso 4 Producto escalar con el campo

∇gi

∇gi ⋅ F

Paso 5 Evaluar sobre la frontera, es decir sustituir la ecuación de la frontera.

Paso 6 Analizar el signo

•  ≤ 0 → no sale

•  ≥ 0 → no entra

129

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  = 0 → tangente

 Ejemplo 1:

𝑥̇ = 2𝑥 − 𝑦 + 1
{
𝑦̇ = −𝑥 + 2𝑦 − 5

𝑋(0) = (

)

2
3

𝑆 = {(𝑥, 𝑦) ∈ ℝ2:  4 − 𝑥 ≤ 𝑦 ≤ 2 + 𝑥}

Reescritura del conjunto (clave); expresamos Scomo intersección de desigualdades del tipo 𝑔 ≤ 0:

𝑔1(𝑥, 𝑦) = 4 − 𝑥 − 𝑦 ≤ 0
{
𝑔2(𝑥, 𝑦) = 𝑦 − 𝑥 − 2 ≤ 0

Por lo tanto, las fronteras son: Γ1: 4 − 𝑥 − 𝑦 = 0,  𝛤2: 𝑦 − 𝑥 − 2 = 0

Campo vectorial

Estudio de la frontera Γ1

✓  Gradiente (normal exterior)

𝐹(𝑥, 𝑦) = (

2𝑥 − 𝑦 + 1
−𝑥 + 2𝑦 − 5

)

∇g1 = (−1, −1)

✓  Producto escalar

∇g1 ⋅ F = −(2x − y + 1) − (−x + 2y − 5)

✓  Evaluamos sobre la frontera y = 4 − x

𝛻𝑔1 ⋅ 𝐹 = −(2𝑥 − (4 − 𝑥) + 1) − [−𝑥 + 2(4 − 𝑥) − 5]

= −(3𝑥 − 3) − (−3𝑥 + 3) = 0

Conclusión: el campo es tangente en Γ1.

Estudio de la frontera Γ2

130

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

✓  Gradiente

✓  Producto escalar

∇g2 = (−1,1)

∇g2 ⋅ F = −(2x − y + 1) + (−x + 2y − 5)

✓  Evaluamos sobre y = 2 + x

𝛻𝑔2 ⋅ 𝐹 = −(2𝑥 − (2 + 𝑥) + 1) + (−𝑥 + 2(2 + 𝑥) − 5)

= −(𝑥 − 1) + (𝑥 − 1) = 0

Conclusión: el campo es tangente en Γ2.

Conclusión (i)

•  El campo no sale del conjunto en ninguna frontera

•  La trayectoria con X(0) ∈ S permanece en S

•  S es positivamente invariante

Ejemplo 2

𝑥̇ = −𝑥 + 4𝑦 − 2
{
𝑦̇ = 𝑥 − 𝑦 − 1

𝑋(0) = (

3
1

)

𝑆 = {(𝑥, 𝑦) ∈ ℝ2:  4 − 2𝑦 ≤ 𝑥 ≤ 2𝑦}

{

𝑔1(𝑥, 𝑦) = 4 − 2𝑦 − 𝑥 ≤ 0
𝑔2(𝑥, 𝑦) = 𝑥 − 2𝑦 ≤ 0

Reescritura del conjunto

Fronteras: 𝛤1: 4 − 2𝑦 − 𝑥 = 0,  𝛤2: 𝑥 − 2𝑦 = 0

Campo vectorial

131

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Estudio de  Γ1

✓  Gradiente

𝐹(𝑥, 𝑦) = (

−𝑥 + 4𝑦 − 2
𝑥 − 𝑦 − 1

)

∇g1 = (−1, −2)

✓  Producto escalar
✓  𝛻𝑔1 ⋅ 𝐹 = −(−𝑥 + 4𝑦 − 2) − 2(𝑥 − 𝑦 − 1)

✓  Evaluamos sobre x = 4 − 2y

𝛻𝑔1 ⋅ 𝐹 = −(−(4 − 2𝑦) + 4𝑦 − 2) − 2[(4 − 2𝑦) − 𝑦 − 1]

= −(6𝑦 − 6) − (6 − 6𝑦) = 0

Campo tangente.

Estudio de Γ2

✓  Gradiente

∇g2 = (1, −2)

✓  Producto escalar

✓  Evaluamos sobre x = 2y

𝛻𝑔2 ⋅ 𝐹 = (−𝑥 + 4𝑦 − 2) − 2(𝑥 − 𝑦 − 1)

(2𝑦 − 2) − 2(𝑦 − 1) = 0

 Campo tangente.

Conclusión: S es positivamente invariante

Ejemplo 3

Sistema: 𝑥̇ = −𝑥 + 𝑦,  𝑦̇ = −𝑥 − 𝑦

Conjunto 𝑆 = {𝑥2 + 𝑦2 ≤ 1}

132

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Para  la  frontera definimos 𝑔(𝑥, 𝑦) = 𝑥2 + 𝑦2 − 1 ≤ 0,  y calculamos el gradiente ∇𝑔=(2𝑥, 2𝑦)  entonces el
porducto escalar ∇𝑔. 𝐹(𝑥, 𝑦) =(2𝑥, 2𝑦)(−𝑥 + 𝑦, −𝑥 − 𝑦) = −2(𝑥2 + 𝑦2) = −2(1),  ya que 𝑥2 + 𝑦2=1. Por lo
tanto no hay cmbion de signo y el flujo apunto  hacia  dentro  del conjunto por lo que se concluye que es
positivamente invariante

FIGURA 77

FIGURA 78

Adicionalmente  si  estudiamos  su  Jacobiano  nos  damos  cuenta  de  que  es  una  espiral  estable,  y  según
Harmant Grobmant sabemos que el punto de equilibrio es hiperbólico y estable.

133

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo 4

Frontera  de  control  en  un  sistema  dinámico  simple  (consideremos  el  sistema  no  lineal  con  control
acotado):

𝑥̇ = 𝑥2 + 𝑢,

∣ 𝑢 ∣≤ 1

Interpretación  física: 𝑥2  dinámica  natural  (empuja  siempre  hacia +∞), 𝑢:  freno  o  empuje  externo,  pero
limitado

Pregunta clave de control:

¿Desde  qué  valores  iniciales  𝑥0 puedo  evitar  que  el  sistema  explote  hacia  +∞ ?  eso  define  su  región
controlable y frontera.

Observa:

•  Si 𝑥 es grande y positivo → 𝑥2 es enorme

•  El control máximo es solo 𝑢 = −1

Hay un punto donde: 𝑥2 = 1, ahí el control máximo empata a la dinámica natural.

Cálculo exacto de la frontera

Usamos el control más favorable:

El sistema límite es:

Buscamos dónde:

𝑢 = −1

𝑥̇ = 𝑥2 − 1

𝑥̇ = 0 ⇒ 𝑥2 − 1 = 0 ⇒ 𝑥 = ±1

Interpretación  geométrica  de  la  región:  𝑥 < 1  entonces  𝑥̇ > 0  (entra),  ahora  sí    −1 < 𝑥 < 1  (puede
estabilizarse), pero 𝑥 = 1 (frontera de control), y  𝑥 > 1 (siempre explota)

134

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Código para simular sistemas dinámicos

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import tkinter as tk
from tkinter import ttk, messagebox
from numpy.linalg import eig, inv
# Función para graficar el sistema
def graficar_sistema(nombre, sistema, A=None, mostrar_autovec=False, x_eq=None):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_title(nombre)
    zoom = 3
    x = np.linspace(-zoom, zoom, 20)
    y = np.linspace(-zoom, zoom, 20)
    X, Y = np.meshgrid(x, y)
    U, V = np.zeros_like(X), np.zeros_like(Y)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            dxdt, dydt = sistema(0, [X[i, j], Y[i, j]])
            U[i, j], V[i, j] = dxdt, dydt
    N = np.sqrt(U**2 + V**2)
    U_norm = U / (N + 1e-8)
    V_norm = V / (N + 1e-8)
    ax.quiver(X, Y, U_norm, V_norm, color='gray')
    init_conds = [(-1, -1), (-1, 1), (1, -1), (1, 1), (0.5, 0), (0, 0.5)]
    for ic in init_conds:
        sol = solve_ivp(sistema, [0, 10], ic, t_eval=np.linspace(0, 10, 500))
        ax.plot(sol.y[0], sol.y[1], lw=1)
    if A is not None and mostrar_autovec:
        vals, vecs = eig(A)
        for i in range(vecs.shape[1]):
            v = vecs[:, i].real
            v = v / np.linalg.norm(v)
            ax.plot([0, 3 * v[0]], [0, 3 * v[1]], 'g--', lw=2)
            ax.plot([0, -3 * v[0]], [0, -3 * v[1]], 'g--', lw=2)
        ax.text(-2.8, 2.6, f"Autovalores: {np.round(vals, 2)}", fontsize=10)
    if x_eq is not None:
        ax.plot(x_eq[0], x_eq[1], 'ro', markersize=8)
        ax.text(x_eq[0] + 0.2, x_eq[1], 'Equilibrio desplazado', color='red')
    def on_click(event):
        if event.inaxes == ax:
            ic = [event.xdata, event.ydata]
            sol_f = solve_ivp(sistema, [0, 10], ic, t_eval=np.linspace(0, 10, 500))
            sol_b = solve_ivp(sistema, [0, -10], ic, t_eval=np.linspace(0, -10, 500))
            ax.plot(sol_f.y[0], sol_f.y[1], 'r', lw=2)
            ax.plot(sol_b.y[0], sol_b.y[1], 'b--', lw=1)
            fig.canvas.draw()
    fig.canvas.mpl_connect('button_press_event', on_click)
    ax.set_xlim(-zoom, zoom)
    ax.set_ylim(-zoom, zoom)
    ax.grid()
    plt.xlabel("x")
    plt.ylabel("y")

135

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

    plt.show()
# GUI
def main_gui():
    root = tk.Tk()
    root.title('Simulador de Sistemas Dinámicos')
    root.geometry('520x450')
    sistemas_famosos = {
        "Van der Pol": {
            "dx": "y",
            "dy": "mu*(1 - x**2)*y - x",
            "A": "",
            "f": "",
            "params": {"mu": 1.0}
        },
        "Nodo espiral (inestable)": {
            "dx": "x - y",
            "dy": "x + y",
            "A": "1 -1; 1 1",
            "f": "",
        },
        "Nodo fuente": {
            "dx": "2*x",
            "dy": "3*y",
            "A": "2 0; 0 3",
            "f": "",
        },
        "Silla": {
            "dx": "x",
            "dy": "-y",
            "A": "1 0; 0 -1",
            "f": "",
        },
        "Centro": {
            "dx": "-y",
            "dy": "x",
            "A": "0 -1; 1 0",
            "f": "",
        },
        "Sistema no homogéneo": {
            "dx": "0",
            "dy": "0",
            "A": "0 1; -1 0",
            "f": "[0, np.sin(t)]",
        }
    }
    selected_system = tk.StringVar()
    tk.Label(root, text="Selecciona un sistema famoso:").pack()
    dropdown = ttk.Combobox(root, textvariable=selected_system, values=list(sistemas_famosos.keys()))
    dropdown.pack()
    def cargar_sistema(event=None):
        nombre = selected_system.get()
        if nombre in sistemas_famosos:
            config = sistemas_famosos[nombre]
            dx_entry.delete(0, tk.END)

136

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

            dx_entry.insert(0, config["dx"])
            dy_entry.delete(0, tk.END)
            dy_entry.insert(0, config["dy"])
            A_entry.delete(0, tk.END)
            A_entry.insert(0, config.get("A", ""))
            ft_entry.delete(0, tk.END)
            ft_entry.insert(0, config.get("f", ""))
    dropdown.bind("<<ComboboxSelected>>", cargar_sistema)
    tk.Label(root, text='dx/dt =').pack()
    dx_entry = tk.Entry(root, width=40)
    dx_entry.pack()
    tk.Label(root, text='dy/dt =').pack()
    dy_entry = tk.Entry(root, width=40)
    dy_entry.pack()
    tk.Label(root, text='Matriz A (opcional):').pack()
    A_entry = tk.Entry(root, width=40)
    A_entry.pack()
    tk.Label(root, text='Campo f(t) (opcional):').pack()
    ft_entry = tk.Entry(root, width=40)
    ft_entry.pack()
    autovec_check = tk.BooleanVar()
    autovec_check.set(True)
    tk.Checkbutton(root, text='Mostrar autovectores y neutros', variable=autovec_check).pack()
    def plot_field():
        dx_formula = dx_entry.get()
        dy_formula = dy_entry.get()
        A_text = A_entry.get()
        ft_text = ft_entry.get()
        mostrar_autovec = autovec_check.get()
        A = None
        if A_text.strip():
            try:
                filas = A_text.strip().split(';')
                A = np.array([[float(num) for num in fila.strip().split()] for fila in filas])
                if A.shape != (2, 2):
                    raise ValueError("A debe ser 2x2")
            except Exception as e:
                messagebox.showerror("Error", f"Error en matriz A: {e}")
                return
        def sistema(t, z):
            x, y = z
            local_vars = {'x': x, 'y': y, 'np': np, 't': t, 'mu': 1.0}
            dx = eval(dx_formula, local_vars)
            dy = eval(dy_formula, local_vars)
            ft = None
            if ft_text.strip():
                try:
                    ft = eval(ft_text, {'t': t, 'np': np})
                except Exception as e:
                    messagebox.showerror("Error", f"Error en f(t): {e}")
                    raise
            if A is not None:
                dx += A[0, 0]*x + A[0, 1]*y
                dy += A[1, 0]*x + A[1, 1]*y

137

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

            if ft is not None:
                dx += ft[0]
                dy += ft[1]
            return [dx, dy]
        x_eq = None
        if A is not None and ft_text.strip():
            try:
                ft0 = eval(ft_text, {'t': 0, 'np': np})
                x_eq = -inv(A) @ ft0
            except Exception as e:
                messagebox.showwarning("Advertencia", f"No se pudo calcular el equilibrio desplazado: {e}")
        nombre = f"Sistema: dx={dx_formula}, dy={dy_formula}"
        graficar_sistema(nombre, sistema, A=A, mostrar_autovec=mostrar_autovec, x_eq=x_eq)
    tk.Button(root, text='Graficar campo', command=plot_field).pack(pady=10)
    root.mainloop()
main_gui()

FIGURA 79

138

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Tiene ejemplos clásicos como: Van der pol y variantes

FIGURA 80

BIBLIOGRAFIAS DEL CAPÍTULO II

Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems (11th
ed.). Wiley.

Hirsch,  M.  W.,  Smale,  S.,  &  Devaney,  R.  L.  (2013).  Differential  equations,  dynamical  systems,  and  an
introduction to chaos (3rd ed.). Academic Press.

Jordan, D. W., & Smith, P. (2007). Nonlinear ordinary differential equations: An introduction for scientists and
engineers (4th ed.). Oxford University Press.

Perko, L. (2001). Differential equations and dynamical systems (3rd ed.). Springer.

Strogatz, S. H. (2015). Nonlinear dynamics and chaos: With applications to physics, biology, chemistry, and
engineering (2nd ed.). CRC Press.

OpenCourseWare.

MIT
https://ocw.mit.edu/courses/mathematics/18-03-differential-equations-spring-2010/

Differential

equations,

(2010).

18.03

Spring

2010.

Dawkins, P. (s. f.). Paul’s online math notes. Lamar University. https://tutorial.math.lamar.edu/

Khan Academy. (s. f.). Differential equations. https://www.khanacademy.org/math/differential-equations

139

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios Sistemas dinámicos no lineales

1. Dinámica de una partícula en un potencial no lineal

𝑥̇ = 𝑦, 𝑦̇ = 𝑥(3 − 𝑥)

Una partícula se mueve sobre una recta bajo una fuerza dependiente de la posición.

a) Determine las posiciones de equilibrio y describa su estabilidad.
b) ¿Para qué condiciones iniciales el movimiento permanece acotado?

2. Oscilador con doble pozo

𝑥̇ = 𝑦, 𝑦̇ = 𝑥3 − 𝑥

Este sistema modela una partícula en un potencial con dos mínimos estables.

a) Identifique los puntos de equilibrio y su naturaleza.
b) Explique qué tipo de trayectorias separan los movimientos oscilatorios de los no acotados.

3. Sistema mecánico con fricción dependiente de la velocidad

𝑥̇ = 𝑦 − 𝑥, 𝑦̇ = 𝑥2 − 1

El sistema describe una masa sometida a una fuerza no lineal y disipación.

a) Determine los equilibrios y clasifíquelos.
b) Describa el comportamiento del sistema para tiempos grandes.

4. Movimiento con restricción radial

𝑥̇ = 𝑥𝑦, 𝑦̇ = 𝑥2 + 𝑦2 − 1

Una partícula cambia su dinámica al cruzar una región circular.

a) Analice el papel del círculo unidad en la dinámica.
b) Determine si el disco unitario es un conjunto invariante.

5. Oscilaciones auto-sostenidas

140

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑥̇ = 𝑦 − 𝑥(𝜇 − 𝑥2 − 𝑦2), 𝑦̇ = −𝑥 + 𝑦(𝜇 − 𝑥2 − 𝑦2)

Modelo de un sistema físico con retroalimentación no lineal.

a) Explique cómo varía la dinámica al cambiar el parámetro 𝜇.
b) Determine si aparece un ciclo límite.

6. Sistema disipativo no lineal

𝑥̇ = −𝑥 + 𝑦 − 𝑥(𝑥2 + 𝑦2), 𝑦̇ = −𝑥 − 𝑦 − 𝑦(𝑥2 + 𝑦2)

El sistema representa un movimiento con pérdidas crecientes.

a) Estudie la estabilidad del origen.
b) Describa el comportamiento asintótico de las trayectorias.

7. Oscilador rotante con saturación

𝑥̇ = 𝑥(1 − 𝑥2 − 𝑦2) − 𝑦, 𝑦̇ = 𝑦(1 − 𝑥2 − 𝑦2) + 𝑥

Este modelo aparece en electrónica y biología.

a) Analice la dinámica radial del sistema.
b) Determine la existencia y estabilidad de órbitas periódicas.

8. Competencia entre dos especies

𝑥̇ = 𝑥(2 − 𝑥 − 𝑦), 𝑦̇ = 𝑦(3 − 2𝑥 − 𝑦)

Dos poblaciones compiten por recursos limitados.

a) Determine si es posible la coexistencia estable.
b) Interprete biológicamente los equilibrios.

9. Reacción química autocatalítica

𝑥̇ = 𝑥2 − 𝑦 + 1, 𝑦̇ = 𝑥(𝑦 + 3)

141

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelo simplificado de una reacción química no lineal.

a) Analice los estados estacionarios del sistema.
b) Describa el comportamiento esperado para grandes concentraciones.

10. Vórtice disipativo

𝑥̇ = −𝑦 − 𝑥(𝑥2 + 𝑦2), 𝑦̇ = 𝑥 − 𝑦(𝑥2 + 𝑦2)

El sistema describe un flujo rotacional con fricción radial.

a) Determine el sentido de rotación del flujo.
b) Analice si el origen es atractor.

11. Interacción económica no simétrica

𝑥̇ = −𝑥 + 𝑥𝑦, 𝑦̇ = −2𝑥 + 𝑥𝑦

Dos variables económicas interactúan de forma no lineal.

a) Analice la estabilidad de los equilibrios.
b) Determine si alguna variable puede crecer indefinidamente.

12. Campo no uniforme

𝑥̇ = 𝑥2 + 𝑦2 − 2, 𝑦̇ = 𝑥2 − 𝑦2

Describe el movimiento de una partícula en un campo espacialmente variable.

a) Determine las regiones donde el movimiento es acelerado.
b) Analice la estabilidad de los equilibrios.

13. Competencia logística

𝑥̇ = 14𝑥 − 0.5𝑥2 − 𝑥𝑦, 𝑦̇ = 16𝑦 − 0.5𝑦2 − 𝑥𝑦

Dos especies con crecimiento logístico interactúan.

142

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

a) Determine el equilibrio de coexistencia.
b) Analice su estabilidad.

14. Competencia asimétrica

Modelado y Simulación – 3.1.025

𝑥̇ = 𝑥(3 − 𝑥) − 2𝑥𝑦, 𝑦̇ = 𝑦(2 − 𝑦) − 𝑥𝑦

Modelo ecológico con competencia desigual.

a) Analice el destino de cada especie.
b) Determine si existe exclusión competitiva.

15. Presa–depredador con límite ambiental

𝑥̇ = 𝑥(1 − 𝑥) − 𝑥𝑦, 𝑦̇ = −𝑦 + 𝑥𝑦

Modelo clásico de interacción biológica.

a) Analice la estabilidad del equilibrio interior.
b) Determine si pueden existir oscilaciones persistentes.

16. Oscilador tipo Van der Pol

𝑥̇ = 𝑦, 𝑦̇ = −𝑥 + 𝑦(1 − 𝑥2)

Sistema mecánico con realimentación no lineal.

a) Analice la estabilidad del origen.
b) Determine la aparición de un ciclo límite.

17. Sistema con amortiguamiento transversal

𝑥̇ = 𝑥 + 𝑦2, 𝑦̇ = −𝑦

Describe un sistema con disipación parcial.

a) Analice el equilibrio del sistema.
b) Describa el efecto del término 𝑦2.

143

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

18. Oscilador no lineal

𝑥̇ = 𝑦, 𝑦̇ = −sin  𝑦

Modelo simplificado de un péndulo.

a) Determine los equilibrios.
b) Analice la posibilidad de movimientos periódicos.

19. Modelo económico con saturación

𝑥̇ = −2𝑥 − 3𝑥𝑦, 𝑦̇ = 3𝑦 − 𝑦2

Interacción entre dos sectores económicos.

a) Analice la estabilidad de los equilibrios.
b) Determine regiones invariantes.

20. Flujo no lineal anisótropo

𝑥̇ = 2𝑥 − 𝑦 + 2𝑥𝑦 + 3(𝑥2 − 𝑦2), 𝑦̇ = 𝑥 − 3𝑦 + 𝑥𝑦 − 3(𝑥2 − 𝑦2)

Modelo abstracto de flujo en un medio complejo.

a) Clasifique el equilibrio en el origen.
b) Discuta la influencia de los términos cuadráticos.

21. Sistema con simetría hiperbólica

𝑥̇ = 𝑥2 − 𝑦2 − 1, 𝑦̇ = 2𝑦

Describe una dinámica con crecimiento direccional.

a) Analice los equilibrios.
b) Describa el comportamiento para 𝑡 → ∞.

22. Sistema de control no lineal

𝑥̇ = 𝑦 − 𝑥2 + 2, 𝑦̇ = 𝑥2 − 𝑥𝑦

144

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelo de control con realimentación cuadrática.

a) Analice la estabilidad del equilibrio.
b) Discuta la influencia del término 𝑥2

23. Interacción híbrida

𝑥̇ = 𝑥(3 − 𝑥) − 2𝑥𝑦, 𝑦̇ = 𝑥𝑦 + (𝑥 − 3)

Sistema con interacción biológica y externa.

a) Analice la estabilidad de los equilibrios.
b) Interprete el término 𝑥 − 3.

24. Modelo general presa–depredador

𝑥̇ = 𝑎𝑥 + 𝑏𝑥𝑦, 𝑦̇ = −𝑐𝑦 + 𝑑𝑥𝑦

Modelo universal de interacción biológica.

a) Determine los equilibrios en función de los parámetros.
b) Discuta la posibilidad de ciclos cerrados.

25. Reacción química con entrada constante

𝑥̇ = 𝑦 − 𝑥2, 𝑦̇ = 1 − 𝑦

Modelo de una reacción con alimentación externa.

a) Determine el equilibrio del sistema.
b) Analice la estabilidad.

Sistema mecánico con fricción cúbica

𝑥̇ = −𝑥 − 𝑦 + 𝑥𝑦3, 𝑦̇ = 𝑥 − 𝑦 + 𝑦3

Modelo de movimiento en un medio no lineal.

145

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

a) Analice la estabilidad del origen.
b) Discuta el efecto de los términos cúbicos.

27. Sistema geométrico no conservativo

𝑥̇ = 𝑥3 + 𝑦2 − 1, 𝑦̇ = 𝑥2 − 𝑦2

Modelo abstracto para estudiar bifurcaciones.

a) Analice los equilibrios.
b) Describa la dinámica lejos del origen.

28. Sistema con acoplamiento cruzado

𝑥̇ = 𝑥(1 − 𝑦2), 𝑦̇ = 𝑦(𝑥2 − 1)

Modelo de interacción energética.

a) Determine los conjuntos invariantes.
b) Clasifique los equilibrios.

29. Sistema cúbico con rotación

𝑥̇ = 𝑥3 − 𝑦, 𝑦̇ = 𝑦 − 𝑥

Modelo no lineal con rotación y crecimiento.

a) Analice la estabilidad del origen.
b) Discuta el efecto del término cúbico sobre el flujo.

30.    Un  sistema  de  control  de  temperatura  con  retroalimentación  dada  por  el  sistema:  𝑥̇ = −𝑥 + 𝑦
(desviación de temperatura), y , 𝑦̇ = −𝑦 + 2 − 𝑥2 (potencia de enfriamiento), como se muestra en la figura
siguiente, y lo que busca es crea una zona de seguridad de operación que evitan que la temperatura y la
potencia salgan de un rango seguro dado por: S= {(𝑥, 𝑦): 𝑥2 + (𝑦 − 1)2 ≤ 1}

a) Haga un análisis de invarianza en la frontera y zona segura.

146

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 81

31. Un sistema de biomasas, población de microorganismos 𝑥(𝑡) y concentración de nutrientes 𝑦(𝑡) está
gobernado por las ecuaciones diferenciales: 𝑥̇ = 𝑥(1 − 𝑦) crecimiento de la biomasa, y, 𝑦̇ = 1 − 𝑥 − 𝑦, el
consumo de nutrientes considere que la biomasa y los nutrientes solo pueden ser positivos y limitados. Se
quiere un estudio de frontera para determinar si el sistema está en la región de control o si escapa a ella,
para esto se tiene la figura siguiente donde S es la región estable:  𝑆 = {(𝑥, 𝑦): 𝑥 > 0, 𝑦 > 0, 𝑦 + 𝑥 ≤ 2}

FIGURA 82

147

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

APLICACIONES DE SISTEMAS DINÁMICOS

En el libro sistemas no lineales y caos de Steven Strogatz plantea la relación amor odio entre dos amantes
(Romeo y Julieta), la descripción de la dinámica emocional es la siguiente:

Aquí se modelan interacciones románticas mediante un sistema de ecuaciones diferenciales lineales.

Romeo y Julieta (Name-calling)

Se da el sistema en su forma estándar:

{

𝑅̇ = 𝑎𝑅 + 𝑏𝐽
𝐽̇ =  𝑐𝑅 + 𝑑𝐽

Para Romeo la ecuación que gobierna la dinámica es: 𝑅̇ = 𝑎𝑅 + 𝑏𝐽

donde:

•  R: el amor (o desamor) de Romeo hacia Julieta

•

J: el amor (o desamor) de Julieta hacia Romeo

•  a: cómo influye su propio estado en él mismo

•  b: cómo lo afecta lo que siente Julieta

De manera similar par a Julieta: 𝐽̇ = 𝑐𝑅 + 𝑑𝐽

𝑑𝑜𝑛𝑑𝑒:

•

𝐽: 𝑒𝑙 𝑠𝑒𝑛𝑡𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑑𝑒 𝐽𝑢𝑙𝑖𝑒𝑡𝑎 ℎ𝑎𝑐𝑖𝑎 𝑅𝑜𝑚𝑒𝑜

•  𝑅: 𝑒𝑙 𝑠𝑒𝑛𝑡𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑑𝑒 𝑅𝑜𝑚𝑒𝑜 ℎ𝑎𝑐𝑖𝑎 𝐽𝑢𝑙𝑖𝑒𝑡𝑎

•  𝑑𝑑 𝑐ó𝑚𝑜 𝑖𝑛𝑓𝑙𝑢𝑦𝑒 𝑠𝑢 𝑝𝑟𝑜𝑝𝑖𝑜 𝑒𝑠𝑡𝑎𝑑𝑜 𝑒𝑛 𝑒𝑙𝑙𝑎 𝑚𝑖𝑠𝑚𝑎

•

𝑐: 𝑐ó𝑚𝑜 𝑙𝑎 𝑎𝑓𝑒𝑐𝑡𝑎 𝑙𝑜 𝑞𝑢𝑒 𝑠𝑖𝑒𝑛𝑡𝑒 𝑅𝑜𝑚𝑒𝑜

Comportamiento del sistema según los valores que adoptan las constantes:

148

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

clasificación de estilos románticos de Romeo

Signo de (a)
𝑎 > 0

Signo de (b)
𝑏 > 0

Estilo romántico
Apasionado

𝑎 > 0

𝑏 < 0

Contradictorio

𝑎 < 0

𝑏 > 0

Dependiente

𝑎 < 0

𝑏 < 0

Evasivo

En el caso de Julieta:
Signo de d

Signo de c

Estilo de Julieta

𝑑 > 0

𝑐 > 0

Apasionada

𝑑 > 0

𝑐 < 0

Contradictoria

𝑑 < 0

𝑐 > 0

Dependiente

d<0

c<0

Evasiva

149

Explicación
Romeo  se  enamora
más  cuando  ya  está
enamorado,  y  aún
más si Julieta lo ama

se
Romeo
de
autoalimenta
amor,  pero  el  amor
de Julieta lo espanta

pierde
Romeo
interés  por  sí  solo,
pero  se  enamora  si
Julieta lo ama

Romeo
se
desenamora  solo  y
aún más si Julieta lo
ama

Explicación
Julieta  se  emociona
sola,  y  aún  más  si
Romeo la ama

Julieta  se  emociona
sola, pero rechaza el
amor de Romeo

pierde

el
Julieta
interés sola, pero se
enamora si Romeo la
ama

pierde

Julieta
el
interés sola, y más si
Romeo la ama.

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Resumen:

Ambos (Romeo y Julieta) pueden clasificarse en los mismos cuatro estilos según los signos de los
coeficientes que definen su sistema emocional:

•  Apasionado: responde positivamente tanto a sí mismo como a la otra persona.

•  Contradictorio: se enamora solo, pero rechaza el amor del otro.

•  Dependiente: necesita del otro para amar, por sí solo se apaga.

•  Evasivo: se apaga solo y el amor del otro también lo ahuyenta.

Pensemos en los siguientes casos:

Caso 1:

{

𝑅̇ = −𝐽
𝐽̇ =  𝑅

Este sistema modela cómo evolucionan los sentimientos de Romeo (R) y Julieta (J) con el tiempo.

Análisis: como En este caso:

•  𝑎 = 0, 𝑏 = −1  ⟹ 𝑅𝑜𝑚𝑒𝑜 𝑛𝑜 𝑟𝑒𝑎𝑐𝑐𝑖𝑜𝑛𝑎 𝑎 𝑠í 𝑚𝑖𝑠𝑚𝑜, 𝑝𝑒𝑟𝑜 𝑟𝑒𝑐ℎ𝑎𝑧𝑎 𝑙𝑜 𝑞𝑢𝑒 𝑠𝑖𝑒𝑛𝑡𝑒 𝐽𝑢𝑙𝑖𝑒𝑡𝑎  ⇒

 𝑒𝑣𝑎𝑠𝑖𝑣𝑜

•

𝑐 = 1, 𝑑 = 0  ⟹  𝐽𝑢𝑙𝑖𝑒𝑡𝑎 𝑛𝑜 𝑟𝑒𝑎𝑐𝑐𝑖𝑜𝑛𝑎 𝑎 𝑠í 𝑚𝑖𝑠𝑚𝑎, 𝑝𝑒𝑟𝑜 𝑠𝑒 𝑒𝑛𝑎𝑚𝑜𝑟𝑎 𝑠𝑖 𝑅𝑜𝑚𝑒𝑜 𝑙𝑎 𝑎𝑚𝑎  ⇒
 𝑑𝑒𝑝𝑒𝑛𝑑𝑖𝑒𝑛𝑡𝑒

Analizamos el punto fijo en el origen:

𝑅̇
0 −1
𝐽̇ ) = (
0
1

(

) (

𝑅
𝐽

)

Como A=(

0 −1
0
1

);

Los valores propios: 𝑑𝑒𝑡(𝐴 − 𝜆𝐼) = 0

−𝜆 −1
|
1 −𝜆

| = (−𝜆)(−𝜆) + 1 = 0, 𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠: 𝜆 ± 𝑖 (centro lineal)

150

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

¿Qué significa esto para la historia de amor?

Las trayectorias serán cerradas y periódicas alrededor del origen. Esto significa que:

•  Romeo  y  Julieta  se  persiguen  eternamente,  sin  llegar  nunca  a  un  estado  estable  de  amor  o

indiferencia.

•  La relación oscila periódicamente: cuando uno se enamora, el otro se aleja, y viceversa.

Una especie de “danza emocional” interminable.

En la siguiente gráfica se puede observar la dinámica:

FIGURA 83

Perfecto, ahora construiremos un ejemplo en el que la dinámica entre Romeo y Julieta dé lugar a una espiral
en el plano de fase, es decir, un punto de equilibrio espiralado (estable o inestable).

Caso 2: condición para espiral

Un sistema lineal tiene una espiral (estable o 𝑖𝑛𝑒𝑠𝑡𝑎𝑏𝑙𝑒) 𝑐𝑢𝑎𝑛𝑑𝑜:

•  𝐸𝑙 𝑡𝑟𝑎𝑧𝑎𝑑𝑜 (𝑠𝑢𝑚𝑎 𝑑𝑒 𝑑𝑖𝑎𝑔𝑜𝑛𝑎𝑙 𝑑𝑒 𝑙𝑎 𝑚𝑎𝑡𝑟𝑖𝑧) 𝑡𝑟(𝐴) ≠ 0

•  𝐸𝑙 𝑑𝑒𝑡𝑒𝑟𝑚𝑖𝑛𝑎𝑛𝑡𝑒 𝛥 = 𝑎𝑑 − 𝑏𝑐 > 0

151

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  𝐸𝑙 𝑑𝑖𝑠𝑐𝑟𝑖𝑚𝑖𝑛𝑎𝑛𝑡𝑒 𝑡𝑟(𝐴)2 − 4𝛥 < 0  →  𝑟𝑎í𝑐𝑒𝑠 𝑐𝑜𝑚𝑝𝑙𝑒𝑗𝑎𝑠 𝑐𝑜𝑛𝑗𝑢𝑔𝑎𝑑𝑎𝑠.

Un ejemplo:

{

𝑑𝑟
𝑑𝑡
𝑑𝑗
𝑑𝑡

= −2𝑅 + 4𝐽

= −4𝑅 − 2𝐽

Resolviendo la dinámica y simulando se obtiene lo siguiente:

FIGURA 84

Esto muestra como el diagrama de fase de una espiral estable en la relación entre Romeo y Julieta.

Interpretación emocional:

•  Las emociones de ambos giran en torno a una dinámica oscilante (espiral), pero eventualmente se

calman, convergiendo al punto de equilibrio (R, J) = (0,0), es decir, indiferencia mutua.

•  Este tipo de dinámica podría representar una relación pasional pero que finalmente se apaga.

Si las condiciones de la dinámica cambian su naturaleza por ejemplo en vez de ser una espiral estable que
converja al equilibrio esta se aleja. Como se ve en esta simulación:

152

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 85

Aquí tienes el diagrama de fase para una espiral inestable en la relación entre Romeo y Julieta.
Interpretación emocional:

•  Las emociones de ambos giran de manera oscilante, pero en vez de calmarse, se intensifican con el

tiempo.

•  Cualquier pequeño conflicto o atracción inicial se descontrola y los aleja cada vez más: una historia

de amor con un final dramático.

Caso 3:
Propongamos  un  sistema  como  un  punto  silla, 𝑥(𝑡) el  amor  odio  de  Rome, 𝑦(𝑡) el  amor  odio  de  Julieta.
Entonces se modela como sigue: 𝑥̇ = 𝑥, 𝑦̇ = −𝑦

Como se ve al principio, Romeo y Julieta están cercanos

FIGURA 86

A medida que pasa el tiempo, la dinámica los separa: uno se enfría (se va al eje 𝑦 = 0) y el otro se exalta
(crece sin control). En ambos sentidos en amor o en odio.

153

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Caso 4: otro caso donde aparezca un ciclo límite seria

{

𝑑𝑅
𝑑𝑡
𝑑𝐽
𝑑𝑡

= 𝑅(1 − 𝑅2 − 𝐽2)

= −𝐽(1 − 𝑅2 − 𝐽2)

FIGURA 87

Interpretación:

•  R(t): amor/odio de Romeo.

•

J(t): amor/odio de Julieta.

•  Hay una frontera circular (radio 1) que separa dos zonas:

o  Dentro  del  círculo 𝑅2 + 𝐽2 < 1:  ambos  tienden  a  equilibrio estable  en  el  ciclo limite  →  la

relación se mantiene en ciclo

o  Fuera del círculo 𝑅2 + 𝐽2 > 1 : ambos se alejan del origen según su signo → amor explosivo

o ruptura descontrolada.

154

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelos de Lotka Volterra

Los modelos de Lotka-Volterra son sistemas de ecuaciones diferenciales usados para describir la dinámica
de poblaciones biológicas en interacción, como depredador-presa o competencia entre especies. Los más
comunes son:

Modelo clásico  {

𝑑𝑥
𝑑𝑡
𝑑𝑦
𝑑𝑡

= 𝑎𝑥 − 𝑏𝑥𝑦

= 𝑐𝑥𝑦 − 𝑑𝑦

Donde:

•  𝑥(𝑡): población de presas
•  𝑦(𝑡): población de depredadores
•  𝑎 > 0: tasa de crecimiento de las presas
•  𝑏 > 0: tasa de depredación
•

𝑐 > 0: eficiencia con que los depredadores convierten presas en descendencia

Este sistema modela una presa que crece de forma exponencial (𝑎𝑥) y una depredación proporcional a (𝑥𝑦).
El depredador depende de la interacción con la presa para reproducirse (𝑐𝑥𝑦) y muere a una tasa natural d.

Por ejemplo, si:

•  𝑎 = 1 (crecimiento  de  presas), 𝑏 = 0.1 (eficiencia  de  caza), 𝑐 = 0.1 (beneficio  del  depredador  por

presa), 𝑑 = 1 (mortalidad del depredador)

resolvemos el sistema y simulamos

FIGURA 88

Aquí tienes la simulación del modelo de Lotka-Volterra:

 Izquierda: diagrama de fase 𝑥 𝑣𝑠 𝑦. Muestra un ciclo cerrado: las poblaciones de presas y depredadores
oscilan periódicamente.

155

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Derecha: evolución temporal de cada población. Puedes ver cómo los depredadores siguen a las presas
con cierto desfase.

Ejemplo competencia entre especie:  {

𝑑𝑥
𝑑𝑡
𝑑𝑦
𝑑𝑡

= 𝑎𝑥 − 𝑏𝑥𝑦

= 𝑐𝑦 − 𝑑𝑥𝑦

donde:

•  𝑥  =  𝑝𝑜𝑏𝑙𝑎𝑐𝑖ó𝑛 𝑑𝑒 𝑐𝑜𝑛𝑒𝑗𝑜𝑠,

•  𝑦  =  𝑝𝑜𝑏𝑙𝑎𝑐𝑖ó𝑛 𝑑𝑒 𝑜𝑣𝑒𝑗𝑎𝑠,

•  𝑎, 𝑐 > 0 𝑐𝑟𝑒𝑐𝑖𝑚𝑖𝑒𝑛𝑡𝑜𝑠 𝑛𝑎𝑡𝑢𝑟𝑎𝑙𝑒𝑠,

•  𝑏, 𝑑 > 0 coeficientes de competencia.

Interpretación:

•  𝑥(𝑡): ovejas

•  𝑦(𝑡): conejos

•  𝑎: tasa de crecimiento natural de ovejas

•

𝑐: tasa de crecimiento natural de conejos

•  𝑏, 𝑑: efecto de competencia cruzada (cada especie daña el crecimiento de la otra)

la dinámica va a depender de los parámetros y las condiciones iniciales, ahora analicemos un problema
más completo

Resolvamos el siguiente ejemplo: 𝑥̇ = 𝑥(3 − 𝑥) − 2𝑥𝑦,  𝑦̇ = 𝑦(2 − 𝑦) − 𝑥𝑦, los puntos de equilibrio son:

Punto  Naturaleza

Autovalores

(0,0)
(3,0)
(0,2)
(1,1)

Nodo inestable
Nodo estable
Nodo estable
Silla

Simulación a continuación:

𝜆1 = 3, 𝜆2 = 2
𝜆1 = −3, 𝜆2 = −1
𝜆1 = −1, 𝜆2 = −2
𝜆1 = 0.414, 𝜆2 = −2.414

156

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 89

Resumen cualitativo

•

•

•

•

(0, 0): Ambas especies están extintas → es una fuente (todo se aleja).

(3, 0): Solo hay ovejas (𝑥) → nodo estable: si no hay conejos (𝑦), la población (𝑥) tiende a 3.

(0, 2): Solo hay conejos (𝑦) → nodo estable: si no hay ovejas (𝑥), la población(y) tiende a 2.

(1,  1):  Coexistencia  de  ambas  especies  →  silla:  trayectoria  sensible  a  condiciones  iniciales;
inestable.

157

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelos de Combate

Uno de los modelos clásicos es el Modelo de Lanchester, que se usa para describir la interacción entre dos
fuerzas enemigas durante un combate.

Caso 1: modelo con dos fuerzas (lineal)

•  𝑥(𝑡) = número de unidades del ejército A en el tiempo 𝑡.

•  𝑦(𝑡)= número de unidades del ejército B en el tiempo 𝑡.

Las ecuaciones diferenciales para el modelo básico son:

𝑑𝑥
𝑑𝑡

= −𝑎𝑦,

𝑑𝑦
𝑑𝑡

= −𝑏𝑥

Donde:

•  𝑎 es la tasa de efectividad de fuego del ejército B sobre A.

•  𝑏 es la tasa de efectividad de fuego del ejército A sobre B.

•  𝑎, 𝑏 > 0

Este modelo asume que el daño infligido es proporcional al tamaño del ejército enemigo.

Análisis

El combate es “dirigido” y “paralelo”: cada lado dispara sobre el otro directamente.

El resultado final depende de la relación

𝑎 𝑥0
𝑏

2

,  𝑦0

2

Se puede demostrar que 𝑏𝑥2 − 𝑎𝑦2 = 𝑐 (es un sistema conservativo)

𝑑𝑥
𝑑𝑦

𝑎𝑦
𝑏𝑥

=

,  resolviendo el sistema 𝑏𝑥 𝑑𝑥 = 𝑎𝑦 𝑑𝑦,

+ 𝑐2, linealizando y reescribiendo
Dado que
se  obtiene 𝑏𝑥2 − 𝑎𝑦2 = 𝑐, ahora  para  el  cálculo  de  la  constante  se  evalúa  en  las  condiciones  iniciales,
𝑏𝑥0

2 − 𝑎𝑦0

+ 𝑐1 =

2 = 𝑐

𝑏𝑥2
2

𝑎𝑦2
2

Caso 2: Modelo de Lanchester cuadrático (no lineal)

𝑑𝑥
𝑑𝑡

= −𝑎𝑥𝑦,

𝑑𝑦
𝑑𝑡

= −𝑏𝑥𝑦

158

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  Aquí, el daño infligido es proporcional al producto del número de unidades de ambos ejércitos.

•  Esto  ocurre  cuando  ambos  ejércitos  disparan  al  azar  y  el  contacto  es  aleatorio  (por  ejemplo,

infantería dispersa).

Análisis:  eliminamos  el  parámetro:

𝑑𝑥
𝑑𝑦

=

𝑎
𝑏

𝑑𝑦 ,  entonces:  𝑥 =

𝑎
𝑏

𝑦 + 𝑐 ,  Igual  acá  para  hallar  c

necesitamos las condiciones iniciales 𝑐 = 𝑥0 −

,    𝑑𝑥 =
𝑎
𝑏

𝑎
𝑏
𝑦0

❖  En las gráficas de evolución temporal, el modelo lineal muestra que las fuerzas decrecen de forma

más suave.

❖  El modelo cuadrático tiende a hacer que las fuerzas caigan más rápido, porque la tasa depende del

producto 𝑥𝑦.

❖  En  la gráfica de (𝑥, 𝑦), la trayectoria del modelo cuadrático  es una línea recta (como vimos en la

teoría).

❖  La trayectoria del modelo lineal es una curva hiperbólica (por la relación cuadrática conservada).

Caso 3: Lanchester con refuerzos

FIGURA 90

𝑑𝑥
𝑑𝑡

= −𝑎𝑦 + 𝑅𝑥(𝑡),

𝑑𝑦
𝑑𝑡

= −𝑏𝑥 + 𝑅𝑦(𝑡)

Donde:

159

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  𝑥(𝑡), 𝑦(𝑡): fuerzas de los ejércitos A y B.

•  𝑎, 𝑏 > 0: tasas de efectividad de fuego enemiga.

•  𝑅𝑥(𝑡), 𝑅𝑦(𝑡): refuerzos o entradas de nuevas tropas en cada ejército.

Interpretación:

•  El primer término −𝑎𝑦  y −𝑏𝑥 representa la pérdida de tropas por acción enemiga (como antes).

•  El segundo término 𝑅𝑥(𝑡), 𝑅𝑦(t) agrega tropas nuevas durante el combate.

•  Este modelo es útil para guerras donde se envían refuerzos continuos o variables.

Se puede analizar como un sistema no homogéneo

Solución general:

𝑑
𝑑𝑡

(𝑥
𝑦)=(

0 −𝑎
0
−𝑏

) (𝑥

𝑦) + (𝑅𝑥(𝑡)
𝑅𝑦(t))

−𝑎𝑦𝑝 + 𝑅𝑥 = 0
{
−𝑏𝑥𝑝 + 𝑅𝑦 = 0

En punto de equilibrio se consigue en: 𝑥𝑝 =

𝑅𝑦
𝑏

,  𝑦𝑝 =

𝑅𝑥
𝑎

Caso 4: con fatiga o desgaste propio

𝑑𝑥
𝑑𝑡

= −𝑎𝑦 − 𝑐𝑥,

𝑑𝑦
𝑑𝑡

= −𝑏𝑥 − 𝑑𝑦

•  Los términos −𝑐𝑥 y −𝑑𝑦 representan la pérdida de tropas por fatiga, enfermedad, desertores, etc.

•

𝑐, 𝑑 > 0 son coeficientes de desgaste interno.

•  Este modelo incorpora una disipación propia además del daño enemigo.
•  Puede dar resultados más realistas cuando la duración de la batalla afecta la capacidad de lucha.

La matriz 𝐴 = [

−𝑐 −𝑎
−𝑏 −𝑑

], La solución depende de la matriz A

160

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo caso lineal

Sea el sistema: 𝑥̇ = −𝑎𝑥, 𝑦̇ = −𝑏𝑦, este sistema es desacoplado así que se pueden hallar rápidamente las
soluciones  en  el  tiempo  para  cada  variable: 𝑥(𝑡) = 𝑥0𝑒−𝑎𝑡, 𝑦(𝑡) = 𝑦0𝑒−𝑏𝑡 ,  ambas  soluciones  tienden  a
cero.

𝑆𝑖   𝑎 = 0.02, 𝑏 = 0.01, 𝑥0 = 1000, 𝑦0 = 1200,  𝑥(𝑡) = 1000𝑒−0.02𝑡, 𝑦(𝑡) = 1200𝑒−0.01𝑡,

CIENCIA Y TECNOLOGÍA:

1.  𝐵𝑖𝑜𝑙𝑜𝑔í𝑎: 𝐶𝑟𝑒𝑐𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑝𝑜𝑏𝑙𝑎𝑐𝑖𝑜𝑛𝑎𝑙

𝑑𝑝
𝑑𝑡

= 𝑟𝑥 (1 −

𝑝
𝑘

)

donde:

•  𝑥(𝑡)𝑒𝑠 𝑙𝑎 𝑝𝑜𝑏𝑙𝑎𝑐𝑖ó𝑛 𝑒𝑛 𝑒𝑙 𝑡𝑖𝑒𝑚𝑝𝑜,
𝑟 > 0: 𝑡𝑎𝑠𝑎 𝑑𝑒 𝑐𝑟𝑒𝑐𝑖𝑚𝑖𝑒𝑛𝑡𝑜,
•
•  𝐾 > 0: 𝑐𝑎𝑝𝑎𝑐𝑖𝑑𝑎𝑑 máxima del entorno (capacidad de carga).

2.  Epidemiologia (Modelo SIR)

𝑑𝑠
𝑑𝑡
𝑑𝐼
𝑑𝑡
𝑑𝑅
𝑑𝑡

{

= −𝛽𝑆𝐼

=  𝛽𝑆𝐼 −  𝛾𝐼

=  𝛾𝐼

𝐸𝑠𝑡𝑒 𝑚𝑜𝑑𝑒𝑙𝑜 𝑑𝑖𝑣𝑖𝑑𝑒 𝑎 𝑙𝑎 𝑝𝑜𝑏𝑙𝑎𝑐𝑖ó𝑛 𝑒𝑛 𝑡𝑟𝑒𝑠 𝑔𝑟𝑢𝑝𝑜𝑠:

•  𝑆(t): susceptibles,
I(t): infectados,
•
•  R(t): recuperados (o inmunes).

Parámetros:

•  β>0: tasa de transmisión,
γ>0: tasa de recuperación
•

ECONOMÍA
Modelo oferta de demanda

161

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑝̇ = 𝑓(𝐷(𝑝) − 𝑆(𝑝))
𝑞̇ = 𝑔(𝑝)

FÍSICA
El problema del Cohete

Un cohete se mueve en el espacio (sin fricción del aire) expulsando masa a una velocidad constante relativa.
La  masa  del  cohete  disminuye  con  el  tiempo  porque  expulsa  combustible.  Se  tiene  la  Ecuación
fundamental (Tsiolkovsky):

Ecuación y Variables involucradas:

𝑚(𝑡)

𝑑𝑣
𝑑𝑡

= −𝑢

𝑑𝑚
𝑑𝑡

m(t) masa del cohete en el tiempo 𝑡
𝑣(𝑡): velocidad del cohete
𝑢: velocidad del gas expulsado respecto al cohete (constante)
𝑚̇ (𝑡) =

< 0: razón de pérdida de masa

𝑑𝑚
𝑑𝑡

FIGURA 91

Ecuación diferencial del oscilador armónico sin fricción:

𝑥̈ + 𝑤2𝑥 = 0

donde:
x(t): posición de la masa en el tiempo,

•
•  ω: frecuencia angular = √ 𝑘
𝑚

,

162

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  k: constante del resorte,

m: masa.

FIGURA 92

Péndulo simple

{𝜃̇ = 𝑣
𝑣̇ = sin 𝜃

Circuito RLC Aplicando las leyes de Kichhoff

FIGURA 93

•  Kirchhoff de tensiones (KVL): la suma algebraica de las tensiones en un lazo es cero.
•  Kirchhoff de corrientes (KCL): la suma algebraica de corrientes que entran a un nodo es cero.

Estas leyes te  permiten plantear ecuaciones que, junto  con las relaciones anteriores, derivan en
ecuaciones diferenciales ordinarias (EDOs).

Ejemplo un circuito RLC serie
Considera un circuito sencillo: una resistencia 𝑅 y un condensador 𝐶 en serie con una fuente 𝑣𝑠(𝑡)

𝑣𝑠(𝑡) = 𝑣𝑅(𝑡) + 𝑣𝐿(𝑡) + 𝑣𝐶(𝑡) = 𝑅𝑖(𝑡) + 𝐿

𝑑𝑖(𝑡)
𝑑𝑡

+

1
𝑐

∫ 𝑖(𝑡)𝑑𝑡

163

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Derivamos para eliminar la integral:

𝑑𝑣𝑠
𝑑𝑡

= 𝑅

𝑑𝑖
𝑑𝑡

+ 𝐿

𝑑𝑖2(𝑡)
𝑑𝑡2 +

1
𝑐

𝑖(𝑡)

FIGURA 94

Sistemas Conservativos

En dinámica 2D, un sistema conservativo es un tipo de sistema que conserva una cantidad escalar llamada
energía (o una función análoga, como una función de Hamilton). Este tipo de sistema no tiene disipación
(por ejemplo, fricción), por lo que la energía total se mantiene constante en el tiempo. Vamos a ver cómo se
modelan estos sistemas, su estructura general, y cómo se analizan.

Tiene la forma:

𝑥̇ = 𝑓(𝑥, 𝑦), 𝑦̇ = 𝑔(𝑥, 𝑦)

Es conservativo si existe una función escalar 𝐻(𝑥, 𝑦) tal que:

𝑑𝐻
𝑑𝑡

=

𝜕𝐻
𝜕𝑥

𝑥̇ +

𝜕𝐻
𝜕𝑦

𝑦̇ = 0

Esto significa que 𝐻(𝑥, 𝑦) es constante a lo largo de las trayectorias del sistema, y se le llama función de
energía o función de Hamilton.

La estructura de un sistema conservativo forma de Hamilton:  {

𝑥̇ =

𝜕𝐻
𝜕𝑦

𝑦̇ = −

𝜕𝐻
𝜕𝑥

Características de un sistema conservativo

164

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

1.  La función 𝐻(𝑥, 𝑦) es constante sobre las trayectorias → se pueden visualizar como curvas de nivel.
2.  No hay fuentes ni sumideros.
3.  Las soluciones suelen ser cerradas (órbitas periódicas) o quasi-periódicas.
4.  Se conserva la "energía total" del sistema.

Ejemplos:

Sistema de pozo doble

𝑥̈ = −

𝑑𝑉
𝑑𝑥

,        {

𝑥̇ = 𝑣
𝑣̇ = 𝑥 − 𝑥3

Esto  define  un  sistema  de  dimensión  2  en  el  espacio  de  fase  (𝑥, 𝑥̇ ),  pero  sigue  siendo  unidimensional
físicamente, porque solo describe el movimiento en una coordenada espacial.

𝑉(𝑥)= Potencial
𝑥2 +
𝑉(𝑥) = −

1
2

1
4

𝑥4,  𝑥̈ = −(−𝑥 + 𝑥3) = 𝑥 − 𝑥3

Los puntos de equilibrio:

(−1,0);  (0,0),  (1,0)

FIGURA 95

Las trayectorias cerca de los equilibrios muestran pequeñas orbitas cerradas las que se alejan con mayor
inercia que pasan de pozo a pozo esas se llaman monoclínicas. Un ejemplo de potencial no lineal:

𝑥̇ = y
{
𝑦̇ = −𝑥 − 𝑥3

Buscamos una función potencial (tipo Hamiltoniana) que cumpla las condiciones

165

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝐻̇ =

𝜕𝐻
𝜕𝑥

𝑥̇ +

𝜕𝐻
𝜕𝑦

𝑦̇ = 0

 𝑥̇ =

𝜕𝐻
𝜕𝑦

𝑦̇ = −

{

𝜕𝐻
𝜕𝑥

𝐻(𝑥, 𝑦) =

1
2

𝑦2 +

1
2

𝑥2 +

1
4

𝑥4

𝑑𝐻
𝑑𝑡

= (𝑥 + 𝑥3)𝑥̇ + 𝑦𝑦̇ = (𝑥 + 𝑥3)𝑦 + 𝑦(−𝑥 − 𝑥3) = 0

Se demuestra es un sistema conservativo, procedemos a simularlo:

FIGURA 96

166

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios de Aplicación

1.  Analice el modelo de romance entre Romeo y Julieta dado por el sistema

{

𝑅̇ = 𝑎𝑅 + 𝑏𝐽
𝐽̇ = 𝑏𝑅 + 𝑎𝐽

𝑎 < 0, 𝑏 > 0, a ambos le va a atraer que el otro demuestre interés, donde 𝑎 = 𝑐𝑎𝑢𝑡𝑒𝑙𝑎, y 𝑏 = 𝑟𝑒𝑠𝑝𝑜𝑛𝑠𝑖𝑣𝑖𝑑𝑎𝑑

2.  Analizar el sistema depredador/presa

𝑥̇ = (𝑎 − 𝑏𝑦)𝑥
{
𝑦̇ = (𝑑𝑥 − 𝑐)𝑦

3.  Oscilador armónico simple: 𝑥̇ = 𝑦, 𝑦̇ = −𝑥, demuestre que es conservativo y halle la función de energía
de Hamilton.

4.  Demostrar que el siguiente sistema se conserva la energía y simular el sistema con un software

𝑥̇ = 𝑦
{
𝑦̇ = −𝑥 − 𝑥3

5.  Halle la función de Hamilton de:

𝑥̇ = 𝑦3
{
𝑦̇ = −𝑥

6.  Halla la función de Hamilton si existe para el siguiente sistema, sino demostrar que el sistema pierde o
gana energía.

𝑥̇ = 𝑦
{
𝑦̇ = −𝑥 − 𝑦

7.  Potencial  de  doble  pozo  simular  la  dinámica  del  sistema  y  graficar,  demuestra  que  el  sistema  es
conservativo

𝑥̇ = 𝑦
{
𝑦̇ = 𝑥 − 𝑥3

8.  Analizar el siguiente sistema conservativo no línea, demostrar que no pierde energía y halla la función
de energía Hamiltoniana correspondiente

𝑥̇ = 𝑦(1 + 𝑥2)
{
𝑦̇ = −𝑥(1 + 𝑦2)

167

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Parametrización en sistemas dinámicos

En el caso de sistemas autónomos consiste en encontrar la trayectoria (curva en el plano) que siguen las
soluciones, normalmente en función del tiempo 𝑡. Para eso, Se parte del sistema:

𝑑𝑥⃗
𝑑𝑡

= 𝐹⃗(𝑥⃗),

𝑑𝑜𝑛𝑑𝑒 𝑥⃗ = (𝑥, 𝑦),

𝑥⃗ =   (𝑥, 𝑦)𝑇

❖  Se encuentra 𝑥(𝑡), 𝑦(𝑡), es decir, una parametrización del movimiento en el plano.

La parametrización consiste en expresar las trayectorias del sistema como curvas en el plano (𝑥, 𝑦) (o en
(𝑥1, 𝑥2, … ), ya sea: en función del tiempo: (x(t), y(t)), o como una relación de variables y=f(x) (eliminando el
tiempo)

La parametrización permite:

a)  Entender cómo se mueven las soluciones.
b)  Representar gráficamente las trayectorias.
c)  Estudiar propiedades del sistema (como energía conservada, comportamiento oscilatorio, etc.).
d)  Clasificar tipos de trayectorias (espirales, círculos, líneas, etc.).

Métodos:

1.  Solución explicita con respecto al tiempo

𝑥̇ = 𝑓(𝑥, 𝑦)      →  𝑥(𝑡), 𝑦(𝑡)
{
𝑦̇ = 𝑔(𝑥, 𝑦)

Ideal cuando el sistema es desacoplado o lineal

2.  eliminación de tiempo usando

𝑑𝑦
𝑑𝑥

𝑑𝑦
𝑑𝑥

=

𝑦̇
𝑥̇

=

𝑔(𝑥, 𝑦)
𝑓(𝑥, 𝑦)

Este método muestra la forma de las trayectorias sin saber cómo cambia en el tiempo, es decir representa
las curvas direcciones en el plano de fase, básicamente dibujamos una función 𝑦 = 𝑓(𝑥).

3.  Curvas de Nivel (energía conservada)

En sistemas conservativos, 𝐻(𝑥, 𝑦) = 𝑐, curvas de nivel, en estas curvas la energía permanece constante
(describe trayectorias cerradas).

168

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Un caso típico sería; 𝑥̇ = 𝑦, 𝑦̇ = − sin(𝑥),  𝑦 = ±√2(𝑐 − 𝑣(𝑥)), ideal para sistema donde hay conservación

de energía como (péndulos, masa resorte y otros)

4.  Transformación a coordenadas polares

Se usa 𝑥 = 𝑟 cos 𝜃 , 𝑦 = 𝑟 sin 𝜃

𝑟̇ =

𝑥𝑥̇ +𝑦𝑦̇
𝑟

,

𝜃̇ =

𝑥𝑦̇ −𝑦𝑥̇
𝑟2

,

𝑥2 + 𝑦2 = 𝑟2

Útil para analizar trayectorias radiales o espirales

La  parametrización  en  sistemas  dinámicos  permite  describir  y  visualizar  trayectorias  sin  necesidad  de
simular  todo  el  sistema.  Según  el  tipo  de  sistema  (lineal,  conservativo,  radial,  etc.),  hay  métodos
específicos para obtener estas curvas.

En un sistema no autónomo existe la dependencia explicita del tiempo, parámetro (𝑡)

Caso sistema no autónomo

𝑥̇ = (𝑥, 𝑦, 𝑡), 𝑦̇ = (𝑥, 𝑦, 𝑡)

A diferencias de sistemas autónomos acá el tiempo actúa como una variable externa

a parametrización en sistemas no autónomos se limita casi exclusivamente a:

❖  Resolver el sistema para obtener (𝑥(𝑡), 𝑦(𝑡))
❖  Visualizar la trayectoria como función del tiempo
❖  Ampliar el espacio de fases: (𝑥, 𝑦, 𝑡)

Ejemplo: 𝑥̇ = 𝑥 + 𝑡, 𝑦̇ = −𝑦 + cos(𝑡)

Se resuelve por separado:

𝑥̇ = 𝑥 + 𝑡, la resolvemos con un factor integrante: tiene la forma 𝑥̇ − 𝑥 = 𝑡, entonces 𝜇(𝑡) = 𝑒∫ − 𝑑𝑡 = 𝑒−𝑡,
multiplicamos por el factor integrante toda la ecuación y obtenemos:

𝑒−𝑡𝑥̇ − 𝑒−𝑡𝑥 = 𝑡𝑒−𝑡, y reescribimos de la  siguiente manera:
integral por partes:

𝑑
𝑑𝑡

(𝑥𝑒−𝑡) = 𝑡𝑒−𝑡 , ahora solo falta resolver  la

169

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

𝑥(𝑡) = 𝑒𝑡 ∫ 𝑡𝑒−𝑡 𝑑𝑡 = −𝑡 − 1 + 𝑐1𝑒𝑡

Para 𝑦̇ = −𝑦 + cos(𝑡),  igual  reescribimos  y  planteamos  una  solución,  en  este  caso  el  factor  integrante
también  se  puede  usar,  y  es  𝜇(𝑡) = 𝑒∫ 𝑑𝑡 = 𝑒𝑡,  entonces  podemos  llegar  a  lo  siguiente:  𝑒𝑡𝑦(𝑡) =
∫ 𝑒𝑡 cos(𝑡) 𝑑𝑡, resolvemos y despejamos: 𝑦(𝑡) =

(sin 𝑡 + cos 𝑡) + 𝑐2𝑒𝑡

1
2

Ejemplo tipo Bifurcación de Hopf

Sistema:

𝑥̇ = 𝜇𝑥 − 𝑦 − 𝑥(𝑥2 + 𝑦2)
{
𝑦̇ = 𝑥 +  𝜇𝑦 − 𝑦(𝑥2 + 𝑦2)

𝜇 es el parámetro, y su punto de equilibrio es: (0,0)

Estudio de estabilidad:

𝐽(𝑥, 𝑦) = (

𝜇 − 3𝑥2 − 𝑦2
1 − 2𝑥𝑦

−1 − 2𝑥𝑦
𝜇 − 𝑥2 − 3𝑦2)

Evaluamos en (0,0)

Resolvemos los autovalores:

𝐽(0,0) = (

𝜇 −1
𝜇
1

)

Los valores propios: 𝑑𝑒𝑡(𝐴 − 𝜆𝐼) = 0

|

𝜇 − 𝜆
1

−1
𝜇 − 𝜆

| = (𝜇 − 𝜆)(𝜇 − 𝜆) + 1 = 0,   𝑒𝑛𝑡𝑜𝑛𝑐𝑒𝑠: 𝜆 = 𝜇 ± 𝑖

Análisis:

•  𝑆𝑖 𝜇 < 0: 𝑝𝑎𝑟𝑡𝑒 𝑟𝑒𝑎𝑙 𝑛𝑒𝑔𝑎𝑡𝑖𝑣𝑎  →  𝑓𝑜𝑐𝑜 𝑒𝑠𝑡𝑎𝑏𝑙𝑒 (𝑒𝑠𝑝𝑖𝑟𝑎𝑙 𝑞𝑢𝑒 𝑠𝑒 𝑐𝑜𝑛𝑡𝑟𝑎𝑒)
•  𝑆𝑖 𝜇 > 0: 𝑝𝑎𝑟𝑡𝑒 𝑟𝑒𝑎𝑙 𝑝𝑜𝑠𝑖𝑡𝑖𝑣𝑎  →  𝑓𝑜𝑐𝑜 𝑖𝑛𝑒𝑠𝑡𝑎𝑏𝑙𝑒 (𝑒𝑠𝑝𝑖𝑟𝑎𝑙 𝑞𝑢𝑒 𝑠𝑒 𝑒𝑥𝑝𝑎𝑛𝑑𝑒)
•  𝑆𝑖 𝜇 = 0: 𝑓𝑜𝑐𝑜 𝑐𝑒𝑛𝑡𝑟𝑜 puro (órbitas cerradas)

Este cambio de estabilidad con aparición de órbitas cerradas es característico de una bifurcación
de Hopf.

170

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 97

Interpretación física (por ejemplo, en un oscilador):

Este sistema puede modelar fenómenos como:

•  Oscilaciones eléctricas en circuitos,
•  Dinámica de poblaciones,
•  Comportamiento de ciertos reactores químicos,
•  Movimiento de fluidos con retroalimentación.

Ejemplo 2 (soluciones explicitas), suponga la dinámica siguiente:

𝜆 −1
𝑋̇ = [
𝜆
1

] 𝑋

𝑋(𝑡) = (

𝑥(𝑡)
𝑦(𝑡)

)

𝑋(𝑡) = 𝑒 𝜆𝑡 [

𝑥0 cos(𝑡) − 𝑦0 sin(𝑡)
𝑥0 sin(𝑡) + 𝑦0 cos(𝑡)

]

Acá la interpretación del parámetro 𝜆:

 𝜆 < 0: 𝐿𝑎𝑠 𝑠𝑜𝑙𝑢𝑐𝑖𝑜𝑛𝑒𝑠 𝑠𝑜𝑛 𝑒𝑠𝑝𝑖𝑟𝑎𝑙𝑒𝑠 𝑞𝑢𝑒 𝑑𝑒𝑐𝑎𝑒𝑛 𝑎𝑙 𝑜𝑟𝑖𝑔𝑒𝑛 (𝑓𝑜𝑐𝑜 𝑒𝑠𝑡𝑎𝑏𝑙𝑒).

𝜆 = 0: 𝐿𝑎𝑠 𝑠𝑜𝑙𝑢𝑐𝑖𝑜𝑛𝑒𝑠 𝑠𝑜𝑛 ó𝑟𝑏𝑖𝑡𝑎𝑠 𝑐𝑒𝑟𝑟𝑎𝑑𝑎𝑠 (𝑐𝑒𝑛𝑡𝑟𝑜), 𝑚𝑜𝑣𝑖𝑚𝑖𝑒𝑛𝑡𝑜 𝑝𝑢𝑟𝑎𝑚𝑒𝑛𝑡𝑒 𝑜𝑠𝑐𝑖𝑙𝑎𝑡𝑜𝑟𝑖𝑜.

𝜆 > 0: 𝐿𝑎𝑠 𝑠𝑜𝑙𝑢𝑐𝑖𝑜𝑛𝑒𝑠 𝑠𝑜𝑛 𝑒𝑠𝑝𝑖𝑟𝑎𝑙𝑒𝑠 𝑞𝑢𝑒 𝑐𝑟𝑒𝑐𝑒𝑛 𝑒𝑥𝑝𝑜𝑛𝑒𝑛𝑐𝑖𝑎𝑙𝑚𝑒𝑛𝑡𝑒 (𝑓𝑜𝑐𝑜 𝑖𝑛𝑒𝑠𝑡𝑎𝑏𝑙𝑒).

171

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejemplo numérico: 𝑆𝑢𝑝𝑜𝑛𝑔𝑎𝑚𝑜𝑠 𝜆 = 0.5, 𝑥0 =   (1, 0), dada estas condiciones iniciales y la dinámica de
un sistema dado la solución que así:

𝑥(𝑡) = 𝑒0.5𝑡 [

cos(𝑡)
sin(𝑡)

]

Esta trayectoria gira en sentido antihorario y se aleja exponencialmente del origen.

¿Qué es la solución final parametrizada?

Cuando una solución final parametrizada en sistemas dinámicos como:

𝑥⃗(𝑡) = 𝑒𝑡 (

sin(𝑡)
−cos(𝑡)

)

Básicamente es una expresión explicita en función de (𝑡), que describe como evoluciona el estado del sistema
en el plano (𝑥(𝑡), 𝑦(𝑡)) a lo largo del tiempo.

Las constantes arbitrarias 𝑐1, 𝑐2 son absorbidas luego de evaluar la solución general en condiciones iniciales.

Ahora  bien,  en  algunos  casos  se  puede  eliminar  el  parámetro  (t),  suponga  que  las  soluciones  ´para  las
variables  de  estado  son:  (𝑡) = cos(𝑡) , 𝑦(𝑡) = − sin(𝑡),   entonces  el  sistema  describe  curvas  soluciones
centradas en el origen ya que 𝑥2 + 𝑦2 = 1

Otro ejemplo suponga:

𝑏𝑒𝑡 ),   𝑥(𝑡) = 𝑎𝑒2𝑡, 𝑦(𝑡) = 𝑏𝑒𝑡, despejando 𝑒𝑡y despejando 𝑒𝑡 =

𝑥⃗(𝑡) = (𝑎𝑒2𝑡
se comporta como una parábola. Esto representa una familia de parábolas que se abren hacia la derecha
si 𝑎 > 0 o hacia la izquierda si 𝑎 < 0

𝑦
, y sustituimos en 𝑥(𝑡) = 𝑎 (
𝑏

𝑦
𝑏

,

2
)

Este otro ejemplo

𝑥⃗(𝑡) = 𝑎𝑒𝑡𝑣⃗1 + 𝑏𝑒−𝑡𝑣⃗2⃗⃗, (solución general)

𝑥⃗(𝑡) = (𝑎𝑒𝑡, 𝑏𝑒−𝑡) parametrizada
𝑎𝑏
𝑥

Las o𝑟𝑏𝑖𝑡𝑎   𝑦 =

 , ℎ𝑖𝑝é𝑟𝑏𝑜𝑙𝑎𝑠

Estructura Orbital

En sistemas dinámicos, la estructura orbital se refiere a la forma y disposición geométrica de las órbitas
(trayectorias de las soluciones) en el espacio de fases, particularmente cerca de los puntos de equilibrio o
atractores.  Es  un  concepto  central  en  el  análisis  cualitativo  de  sistemas,  ya  que  describe  cómo  se

172

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

comportan las soluciones sin necesidad de resolver el sistema de forma explícita. La estructura orbital de
un sistema dinámico es el conjunto de todas las órbitas (curvas solución del sistema en el espacio de fases)
organizadas  en  torno  a:  puntos  de  equilibrio,  ciclos  límite,  variedades  estables  e  inestables,  y  otras
estructuras invariantes como toroides o atractores extraños.

Componentes de la estructura orbital

1.  Órbitas (trayectorias):

o  Pueden ser cerradas (ciclos límite), espirales, líneas rectas, etc.

2.  Puntos de equilibrio:

o  Nodo, espiral, centro, silla, etc.
o  Determinan la organización local de las órbitas.

3.  Variedades estables/inestables:

o  Son trayectorias que se acercan o alejan del equilibrio a medida que 𝑡 → ±∞

4.  Separatrices:

o  Curvas  especiales  que  separan  comportamientos  cualitativamente  distintos  (ej.  la

trayectoria de una silla).

5.  Ciclos límite:

o  Órbitas cerradas aisladas que atraen o repelen otras trayectorias.

6.  Conjunto límite 𝜔(𝑥0):

o  Conjunto de puntos que una órbita se aproxima cuando 𝑡 → +∞
o  El conjunto 𝛼(𝑥0) es el análogo para 𝑡 → −∞

Conjuntos Límites

En sistemas dinámicos, los  conjuntos límite describen el comportamiento a largo plazo de una solución
(órbita). Nos  indican hacia  dónde tiende  una  trayectoria cuando el tiempo va hacia el infinito (positivo o
negativo).

Sea 𝜙(𝑡, 𝑥0) la solución del sistema dinámico con condición inicial 𝑥0. Entonces:

El conjunto límite positivo de 𝑥0, denotado 𝜔(𝑥0), es:

𝜔(𝑥0) = {𝑦 ∈ ℝ𝑛 | ∃𝑡𝑛 → +∞ tal que 𝜙(𝑡𝑛, 𝑥0) → 𝑦}

El conjunto límite negativo de 𝑥0, denotado 𝛼(𝑥0), es:
𝛼(𝑥0) = {𝑦 ∈ ℝ𝑛 | ∃𝑡𝑛 → −∞ tal que 𝜙(𝑡𝑛, 𝑥0) → 𝑦}

Es decir:

173

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  𝜔(𝑥0): lo que la órbita se acerca cuando 𝑡 → +∞
•  𝛼(𝑥0): lo que la órbita se acerca cuando 𝑡 → −∞

Ejemplo:

{𝑥̇ = −𝑥 + 𝑦, 𝑦̇ = −𝑦, 𝑦 𝑒𝑙 𝑝𝑢𝑛𝑡𝑜 𝑖𝑛𝑖𝑐𝑖𝑎𝑙 𝑒𝑠 (1,1)

Este sistema es un nodo degenerado:

 Autovalor: 𝜆 = −1,  𝐴𝑢𝑡𝑜𝑣𝑒𝑐𝑡𝑜𝑟: 𝑣 = [1, 0], vector generalizado: 𝑤 = [0, 1]

Entonces:

𝑋⃗(𝑡) = 𝑒−𝑡 (𝑐1 (

1
0

) + 𝑐2  ((

0
1

) + 𝑡 (

1
0

)))

Para  condiciones  iniciales  𝑥0 = (1
arbitrarias, entonces la solución particular es:

1),  resolvemos  el  sistema  y  hallamos  los  valores  de  las  constantes

𝑋⃗(𝑡) = 𝑒−𝑡 (

𝑡 + 1
1

),

𝑥(𝑡) = 𝑒−𝑡(𝑡 + 1), 𝑒 𝑦(𝑡) = 𝑒−𝑡

Comportamiento cuando 𝑡 → +∞

𝑥(𝑡) = (1 + 𝑡)𝑒−𝑡 → 0,
𝑦(𝑡) = 𝑒−𝑡 → 0

Entonces:  lim
𝑡→∞

𝑋⃗(𝑡) = 0

𝜔(1,1) = {(0,0)}

Comportamiento cuando 𝑡 → −∞

𝑥(𝑡) = (1 + 𝑡)𝑒−𝑡 → −∞ ⋅ ∞ = ∞ (crece exponencialmente)

Se resuelve la indeterminación con L’Hopital

∥ 𝑥(𝑡) ∥→ ∞

𝛼(1,1) = ∅, la trayectoria escapa al infinito hacia atrás

Resumen de la simbología

174

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Símbolo

𝜙𝑡(𝑥0)

𝜔(𝑥0)

𝛼(𝑥0)

𝑂(𝑥0)

𝑂+(𝑥0)

𝑂−(𝑥0)

Significado

Flujo (trayectoria) que pasa por el punto 𝑥0 al tiempo 𝑡

Conjunto límite positivo: conjunto de puntos donde se acumula la órbita 𝜙𝑡(𝑥0)
cuando 𝑡 → +∞

Conjunto límite negativo: conjunto de puntos donde se acumula 𝜙𝑡(𝑥0) cuando
𝑡 → −∞

Órbita completa del punto 𝑥0, incluye todos los tiempos 𝑡 ∈ ℝ

Órbita positiva: trayectoria para 𝑡 ≥ 0

Órbita negativa: trayectoria para 𝑡 ≤ 0

Ejercicios propuestos (autónomos y no autónomos):

1.  𝑥̇ = −𝑥, 𝑦̇ = −𝑦  (parametrízalo con respecto al tiempo)
2.  𝑥̇ = 𝑥, 𝑦̇ = 𝑥 + 𝑦  (solución temporal)
3.  𝑥̇ = 𝑦, 𝑦̇ = −𝑥 (curvas de nivel)
4.  𝑥̇ = 𝑥2, 𝑦̇ = −𝑦 (eliminación del parámetro)
5.  𝑥̇ = 𝑦, 𝑦̇ = − sin(𝑥), (conservativo)
6.  𝑥̇ = 𝑥 + 𝑡, 𝑦̇ = −𝑦 + cos(𝑡), (no autónomo)
7.  𝑥̇ = −𝑥 + 𝑡2, 𝑦̇ = 𝑦 + sin(𝑡) (no autónomo)

𝑑𝑦
𝑑𝑥

𝑑𝑦
8.  𝑥̇ = 𝑥, 𝑦̇ = 𝑥𝑦,  derivada
𝑑𝑥
9.  𝑥̇ = 𝑦, 𝑦̇ = −𝑥 + sin(𝑡) (sistema forzado no autonomo)
10.  𝑥̇ = −𝑦 + 𝑎𝑥(𝑥2 + 𝑦2), 𝑦̇ = 𝑥 + 𝑎𝑦(𝑥2 + 𝑦2), analice y use coordenadas polares
11.  Analice y simule el siguiente sistema 𝑥̇   = 𝑦, 𝑦̇   =  2𝑦 + 𝑦2
12.  Determinar la estructura orbital para los siguientes sistemas:

a)  𝑥̇   = 𝑥 +  𝜇𝑦, 𝑦̇   = 𝜇𝑥 − 𝑦
b)  𝑥̇ = −𝑥, 𝑦̇ = −2𝑦, condición inicial (𝑥0, 𝑦0) = (1,1)
c)  𝑥̇ = 𝑥, 𝑦̇ = 2𝑦, condición inicial (𝑥0, 𝑦0) = (1,1)
d)  𝑥̇ = −𝑥 − 𝑦, 𝑦̇ = 𝑥 − 𝑦
e)  𝑥̇ = −𝑦, 𝑦̇ = 𝑥
f)    𝑥̇ = 𝑥(1 − 𝑦), 𝑦̇ = 𝑦(𝑥 − 1)
g)  𝑥̇ = 𝑦 + 𝑥(1 − 𝑥2 − 𝑦2), 𝑦̇ = −𝑥 + 𝑦(1 − 𝑥2 − 𝑦2)
h)  𝑥̇ = 𝑥(1 − 𝑥2 − 𝑦2), 𝑦̇ = 𝑦(1 − 𝑥2 − 𝑦2)

175

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios Adicionales

Analizar los sistemas con bifurcación: Grafique con un software y compare sus cálculos y análisis manuales

Unidimensionales

a)  𝑥̇ = 𝜇 + 𝑥 − 𝑥3
b)  𝑥̇ = 𝜇 − 2𝑥2
c)  𝑥̇ = 𝜇𝑥2 − 𝑥3
d)  𝑥̇ = 𝜇 + 2𝑥2
e)  𝑥̇ = 𝜇𝑥2 − 2𝜇𝑥 + 1
f)  𝑥̇ = 𝜇𝑥 + 𝑥3 − 𝑥5
g)  𝑥̇ = 1 + 𝜇𝑥 − 𝑥3

Sistemas 2d

1.  𝑥̇ = 𝑥 + 𝑦 − 𝜇,

 𝑦̇ = 2𝑥 + 2𝑦 + 1 − 𝜇,

a). Analizar su estructura orbital, demostrar que hay una bifurcación en 𝜇 = −1, y que el sistema tiene una
línea de puntos de equilibrios sobre la recta 𝑥 + 𝑦 = −1

b). Demostrar que las soluciones se comportan como: 𝑋(𝑡) = 𝑐1( 1

−1) + 𝑐2(1

2)𝑒3𝑡

2.  𝑥̇   =  𝜇𝑥 +  𝜇𝑦 + 1, 𝑦̇   = 𝑥 + 𝑦 −  𝜇
3.  𝑥̇ =  𝑦 + 2, 𝑦̇ = 𝑥  − 𝑦 −  𝜇
4.  𝑥̇   =  𝑥 +  𝜇𝑦, 𝑦̇   =   𝜇𝑥 −  𝑦
5.  𝑥̇   =   𝜇𝑥 −   𝑥2, 𝑦̇   = − 𝑦

Modelos de combate y Epidemiológicos y Físicos

a)  Explicar el signo de cado de los coeficientes positivos 𝑎, 𝑏 en el modelo lanchesteriano de combate de
dos  fuerzas  convencionales 𝑥 𝑒 𝑦,  y  analizar  su  dinámica  (en  el  primer  cuadrante),  determinando  la
ecuación de las orbitas para cada 𝑋0. Rehacer, ahora considerando una tasa de refuerzo constante para
cada fuerza 𝛼, 𝛽.  𝑥̇   = − 𝑎𝑦,  𝑦̇   =   −𝑏𝑥.

176

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

b)  Si  en  el  modelo  lanchesteriano  la  fuerza  𝑥  es  no  convencional,  analizar  su  dinamica  (en  el  primer
cuadrante), determinando la ecuacion de las orbitas para cada 𝑋0.  Rehacer, ahora considerando una tasa
de refuerzo constante 𝛼, 𝛽 para cada fuerza.  𝑥̇   =  𝑎𝑥𝑦, 𝑦̇   =  𝑏𝑥

c)  Interpretar  los  coeficientes  positivos  𝑎𝑏, 𝑐𝑑  y  analizar  la  dinamica  del  sistema  de  Lotka-Volterra  en
espacios  limitados  de  recursos  sin  interacciones  intra-especies,  especificando  hipótesis  sobre  el
depredador y la presa consistentes con el modelo y resolverlo. Analizar las modificaciones introducidas
por una intervención externa de tasa constante. 𝑥̇ = (𝑎 −  𝑏𝑦)𝑥, 𝑦̇   =   −(𝑑 − 𝑐𝑥)𝑦

d)  Interpretar los coeficientes positivos ab cd, 𝛼, 𝛽 y analizar la dinamica del sistema de Lotka-Volterra en
espacios  limitados  de  recursos  con  interaciones  intra-especies  (conviene  considerar  dos  casos
distintos,segun que las nulclinas se intersequen o no en el primer cuadrante: en el primer caso se tendra
una extincion del depredador con una estabilizacion de la presa en a , mientras que en el segundo una
estabilizacion asintotica en la interseccion, para cualquier condicion inicial en el primer cuadrante). 𝑥̇   =
(𝑎 − 𝑏𝑦 −  𝛼𝑥)𝑥, 𝑦̇   =   (−𝑑 +  𝑐𝑥 −  𝛽𝑦)𝑦

e)  El principio de exclusión competitiva afirma que si dos especies similares 𝑥𝑦 compiten en un espacio que
puede  albergar  más  miembros  de  𝑥  que  de  𝑦,  entonces  y  termina  extinguiendose  y  todo  el  espacio
saturado de 𝑥. Probarlo interpretando el siguiente sistema con 𝑎  >  𝑏.  𝑥̇   = (𝑎 − 𝑥 − 𝑦)𝑥, 𝑦̇   = (𝑏 −  𝑥 −
 𝑦)𝑦

f)  Un  modelo  epidemiológico  de  propagación  de  una  enfermedad  que  identifica  con  𝑥  a  la  población
contagiosa (tasa de infección constante 𝑟  >  0 y con 𝑦 a la contagiada, tomando como constante  𝛾 >  0
𝛾
la tasa de retiro se representa por el siguiete sistema. Probar que existe un umbral epidemiológico 𝜌=
,
𝑟
que siempre quedan sin contraer la enfermedad algunos individuos 𝑥̇   =   −𝑟𝑥𝑦, 𝑦̇   = 𝑟𝑥𝑦 − 𝛾𝑦

g)  Una  epidemia  (SIR)  donde 𝛼 > 0, tasa  de  contagio, 𝛽 > 0,  tasa  de  recuperación,  y 𝑥(𝑡) > 0 población

susceptible,  𝑦(𝑡) > 0 población infectada, según el modelo:

𝑥̇ = −𝛼𝑥𝑦, 𝑦̇ = 𝛼𝑥𝑦 − 𝛽𝑦,

1.  Haga un análisis cualitativo de la dinámica del sistema
2.  Demuestre que la solución paramétrica del sistema es: 𝑦(𝑥) = −𝑥 +
3.  Use el método de newton Raphson para aproximar la cantidad de susceptibles no contagiados si

ln(𝑥) + 𝑐

𝛽
𝛼

los hay al finalizar el brote, use como semilla 𝑥0 = 1.5 (escala 1000:1)

4.  Simule el sistema para condiciones iniciales 𝑥0 = 3,  𝑦0 = 0.197, (en miles), 𝛼 = 0.1, 𝛽 = 0.2 para
esto  use  la  solución  paramétrica  del  sistema.  Presente  la  dinámica  en  un  diagrama  de  fase,
indicando punto máximo del brote de la epidemia, inicio y fin de esta. Umbral 𝜌 =

𝛽
𝛼

h)  Un video juego simula un brote zombi que se propaga en una isla aislada. El número de humanos 𝑥(𝑡)
y zombis 𝑦(𝑡)) evoluciona según las siguientes reglas:

❖  Cada vez que un humano se encuentra con un zombi, tiene una probabilidad de ser transformado

en zombi.

177

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

❖  Los zombis se desgastan si no encuentran humanos (muerte zombi).
❖  No nacen humanos ni zombis nuevos fuera de estas interacciones.

El sistema se modela con: 𝑥̇ = −𝛼𝑥𝑦, 𝑦̇ = 𝛼𝑥𝑦 − 𝛽𝑦, donde:

𝑥(𝑡): número de humanos vivos

𝑦(𝑡): número de zombis activos

La dinámica muestra que:

−𝛼𝑥𝑦: los zombis convierten humanos en zombis a una tasa proporcional al producto 𝑥𝑦(encuentros). Por
cada encuentro, se convierten 𝛼 humanos en zombis (por simplicidad).
+𝛼𝑥𝑦: zombis nuevos surgen al atacar humanos.
−𝛽𝑦: los zombis desaparecen a razón de 1 por unidad de tiempo si no atacan (fatiga, hambre, lucha, etc.)

1.  Haga un análisis cualitativo de la dinámica del sistema
2.  Simule el sistema para condiciones iniciales 𝑥0 = 35,  𝑦0 = 2,  𝛼 = 0.1, 𝛽 = 2 para esto use la solución

paramétrica del sistema 𝑦(𝑥) = −𝑥 +

ln(𝑥) + 𝑐 (demuestre su validez)

𝛽
𝛼

3.  Use el método de newton Raphson para aproximar la cantidad de sobreviviente si los hay al finalizar el

brote, use como semilla 𝑥0 = 9

4.  Grafique la dinámica en un diagrama de fase, indique punto máximo del brote de la epidemia, inicio y fin

de esta

i)  Modele y analice el siguiente sistema dinámico unidimensional, modelo de Verhulst, para ambientes
de  recursos  restringidos,  postula  que  la  población  afectada  varia  con  una  velocidad  proporcional  a  la
= 𝑘𝑝(𝑛 − 𝑝),  donde (n) es la población total,
población total de dicho ambiente y los afectados según:
(p)  población  afectada  y  (k)  una  constante  de  propagación.  Para  modelar  el  contagio  de  un  virus  que
propaga  el  paciente  cero.  Demostrar  que  la  solución  del  sistema  es:  𝑃(𝑡) =
1+𝐴𝑒−𝑁𝑘𝑡  ,    donde  A  es  una
constante arbitraria. Y hallar el número de infectados para el día 4, si el día cero hay uno solo, y el día 3 hay
20, n=100.

𝑑𝑝
𝑑𝑡

𝑁

j)  Un  pequeño  reactor  se  apaga  y  la  temperatura  de  su  núcleo  comienza  a  descender  según  la  ley  de
enfriamiento de newton. Considere que no tiene energía residual y que la constante de enfriamiento es 𝑘 =
0.04 𝑚𝑖𝑛−1,  Suponga  que  la  lectura 𝑇(0) = 200º C ,  y  la  temperatura  ambiental  constante  de 𝑇𝑎 = 25ºC,
¿Cuál sería la lectura de temperatura si la medimos a los 30 min?

 Ley de enfriamiento de Newton sin retroalimentación por inducción:

𝑑𝑇
𝑑𝑡

= −𝑘(𝑇 − 𝑇𝑎)

178

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Otros sistemas

1.  Un asteroide se encuentra girando alrededor del planeta (debido a la gravedad) y existe un parámetro
𝜇  que  representa  la  "capacidad  de  desvío"  (por  ejemplo,  por  efectos  gravitatorios  adicionales  o  por
intervención  humana).  x(t):  es  la  desviación  horizontal  respecto  al  punto  de  impacto  directo. 𝑦(𝑡):  es  la
desviación vertical respecto al punto de impacto directo.

La dinámica simplificada del sistema está dada por: 𝑥̇ = 𝜇𝑥 − 𝑦 − 𝑥(𝑥2 + 𝑦2), 𝑦̇ = 𝑥 + 𝜇𝑦 − 𝑦(𝑥2 + 𝑦2)

El  parámetro  𝜇  puede  ser  interpretado  como  una  medida  del  control  efectivo  sobre  el  asteroide,  por
ejemplo:

•  Desviación gravitacional inducida,
Empuje con impacto de sonda,
•
Influencia del viento solar,
•

a) Analiza la estabilidad del punto de equilibrio en el origen considerando diferentes valores del parámetro
𝜇. Explica qué sucede en el sistema cuando 𝜇 cambia de valores negativos a positivos. ¿Qué interpretación
física tiene este cambio dinámico en relación con la trayectoria

b) Grafica el diagrama de fase del sistema en el plano (𝑥, 𝑦) Interpreta cómo la presencia de la bifurcación
modifica las trayectorias.

2.  Un patinador artístico gira sobre su eje vertical mientras intenta mantener el equilibrio. Su velocidad
angular  de  giro  está  representada  por  la  variable  𝑥(𝑡)  y  su  balanceo  lateral  por  𝑦(𝑡),  La  dinámica
simplificada del sistema está dada por: 𝑥̇ = 𝜇𝑥 − 𝑦 − 𝑥(𝑥2 + 𝑦2), 𝑦̇ = 𝑥 + 𝜇𝑦 − 𝑦(𝑥2 + 𝑦2)

donde:
•  𝑥(𝑡): velocidad angular del giro en rad/s,
•  𝑦(𝑡)): ángulo de inclinación lateral en rad,
•  𝜇: parámetro que representa la habilidad o control del patinador para mantener la estabilidad (puede
depender, por ejemplo, de la experiencia o de la concentración).

a) Analiza la estabilidad del punto de equilibrio en el origen considerando diferentes valores del parámetro
𝜇. Explica qué sucede en el sistema cuando 𝜇 cambia de valores negativos a positivos. ¿Qué
interpretación física tiene este cambio dinámico en relación con el control del giro y el equilibrio del
patinador?
b) Grafica el diagrama de fase del sistema en el plano (𝑥, 𝑦) Interpreta cómo la presencia de la bifurcación
modifica la estabilidad del giro del patinador y describe el efecto visualizado en el comportamiento de las
trayectorias.

3.  El siguiente sistema dinámico 𝑥̇ = 𝑦, 𝑦̇ = 𝜇(1 − 𝑥2)𝑦 − 𝑥, modela  los latidos cardiacos (Van der  Pol
modificado),  Este  sistema  genera  oscilaciones  periódicas  cuando  μ>0.  Para  valores  grandes  de  μ,  el
sistema tiene oscilaciones tipo "relajación", que son parecidas a los latidos del corazón: una subida rápida,
una meseta, y una bajada rápida.

179

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

a)  Haga un análisis cualitativo de la dinámica y determine si hay un ciclo limite
b)  Grafique el diagrama de fase para para distintos valores de 𝜇

4.  En  un  pequeño  ecosistema  interactúan  dos  poblaciones:   𝑥(𝑡):  número  de  abejas  recolectoras  en

actividad.
𝑦(𝑡): cantidad de flores con néctar disponible. La dinámica se describe con el siguiente sistema: 𝑥̇ =
𝑥(1 − 𝑥) + 2𝑥𝑦, 𝑦̇ = −𝑦 + 2𝑥𝑦.

Las abejas se reproducen con un crecimiento logístico 𝑥(1 − 𝑥), limitado por recursos y espacio.

La recolección de néctar estimula la actividad de las abejas: el término 2𝑥𝑦 representa la cooperación
entre flores y abejas.

Las flores pierden néctar de forma natural −𝑦, pero su renovación se favorece cuando hay abejas cerca
2𝑥𝑦, porque las abejas polinizan y promueven nuevas flores.

c)  Haga un análisis cualitativo de la dinámica para valores de 𝑥(𝑡), 𝑦(𝑡) > 0
d)  Grafique el diagrama de fase (primer cuadrante, solo para poblaciones positivas)

5. Un  enjambre  de  nanobots  realiza  tareas  de  construcción  y  puede  estar  en  dos  estados;    𝑥(𝑡) :
proporción  de  nanobot  activos  (construyendo).  𝑦(𝑡):  proporción  de  nanobot  inactivos  en
espera, el modelo:

𝑥̇ = 𝑎𝑥(1 − 𝑥),  𝑦̇ = 𝑏𝑦(2 − 𝑦)   los  parámetros  𝑎 > 0  es  la  tasa  de  activación  o  crecimiento  de
nanobot activos. 𝑏 > 0 es la tasa activación o crecimiento de nanobot inactivos.

a) Encuentra y clasifica los puntos de equilibrio del sistema. ¿Qué representan estos estados

para la proporción de nanobots activos e inactivos?

b) Analiza la estabilidad de cada punto de equilibrio. ¿Cuál es el estado estable que representa el

comportamiento esperado a largo plazo del enjambre?

6.  Un sistema logístico que modela la saturación de un de servidor de la forma 𝑥̇ = 𝑟𝑥 (1 −

𝑥
𝑘

),

1
 Se quiere hallar los puntos de equilibrio, y demostrar que el servidor se satura en: 𝑡𝑠 =
𝑟

𝑙𝑛 (

𝑘−𝑥0
𝑥0

) , y que la

solución  del  sistema  es:  𝑥(𝑡) =
crecimiento: 𝑟 = 0.15 (min), 𝑦 𝑥0 = 1500 𝑟𝑝𝑠. Graficar el comportamiento temporal del sistema.

1+𝐴𝑒−𝑟𝑡 ,  donde  la  capacidad  máxima  es:  𝑘 = 20000 𝑟𝑝𝑠,  tasa  de

𝑘

7.  En un laboratorio de investigación en la Cordillera de los Andes, un contenedor con un isótopo radiactivo
Iodo-131 sufre una pequeña fuga. Este isótopo se usa en medicina nuclear y tiene una vida media de 8
días.  En  el  instante  del  accidente  (t  =  0),  la  cantidad  liberada  fue  de  120  miligramos  y  se  esparció
uniformemente en una sala sellada.

180

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

El proceso de desintegración sigue la ley:

𝑑𝑁
𝑑𝑡

= −𝜆𝑁

donde 𝑁(𝑡)es la cantidad de sustancia (en mg) y 𝜆 =

ln 2
𝑇1/2

, Vida media: 𝑇1/2 = 8días, Cantidad inicial:

𝑁(0) = 120mg, Tiempo de observación: hasta 40 días, Nivel seguro para ingreso humano: menos de 5 mg

a) ¿Cuánta sustancia radiactiva queda luego de 16 días?
b) ¿Luego de cuántos días el nivel está por debajo del umbral seguro de 5 mg?

Sistemas conservativos

Probar que es un centro o una silla

a)  𝑥̇ = 𝑥 −  2𝑥𝑦, 𝑦̇   = 𝑥 −  𝑦 + 𝑦2
b)  𝑥̇   = 2𝑥𝑦, 𝑦̇   = 1 + 3𝑥2 − 𝑦2

Sistema de orden 2 (analizar el sistema transformar a un sistema 2d)

a)  𝑥̈ + 2𝑥̇ + 2𝑥 = 0  𝑥(0) = 1, 𝑥̇(0) = 0
b)  𝑥̈ + 2𝑥̇ + 𝑥 = 0, 𝑥(0) = 1,  𝑥 ̇ (0) = 0

Sistemas no homogéneos resolver para condiciones iniciales

a)  𝑥̇   = 2𝑥 − 𝑦 + 1, 𝑦̇   = − 𝑥 + 2𝑦 −  5, 𝑋(0) = (2
3)
b)  𝑥̇   = − 𝑥 + 4𝑦 − 2, 𝑦̇   = 𝑥 −  𝑦 − 1,    𝑋(0) = (3
1)

Conjuntos límites unidimensionales

En cada uno de los siguientes casos, efectuar un análisis cualitativo completo, incluyendo consideraciones
acerca de los conjuntos límite.

a)  𝑥̇ = 𝑥2 − 𝑥 −  2
b)  𝑥̇   =   𝑥3 −  4𝑥2 + 4𝑥
c)  𝑥̇ =  𝑥 − 𝑥3
d)  𝑥̇   =   𝑥4 −   𝑥2
e)  𝑥̇   = −𝑥4 + 𝑥2

181

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios de sistemas no lineales, Variedades (Manifold)

Ejercicio 1 – Variedades en sistema lineal
Dado el sistema:

𝑥̇ = 3𝑥 + 𝑦, 𝑦̇ = −𝑥 + 𝑦

1.  Hallar los autovalores y autovectores.
2.  Determinar la variedad estable e inestable.
3.  Escribir la solución general indicando las direcciones de las variedades.

Forma matricial

Autovalores

Autovalor doble:

𝑋̇ = 𝐴𝑋, 𝐴 = (

3
1
−1 1

)

det (𝐴 − 𝜆𝐼) = [
= 𝜆2 − 4𝜆 + 4 = (𝜆 − 2)2

3 − 𝜆
−1

1
1 − 𝜆

] ∣= (3 − 𝜆)(1 − 𝜆) + 1

Es repulsor → no hay variedad estable.

𝜆1 = 𝜆2 = 2 > 0

Autovector

De aquí:

Variedades
•  Como λ>0:

(𝐴 − 2𝐼)𝑣 = 0 ⇒ (

1
1
−1 −1

) 𝑣 = 0

𝑣1 = (

1
−1

)

Variedad inestable: dirección del autovector

Variedad estable:

𝑊𝑢 = span{(1, −1)}

𝑊 𝑠 = {0}

Ejercicio 2 – Variedad estable/inestable lineal

𝑥̇ = 𝑥 − 4𝑦, 𝑦̇ = 2𝑥 − 𝑦

182

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

1.  Clasificar el origen.
2.  Encontrar ecuaciones explícitas de 𝑊 𝑠 y 𝑊𝑢.

Ejercicio 3 – Variedad inestable no lineal

𝑥̇ = 𝑥, 𝑦̇ = −2𝑦 + 𝑥2

1.  Mostrar que el eje x es variedad inestable del origen.
2.  Hallar la variedad estable como gráfica 𝑦 = ℎ(𝑥).

Buscamos 𝑦 = ℎ(𝑥) invariante:

ℎ′(𝑥)𝑥̇ = 𝑦̇
ℎ′(𝑥) 𝑥 = −2ℎ(𝑥) + 𝑥2

EDO para h(x).

Ejercicio 4 – Variedad central

𝑥̇ = −𝑥, 𝑦̇ = 𝑦2

1.  Probar que el eje y es variedad central.
2.  Analizar estabilidad usando reducción a la variedad.

Ejercicio 5 – Tipo Liénard y variedad lenta
Van der Pol:

𝑥̇ = 𝑦, 𝑦̇ = 𝜇(1 − 𝑥2)𝑦 − 𝑥

1.  Para |μ|≫1 identificar variedad lenta aproximada.
2.  Relacionarla con nulclina 𝑥 = 0.

Ejercicio 6 – Método del gráfico invariante

𝑥̇ = −3𝑥 + 𝑦, 𝑦̇ = −𝑦 + 𝑥3

1.  Calcular jacobiano.
2.  Usar ecuación de invariancia para hallar 𝑦 = ℎ(𝑥) hasta orden 3.

Ejercicio 7 – Región tipo cuña
Sistema:

Sea

𝑥̇ = 2𝑥 + 𝑦, 𝑦̇ = −3𝑦

𝑆 = {(𝑥, 𝑦): ∣ 𝑥 ∣ ≥ ∣ 𝑦 ∣}

1.  Estudiar el flujo en la frontera |x|=|y|.
2.  Decidir si S contiene la variedad inestable.

183

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicio 8 – Degenerado con vector generalizado

𝐴 = (

1 1
0 1

)

1.  Hallar autovector y generalizado.
2.  Interpretar variedad inestable única.

Ejercicio 9 – Lotka–Volterra

𝑥̇ = 𝑥(2 − 𝑦), 𝑦̇ = 𝑦(𝑥 − 1)

1.  Hallar equilibrios.
2.  Clasificar y obtener variedad estable del punto silla.

Ejercicio 10 – Coordenadas polares

𝑟̇ = 𝑟(1 − 𝑟2), 𝜃̇ = 1

1.  Mostrar que r=0 y r=1 son variedades invariantes.
2.  Relacionarlo con ciclo límite.

¿Qué es una región atrapante?

Un conjunto 𝑆 ⊂ ℝ2 es región atrapante si: ∃𝑇 > 0 tal que ∀𝑥0 ∈ 𝑆, 𝜑(𝑡, 𝑥0) ∈ ∀𝑡 ≥ 𝑇

En la práctica: El flujo entra o es tangente en la frontera, Las trayectorias no pueden escapar

 MÉTODO GENERAL (ALGORITMO PRÁCTICO)

Cuando te dan un sistema plano:

 Paso 1 — Busca una “cantidad radial”

Candidatos típicos:

𝑉 = 𝑥2 + 𝑦2, 𝑉 = 𝑎𝑥2 + 𝑏𝑦2, 𝑉 =∥ (𝑥, 𝑦) ∥2

Paso 2 — Calcula 𝑉̇

Paso 3 — Estudia el signo de 𝑉̇ en la frontera

𝑉̇ = ∇𝑉 ⋅ 𝐹(𝑥, 𝑦)

184

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

•  𝑉̇ < 0→ entra

•  𝑉̇ > 0→ sale

•  𝑉̇ = 0→ tangente

Paso 4 — Construí el conjunto

•  Disco: { 𝑉 ≤ 𝑐 }

•  Corona: { 𝑐1 ≤ 𝑉 ≤ 𝑐2 }

Paso 5 — Cerrado + acotado ⇒ compacto

 ya tenéis región atrapante

 EJERCICIO 1 — Van der Pol clásico (caso fundamental)

𝑥̇ = 𝑦, 𝑦̇ = 𝜇(1 − 𝑥2)𝑦 − 𝑥, 𝜇 > 0

Paso 1: Puntos de equilibrio

𝑦 = 0, −𝑥 = 0 ⇒ (0,0)

Paso 2: Comportamiento cerca del origen

Jacobiano:

𝐽(0,0) = (

0
1
−1 𝜇

) ⇒ foco inestable

Las trayectorias salen del origen.

Paso 3: Conjunto atrapante

Consideramos una corona

𝑆 = {(𝑥, 𝑦): 𝑟1

2 ≤ 𝑥2 + 𝑦2 ≤ 𝑟2

2}

•  Para 𝑟 grande → disipación → el flujo entra

•  Para  𝑟 pequeño  →

foco

inestable  →  el

flujo  sale,  S  es  compacto  e

invariante

 El único equilibrio está fuera del interior dinámico

185

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Paso 4: Conclusión

Por Poincaré–Bendixson, existe al menos un ciclo límite estable. Resultado: Van der Pol tiene un ciclo límite
único y estable.

EJERCICIO 2 — Sistema polinómico con divergencia negativa

𝑥̇ = 𝑦 − 𝑥(𝑥2 + 𝑦2 − 1), 𝑦̇ = −𝑥 − 𝑦(𝑥2 + 𝑦2 − 1)

Paso 1: Equilibrio

Paso 2: Función radial

Calculando:

(0, 0)

𝑉 = 𝑥2 + 𝑦2 ⇒ 𝑉̇ = 2𝑥𝑥̇ + 2𝑦𝑦̇

𝑉̇ = −2(𝑥2 + 𝑦2)(𝑥2 + 𝑦2 − 1)

Paso 3: Análisis

•  Si 𝑥2 + 𝑦2 < 1→ 𝑉̇ > 0 (sale)

•  Si 𝑥2 + 𝑦2 > 1→ 𝑉̇ < 0 (entra)

La circunferencia 𝑥2 + 𝑦2 = 1 es atractora

Paso 4: Poincaré–Bendixson

La región anular es compacta, invariante y sin equilibrios internos.  Resultado: Existe un ciclo límite estable
exactamente en 𝑥2 + 𝑦2 = 1.

EJERCICIO 3 — Existencia sin conocer la forma del ciclo

𝑥̇ = 𝑦, 𝑦̇ = −𝑥 + (1 − 𝑥2)𝑦

Paso 1: Equilibrio

(0, 0)

186

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Linealización → foco inestable.

Paso 2: Conjunto atrapante

Tomamos 𝑉 = 𝑥2 + 𝑦2:

•  Para ∣ 𝑥 ∣< 1: 𝑉̇ > 0

•  Para ∣ 𝑥 ∣> 1: 𝑉̇ < 0

Existe una corona atrapante.

𝑉̇ = 2(1 − 𝑥2)𝑦2

Paso 3: Aplicación del teorema

•  Compacto

•

Invariante

•  Sin equilibrio en el interior

Conclusión: existe al menos un ciclo límite.

 EJERCICIO 4 — Demostrar que NO hay ciclos límite (contraste)

𝑥̇ = −𝑦, 𝑦̇ = 𝑥

∇ ⋅ 𝐹 = 0

𝐻 =

1
2

(𝑥2 + 𝑦2) ⇒ 𝐻̇ = 0

Paso 1: Divergencia

Paso 2: Sistema conservativo

Paso 3: Conclusión

•

Todas las trayectorias son curvas de nivel, y no hay conjuntos atrapantes

 Resultado:  Poincaré–Bendixson: No aplica, no hay ciclos límite (solo órbitas cerradas no aisladas)

187

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicios resueltos –Lyapunov y Lasalle

Antes  recordemos  la  definición:  Teorema  (directo)  de  Lyapunov  –  Estabilidad,  Considera  el  sistema
dinámico autónomo

𝑥̇ = 𝑓(𝑥), 𝑓(0) = 0

(donde 𝑥 = 0 es un punto de equilibrio). Definición: Supongamos que existe una función escalar

𝑉: ℝ𝑛 → ℝ

tal que:

1.  Positividad

𝑉(0) = 0, 𝑉(𝑥) > 0 para 𝑥 ≠ 0

2.  Derivada no positiva a lo largo de las trayectorias

𝑉̇ (𝑥) = ∇𝑉(𝑥) ⋅ 𝑓(𝑥) ≤ 0

Entonces: El equilibrio 𝑥 = 0 es estable en el sentido de Lyapunov.

Estabilidad asintótica (Lyapunov fuerte), si además se cumple:

3.  Derivada estrictamente negativa

𝑉̇ (𝑥) < 0para todo 𝑥 ≠ 0

Entonces:  El equilibrio 𝑥 = 0es asintóticamente estable.

 Interpretación intuitiva

•  𝑉(𝑥) se interpreta como una energía o altura.

•  𝑉 > 0: el sistema está “por encima del mínimo”.

•  𝑉̇ ≤ 0: la energía no aumenta.

•  𝑉̇ < 0: la energía disminuye estrictamente, forzando al sistema a caer al equilibrio.

 Como una bolita en un cuenco: ver figura

•  Si no sube → estabilidad, Si siempre baja → estabilidad asintótica

188

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

FIGURA 98

Cuando Lyapunov no basta (Teorema de Invariancia de LaSalle)

Considérese el sistema autónomo:

𝑥̇ = 𝑓(𝑥), 𝑥 ∈ ℝ𝑛

donde 𝑓es localmente Lipschitz (para garantizar existencia y unicidad de soluciones). Sea 𝑉: ℝ𝑛 → ℝ una
función de clase 𝐶1 tal que:

1.  𝑉(𝑥) ≥ 0 en un conjunto 𝐷 ⊂ ℝ𝑛

2.  𝑉̇ (𝑥) = ∇𝑉(𝑥) ⋅ 𝑓(𝑥) ≤ 0 en 𝐷

Sea además: Ω ⊂ 𝐷 un conjunto compacto e invariante positivo (toda trayectoria que entra a Ω permanece
en él para 𝑡 ≥ 0).

Definimos el conjunto:

𝐸 = {𝑥 ∈ Ω: 𝑉̇ (𝑥) = 0}

A Continuación, se muestra una representación geométrica que como actúa el teorema de LaSalle

189

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

y sea 𝑀el mayor conjunto invariante contenido en 𝐸.

FIGURA 99

 Conclusión: Entonces, toda solución 𝑥(𝑡)con condición inicial en Ω tiende a 𝑀cuando 𝑡 → ∞:

𝑥(𝑡) ⟶ 𝑀 cuando 𝑡 → ∞

La figura muestra una idea intuitiva de como la energía deja de disminuir y se hace cero en la zona plana,
ese sería el conjunto de mayor conjunto invariante.

FIGURA  100

190

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicio 1: Estabilidad por Lyapunov (caso clásico)
Sistema

Punto de equilibrio

Función de Lyapunov candidata

La elección natural:

{

𝑥̇ = −𝑥
𝑦̇ = −𝑦

(𝑥, 𝑦) = (0,0)

𝑉(𝑥, 𝑦) = 𝑥2 + 𝑦2

 Positiva definida,  𝑉(0,0) = 0, 𝑉(𝑥, 𝑦) > 0 si (𝑥, 𝑦) ≠ 0

 Derivada de 𝑉sobre trayectorias

𝑉̇ = 2𝑥𝑥̇ + 2𝑦𝑦̇
𝑉̇ = 2𝑥(−𝑥) + 2𝑦(−𝑦) = −2𝑥2 − 2𝑦2

 Negativa definida

 Conclusión

(0,0) es estable asintoˊ ticamente global

Intuición: toda trayectoria “baja” hacia el mínimo de 𝑉.

Ejercicio 2: Lyapunov con estabilidad (no asintótica)

Sistema

Punto de equilibrio

{

𝑥̇ = −𝑦
𝑦̇ = 𝑥

(0, 0)

191

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Función de Lyapunov

Conclusión

•  𝑉 positiva definida

•  𝑉̇ = 0

𝑉(𝑥, 𝑦) = 𝑥2 + 𝑦2
𝑉̇ = 2𝑥(−𝑦) + 2𝑦(𝑥) = 0

(0,0) es estable pero NO asintoˊ ticamente estable

Interpretación: Trayectorias=curvas de nivel (orbitas cerradas), no hay disipación, sistema conservativo.

Ejercicio 3: LaSalle – estabilidad asintótica

Sistema

𝑥̇ = −𝑥
{
𝑦̇ = −𝑦3

Función de Lyapunov

1
2

1
2

𝑥2 +

𝑦2
𝑉(𝑥, 𝑦) =
𝑉̇ = 𝑥(−𝑥) + 𝑦(−𝑦3) = −𝑥2 − 𝑦4 ≤ 0

No es negativa definida, es negativa semidefinida

Conjunto donde 𝑉̇ = 0

Aplicación de LaSalle

El mayor conjunto invariante dentro de

𝑥 = 0, 𝑦 = 0

{ 𝑉̇ = 0 }

es solo el origen.

Conclusión (LaSalle)

(0,0) es estable asintoˊ ticamente

Clave: aunque 𝑉 ̇ no sea estrictamente negativa, LaSalle completa el argumento.

192

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Ejercicio 4: LaSalle con conjunto invariante no trivial

Sistema

 Lyapunov

Conjunto 𝑉̇ = 0

Análisis del conjunto invariante

Sobre 𝑥 = 0:

Todo el eje 𝑦 es invariante

𝑥̇ = −𝑥
{
𝑦̇ = 0

1
2

𝑥2
𝑉(𝑥, 𝑦) =
𝑉̇ = −𝑥2 ≤ 0

𝑥 = 0 ⇒ {(0, 𝑦): 𝑦 ∈ ℝ}

𝑦̇ = 0 ⇒ 𝑦 = constante

Conclusión:  𝜔(𝑥0, 𝑦0) = (0, 𝑦0)
No converge al origen, converge a una recta invariante

 Ejercicio 5: LaSalle + región invariante

Sistema

Lyapunov

Conjunto 𝑉̇ = 0

𝑥̇ = −𝑥(𝑥2 + 𝑦2)
{
𝑦̇ = −𝑦(𝑥2 + 𝑦2)

𝑉 = 𝑥2 + 𝑦2
𝑉̇ = −2(𝑥2 + 𝑦2)2 ≤ 0

𝑥2 + 𝑦2 = 0 ⇒ (0,0)

193

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Conclusión: (0,0) es estable asintoˊ ticamente global (Todas las trayectorias “caen radialmente”).

En coordenadas polares el sistema sería: 𝑟̇ = −𝑟3, 𝜃̇ = 0

Análisis dinámico radial: 𝑟̇ = −𝑟3 entonces 𝑟 > 0 ⇒ 𝑟̇ < 0, 𝑟 = 0 equilibrio, Solución explícita:

𝑟(𝑡) =

𝑟0
√1 + 2𝑟0

2𝑡

⇒ lim
𝑡→∞

𝑟(𝑡) = 0

Ecuación angular 𝜃(𝑡) = 𝜃0

Las trayectorias son rectas radiales que apuntan al origen.

Interpretación con Lyapunov (LaSalle)
Tomamos: 𝑉 = 𝑟2 ⇒ 𝑉̇ = 2𝑟𝑟̇ = −2𝑟4 ≤ 0

•  𝑉̇ = 0   ⟺   𝑟 = 0
•  El único conjunto invariante es el origen

Conclusión: (0,0) e

s asintticamente estable global

Ejercicio 6:

Sistema

Lyapunov

{

𝑥̇ = −𝑥
𝑦̇ = −𝑥𝑦2

1
2

(𝑥2 + 𝑦2)
𝑉 =
𝑉̇ = −𝑥2 − 𝑥𝑦3 ≤ 0

El conjunto 𝑉̇ = 0contiene el eje 𝑦, pero sobre 𝑥 = 0:

𝑦̇ = 0

 Resultado:

•  No hay atracción al origen
•  El eje 𝑦 es invariante
•  El origen es estable pero no asintóticamente estable

194

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Glosario de términos básicos

A
Atractor:  Conjunto  hacia  el  cual  evolucionan  las  trayectorias  del  sistema  para  un  conjunto  abierto  de
condiciones iniciales.

•  En 2D puede ser: punto fijo, ciclo límite, atractor extraño.
•  Matemáticamente:

lim
𝑡→∞

dist(𝑥(𝑡), 𝐴) = 0.

Autovalor: Escala un autovector en el sistema linealizado:

𝐴𝑣 = 𝜆𝑣.

Determina estabilidad: ℜ(𝜆) < 0: estable, ℜ(𝜆) > 0: inestable, ℜ(𝜆) = 0: caso no hiperbólico

Autovector: Dirección donde el flujo se estira o comprime linealmente.

Si 𝐴𝑣 = 𝜆𝑣, entonces 𝑣es autovector asociado a 𝜆. Define variedades estables/inestable en sillas.

B
Bifurcación:  Cambio  cualitativo  en
Un sistema bifurca cuando:

la  estructura  del  sistema  al  variar  un  parámetro  𝜇 .

∂𝑓
∂𝑥

(𝑥∗, 𝜇) cambia de signo o valor estructural.

Ejemplos: Hopf, saddle-node, transcrítica, pitchfork.

Bifurcación de Hopf: Aparece cuando un par de autovalores complejos cruza el eje imaginario:

𝜆(𝜇) = 𝛼(𝜇) ± 𝑖𝜔, 𝛼(𝜇0) = 0.

Genera un ciclo límite.

C
Campo vectorial: Asociación que asigna un vector a cada punto:

F(𝑥, 𝑦) = (𝑓(𝑥, 𝑦), 𝑔(𝑥, 𝑦)).

Define la dirección del movimiento en cada punto.
Ciclo límite: Órbita cerrada aislada.

•  Estable: las trayectorias cercanas entran.

195

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Inestable: salen.

•
•  Se detecta buscando soluciones periódicas:

𝑥(𝑡 + 𝑇) = 𝑥(𝑡).

D
Diagrama  de  bifurcación:  Muestra  cómo  cambian  los  equilibrios  o  ciclos  con  el  parámetro  𝜇 .
Ejemplo:

𝑥′ = 𝜇𝑥 − 𝑥3.

E
Estado estable (Lyapunov): Un punto 𝑥∗es estable si:

∀𝜖 > 0 ∃𝛿 > 0:  ∥ 𝑥(0) − 𝑥∗ ∥< 𝛿 ⇒∥ 𝑥(𝑡) − 𝑥∗ ∥< 𝜖.

Ecuación diferencial autónoma: No depende explícitamente del tiempo:

𝑥̇ = 𝑓(𝑥).

F
Función de Lyapunov: Una función 𝑉(𝑥) tal que:

•  𝑉(𝑥) > 0excepto en el equilibrio, 𝑉̇ (𝑥) = ∇𝑉 ⋅ 𝑓(𝑥) < 0.

Implica estabilidad.

Flujo: Aplicación que evoluciona estados en el tiempo:

𝜙𝑡(𝑥0) = 𝑥(𝑡).

G
Gradiente (sistema gradiente): Sistemas que derivan de un potencial 𝑈:

𝑥̇ = −∇𝑈(𝑥).

No tienen ciclos límite.

H
Heteroclínica: Conexión entre dos sillas distintas:

lim
𝑡→−∞

𝑥(𝑡) = 𝑝, lim
𝑡→∞

𝑥(𝑡) = 𝑞.

196

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Hipérbolico (punto crítico): Ningún autovalor tiene parte real cero:

Re(𝜆𝑖) ≠ 0.

La clasificación del equilibrio se determina solo por la linealización.

I
Invariante (conjunto invariante): Conjunto 𝑆 tal que

𝑥(0) ∈ 𝑆 ⇒ 𝑥(𝑡) ∈ 𝑆,  ∀𝑡.

Ejemplos: variedades, ciclos límite, órbitas homoclínicas.

Inestabilidad: Ocurre cuando una pequeña perturbación crece:

∥ 𝑥(𝑡) − 𝑥∗ ∥≈ 𝑒𝛼𝑡, 𝛼 > 0.

Integrador numérico: Método para aproximar soluciones: Euler, RK4, Adams-Bashforth, etc.

Isoclina: Curva donde la pendiente del campo vectorial es constante:

𝑑𝑦
𝑑𝑥

= 𝑚.

J
Jacobiano: Matriz de derivadas que linealiza el sistema:

𝐽(𝑥, 𝑦) =

𝜕𝑓
𝜕𝑥
𝜕𝑔
𝜕𝑥

(

𝜕𝑓
𝜕𝑦
𝜕𝑔
𝜕𝑦)

Indispensable para clasificación local.

L
Linealización: Aproximación del sistema cerca del equilibrio:

𝑥̇ = 𝑓(𝑥) ≈ 𝐽(𝑥∗)(𝑥 − 𝑥∗).

Límite superior ω-límite: Conjunto de acumulación hacia 𝑡 → ∞.

M
Manifold / Variedad estable: Conjunto de puntos que convergen al equilibrio:

197

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Manifold inestable

𝑊 𝑠(𝑝) = {𝑥: lim
𝑡→∞

𝜙𝑡(𝑥) = 𝑝}.

𝑊𝑢(𝑝) = {𝑥: lim
𝑡→−∞

𝜙𝑡(𝑥) = 𝑝}.

Dimensión = número de autovalores con parte real negativa.

Manifold central: Asociado a autovalores con parte real cero. Se usa para estudiar bifurcaciones.

N
Nodo: Equilibrio con dos autovalores reales.

•  Si ambos <0: nodo estable.
•  Si ambos >0: nodo inestable.

Solución general:

𝑥(𝑡) = 𝑐1𝑒 𝜆1𝑡𝑣1 + 𝑐2𝑒 𝜆2𝑡𝑣2.

Nulclinas: Curvas donde las derivadas se anulan:

𝑓(𝑥, 𝑦) = 0,

𝑔(𝑥, 𝑦) = 0.

Su intersección da los puntos de equilibrio.

O
Órbita (trayectoria)
El camino seguido por una solución:

Órbita cerrada
Periódica de periodo 𝑇. Un ciclo límite es un tipo especial de órbita cerrada que es aislada.
P
Pendiente de trayectoria

𝛾(𝑡) = 𝜑(𝑡, 𝑥0).

𝑑𝑦
𝑑𝑥

=

𝑔(𝑥, 𝑦)
𝑓(𝑥, 𝑦)

.

Poincaré-Bendixson: En 2D: si la órbita está en un conjunto compacto sin equilibrios, debe haber un ciclo
límite.

R
Retrato  de  fase:  Dibujo  del  flujo  del  sistema  en  el  plano.  Incluye:  nulclinas,  trayectorias,  equilibrios,
variedades.

Resonancia: Cuando las frecuencias naturales satisfacen una relación racional, afectando la dinámica.

198

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

S
Silla (punto silla): Autovalor positivo y uno negativo.
Solución general:

𝑥(𝑡) = 𝑐1𝑒𝜆𝑠𝑡𝑣𝑠 + 𝑐2𝑒 𝜆𝑢𝑡𝑣𝑢.

Sistema conservativo
Conserva una función 𝐻(𝑥, 𝑦):

No puede tener atractores.

𝑑𝐻
𝑑𝑡

= 0.

T
Trayectoria: Solución del sistema para una condición inicial.

Transversalidad: La intersección de variedades es estructuralmente estable si es transversal.

V
Variedad central: Asociada a autovalores con parte real cero. Única forma de estudiar equilibrios no
hiperbólicos.

Variedad estable / inestable: Ya definidas, pero fórmula local importante:

𝑊local

𝑠 = {𝑥 = 𝑐1𝑣𝑠 + ℎ(𝑐1)}.

Bibliografía del glosario

Hirsch, M. W., Smale, S., & Devaney, R. L. (2013). Differential equations, dynamical systems, and an
introduction to chaos (3rd ed.). Academic Press.
Strogatz, S. H. (2015). Nonlinear dynamics and chaos: With applications to physics, biology, chemistry,
and engineering (2nd ed.). Westview Press.
Perko, L. (2013). Differential equations and dynamical systems (3rd ed.). Springer.
Khalil, H. K. (2002). Nonlinear systems (3rd ed.). Prentice Hall.
Wiggins, S. (2003). Introduction to applied nonlinear dynamical systems and chaos (2nd ed.). Springer.
Jordan, D. W., & Smith, P. (2007). Nonlinear ordinary differential equations: An introduction for scientists
and engineers (4th ed.). Oxford University Press.
Guckenheimer, J., & Holmes, P. (1990). Nonlinear oscillations, dynamical systems, and bifurcations of
vector fields. Springer.

Métodos numéricos y teoría de estabilidad
Boyce, W. E., & DiPrima, R. C. (2017). Elementary differential equations and boundary value problems
(11th ed.). Wiley.
Atkinson, K. E. (1989). An introduction to numerical analysis (2nd ed.). Wiley.

199

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Hairer, E., Nørsett, S. P., & Wanner, G. (1993). Solving ordinary differential equations I: Nonstiff problems
(2nd ed.). Springer.
LaSalle, J., & Lefschetz, S. (1961). Stability by Liapunov’s direct method. Academic Press.
Sistemas Hamiltonianos y conservativos
Arnold, V. I. (1989). Mathematical methods of classical mechanics (2nd ed.). Springer.
Goldstein, H., Poole, C., & Safko, J. (2002). Classical mechanics (3rd ed.). Addison-Wesley.

Caos, atractores y teoría moderna
Lorenz, E. N. (1993). The essence of chaos. University of Washington Press.
Ott, E. (2002). Chaos in dynamical systems (2nd ed.). Cambridge University Press.
Sprott, J. C. (2003). Chaos and time-series analysis. Oxford University Press.

Sistemas discretos, mapas y fractales
Devaney, R. L. (2003). An introduction to chaotic dynamical systems (2nd ed.). Westview Press.
Peitgen, H.-O., Jürgens, H., & Saupe, D. (2004). Chaos and fractals: New frontiers of science (2nd ed.).
Springer.

Teoría geométrica y variedades
Guckenheimer, J., & Holmes, P. (1990). Nonlinear oscillations, dynamical systems, and bifurcations of
vector fields. Springer.
Wiggins, S. (1994). Normally hyperbolic invariant manifolds in dynamical systems. Springer.

200

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Prácticas de Laboratorio

1. Crecimiento Logístico

𝑥̇   =  𝑟𝑥(1  −  𝑥/𝐾)

Modelo  fundamental  de crecimiento  poblacional  en  un entorno  con recursos  limitados.  A  diferencia  del
crecimiento exponencial (infinito), aquí la población se frena al acercarse a un techo llamado 'Capacidad
de Carga' (K). Propuesto por Pierre François Verhulst en 1838. Verhulst ajustó el modelo de Malthus (que
predecía una catástrofe por superpoblación) introduciendo el término de autolimitación cuadrática.

APLICACIONES Y EJEMPLOS

1. Cultivo de levaduras o bacterias en una placa de Petri (nutrientes finitos).

2. Adopción de una nueva tecnología (celulares) hasta saturar el mercado.

3. Crecimiento de tumores en etapas tempranas avasculares.

PREGUNTAS INTUITIVAS

1. ¿Qué sucede con la velocidad de crecimiento (𝑑𝑥/𝑑t) cuando x es exactamente la mitad de 𝐾? (Pista: es
el punto de máxima velocidad).

2. Si iniciamos con una población mayor que la capacidad (𝑥  >  𝐾), ¿qué predice la ecuación? ¿Crece o
decrece?

2. SIR Epidemiológico:

𝑆̇   =   −𝛽𝑆𝐼

𝐼̇   =  𝛽𝑆𝐼  − 𝛾𝐼

𝑅̇   =  𝛾𝐼

S: Susceptibles, I: Infectados, R: Recuperados, 𝛽: Tasa de contacto, 𝛾: Tasa de recuperación

Divide  a  la  población  en  tres  compartimentos.  Es  la  base  de  la  epidemiología  moderna.  La  clave  es  el
número  reproductivo básico  R0  = beta/gamma.  Si 𝑅0  >  1,  hay  brote;  si 𝑅0  <  1,  la  enfermedad muere.
Kermack y McKendrick (1927) formularon este sistema para explicar la Gran Plaga de Londres y el cólera en
India.  Demostraron  que  una  epidemia  termina  no  porque  se  acaben  las  personas,  sino  porque  baja  la
densidad de susceptibles (inmunidad de rebaño).

APLICACIONES

1. COVID-19, Gripe estacional, Sarampión.

2. Difusión de rumores o "fake news" en redes sociales (donde 'Recuperado' es alguien que ya no cree o
ignora el rumor).

201

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

3. Marketing viral.

PREGUNTAS INTUITIVAS

1. ¿Por qué la curva de infectados (I) siempre sube y luego baja? ¿Qué condición matemática marca el pico
máximo?

2. Si aumentamos la tasa de recuperación (gamma) mediante mejores medicinas, ¿qué le pasa al pico de
la curva?

3. Lotka–Volterra (Presa-Depredador)

𝑑𝑥/𝑑𝑡  =  𝑎𝑥  −  𝑏𝑥𝑦

𝑑𝑦/𝑑𝑡  =   −𝑐𝑦  +  𝑑𝑥𝑦

𝑥: Presas (Conejos), 𝑦: Depredadores (Zorros), a,c: Tasas naturales, b,d: Interacción

Describe la  dinámica  cíclica  entre  dos  especies  donde  una  se  alimenta  de  la  otra.  Predice  oscilaciones
perpetuas:  muchos  conejos  traen  muchos  zorros  ->  muchos  zorros  comen  demasiados  conejos  ->  los
conejos  bajan  ->  los  zorros  mueren  de hambre  ->  los  conejos  se  recuperan.  Vito  Volterra  (1926)  creó  el
modelo  para  explicar  por  qué,  durante  la  1ª  Guerra  Mundial  (cuando  la  pesca  se  detuvo),  aumentó  el
porcentaje de peces depredadores (tiburones) en el mar Adriático. Alfred Lotka llegó a ecuaciones similares
en química.

GEOMETRÍA

Las trayectorias son órbitas cerradas alrededor de un centro. No hay un atractor simple; la amplitud del
ciclo depende de las condiciones iniciales (memoria del sistema).

PREGUNTAS INTUITIVAS

1. Si cazamos a ambas especies por igual (retiramos un % de 𝑋 y de 𝑌), ¿a quién favorecemos? (Paradoja
de Volterra).

2. ¿Por qué las oscilaciones están desfasadas? (El pico de depredadores siempre ocurre *después* del pico
de presas).

4. Oscilador de Van der Pol:

𝑑𝑥/𝑑𝑡  =  𝑦

𝑑𝑦/𝑑𝑡  =  𝜇(1  −   𝑥2)𝑦  −  𝑥

𝑥: Posición/Voltaje, y: Velocidad/Corriente, 𝜇: Amortiguamiento no lineal

Es  un  oscilador  con  "amortiguamiento  negativo".  Si  la  amplitud  es  pequeña,  el  sistema  inyecta  energía
(crece). Si es grande, disipa energía (frena). Esto crea un **CICLO LÍMITE**: todas las trayectorias convergen
a una órbita específica. Balthasar van der Pol (1920) lo estudió para circuitos de radio con válvulas de vacío.

Aplicaciones modernas:

1. El latido del corazón (nódulo sinusal).

202

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

2. Potenciales de acción en neuronas (modelo FitzHugh-Nagumo simplificado).

3. Vibraciones en estructuras por el viento (puente de Tacoma Narrows, conceptualmente).

PREGUNTAS INTUITIVAS 1. Cambia '𝜇' a 0. ¿En qué se convierte el sistema? (Respuesta: Oscilador
armónico simple).

2. Aumenta 'mu' a 5 o 10. Observa cómo la onda deja de ser senoidal y se vuelve "cuadrada" (oscilaciones
de relajación).

5. Competencia entre Especies:

𝑑𝑥/𝑑𝑡  =  𝑥(3  −  𝑥  −  2𝑦)

𝑑𝑦/𝑑𝑡 =  𝑦(2  −  𝑥  −  𝑦)

𝑥: Especie 1, 𝑦: Especie 2

Dos especies compiten por el mismo recurso (comida, espacio). Dependiendo de los parámetros, pueden
coexistir o una puede llevar a la otra a la extinción (Exclusión Competitiva).

PREGUNTAS INTUITIVAS

1. Observa los puntos de equilibrio en los ejes.

2. ¿Existe un equilibrio donde ambas sobrevivan (𝑥 > 0, 𝑦 > 0)? ¿Es estable o inestable?

3. Prueba diferentes condiciones iniciales: ¿Gana siempre la misma especie o depende de quién empieza
con ventaja?

6. Atractor de Lorenz (Caos):

𝑑𝑥/𝑑𝑡  =  𝜎(𝑦  −  𝑥)

𝑑𝑦/𝑑𝑡  =  𝑥(𝜌  −  𝑧)   −  𝑦

𝑑𝑧/𝑑𝑡  =  𝑥𝑦  −  𝛽𝑧

x: Convección, y: 𝐷𝑖𝑓𝑓. 𝑇𝑒𝑚𝑝 𝐻𝑜𝑟𝑖𝑧, 𝑧: 𝐷𝑖𝑓𝑓. 𝑇𝑒𝑚𝑝 𝑉𝑒𝑟𝑡

El padre de la **Teoría del Caos**. Modelo simplificado de convección atmosférica. Muestra "sensibilidad
a las condiciones iniciales": dos puntos casi idénticos divergen exponencialmente. Edward Lorenz (1963)
descubrió el caos por accidente al redondear decimales en una simulación meteorológica y ver que el clima
predicho cambiaba totalmente. "El aleteo de una mariposa en Brasil puede causar un tornado en Texas".

NOTA DE VISUALIZACIÓN: Este sistema es 3D. El simulador mostrará una proyección 2D (x vs y) o series
temporales. Observa cómo la trayectoria salta de un "ala" a la otra de forma impredecible.

7. Dinámica del Amor (Strogatz):

𝑑𝑅/𝑑𝑡  =  𝑎𝑅  +  𝑏𝐽

𝑑𝐽/𝑑𝑡  =  𝑐𝑅  +  𝑑𝐽

203

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

R: Amor de Romeo, J: Amor de Julieta, a,b,c,d: Coeficientes de reacción

Modelo pedagógico introducido por Steven Strogatz.

𝑑𝑅/𝑑𝑡  =  𝑎𝑅  +  𝑏𝐽.

Si 𝑎  <  0: Romeo es cauto (se enfría si él ama mucho).

Si 𝑏  >  0: Romeo se entusiasma si Julieta lo ama.

Dependiendo de los signos de a,b,c,d, la relación puede ser:

- Un ciclo eterno (amor/odio).

- Fuego explosivo (ambos al infinito).

- Extinción del amor (0,0).

ACTIVIDAD

Juega con los signos de los parámetros para modelar:

- Amantes narcisistas

- Amantes cautelosos

8. Bifurcación Hopf (Supercrítica):

𝑑𝑥/𝑑𝑡  =  𝜇𝑥  −  𝑦  −  𝑥(𝑥2 + 𝑦2)

𝑑𝑦/𝑑𝑡  =  𝑥  +  𝜇𝑦  −  𝑦(𝑥2 + 𝑦2)

𝑥: 𝑅𝑒, 𝑦: 𝐼𝑚, 𝑚𝑢: Parámetro de bifurcación

Describe el nacimiento de un **ciclo límite** a partir de un equilibrio estable.

- Si 𝜇 < 0: El origen (0,0) es un foco estable (espiral hacia adentro).

- Si 𝜇 > 0: El origen se vuelve inestable y nace un ciclo límite estable (círculo).

PREGUNTAS INTUITIVAS

En un simulador, usa un deslizador para variar 'mu'. Pásalo de negativo a positivo lentamente.

¿En qué momento exacto cambia el comportamiento cualitativo del sistema?

9. Circuito RLC (Oscilador Amortiguado):

𝑑𝑉𝑐/𝑑𝑡  =  𝐼 / 𝐶

𝑑𝐼/𝑑𝑡  =   (𝑉_𝑖𝑛  −  𝑉𝑐  −  𝑅𝐼) / 𝐿

𝑉𝑐: Voltaje del Capacitor, I: Corriente del Inductor, 𝑅, 𝐿, 𝐶: Resistencia, Inductancia, Capacitancia

204

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelo  de  segundo  orden  fundamental  en  ingeniería  eléctrica.  Representa  un  circuito  con  Resistencia,
Inductancia  y  Capacitancia.  La  dinámica  depende  del  factor  de  amortiguamiento  (zeta).  Estudiado
extensamente en el siglo XIX y XX, es la base para entender sistemas oscilatorios y de filtrado en electrónica.

GEOMETRÍA

En el plano de fase (𝑉𝑐 𝑣𝑠 𝐼), muestra un foco (oscilador) o un nodo (sobreamortiguado) convergente al
punto de equilibrio 𝑉𝑐  =  𝑉_𝑖𝑛.

PREGUNTAS INTUITIVAS

1. Aumenta R (resistencia). ¿El sistema se vuelve más oscilatorio o amortiguado (lento y sin oscilaciones)?

2. ¿Cuál es el punto de equilibrio del voltaje del capacitor (𝑉𝑐) en estado estacionario? (Pista: 𝑑𝑉𝑐/𝑑𝑡  =  0).

10. Bifurcación Silla-Nodo:

𝑑𝑥/𝑑𝑡  =  𝜇  −   𝑥2

x: Estado, mu: Parámetro de bifurcación

Es la bifurcación más simple donde un par de puntos de equilibrio (uno estable y uno inestable, formando
un "silla-nodo") se crean o se aniquilan.

- Si 𝜇 < 0: No hay equilibrios.

- Si 𝜇 = 0: Los dos equilibrios se unen y desaparecen (el punto de bifurcación).

- Si 𝜇 > 0: Existen dos equilibrios

PREGUNTAS INTUITIVAS

1. En un simulador usa el slider de 𝜇. ¿En qué valor de '𝜇' cambian radicalmente el número de equilibrios?

2. Si empiezas en un punto y luego ajustas 'mu' hasta que los equilibrios desaparecen, ¿qué le sucede a tu
trayectoria?

11. Control de Velocidad (PI):

𝑑𝐸/𝑑𝑡  =  𝑟  −  𝑥

𝑑𝑥/𝑑𝑡  =  𝐾𝑝 ∗ 𝑑𝐸  +  𝐾𝑖 ∗ 𝐸

E: Error Integral, x: Velocidad (Salida), r: Referencia (Setpoint), Kp, Ki: Ganancias P y I

Un modelo de control de sistema simple (primer orden, motor) controlado por un lazo Proporcional-Integral
(PI).

- Kp (Proporcional): Reacciona al error actual.

- Ki (Integral): Elimina el error acumulado a largo plazo.

APLICACIONES

205

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Regulación de velocidad de motores, control de temperatura, control de flujo en procesos químicos. Es la
forma más común de control industrial.

GEOMETRÍA

En el plano (E vs x), el sistema converge al punto donde E=0 (el error es cero) y 𝑥 = 𝑟 (la velocidad alcanzó
la referencia).

PREGUNTAS INTUITIVAS

1. Aumenta Kp. ¿Cómo afecta la velocidad de respuesta y la oscilación inicial (sobreimpulso)?

2. Aumenta Ki. ¿Cómo afecta el tiempo para alcanzar la referencia 'r'?

12. Despegue de Cohete (1D Vertical):

𝐷ℎ/𝑑𝑡  =  𝑣

𝑑𝑣/𝑑𝑡  =   (𝑇  −  𝐷  −  𝑚𝑔) / 𝑚

𝑑𝑚/𝑑𝑡  =   −𝑇 / (𝐼𝑠𝑝  ∗  𝑔)

h: Altura, v: Velocidad, m: Masa de Cohete, T: Empuje (Thrust), D: Arrastre (Drag), Isp: Impulso Específico

Simulación unidimensional (vertical) de la Segunda Ley de Newton para un cohete: Suma de Fuerzas = masa
* aceleración. La masa (m) del cohete disminuye con el tiempo debido al consumo de combustible.

ECUACIÓN DE COHETE (Tsfiolkovsky)

La  ecuación  fundamental  que  rige  esto  es  la  **Ecuación  de  Tsiolkovsky**,  donde  la  aceleración  es
proporcional al empuje y la velocidad de escape.

APLICACIONES

Diseño de perfiles de empuje, cálculo de la delta-V, simulación de etapas de ascensión inicial.

PREGUNTAS INTUITIVAS

1. El término `𝑑𝑚/dt` indica que la masa disminuye. ¿Qué sucede si el Empuje (T) es muy pequeño al inicio?

2. ¿A qué altura se empieza a notar la aceleración exponencial debido a la pérdida de masa?

13. Péndulo Simple Lineal (Conservativo):

𝐷𝑡ℎ𝑒𝑡𝑎/𝑑𝑡  =  𝑜𝑚𝑒𝑔𝑎

𝑑𝑜𝑚𝑒𝑔𝑎/𝑑𝑡  =   −(𝑔/𝐿)   ∗  𝑡ℎ𝑒𝑡𝑎

theta: Ángulo (radianes), omega: Velocidad Angular, g: Gravedad, L: "Longitud de la cuerda

206

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

El  modelo  clásico  para  pequeñas  oscilaciones  (linealizado).  Es  un  **Sistema  Conservativo**,  lo  que
significa que la energía mecánica total (potencial + cinética) se mantiene constante.

GEOMETRÍA

El diagrama de fase (theta vs omega) muestra **órbitas cerradas perfectas (elipses o círculos) ** alrededor
del origen (0,0), que es un **Centro** (equilibrio estable no asintótico).

PREGUNTAS INTUITIVAS

1.  Si  duplicas  la  longitud  (L),  ¿la  frecuencia  de  oscilación  (el  tiempo  que  tarda  en  volver)  aumenta  o
disminuye?

2.  ¿Qué  pasaría  si  agregáramos  un  término  ` − (𝑘/𝑚) ∗ 𝑜𝑚𝑒𝑔𝑎 `  a  ` 𝑑𝑜𝑚𝑒𝑔𝑎 `?  (Pista:  esto  sería  el
amortiguamiento por aire).

14. Potencial de Pozo Doble

𝑑𝑥/𝑑𝑡  =  𝑦

𝑑𝑦/𝑑𝑡  =  𝑥  −   𝑥3

x: Posición, y: Velocidad, d: Amortiguamiento

Describe el movimiento de una partícula en un potencial V(x) =

𝑦2
2

1
 -
2

𝑥2 +

1
4

𝑥4. El sistema tiene dos mínimos

estables y un máximo inestable. Modelado comúnmente en física de materiales y cuántica.

BIESTABILIDAD

El sistema es **Biestable**, con dos equilibrios estables (atractores). El estado final de la partícula depende
de la condición inicial (memoria) y la energía.

GEOMETRÍA

El origen (0,0) es un **punto silla**. Los otros dos equilibrios son **focos o nodos estables**. La trayectoria
puede saltar de un pozo a otro si la energía inicial es suficiente.

PREGUNTAS INTUITIVAS

1. ¿Cuáles son los tres puntos de equilibrio del sistema (d=0)?

2. Si aumentas el amortiguamiento (d), ¿cuál es el comportamiento final de la partícula?

15. Problema de Dos Cuerpos (Órbitas):

𝑑𝑟𝑥/𝑑𝑡  =  𝑣_𝑥

𝑑𝑟𝑦/𝑑𝑡  =  𝑣_𝑦

𝑟_𝑚𝑎𝑔_𝑠𝑞  =  𝑟_𝑥 ∗ 𝑟_𝑥  +  𝑟_𝑦 ∗ 𝑟_𝑦

207

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

𝑑𝑣𝑥/𝑑𝑡  =   −𝐺 ∗ 𝑀 ∗ 𝑟_𝑥 / 𝑟_𝑚𝑎𝑔_𝑠𝑞 ∗∗ 1.5

𝑑𝑣𝑦/𝑑𝑡  =   −𝐺 ∗ 𝑀 ∗ 𝑟_𝑦 / 𝑟_𝑚𝑎𝑔_𝑠𝑞 ∗∗ 1.5

Modelado y Simulación – 3.1.025

𝑟_𝑥, 𝑟_𝑦: Posición del cuerpo 2, 𝑣_𝑥, 𝑣_𝑦: Velocidad del cuerpo 2, G*M: "Parámetro gravitacional

La base de la mecánica celeste. Describe la órbita de un cuerpo pequeño alrededor de uno masivo e inmóvil
(ej.  satélite  alrededor  de  la  Tierra,  o  Tierra  alrededor  del  Sol).  Las  órbitas  resultantes  son  **Cónicas  de
Kepler** (círculos, elipses, parábolas o hipérboles).

LEYES DE KEPLER

1. Órbitas Elípticas.

2. Ley de las Áreas (Conservación del Momento Angular).

3. Relación T² ∝ a³ (Periodo vs Semieje Mayor).

GEOMETRÍA

El plano de fase se representa como el plano de posición (𝑟_𝑥, 𝑟_𝑦).

PREGUNTAS INTUITIVAS

1. Si aumentas la velocidad inicial (𝑣_𝑦), ¿qué le sucede a la órbita?

2. ¿Qué condición inicial debes cumplir para obtener una órbita circular perfecta?

16. Problema Simplificado de Tres Cuerpos:

𝑑1_𝑠𝑞  =   (𝑟_𝑥 + 𝑚𝑢) ∗∗ 2  +  𝑟_𝑦 ∗∗ 2

𝑑2_𝑠𝑞  =   (𝑟_𝑥 − (1 − 𝑚𝑢)) ∗∗ 2  +  𝑟_𝑦 ∗∗ 2

𝑑𝑟𝑥  =  𝑣_𝑥

𝑑𝑟𝑦  =  𝑣_𝑦

𝑑𝑣𝑥  =  2 ∗ 𝑣_𝑦  +  𝑟_𝑥  −   (1 − 𝑚𝑢)(𝑟_𝑥 + 𝑚𝑢)/(𝑑1_𝑠𝑞 ∗∗ 1.5)   −  𝑚𝑢(𝑟_𝑥 − (1 − 𝑚𝑢))/(𝑑2_𝑠𝑞 ∗∗ 1.5)

𝑑𝑣𝑦  =   −2 ∗ 𝑣_𝑥  +  𝑟_𝑦  −   (1 − 𝑚𝑢) ∗ 𝑟_𝑦/(𝑑1_𝑠𝑞 ∗∗ 1.5)   −  𝑚𝑢 ∗ 𝑟_𝑦/(𝑑2_𝑠𝑞 ∗∗ 1.5)

𝑟_𝑥, 𝑟_𝑦: 𝑃𝑜𝑠𝑖𝑐𝑖ó𝑛 𝑑𝑒𝑙 𝑐𝑢𝑒𝑟𝑝𝑜 3, 𝑣_𝑥, 𝑣_𝑦: 𝑉𝑒𝑙𝑜𝑐𝑖𝑑𝑎𝑑 𝑑𝑒𝑙 𝑐𝑢𝑒𝑟𝑝𝑜 3, 𝑚𝑢: 𝑅𝑎𝑡𝑖𝑜 𝑑𝑒 𝑚𝑎𝑠𝑎𝑠 𝑚2/(𝑚1 + 𝑚2)

Modelo Restringido Circular (CRTBP): Dos cuerpos masivos (ej. Tierra y Luna) orbitan en círculo, y un tercer
cuerpo  sin  masa  (ej.  una  sonda)  se  mueve  en  el  mismo  plano.  Las  soluciones  son  generalmente  no
periódicas y extremadamente sensibles a la condición inicial (**caóticas**).

PUNTOS DE LAGRANGE (L1, L2, L3, L4, L5)

El sistema tiene 5 puntos de equilibrio (puntos de Lagrange). Una sonda puede permanecer "estacionaria"
en estos puntos.

208

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

GEOMETRÍA

El  plano  de  fase  se  representa  como  el  plano  de  posición (𝑟_𝑥, 𝑟_𝑦). El  movimiento  es  en  un  marco  de
referencia rotatorio.

PREGUNTAS INTUITIVAS

1. Busca en internet las "órbitas de herradura" o "Lissajous" para ver la complejidad que puede generar este
sistema.

2. ¿Qué tan sensible es el movimiento a pequeños cambios en la velocidad inicial?

NUEVOS MODELOS DE LANCHESTER

17. Combate Lanchester Lineal (Antiguo)

𝑑𝑥/𝑑𝑡  =   −𝑎𝑦,  𝑑𝑦/𝑑𝑡  =   −𝑏𝑥

𝑥: Fuerza X (Azul), 𝑦: "Fuerza Y (Rojo), a: Efectividad de Y, b: Efectividad de 𝑋

CONCEPTO BÁSICO

Modelo  de  Lanchester  de  **Combate  Antiguo**  o  **Guerra  de  Área**.  Asume  que  las  bajas  dependen
linealmente de la fuerza enemiga. Históricamente, se aplica a combates donde las tropas están dispersas
(ej. la Edad Media) o donde las fuerzas no pueden enfocarse.

NOTA CLAVE

Las  bajas que  la  Fuerza 𝑋 (𝑑𝑥/𝑑𝑡)  sufre son proporcionales  a  la  **cantidad**  de  la  Fuerza  Y  (y), no  a  su
propia cantidad. Lo contrario para Y.

PREDICCIÓN

El resultado de la batalla está determinado por la siguiente ecuación de conservación (aunque no se use
directamente  en  el  ODE):  𝑏𝑥2   −  𝑎𝑦2   =  𝐶 .  Es  decir,  las  fuerzas  se  cancelan  en  términos  de  su
**cuadrado**.

PREGUNTAS INTUITIVAS

1. ¿Quién ganaría si ambas fuerzas comienzan iguales (100, 100), pero la efectividad de Y es el doble (a=1.0,
b=0.5)?

2. ¿Cuál es el punto de equilibrio (0,0)? ¿Es estable, inestable, o un punto silla?

18. Combate Lanchester Cuadrático (Moderno):

𝑑𝑥/𝑑𝑡  =   −𝑎𝑥𝑦, 𝑑𝑦/𝑑𝑡  =   −𝑏𝑥𝑦

𝑥: Fuerza 𝑋 (Azul), y: Fuerza 𝑌 (Rojo), a: Efectividad de Y, b: Efectividad de 𝑋

209

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Modelo  de  Lanchester  de  **Combate  Moderno**  o  **Guerra  Concentrada**.  Asume  que  las  bajas  son
proporcionales a la **multiplicación** de las fuerzas. Se aplica a combates modernos donde el fuego es
concentrado (ej. armas de largo alcance) y la fuerza puede enfocarse en el enemigo.

NOTA CLAVE: El poder de la fuerza dominante crece exponencialmente. Una ventaja pequeña en fuerza se
traduce en una ventaja decisiva en el resultado.

LEY CUADRÁTICA

El resultado de la batalla está determinado por la Ley Cuadrática de Lanchester, donde la cantidad de bajas
es proporcional al **cuadrado de la fuerza** que queda.

PREGUNTAS INTUITIVAS

1. ¿Quién ganaría si ambas fuerzas comienzan iguales (100, 100), pero la efectividad de Y es el doble (a=1.0,
b=0.5)? Compara con el caso lineal.

2. ¿El resultado se ve afectado por el tiempo de simulación, o solo por la condición inicial y los parámetros?

MODELOS DE DINÁMICAS BIOLÓGICAS

19. Feromonas de Hormigas (Estación de Atractores):

𝑑𝑥/𝑑𝑡  =  𝑎𝑥(1  −  𝑥/𝐾)   −  𝑏𝑥𝑦,  𝑑𝑦/𝑑𝑡  =  𝑐𝑥𝑦  −  𝑑𝑦2

x: Hormigas en el Nido, y: Feromona en Camino, a, K: Logístico, b, c: Interacción, d: Disipación

Modelo  simplificado  de  la  dinámica  de  la  colonia  y  la  traza  de  feromonas.  Las  hormigas  siguen  una
feromona (Y), pero la feromona se disipa (término -d𝑦2) y el crecimiento de la colonia (𝑋) es logístico (𝑎(1 −
𝑥/𝐾)).

ATRACCIÓN COLECTIVA

El término **cxy** representa el fenómeno de que cuantas más hormigas (𝑋) y más feromona (𝑌) haya, más
feromona se deposita, reforzando el camino.

FENÓMENO

Este  sistema  puede  exhibir  **biestabilidad  o  ciclos  límite**,  representando  períodos  de  alta  actividad
(mucha feromona, muchas hormigas fuera) seguidos de períodos de descanso o extinción de la traza.

PREGUNTAS INTUITIVAS

1. Si aumentamos la disipación (d), ¿el nivel de feromona en estado estacionario aumenta o disminuye?

2. Si la colonia es pequeña (𝐾 = 2), ¿existe una probabilidad de que la traza de feromona (𝑌) desaparezca
completamente?

210

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

BIBLIOGRAFÍA DE MODELOS

Differential equations and dynamical systems
Hirsch, M. W., Smale, S., & Devaney, R. L. (2013). Differential equations and dynamical systems. Springer.
Elements of applied bifurcation theory
Kuznetsov, Y. A. (2004). Elements of applied bifurcation theory. Springer.
Nonlinear dynamics and chaos
Strogatz, S. H. (2015). Nonlinear dynamics and chaos. Westview Press.
Ordinary differential equations
Teschl, G. (2012). Ordinary differential equations. American Mathematical Society.
Modelo logístico y crecimiento poblacional
Mathematical biology I
Murray, J. D. (2002). Mathematical biology I. Springer.
An essay on the principle of population
Malthus, T. (1798). An essay on the principle of population.
Notice sur la loi que la population suit dans son accroissement
Verhulst, P. F. (1838). Notice sur la loi que la population suit dans son accroissement.
Epidemiología matemática (modelo SIR)
Mathematical epidemiology
Brauer, F., & Castillo-Chávez, C. (2012). Mathematical epidemiology. Springer.
A contribution to the mathematical theory of epidemics
Kermack, W. O., & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics.
Presa–depredador (Lotka–Volterra)
Elements of physical biology
Lotka, A. J. (s. f.). Elements of physical biology.
Fluctuations in the abundance of a species
Volterra, V. (1926). Fluctuations in the abundance of a species.
Dynamic models in biology
Ellner, S., & Guckenheimer, J. (s. f.). Dynamic models in biology. Princeton University Press.
Oscilador de Van der Pol
On relaxation oscillations
Van der Pol, B. (s. f.). On relaxation oscillations.
Nonlinear oscillations
Andronov, A. A., et al. (s. f.). Nonlinear oscillations. Pergamon Press.
Caos y atractor de Lorenz
Deterministic nonperiodic flow
Lorenz, E. N. (s. f.). Deterministic nonperiodic flow. Journal of the Atmospheric Sciences.
Chaos: Making a New Science
Gleick, J. (s. f.). Chaos: Making a new science.
Control PI y sistemas de ingeniería
Modern control engineering
Ogata, K. (s. f.). Modern control engineering. Pearson.

211

FUNDAMENTOS TEÓRICOS
Docente: Ing. Omar J. Cáceres

Modelado y Simulación – 3.1.025

Feedback control of dynamic systems
Franklin, G. F., Powell, J. D., & Emami-Naeini, A. (s. f.). Feedback control of dynamic systems.
Circuito RLC
Engineering circuit analysis
Hayt, W. H., Kemmerly, J. E., & Durbin, S. M. (s. f.). Engineering circuit analysis. McGraw-Hill.
Mecánica celeste (dos y tres cuerpos)
An introduction to celestial mechanics
Szebehely, V. (s. f.). An introduction to celestial mechanics.
Solar system dynamics
Murray, C. D., & Dermott, S. F. (s. f.). Solar system dynamics.
Guerra y modelos de Lanchester
Aircraft in warfare: The dawn of the fourth arm
Lanchester, F. W. (1916). Aircraft in warfare: The dawn of the fourth arm.
Mathematical models of warfare
Taylor, J. G. (s. f.). Mathematical models of warfare.
Dinámica biestable, potenciales y física
Stochastic processes in physics and chemistry
Van Kampen, N. G. (s. f.). Stochastic processes in physics and chemistry.
Pattern formation and dynamics in nonequilibrium systems
Cross, M. C., & Hohenberg, P. C. (s. f.). Pattern formation and dynamics in nonequilibrium systems.
Dinámica del amor (Strogatz)
Love affairs and differential equations
Strogatz, S. H. (s. f.). Love affairs and differential equations.
Cohetes y ecuación de Tsiolkovsky
Rocket motion in a resisting medium
Tsiolkovsky, K. (1903). Rocket motion in a resisting medium.
Rocket propulsion elements
Sutton, G. P. (s. f.). Rocket propulsion elements.

212

