# Reporte: Sistema Difuso de Propinas

## Objetivo
El proyecto recomienda una propina a partir de la calidad de la comida y del servicio.

En el estado actual del código, el flujo activo usa solo funciones de pertenencia triangular y trapezoidal.

---

## Qué hace `main.py`

`main.py` define las funciones que convierten valores nítidos en grados difusos.

### Funciones activas
- `FuncionPertenenciaTriangular`
- `FuncionPertenenciaTrapezoidal`
- `fuzzificar_valor_triangular(...)`
- `fuzzificar_valor_trapezoidal(...)`
- `fuzzificar_comida_servicio_triangular(...)`
- `fuzzificar_comida_servicio_trapezoidal(...)`

### Configuraciones activas
- `CONFIGURACION_TRIANGULAR_COMIDA`
- `CONFIGURACION_TRIANGULAR_SERVICIO`
- `CONFIGURACION_TRAPEZOIDAL_COMIDA`
- `CONFIGURACION_TRAPEZOIDAL_SERVICIO`

Su tarea es producir diccionarios de grados de pertenencia para comida y servicio. Esos diccionarios son los que usa `defuzzification.py`.

---

## Qué hace `defuzzification.py`

`defuzzification.py` contiene la inferencia y la defuzzificación.

### Estructura
- Define etiquetas lingüísticas de comida y servicio.
- Define las 25 reglas difusas del sistema.
- Agrupa las reglas por salida: `nada`, `poca`, `regular`, `buena` y `excelente`.
- Evalúa cada grupo con producto entre antecedentes.
- Convierte la salida difusa en un valor nítido con promedio ponderado.

### Flujo actual
1. `main.py` calcula los grados triangulares.
2. `main.py` calcula los grados trapezoidales.
3. `defuzzification.py` une ambos con `unir_grados_por_maximo(...)`.
4. `Defuzzification.evaluar_reglas(...)` calcula la activación de cada salida.
5. `Defuzzification.defuzzificar_por_promedio_ponderado(...)` calcula la propina final.
6. Se imprime un único resultado en consola.

### Resultado actual
La consola muestra solo un resultado final, el de la unión triangular + trapezoidal.

---

## Qué está sucediendo dentro del código

El proyecto no compara sistemas distintos. Lo que hace es combinar dos lecturas de la misma entrada:

- triangular genera una versión difusa con forma de triángulo.
- trapezoidal genera otra versión difusa con forma de trapecio.
- ambas se fusionan por máximo para conservar el grado más alto por etiqueta.
- luego se evalúan las 25 reglas difusas.
- finalmente se obtiene una propina nítida.

Eso significa que la salida mostrada por consola sale de la unión triangular + trapezoidal, no de una sola función por separado.

---

## Qué ya no forma parte del flujo activo

- campana generalizada
- gráfica ajustada anterior
- gaussiana
- sigmoidal
- S
- Z
- Pi
- salidas comparativas múltiples

---

## Ejecución

```bash
python defuzzification.py
```

La salida esperada es un solo bloque con los grados de activación y el valor nítido final de la propina recomendada.

---

## Conclusión

El código actual sí está alineado con su intención vigente: fuzzificar con triangular y trapezoidal, unir ambos resultados, evaluar reglas difusas y obtener una sola propina recomendada.