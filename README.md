# Reporte: Funciones de Pertenencia Difusa

## Objetivo
Diseñar clases en Python que representen diferentes tipos de funciones de pertenencia difusa y permita evaluar el grado de pertenencia de distintos valores de entrada.

## Tipos de funciones de pertenencia
El programa implementa cuatro tipos diferentes de funciones de pertenencia, cada una con características y aplicaciones distintas.

---

## 1. Función Triangular
La clase `FuncionPertenenciaTriangular` modela una función triangular, que es una de las formas más usadas en lógica difusa por su simplicidad y facilidad de interpretación.

### Atributos utilizados
- `a`: punto donde inicia la activación de la función.
- `b`: punto de máxima pertenencia.
- `c`: punto donde termina la activación de la función.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

### Fórmula matemática

$$
\mu_{\text{triangular}}(x) =
\begin{cases}
0, & x \le a \\
\frac{x-a}{b-a}, & a < x \le b \\
\frac{c-x}{c-b}, & b < x < c \\
0, & x \ge c
\end{cases}
$$

### Ventajas
- Sencilla de implementar.
- Bajo costo computacional.
- Fácil de interpretar.
- Adecuada para aplicaciones educativas y de control básico.

### Ejemplo de uso
```python
fp1 = FuncionPertenenciaTriangular(0, 5, 10)
fp2 = FuncionPertenenciaTriangular(5, 10, 15)
```

---

## 2. Función Trapezoidal
La clase `FuncionPertenenciaTrapezoidal` modela una función trapezoidal. A diferencia de la triangular, posee una región central donde la pertenencia es constantemente igual a 1.

### Atributos utilizados
- `a`: inicio de la activación.
- `b`: comienzo de la zona de pertenencia total.
- `c`: final de la zona de pertenencia total.
- `d`: fin de la activación.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

## Fórmula implementada
La función trapezoidal usa la siguiente expresión:

$$
\mu_{\text{trapezoidal}}(x) =
\begin{cases}
0, & x \le a \\
\frac{x-a}{b-a}, & a < x \le b \\
1, & b < x < c \\
\frac{d-x}{d-c}, & c \le x < d \\
0, & x \ge d
\end{cases}
$$

### Ventajas
- Representa zonas de pertenencia total constantes durante un intervalo.
- Es sencilla de implementar.
- Se utiliza mucho en controladores difusos tipo Mamdani.

### Ejemplo de uso
```python
fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)
```

---

## 3. Función Gaussiana
La clase `FuncionPertenenciaGaussiana` modela una función gaussiana, que tiene forma de campana suave.

### Atributos utilizados
- `c`: centro de la campana gaussiana.
- `sigma`: desviación estándar que controla el ancho de la campana.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

### Fórmula matemática

$$
\mu_{\text{gaussiana}}(x) = e^{-\frac{1}{2}\left(\frac{x-c}{\sigma}\right)^2}
$$

### Ventajas
- Suavidad: transición gradual sin cambios abruptos.
- Natural: similar a muchos fenómenos físicos.
- Eficiente en cálculos de sistemas difusos avanzados.

### Ejemplo de uso
```python
fp_gauss = FuncionPertenenciaGaussiana(10, 2)
```

---

## 4. Función de Campana Generalizada
La clase `FuncionPertenenciaCampanaGeneralizada` modela una función de campana generalizada, que permite mayor flexibilidad en la forma de la campana.

### Atributos utilizados
- `a`: parámetro que controla la pendiente de la campana.
- `b`: centro de la campana.
- `c`: parámetro que controla el ancho de la campana.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

### Fórmula matemática

$$
\mu_{\text{campana}}(x) = \frac{1}{1 + \left|\frac{x-b}{a}\right|^{2c}}
$$

### Ventajas
- Gran flexibilidad en la forma de la campana.
- Permite ajustar la suavidad mediante los parámetros.
- Muy utilizada en controladores difusos avanzados.

### Ejemplo de uso
```python
fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)
```

---

## Objetos creados en el programa
En el programa principal se crean las siguientes instancias:
- `fp1 = FuncionPertenenciaTriangular(0, 5, 10)`
- `fp2 = FuncionPertenenciaTriangular(5, 10, 15)`
- `fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)`
- `fp_gauss = FuncionPertenenciaGaussiana(10, 2)`
- `fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)`

## Uso del programa
Al ejecutar `main.py`, el programa solicita valores de entrada por consola. Puedes escribir varios números separados por comas, por ejemplo:

```text
0, 1.5, 3, 6, 9, 12
```

Si presionas Enter sin escribir nada, el programa usa un conjunto de valores de ejemplo.

El programa evaluará todos los valores ingresados en cada una de las cinco funciones de pertenencia creadas.

---

## Resultados de ejecución
Se ejecutó el programa con el siguiente rango de datos:

**Rango de datos:** `0, 2.5, 5, 7.5, 10, 12.5, 15`

### Resultados obtenidos

#### Función Triangular fp1 (a=0, b=5, c=10):
| x | Pertenencia |
|---|---|
| 0.0 | 0.00 |
| 2.5 | 0.50 |
| 5.0 | 1.00 |
| 7.5 | 0.50 |
| 10.0 | 0.00 |
| 12.5 | 0.00 |
| 15.0 | 0.00 |

#### Función Triangular fp2 (a=5, b=10, c=15):
| x | Pertenencia |
|---|---|
| 0.0 | 0.00 |
| 2.5 | 0.00 |
| 5.0 | 0.00 |
| 7.5 | 0.50 |
| 10.0 | 1.00 |
| 12.5 | 0.50 |
| 15.0 | 0.00 |

#### Función Trapezoidal fp_trap (a=0, b=5, c=10, d=15):
| x | Pertenencia |
|---|---|
| 0.0 | 0.00 |
| 2.5 | 0.50 |
| 5.0 | 1.00 |
| 7.5 | 1.00 |
| 10.0 | 1.00 |
| 12.5 | 0.50 |
| 15.0 | 0.00 |

#### Función Gaussiana fp_gauss (c=10, sigma=2):
| x | Pertenencia |
|---|---|
| 0.0 | 0.00 |
| 2.5 | 0.00 |
| 5.0 | 0.04 |
| 7.5 | 0.46 |
| 10.0 | 1.00 |
| 12.5 | 0.46 |
| 15.0 | 0.04 |

#### Función Campana Generalizada fp_campana (a=5, b=10, c=2):
| x | Pertenencia |
|---|---|
| 0.0 | 0.06 |
| 2.5 | 0.16 |
| 5.0 | 0.50 |
| 7.5 | 0.94 |
| 10.0 | 1.00 |
| 12.5 | 0.94 |
| 15.0 | 0.50 |

### Análisis de resultados
- Las funciones triangulares (fp1 y fp2) muestran transiciones lineales con máxima pertenencia en sus puntos centrales (5 y 10 respectivamente).
- La función trapezoidal (fp_trap) mantiene pertenencia total (1.0) en el intervalo [5, 10], mostrando la característica distintiva de esta forma.
- La función gaussiana (fp_gauss) presenta una transición suave con máximo en x=10 y decrece gradualmente en ambas direcciones.
- La función de campana generalizada (fp_campana) tiene el máximo en x=10 y muestra transiciones más suaves y simétricas que la gaussiana.

## Conclusión
Este proyecto implementa cuatro tipos diferentes de funciones de pertenencia, permitiendo comparar cómo distintas formas matemáticas representan el concepto de pertenencia parcial en lógica difusa. Cada función tiene características particulares que la hacen más adecuada para diferentes aplicaciones:

- **Triangular**: Educativa, simple y eficiente.
- **Trapezoidal**: Ideal para representar zonas de pertenencia total.
- **Gaussiana**: Suave, natural y con transiciones graduales.
- **Campana generalizada**: Flexible y adaptable a diferentes formas.

El programa permite evaluar todos estos tipos simultáneamente sobre los mismos valores de entrada, facilitando la comparación y el aprendizaje sobre funciones de pertenencia difusas.