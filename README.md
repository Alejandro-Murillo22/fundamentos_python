# Fundamentos de Python: Variables, Operadores y Manipulacion de Cadenas

Este repositorio contiene las soluciones a los laboratorios de las Secciones 1 a 4 de la guía de Fundamentos de Python, junto con la documentación y resolución paso a paso de los Ejercicios de Operadores Matemáticos.

## Datos del proyecto

* **Lenguaje:** Python 3
* **Entorno de desarrollo:** Visual Studio Code

---

## Estructura del repositorio

El código está organizado en carpetas según la sección correspondiente de la guía:

```text
fundamentos_python/
│
├── README.md
└── src/
    ├── seccion1/
    │   ├── S1.py
    │   ├── S2.py
    │   └── S3.py
    ├── seccion2/
    │   └── S1.py
    ├── seccion3/
    │   ├── S1.py
    └── seccion4/
        ├── Algoritmos.py
        ├── S1.py
        ├── S2.py
        └── S3.py
Documentación de Ejercicios de Operadores Matemáticos
A continuación se detalla la evaluación manual y la explicación paso a paso de las expresiones matemáticas propuestas.

Ejercicio 1
Expresión: 5 + 3 * 2

Resultado: 11

¿Por qué?: La multiplicación (3 * 2 = 6) tiene mayor prioridad que la suma, por lo que se realiza primero: 5 + 6 = 11.

Ejercicio 2
Expresión: 8 / 2 + 4 * 3

Resultado: 16.0

¿Por qué?: La división y la multiplicación se ejecutan de izquierda a derecha (8 / 2 = 4.0 y 4 * 3 = 12) antes de sumar. La división / en Python siempre retorna un float, dando 4.0 + 12 = 16.0.

Ejercicio 3
Expresión: (7 + 3) * 2 - 5

Resultado: 15

¿Por qué?: El paréntesis tiene la máxima prioridad (7 + 3 = 10), luego se multiplica (10 * 2 = 20) y finalmente se resta 5.

Ejercicio 4
Expresión: 10 - 4 + 2 * 3

Resultado: 12

¿Por qué?: Primero se calcula la multiplicación (2 * 3 = 6). Luego, la resta y la suma se evalúan de izquierda a derecha: 10 - 4 = 6, y 6 + 6 = 12.

Ejercicio 5
Expresión: (10 / 2) * (3 + 2) - 4

Resultado: 21.0

¿Por qué?: Se resuelven primero ambos paréntesis (10 / 2 = 5.0 y 3 + 2 = 5). Se multiplican sus resultados (5.0 * 5 = 25.0) y se resta 4.

Ejercicio 6
Expresión: 2 + 3 * (4 - 1)

Resultado: 11

¿Por qué?: Primero el paréntesis (4 - 1 = 3), luego la multiplicación (3 * 3 = 9) y al final la suma con 2.

Ejercicio 7
Expresión: 5 * 2 ** 3

Resultado: 40

¿Por qué?: La exponenciación (**) tiene mayor prioridad que la multiplicación: 2 ** 3 = 8, y luego 5 * 8 = 40.

Ejercicio 8
Expresión: 6 + 4 / 2 ** 2

Resultado: 7.0

¿Por qué?: Primero la potencia (2 ** 2 = 4), luego la división (4 / 4 = 1.0), y finalmente la suma (6 + 1.0 = 7.0).

Ejercicio 9
Expresión: 10 % 3 + 2 * 5

Resultado: 11

¿Por qué?: El módulo y la multiplicación van primero de izquierda a derecha: 10 % 3 = 1 (residuo de la división) y 2 * 5 = 10. Al sumar da 1 + 10 = 11.

Ejercicio 10
Expresión: (8 + 2) * 3 ** 2

Resultado: 90

¿Por qué?: Primero el paréntesis (8 + 2 = 10), luego la potencia (3 ** 2 = 9), y finalmente la multiplicación (10 * 9 = 90).

Ejercicio 11
Expresión: 7 + 2 * (3 + 5) / 4

Resultado: 11.0

¿Por qué?: Se resuelve el paréntesis (3 + 5 = 8), luego multiplicación y división de izquierda a derecha (2 * 8 = 16, 16 / 4 = 4.0), y al final la suma con 7.

Ejercicio 12
Expresión: 2 ** 3 * 4 / 2

Resultado: 16.0

¿Por qué?: Primero la potencia (2 ** 3 = 8). Luego la multiplicación y división de izquierda a derecha: 8 * 4 = 32, y 32 / 2 = 16.0.

Ejercicio 13
Expresión: 9 - 6 + 3 ** 2

Resultado: 12

¿Por qué?: Primero la potencia (3 ** 2 = 9). Luego resta y suma de izquierda a derecha: 9 - 6 = 3, y 3 + 9 = 12.

Ejercicio 14
Expresión: (7 - 2) * 5 + 3 ** 2

Resultado: 34

¿Por qué?: Se calcula el paréntesis (7 - 2 = 5) y la potencia (3 ** 2 = 9). Luego se multiplica (5 * 5 = 25) y se suma 9.

Ejercicio 15
Expresión: 4 * 2 ** 3 / 8 + 1

Resultado: 5.0

¿Por qué?: Primero la potencia (2 ** 3 = 8). Luego multiplicación y división de izquierda a derecha (4 * 8 = 32, 32 / 8 = 4.0), y finalmente se le suma 1.

Ejecución de los scripts
Para clonar el repositorio y probar cualquiera de los programas en tu máquina local, sigue estos pasos desde la terminal:

### 1. Clonar e ingresar al proyecto
```bash
# Clonar el repositorio
git clone [https://github.com/TU_USUARIO/fundamentos_python.git](https://github.com/TU_USUARIO/fundamentos_python.git)

# Entrar a la carpeta del proyecto
cd fundamentos_python => cd src y en esta carpeta ejecuta cualquier script que quieras probar