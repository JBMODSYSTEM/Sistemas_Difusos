# Reporte: Función de Pertenencia Difusa

## Objetivo
Diseñar una clase en Python que represente una función de pertenencia difusa y permita evaluar el grado de pertenencia de distintos valores de entrada.

## Diseño de la clase
La clase `FuncionPertenencia` modela una función triangular, que es una de las formas más usadas en lógica difusa por su simplicidad y facilidad de interpretación.

### Atributos utilizados
- `a`: punto donde inicia la activación de la función.
- `b`: punto de máxima pertenencia.
- `c`: punto donde termina la activación de la función.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

## Fórmula implementada
La clase usa la siguiente función triangular:

$$
\mu_A(x) =
\begin{cases}
0, & x \le a \\
\frac{x-a}{b-a}, & a < x \le b \\
\frac{c-x}{c-b}, & b < x < c \\
0, & x \ge c
\end{cases}
$$

## Objetos creados
En el programa se crean dos instancias:
- `fp1 = FuncionPertenencia(0, 5, 10)`
- `fp2 = FuncionPertenencia(5, 10, 15)`

Cada objeto representa un conjunto difuso triangular distinto, por lo que un mismo valor puede tener diferentes grados de pertenencia en cada uno.

## Diferencias observadas
- `fp1` tiene su máximo en `x = 5` y cubre el intervalo aproximado de `0` a `10`.
- `fp2` tiene su máximo en `x = 10` y cubre el intervalo aproximado de `5` a `15`.
- Los valores cercanos al centro de cada triángulo tienen mayor grado de pertenencia.
- Los valores fuera del intervalo de activación tienen pertenencia `0`.

## Uso del programa
Al ejecutar `main.py`, el programa solicita valores de entrada por consola. Puedes escribir varios números separados por comas, por ejemplo:

```text
0, 1.5, 3, 6, 9, 12
```

Si presionas Enter sin escribir nada, el programa usa un conjunto de valores de ejemplo.

## Conclusión
La función triangular es adecuada para aplicaciones educativas y de control básico porque transforma fácilmente valores numéricos en grados lingüísticos. En este caso, permite representar de forma clara el concepto de pertenencia parcial en lógica difusa.

## Función trapezoidal
Además de la función triangular, el programa incluye una función trapezoidal representada por la clase `FuncionPertenenciaTrapezoidal`.

### Atributos utilizados
- `a`: inicio de la activación.
- `b`: comienzo de la zona de pertenencia total.
- `c`: final de la zona de pertenencia total.
- `d`: fin de la activación.

### Fórmula implementada
La función trapezoidal usa la siguiente expresión:

$$
\mu_A(x) =
\begin{cases}
0, & x \le a \\
\frac{x-a}{b-a}, & a < x \le b \\
1, & b < x < c \\
\frac{d-x}{d-c}, & c \le x < d \\
0, & x \ge d
\end{cases}
$$

### Ejemplo creado
- `fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)`

### Ventajas
- Representa zonas de pertenencia total constantes durante un intervalo.
- Es sencilla de implementar.
- Se utiliza mucho en controladores difusos tipo Mamdani.