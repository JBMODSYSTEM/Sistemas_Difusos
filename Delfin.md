# Delfín

## Documentación de `defuzzification.py`

En este archivo documento el sistema difuso usado para calcular la propina recomendada a partir de dos entradas:

- `calidad_comida`
- `calidad_servicio`

El objetivo de este módulo es aplicar reglas difusas, agrupar la activación de cada salida y convertir ese resultado difuso en un valor numérico final, también llamado `crisp` o valor nítido.

---

## 1. Tecnologías y enfoque utilizado

### Lenguaje
- Python

### El enfoque metodológico
- Lógica difusa
- Inferencia por reglas tipo Mamdani simplificada
- Agregación por máximo (`max`)
- Evaluación de antecedentes mediante producto
- Defuzzificación por promedio ponderado

### La idea general
El programa no trabaja con respuestas binarias de sí o no. En su lugar, asigna grados de pertenencia entre `0.0` y `1.0` a cada etiqueta difusa y luego combina esos grados para obtener una propina final más realista.

---

## 2. Qué problema resuelve

COn este sistema buscamos responder a la pregunta:

> ¿Qué propina se recomienda según la calidad de la comida y del servicio?

Para eso usamos cinco posibles salidas difusas:

- `nada`
- `poca`
- `regular`
- `buena`
- `excelente`

Cada salida se activa con distintas reglas según la combinación de comida y servicio.

---

## 3. Variables lingüísticas del sistema

### Entradas

#### Calidad de la comida
Representada en el código por las etiquetas:

- `mmc` = muy mala comida
- `mc` = mala comida
- `rc` = regular comida
- `bc` = buena comida
- `mbc` = muy buena comida

#### Calidad del servicio
Representada por:

- `mms` = muy mal servicio
- `ms` = mal servicio
- `rs` = regular servicio
- `bs` = buen servicio
- `mbs` = muy buen servicio

### Salidas

#### Propinas
Representadas por:

- `n` = nada
- `p` = poca
- `r` = regular
- `b` = buena
- `e` = excelente

---

## 4. Estructura general del archivo

El archivo `defuzzification.py` lo organicé de esta manera:

1. Definición de las reglas difusas.
2. Tabla de propinas para consultar combinaciones directas.
3. Valores numéricos de salida para defuzzificación.
4. Funciones de evaluación de reglas.
5. Función de defuzzificación por promedio ponderado.
6. Función principal de inferencia.
7. Impresión de resultados en consola.

---

## 5. Reglas difusas

Este sistema contiene 25 reglas en total, agrupadas por la salida que producen.

### 5.1 Reglas para `nada`
- `R1 = mmc * mms`
- `R2 = mmc * ms`
- `R3 = mc * mms`
- `R4 = mc * ms`
- `R5 = rc * mms`
- `R6 = rc * ms`

### 5.2 Reglas para `poca`
- `R7 = mmc * rs`
- `R8 = mmc * bs`
- `R9 = mmc * mbs`
- `R10 = mc * rs`
- `R11 = mc * bs`
- `R12 = rc * rs`
- `R13 = bc * mms`
- `R14 = bc * ms`
- `R15 = mbc * mms`

### 5.3 Reglas para `regular`
- `R16 = mc * mbs`
- `R17 = rc * bs`
- `R18 = rc * mbs`
- `R19 = bc * rs`
- `R20 = bc * bs`
- `R21 = mbc * ms`
- `R22 = mbc * rs`

### 5.4 Reglas para `buena`
- `R23 = bc * mbs`
- `R24 = mbc * bs`

### 5.5 Reglas para `excelente`
- `R25 = mbc * mbs`

---

## 6. Tabla de propinas

La tabla `TABLA_PROPINAS` guarda la salida lingüística resultante de cada combinación de comida y servicio.

| Comida \ Servicio | mms | ms | rs | bs | mbs |
|---|---|---|---|---|---|
| mmc | n | n | p | p | p |
| mc  | n | n | p | p | r |
| rc  | n | n | p | r | r |
| bc  | p | p | r | r | b |
| mbc | p | r | r | b | e |

Con esta tabla se resume la lógica del sistema y permite analizar rápidamente qué salida se asocia a cada combinación.

---

## 7. Valores de salida para defuzzificación

Ya que la defuzzificación necesita convertir cada etiqueta lingüística en un valor numérico. Utilizamos `VALORES_SALIDA` con este fin y quedá de la siguiente manera.

- `nada` = `0.0`
- `poca` = `2.5`
- `regular` = `5.0`
- `buena` = `7.5`
- `excelente` = `10.0`

Estos valores funcionan como puntos representativos de cada etiqueta.

---

## 8. Métodos y funciones del archivo

### `obtener_propina(calidad_comida, calidad_servicio)`
Devuelve la etiqueta de propina que corresponde a una combinación específica de comida y servicio.

#### Ejemplo
```python
obtener_propina("mc", "bs")
```
Resultado:
```python
"p"
```

---

### `evaluar_regla(comida, servicio, grados_comida, grados_servicio)`
Calcula la fuerza de una regla difusa.

#### Lógica usada
En esta implementación se multiplica el grado de pertenencia de la comida por el grado de pertenencia del servicio:

$$
\text{fuerza} = \mu_{comida} \times \mu_{servicio}
$$

Significa que mientras más altos sean ambos valores, mayor será la activación de la regla.

---

### `evaluar_grupo_reglas(reglas, grados_comida, grados_servicio)`
Evalúa un grupo de reglas y devuelve la activación máxima de ese grupo.

#### Método usado
- Recorre todas las reglas del grupo.
- Calcula la fuerza de cada una.
- Devuelve el valor más alto con `max()`.

Debido a que después de evaluar todas las reglas que producen una misma salida nos interesa conservar la activación más fuerte.

---

### `evaluar_reglas(grados_comida, grados_servicio)`
Agrupamos las 25 reglas por salida y  nos devuelve un diccionario con la activación de cada propina.

#### Resultado esperado
Devuelve una estructura como esta:

```python
{
    "nada": 0.4,
    "poca": 0.7,
    "regular": 0.2,
    "buena": 0.1,
    "excelente": 0.0,
}
```

Cada clave corresponde a una salida difusa y cada valor es su grado de activación.

---

### `defuzzificar_por_promedio_ponderado(agregados, valores_salida=None)`
Convierte la salida difusa en un valor nítido usando promedio ponderado.

#### Fórmula
$$
crisp = \frac{\sum (valor\_salida_i \times grado_i)}{\sum grado_i}
$$

#### Explicación
- `valor_salida_i` es el valor numérico de cada etiqueta difusa.
- `grado_i` es el grado de activación de esa etiqueta.
- El numerador suma los productos entre ambos.
- El denominador suma todos los grados activados.

Si el denominador es `0.0`, la función devuelve `0.0` para evitar división entre cero.

---

### `inferir_y_defuzzificar(grados_comida, grados_servicio, valores_salida=None)`
Es la función principal del módulo.

#### Hace tres pasos:
1. Evalúa las reglas.
2. Agrupa los resultados por salida.
3. Defuzzifica para obtener el valor nítido final.

#### Devuelve
- `resultados_reglas`: activación de `nada`, `poca`, `regular`, `buena` y `excelente`
- `nitido`: valor final recomendado de propina

---

### `imprimir_resultados(resultados_reglas, nitido)`
Muestra en consola los grados de activación de cada salida y el valor nítido final.

Esta función sirve para ver el resultado de la inferencia de forma clara y entendible.

---

## 9. Flujo de ejecución del programa

Cuando se ejecuta `defuzzification.py`, el proceso es el siguiente:

1. Se definen grados de pertenencia para comida y servicio.
2. Se evalúan las 25 reglas.
3. Se agrupan las reglas por salida difusa.
4. Se aplica defuzzificación por promedio ponderado.
5. Se imprime el resultado final.

---

## 10. Ejemplo de uso

Incluimos un ejemplo directo al final:

```python
grados_comida = {"mmc": 0.1, "mc": 0.5, "rc": 0.8, "bc": 0.3, "mbc": 0.1}
grados_servicio = {"mms": 0.1, "ms": 0.4, "rs": 0.7, "bs": 0.5, "mbs": 0.2}
```

Luego se llama a:

```python
resultados_reglas, nitido = inferir_y_defuzzificar(grados_comida, grados_servicio)
```

Y finalmente se imprime:

```python
imprimir_resultados(resultados_reglas, nitido)
```

---

## 11. Qué significa `crisp`

`crisp` o valor nítido es el resultado final de la defuzzificación.

En otras palabras:
- antes del proceso, el sistema maneja etiquetas difusas como `nada`, `poca` o `buena`
- después del proceso, el sistema devuelve un número concreto que puede interpretarse como la propina recomendada

---

## 12. Resumen corto

Este módulo implementa un sistema difuso para calcular propinas usando:

- 25 reglas difusas
- agrupación por salida con `max`
- evaluación de antecedentes con producto
- defuzzificación por promedio ponderado

El resultado final es una propina numérica fácil de interpretar.
