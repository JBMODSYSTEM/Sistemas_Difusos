class FuncionPertenencia:
	"""Representa una función de pertenencia triangular."""

	def __init__(self, a, b, c):
		# a, b y c definen los tres puntos de la función triangular.
		self.a = a
		self.b = b
		self.c = c

	def evaluar(self, x):
		# Implementando la función triangular de la formula en Función triangular.
		if x <= self.a:
			return 0.0
		if self.a < x <= self.b:
			return (x - self.a) / (self.b - self.a)
		if self.b < x < self.c:
			return (self.c - x) / (self.c - self.b)
		return 0.0


class FuncionPertenenciaTrapezoidal:
	"""Representa una función de pertenencia trapezoidal."""

	def __init__(self, a, b, c, d):
		# a, b, c y d definen los cuatro puntos de la función trapezoidal.
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def evaluar(self, x):
		# Implementa la función trapezoidal por tramos.
		if x <= self.a:
			return 0.0
		if self.a < x <= self.b:
			return (x - self.a) / (self.b - self.a)
		if self.b < x < self.c:
			return 1.0
		if self.c <= x < self.d:
			return (self.d - x) / (self.d - self.c)
		return 0.0

# Función para mostrar los resultados de evaluación de la función de pertenencia para un conjunto de valores.
def mostrar_resultados(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


def mostrar_resultados_trapezoidal(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}, d={funcion.d}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


def obtener_valores_usuario():
	# Permite ingresar varios valores separados por coma, ademas si no se ingresa nada, se usan valores por defecto.
	entrada = input("Ingresa valores de entrada separados por coma (por ejemplo: 0, 2.5, 5, 7.5): ").strip()
	if not entrada:
		return [0, 2.5, 5, 7.5, 10, 12.5, 15]
	
	# Procesa la entrada del usuario, convirtiendo cada valor a float y almacenándolos en una lista.
	valores = []
	for parte in entrada.split(","):
		texto = parte.strip()
		if texto:
			valores.append(float(texto))
	return valores


if __name__ == "__main__":
	# Se crean dos objetos con parámetros distintos para comparar su comportamiento.
	fp1 = FuncionPertenencia(0, 5, 10)
	fp2 = FuncionPertenencia(5, 10, 15)
	fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)

	valores = obtener_valores_usuario()

	mostrar_resultados(fp1, "fp1", valores)
	mostrar_resultados(fp2, "fp2", valores)
	mostrar_resultados_trapezoidal(fp_trap, "fp_trap", valores)

