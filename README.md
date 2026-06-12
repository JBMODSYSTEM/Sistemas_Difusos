# Reporte: Funciones de Pertenencia Difusa

## Objetivo
Diseñar clases en Python que representen distintos tipos de funciones de pertenencia difusa y permitan evaluar el grado de pertenencia de valores de entrada.

## Tipos de funciones de pertenencia
El programa implementa ocho funciones de pertenencia: triangular, trapezoidal, gaussiana, campana generalizada, sigmoidal, S, Z y Pi.

---

## 1. Función Triangular
La clase `FuncionPertenenciaTriangular` modela una función triangular, una de las formas más usadas en lógica difusa por su simplicidad.

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

### Ejemplo de uso
```python
fp1_tri = FuncionPertenenciaTriangular(0, 5, 10)
fp2_tri = FuncionPertenenciaTriangular(5, 10, 15)
```

---

## 2. Función Trapezoidal
La clase `FuncionPertenenciaTrapezoidal` modela una función trapezoidal con una zona central de pertenencia total.

### Atributos utilizados
- `a`: inicio de la activación.
- `b`: comienzo de la zona de pertenencia total.
- `c`: final de la zona de pertenencia total.
- `d`: fin de la activación.

### Método principal
- `evaluar(x)`: recibe un valor de entrada y devuelve su grado de pertenencia en el intervalo `[0, 1]`.

### Fórmula matemática

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

### Ejemplo de uso
```python
fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)
```

---

## 3. Función Gaussiana
La clase `FuncionPertenenciaGaussiana` modela una función gaussiana con forma de campana suave.

### Atributos utilizados
- `c`: centro de la campana gaussiana.
- `sigma`: desviación estándar que controla el ancho de la campana.

### Fórmula matemática

$$
\mu_{\text{gaussiana}}(x) = e^{-\frac{1}{2}\left(\frac{x-c}{\sigma}\right)^2}
$$

### Ejemplo de uso
```python
fp_gauss = FuncionPertenenciaGaussiana(10, 2)
```

---

## 4. Función de Campana Generalizada
La clase `FuncionPertenenciaCampanaGeneralizada` modela una campana más flexible que la gaussiana.

### Atributos utilizados
- `a`: parámetro que controla la pendiente.
- `b`: centro de la campana.
- `c`: parámetro que controla el ancho de la campana.

### Fórmula matemática

$$
\mu_{\text{campana}}(x) = \frac{1}{1 + \left|\frac{x-b}{a}\right|^{2c}}
$$

### Ejemplo de uso
```python
fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)
```

---

## 5. Función Sigmoidal
La clase `FuncionPertenenciaSigmoidal` modela una función sigmoidal útil para transiciones suaves y no simétricas.

### Atributos utilizados
- `a`: controla la pendiente.
- `c`: punto de inflexión.

### Fórmula matemática

$$
\mu_{\text{sigmoidal}}(x) = \frac{1}{1 + e^{-a(x-c)}}
$$

### Ejemplo de uso
```python
fp_sigmoidal = FuncionPertenenciaSigmoidal(1, 10)
```

---

## 6. Función S
La clase `FuncionPertenencia_S` representa una transición monótona que crece de 0 a 1 en el intervalo `[a, b]`.

### Atributos utilizados
- `a`: inicio de la subida.
- `b`: fin de la subida.

### Fórmula matemática

$$
\mu_{\text{S}}(x) =
\begin{cases}
0, & x \le a \\
2\left(\frac{x-a}{b-a}\right)^2, & a < x \le \frac{a+b}{2} \\
1 - 2\left(\frac{x-b}{b-a}\right)^2, & \frac{a+b}{2} < x < b \\
1, & x \ge b
\end{cases}
$$

### Ejemplo de uso
```python
fp_S = FuncionPertenencia_S(0, 10)
```

---

## 7. Función Z
La clase `FuncionPertenencia_Z` es el espejo inverso de la función S.

### Atributos utilizados
- `a`: inicio de la caída.
- `b`: fin de la caída.

### Fórmula matemática

$$
\mu_{\text{Z}}(x) =
\begin{cases}
1, & x \le a \\
1 - 2\left(\frac{x-a}{b-a}\right)^2, & a < x \le \frac{a+b}{2} \\
2\left(\frac{x-b}{b-a}\right)^2, & \frac{a+b}{2} < x < b \\
0, & x \ge b
\end{cases}
$$

### Ejemplo de uso
```python
fp_Z = FuncionPertenencia_Z(0, 10)
```

---

## 8. Función Pi
La clase `FuncionPertenenciaPi` combina una subida S y una bajada Z para formar una función con una región central de pertenencia alta.

### Atributos utilizados
- `a`, `b`, `c`, `d`: definen los puntos de transición.

### Fórmula matemática

$$
\mu_{\text{Pi}}(x) =
\begin{cases}
0, & x \le a \\
2\left(\frac{x-a}{b-a}\right)^2, & a < x \le \frac{a+b}{2} \\
1 - 2\left(\frac{x-b}{b-a}\right)^2, & \frac{a+b}{2} < x \le b \\
1, & b \le x \le c \\
1 - 2\left(\frac{x-c}{d-c}\right)^2, & c < x \le \frac{c+d}{2} \\
2\left(\frac{x-d}{d-c}\right)^2, & \frac{c+d}{2} < x < d \\
0, & x \ge d
\end{cases}
$$

### Ejemplo de uso
```python
fp_Pi = FuncionPertenenciaPi(0, 5, 10, 15)
```

---

## Objetos creados en el programa
En el programa principal se crean estas instancias:
- `fp1_tri = FuncionPertenenciaTriangular(0, 5, 10)`
- `fp2_tri = FuncionPertenenciaTriangular(5, 10, 15)`
- `fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)`
- `fp_gauss = FuncionPertenenciaGaussiana(10, 2)`
- `fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)`
- `fp_sigmoidal = FuncionPertenenciaSigmoidal(1, 10)`
- `fp_S = FuncionPertenencia_S(0, 10)`
- `fp_Z = FuncionPertenencia_Z(0, 10)`
- `fp_Pi = FuncionPertenenciaPi(0, 5, 10, 15)`

## Ejecución
Para probar el programa, ejecuta `main.py` y escribe valores separados por coma cuando se soliciten.

## Conclusión
Este proyecto permite comparar distintas formas matemáticas para modelar pertenencia parcial en lógica difusa. Cada función tiene características propias y se adapta mejor a distintos problemas de control o análisis.
