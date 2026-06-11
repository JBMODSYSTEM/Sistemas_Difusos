import math
# Este programa define dos clases para representar funciones de pertenencia: una triangular y otra trapezoidal.

''' 
La clase FuncionPertenenciaTriangular tiene un método evaluar que calcula el grado de 
pertenencia de un valor x según la forma triangular definida por los puntos a, b y c. 
'''
class FuncionPertenenciaTriangular:
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

# Función para mostrar los resultados de evaluación de la función de pertenencia para un conjunto de valores.
def mostrar_resultados(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")

'''
La clase FuncionPertenenciaTrapezoidal tiene un método evaluar que calcula el grado de 
pertenencia de un valor x según la forma trapezoidal definida por los puntos a, b, c y d.
'''
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


def mostrar_resultados_trapezoidal(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}, d={funcion.d}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


class FuncionPertenenciaGaussiana:
	"""Representa una función de pertenencia gaussiana."""

	def __init__(self, c, sigma):
		# c es el centro de la campana y sigma controla su ancho.
		self.c = c
		self.sigma = sigma

	def evaluar(self, x):
		# Implementa la función gaussiana usando la fórmula estándar.
		return math.exp(-0.5 * ((x - self.c) / self.sigma) ** 2)
	

def mostrar_resultados_gaussiana(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (c={funcion.c}, sigma={funcion.sigma}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


class FuncionPertenenciaCampanaGeneralizada:
	"""Representa una función de pertenencia de campana generalizada."""

	def __init__(self, a, b, c):
		# a controla la pendiente, b es el centro y c controla el ancho de la campana.
		self.a = a
		self.b = b
		self.c = c

	def evaluar(self, x):
		# Implementa la función de campana generalizada usando la fórmula estándar.
		return 1 / (1 + abs((x - self.b) / self.a) ** (2 * self.c))
	

def mostrar_resultados_campana(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


class FuncionPertenenciaSigmoidal:
	"""Representando una función de pertenencia sigmoidal."""
	
	def __init__(self, a, c):
		# a controla la pendiente y c es el punto de inflexión de la función sigmoidal.
		self.a = a
		self.c = c

	def evaluar(self, x):
		# Implementa la función sigmoidal usando la fórmula estándar.
		return 1 / (1 + math.exp(-self.a * (x - self.c)))


def mostrar_resultados_sigmoidal(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, c={funcion.c}):")
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
	# Se crean instancias de cada tipo de función de pertenencia con parámetros específicos, se obtienen los valores del usuario
	fp1_tri = FuncionPertenenciaTriangular(0, 5, 10)
	fp2_tri = FuncionPertenenciaTriangular(5, 10, 15)
	fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)
	fp_gauss = FuncionPertenenciaGaussiana(10, 2)
	fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)
	fp_sigmoidal = FuncionPertenenciaSigmoidal(1, 10)
	valores = obtener_valores_usuario()

	# Se muestran los resultados de evaluación de cada función de pertenencia para los valores ingresados por el usuario.
	mostrar_resultados(fp1_tri, "fp1_tri", valores)
	mostrar_resultados(fp2_tri, "fp2_tri", valores)
	mostrar_resultados_trapezoidal(fp_trap, "fp_trap", valores)
	mostrar_resultados_gaussiana(fp_gauss, "fp_gauss", valores)
	mostrar_resultados_campana(fp_campana, "fp_campana", valores)
	mostrar_resultados_sigmoidal(fp_sigmoidal, "fp_sigmoidal", valores)
