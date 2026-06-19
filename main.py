"""Funciones de pertenencia del proyecto: triangular y trapezoidal."""

class FuncionPertenenciaTriangular:
	"""Representa una función de pertenencia triangular."""

	def __init__(self, a, b, c):
		# a, b y c definen los tres puntos de la función triangular.
		self.a = a
		self.b = b
		self.c = c

	def evaluar(self, x):
		if x <= self.a:
			return 0.0
		if self.a < x <= self.b:
			return (x - self.a) / (self.b - self.a)
		if self.b < x < self.c:
			return (self.c - x) / (self.c - self.b)
		return 0.0

def mostrar_resultados(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}, c={funcion.c}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")

class FuncionPertenenciaTrapezoidal:
	"""Representa una función de pertenencia trapezoidal."""

	def __init__(self, a, b, c, d):
		# a, b, c y d definen los cuatro puntos de la función trapezoidal.
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def evaluar(self, x):
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
# Configuraciones base para fuzzificar comida y servicio con funciones triangulares.
CONFIGURACION_TRIANGULAR_COMIDA = {
	"mmc": (0.0, 1.25, 2.5),
	"mc": (0.0, 2.5, 5.0),
	"rc": (2.5, 5.0, 7.5),
	"bc": (5.0, 7.5, 10.0),
	"mbc": (7.5, 8.75, 10.0),
}

CONFIGURACION_TRIANGULAR_SERVICIO = {
	"mms": (0.0, 1.25, 2.5),
	"ms": (0.0, 2.5, 5.0),
	"rs": (2.5, 5.0, 7.5),
	"bs": (5.0, 7.5, 10.0),
	"mbs": (7.5, 8.75, 10.0),
}

# Configuraciones base para fuzzificar comida y servicio con funciones trapezoidales.
CONFIGURACION_TRAPEZOIDAL_COMIDA = {
	"mmc": (0.0, 0.5, 1.5, 2.5),
	"mc": (1.0, 2.0, 3.5, 5.0),
	"rc": (3.0, 4.0, 6.0, 7.5),
	"bc": (5.5, 6.5, 8.0, 9.0),
	"mbc": (7.5, 8.5, 9.5, 10.0),
}

CONFIGURACION_TRAPEZOIDAL_SERVICIO = {
	"mms": (0.0, 0.5, 1.5, 2.5),
	"ms": (1.0, 2.0, 3.5, 5.0),
	"rs": (3.0, 4.0, 6.0, 7.5),
	"bs": (5.5, 6.5, 8.0, 9.0),
	"mbs": (7.5, 8.5, 9.5, 10.0),
}


def fuzzificar_valor_con_funcion(valor, configuracion, clase_funcion):
	"""Convierte un valor nítido en grados de pertenencia usando una clase de función dada.

	Es el punto común para triangular y trapezoidal.
	"""

	grados = {}
	for etiqueta, parametros in configuracion.items():
		funcion = clase_funcion(*parametros)
		grados[etiqueta] = funcion.evaluar(valor)
	return grados


def fuzzificar_valor_triangular(valor, configuracion):
	"""Convierte un valor nítido en grados de pertenencia usando triángulos."""

	return fuzzificar_valor_con_funcion(valor, configuracion, FuncionPertenenciaTriangular)


def fuzzificar_valor_trapezoidal(valor, configuracion):
	"""Convierte un valor nítido en grados de pertenencia usando trapecios."""

	return fuzzificar_valor_con_funcion(valor, configuracion, FuncionPertenenciaTrapezoidal)


def fuzzificar_comida_servicio_triangular(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio usando funciones triangulares.

	Los diccionarios resultantes se usan como base para la inferencia.
	"""

	grados_comida = fuzzificar_valor_triangular(valor_comida, CONFIGURACION_TRIANGULAR_COMIDA)
	grados_servicio = fuzzificar_valor_triangular(valor_servicio, CONFIGURACION_TRIANGULAR_SERVICIO)
	return grados_comida, grados_servicio


def fuzzificar_comida_servicio_trapezoidal(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio usando funciones trapezoidales.

	Los diccionarios resultantes se usan como base para la inferencia.
	"""

	grados_comida = fuzzificar_valor_trapezoidal(valor_comida, CONFIGURACION_TRAPEZOIDAL_COMIDA)
	grados_servicio = fuzzificar_valor_trapezoidal(valor_servicio, CONFIGURACION_TRAPEZOIDAL_SERVICIO)
	return grados_comida, grados_servicio
