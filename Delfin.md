# Delfín

## Documentación técnica del estado actual

El proyecto implementa un sistema difuso para propinas con dos entradas:

- calidad de la comida
- calidad del servicio

En el estado actual del código, el flujo activo usa solo funciones triangular y trapezoidal.

---

## `main.py`

`main.py` contiene las funciones que transforman valores nítidos en grados difusos.

### Qué define
- `FuncionPertenenciaTriangular`
- `FuncionPertenenciaTrapezoidal`

### Qué configura
- `CONFIGURACION_TRIANGULAR_COMIDA`
- `CONFIGURACION_TRIANGULAR_SERVICIO`
- `CONFIGURACION_TRAPEZOIDAL_COMIDA`
- `CONFIGURACION_TRAPEZOIDAL_SERVICIO`

### Qué hace
Toma un valor de entrada y devuelve un diccionario con los grados de pertenencia para cada etiqueta lingüística. Ese resultado es el que después consume `defuzzification.py`.

### Funciones activas
- `fuzzificar_valor_triangular(...)`
- `fuzzificar_valor_trapezoidal(...)`
- `fuzzificar_comida_servicio_triangular(...)`
- `fuzzificar_comida_servicio_trapezoidal(...)`

---

## `defuzzification.py`

`defuzzification.py` contiene la inferencia y la defuzzificación.

### Qué define
- etiquetas de comida y servicio
- etiquetas de salida de propina
- las 25 reglas difusas agrupadas por salida
- la clase `Defuzzification`

### Qué hace la clase `Defuzzification`
1. Evalúa cada grupo de reglas.
2. Calcula la activación de cada regla con producto entre los grados de antecedente.
3. Agrupa la activación por salida usando el máximo.
4. Convierte la salida difusa en un valor nítido con promedio ponderado.

### Flujo actual del programa
1. `main.py` calcula grados triangulares.
2. `main.py` calcula grados trapezoidales.
3. `defuzzification.py` une ambos conjuntos por máximo con `unir_grados_por_maximo(...)`.
4. `Defuzzification.evaluar_reglas(...)` calcula la activación de las cinco salidas.
5. `Defuzzification.defuzzificar_por_promedio_ponderado(...)` obtiene un único valor nítido.
6. Se imprime un solo resultado final.

---

## Qué está pasando dentro del código

El proyecto no compara dos sistemas distintos: combina dos formas de fuzzificar la misma entrada.

- La parte triangular genera una interpretación difusa con triángulos.
- La parte trapezoidal genera otra interpretación difusa con trapecios.
- Luego ambas se fusionan por máximo para conservar el grado más alto por etiqueta.
- Después se evalúan las reglas difusas del problema de propinas.
- Por último, se calcula una propina final nítida.

Eso significa que la salida mostrada por consola sale de la unión de triangular y trapezoidal aplicada antes de la inferencia.

---

## Lo que ya no forma parte del flujo activo

- campana generalizada
- gráfica ajustada anterior
- gaussiana
- sigmoidal
- S
- Z
- Pi
- salidas comparativas múltiples

---

## Resultado esperado

Al ejecutar `defuzzification.py`, la consola muestra un solo bloque con:

- los grados de activación de `nada`, `poca`, `regular`, `buena` y `excelente`
- el valor nítido final de la propina recomendada

Ese es el comportamiento real del proyecto en su estado actual.