# Delfín

## Documentación de `defuzzification.py`

Este documento explica la clase principal `Defuzzification` y el sistema difuso que implementa para recomendar una propina a partir de dos entradas:

- calidad de la comida
- calidad del servicio

El propósito del módulo es aplicar reglas difusas, agrupar la activación de las salidas y convertir ese resultado en un valor numérico final o `crisp`.

---

## 1. Tecnologías y enfoque

### Lenguaje
- Python

### Técnica utilizada
- Lógica difusa
- Inferencia por reglas
- Agregación por máximo (`max`)
- Antecedentes evaluados con producto
- Defuzzificación por promedio ponderado

### Idea general
El sistema no responde con valores absolutos de sí o no. Trabaja con grados de pertenencia entre `0.0` y `1.0`, lo que permite una recomendación más realista y gradual.

---

## 2. Qué resuelve el software

El sistema responde a esta pregunta:

> ¿Qué propina se recomienda según la calidad de la comida y del servicio?

Las salidas posibles son:

- `nada`
- `poca`
- `regular`
- `buena`
- `excelente`

Cada una se activa con un grupo específico de reglas.

---

## 3. Estructura de datos del módulo

### Entradas lingüísticas

#### Calidad de la comida
- `mmc` = muy mala comida
- `mc` = mala comida
- `rc` = regular comida
- `bc` = buena comida
- `mbc` = muy buena comida

#### Calidad del servicio
- `mms` = muy mal servicio
- `ms` = mal servicio
- `rs` = regular servicio
- `bs` = buen servicio
- `mbs` = muy buen servicio

### Salidas lingüísticas
- `n` = nada
- `p` = poca
- `r` = regular
- `b` = buena
- `e` = excelente

---

## 4. Clase principal

La clase principal del sistema es `Defuzzification`.

### Responsabilidad de la clase
Encapsula toda la lógica del sistema difuso:

1. consulta de la tabla de propinas
2. evaluación de reglas
3. agrupación por salida
4. defuzzificación por promedio ponderado
5. impresión de resultados

### Constructor
#### `__init__(self, valores_salida=None)`
Inicializa la clase con los valores numéricos de salida.

Si no se recibe un diccionario personalizado, la clase usa `VALORES_SALIDA`.

---

## 5. Constantes del archivo

### `REGLAS_NADA`
Agrupa las reglas que activan la salida `nada`.

### `REGLAS_POCA`
Agrupa las reglas que activan la salida `poca`.

### `REGLAS_REGULAR`
Agrupa las reglas que activan la salida `regular`.

### `REGLAS_BUENA`
Agrupa las reglas que activan la salida `buena`.

### `REGLAS_EXCELENTE`
Agrupa las reglas que activan la salida `excelente`.

### `REGLAS_POR_SALIDA`
Diccionario que organiza todas las reglas por clase de salida.

### `TABLA_PROPINAS`
Tabla que relaciona cada combinación de comida y servicio con la etiqueta de propina correspondiente.

### `VALORES_SALIDA`
Diccionario con los valores numéricos usados para defuzzificar:

- `nada` = `0.0`
- `poca` = `2.5`
- `regular` = `5.0`
- `buena` = `7.5`
- `excelente` = `10.0`

---

## 6. Métodos de `Defuzzification`

### `obtener_propina(calidad_comida, calidad_servicio)`
Devuelve la etiqueta de propina asociada a una combinación concreta de comida y servicio.

#### Ejemplo
```python
defuzz = Defuzzification()
defuzz.obtener_propina("mc", "bs")
```

Resultado:
```python
"p"
```

---

### `evaluar_regla(comida, servicio, grados_comida, grados_servicio)`
Calcula la activación de una regla difusa individual.

#### Fórmula usada
$$
fuerza = \mu_{comida} \times \mu_{servicio}
$$

Esto significa que la regla se activa más cuando ambos antecedentes tienen grados altos.

---

### `evaluar_grupo_reglas(reglas, grados_comida, grados_servicio)`
Evalúa todas las reglas de un grupo y devuelve la mayor activación del grupo.

#### Proceso
1. Recorre cada regla del grupo.
2. Calcula su fuerza con producto.
3. Conserva la activación más alta con `max()`.

---

### `evaluar_reglas(grados_comida, grados_servicio)`
Evalúa los cinco grupos de reglas y devuelve un diccionario con la activación final de cada salida.

#### Estructura devuelta
```python
{
    "nada": 0.4,
    "poca": 0.7,
    "regular": 0.2,
    "buena": 0.1,
    "excelente": 0.0,
}
```

---

### `defuzzificar_por_promedio_ponderado(grados, valores_salida=None)`
Convierte el resultado difuso en un valor numérico final.

#### Fórmula
$$
crisp = \frac{\sum(valor\_salida_i \times grado_i)}{\sum grado_i}
$$

#### Interpretación
- `valor_salida_i` es el valor numérico de cada propina.
- `grado_i` es la activación de esa propina.
- El numerador suma los productos.
- El denominador suma las activaciones totales.

Si no hay activaciones, retorna `0.0` para evitar división entre cero.

---

### `inferir_y_defuzzificar(grados_comida, grados_servicio, valores_salida=None)`
Integra todo el flujo de cálculo.

#### Hace tres cosas
1. Evalúa las reglas.
2. Agrupa las activaciones por salida.
3. Calcula el valor nítido final.

#### Devuelve
- `resultados_reglas`
- `nitido`

---

### `imprimir_resultados(resultados_reglas, valor_nitido)`
Imprime en consola los grados de activación y el valor nítido final.

---

## 7. Funciones de compatibilidad

Además de la clase, el archivo mantiene funciones de nivel módulo para no romper usos anteriores:

- `obtener_propina(...)`
- `evaluar_regla(...)`
- `evaluar_grupo_reglas(...)`
- `evaluar_reglas(...)`
- `defuzzificar_por_promedio_ponderado(...)`
- `inferir_y_defuzzificar(...)`
- `imprimir_resultados(...)`

También existe el alias `defuzzification = Defuzzification` para facilitar referencias externas.

---

## 8. Flujo de ejecución

Cuando se ejecuta `defuzzification.py`, el proceso es el siguiente:

1. Se crea una instancia de `Defuzzification`.
2. Se definen grados de pertenencia para comida y servicio.
3. Se evalúan las reglas.
4. Se agrupan por salida difusa.
5. Se aplica defuzzificación por promedio ponderado.
6. Se imprimen los resultados.

---

## 9. Ejemplo de uso

El archivo incluye este ejemplo al final:

```python
grados_comida = {"mmc": 0.1, "mc": 0.5, "rc": 0.8, "bc": 0.3, "mbc": 0.1}
grados_servicio = {"mms": 0.1, "ms": 0.4, "rs": 0.7, "bs": 0.5, "mbs": 0.2}

resultados_reglas, valor_nitido = Defuzzification().inferir_y_defuzzificar(grados_comida, grados_servicio)
Defuzzification.imprimir_resultados(resultados_reglas, valor_nitido)
```

---

## 10. Qué significa `crisp`

`crisp` o valor nítido es el número final que sale del proceso de defuzzificación.

En este proyecto representa la propina recomendada en una escala numérica.

---

## 11. Resumen final

`defuzzification.py` implementa un sistema difuso para propinas usando:

- 25 reglas agrupadas por salida
- producto para evaluar antecedentes
- máximo para agregar reglas de una misma salida
- promedio ponderado para obtener el valor final

La clase `Defuzzification` concentra toda la lógica principal y hace que el módulo sea más claro, reutilizable y fácil de extender.

---

## 12. Cambios recientes (integración de fuzzificación por campana)

Se añadieron mejoras para permitir un flujo extremo a extremo desde entradas nítidas hasta la propina defuzzificada:

- Se creó en `main.py` una implementación reutilizable de campanas generalizadas y helpers:
    - `FuncionPertenenciaCampanaGeneralizada(a, b, c)` — función de pertenencia en forma de campana.
    - `fuzzificar_valor_campana(valor, configuracion)` — genera los grados de pertenencia para una etiqueta.
    - `fuzzificar_comida_servicio(valor_comida, valor_servicio)` — fuzzifica ambas entradas usando configuraciones base.

- En `defuzzification.py` se agregó:
    - Import de `fuzzificar_comida_servicio` desde `main.py`.
    - Método `inferir_y_defuzzificar_desde_entradas(valor_comida, valor_servicio, ...)` que fuzzifica
        las entradas nítidas y luego ejecuta la inferencia y la defuzzificación existentes.

- Se mantiene la API previa (métodos y funciones de compatibilidad), por lo que el cambio es retrocompatible.

## 13. Actualización del código

La relación entre `main.py` y `defuzzification.py` quedó organizada de esta forma:

### `main.py`
- Contiene las clases de funciones de pertenencia.
- Define las configuraciones para comida y servicio.
- Convierte valores nítidos en grados difusos.
- Soporta tres estilos de fuzzificación para este proyecto:
    - campana generalizada
    - triangular
    - trapezoidal
- También incluye la versión ajustada a la gráfica dibujada a mano, con hombros en los extremos y triángulos en el centro.

### `defuzzification.py`
- Recibe los grados generados por `main.py`.
- Evalúa las 25 reglas difusas.
- Agrupa el resultado por salida de propina.
- Calcula un valor final nítido usando promedio ponderado.
- Imprime un único resultado por consola cuando se unen triangular y trapezoidal por máximo.

### Qué pasa al ejecutar el programa
1. Se definen `valor_comida` y `valor_servicio`.
2. `main.py` los transforma en grados de pertenencia.
3. `defuzzification.py` une triangular y trapezoidal, aplica las reglas difusas y calcula el valor nítido final.
4. La consola muestra un solo bloque con el resultado final.

Esto hace visible cómo cambia la recomendación final al unir las dos formas de pertenencia principales.

### Ejecución y verificación

Puedes ejecutar el flujo integrado con:

```bash
python defuzzification.py
```

Salida de ejemplo verificada durante la integración:

```
Grados de activación para cada etiqueta de propina:
    nada: 0.0151
    poca: 0.1569
    regular: 0.9407
    buena: 0.3820
    excelente: 0.0391
Valor nítido de la propina recomendada: 5.4451
```

