import math
# Este archivo define las funciones de pertenencia que luego consume defuzzification.py.
# La idea es convertir valores nítidos de comida y servicio en grados difusos para que,
# después, defuzzification.py evalúe las reglas y calcule la propina final.

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

# Función auxiliar para ver en consola cómo responde una función de pertenencia.
# Sirve para comprobar las formas que luego se reutilizan en defuzzification.py.
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


'''La clase FuncionPertenenciaGaussiana tiene un método evaluar que calcula el grado de 
pertenencia de un valor x según la forma gaussiana definida por el centro c y el ancho sigma.'''

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


# Configuraciones base para fuzzificar comida y servicio con campanas generalizadas.
# Esta variante se mantiene como referencia educativa y comparativa.
CONFIGURACION_CAMPANA_COMIDA = {
	"mmc": (2.0, 0.0, 2.0),
	"mc": (2.0, 2.5, 2.0),
	"rc": (2.0, 5.0, 2.0),
	"bc": (2.0, 7.5, 2.0),
	"mbc": (2.0, 10.0, 2.0),
}

CONFIGURACION_CAMPANA_SERVICIO = {
	"mms": (2.0, 0.0, 2.0),
	"ms": (2.0, 2.5, 2.0),
	"rs": (2.0, 5.0, 2.0),
	"bs": (2.0, 7.5, 2.0),
	"mbs": (2.0, 10.0, 2.0),
}


# Configuraciones base para fuzzificar comida y servicio con funciones triangulares.
# defuzzification.py usa estos grados cuando se requiere comparar o combinar
# el comportamiento triangular con el trapezoidal.
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
# En conjunto con la configuración triangular, permite generar el resultado unificado
# que se imprime en consola desde defuzzification.py.
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


def fuzzificar_valor_campana(valor, configuracion):
	"""Convierte un valor nítido en grados de pertenencia usando campanas.

	Se conserva para pruebas y comparaciones, aunque la salida final actual del sistema
	se calcula uniendo triangular y trapezoidal en defuzzification.py.
	"""

	grados = {}
	for etiqueta, parametros in configuracion.items():
		funcion = FuncionPertenenciaCampanaGeneralizada(*parametros)
		grados[etiqueta] = funcion.evaluar(valor)
	return grados


def fuzzificar_valor_con_funcion(valor, configuracion, clase_funcion):
	"""Convierte un valor nítido en grados de pertenencia usando una clase de función dada.

	Es el punto común para triangular y trapezoidal, que después alimentan
	la unión de grados usada por defuzzification.py.
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


def fuzzificar_comida_servicio(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio con campanas generalizadas.

	Se usa solo como referencia comparativa; la ruta principal de ejecución actual
	une triangular y trapezoidal antes de llamar a defuzzification.py.
	"""

	grados_comida = fuzzificar_valor_campana(valor_comida, CONFIGURACION_CAMPANA_COMIDA)
	grados_servicio = fuzzificar_valor_campana(valor_servicio, CONFIGURACION_CAMPANA_SERVICIO)
	return grados_comida, grados_servicio


def fuzzificar_comida_servicio_triangular(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio usando funciones triangulares.

	Los diccionarios resultantes se combinan con los trapezoidales por máximo.
	"""

	grados_comida = fuzzificar_valor_triangular(valor_comida, CONFIGURACION_TRIANGULAR_COMIDA)
	grados_servicio = fuzzificar_valor_triangular(valor_servicio, CONFIGURACION_TRIANGULAR_SERVICIO)
	return grados_comida, grados_servicio


def fuzzificar_comida_servicio_trapezoidal(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio usando funciones trapezoidales.

	Los diccionarios resultantes se combinan con los triangulares por máximo.
	"""

	grados_comida = fuzzificar_valor_trapezoidal(valor_comida, CONFIGURACION_TRAPEZOIDAL_COMIDA)
	grados_servicio = fuzzificar_valor_trapezoidal(valor_servicio, CONFIGURACION_TRAPEZOIDAL_SERVICIO)
	return grados_comida, grados_servicio


def fuzzificar_hombro_izquierdo(valor, inicio, fin):
	"""Calcula una membresía tipo hombro izquierdo: 1 al inicio y 0 al final.

	Se usa para imitar la forma de los extremos de la gráfica dibujada a mano.
	"""

	if valor <= inicio:
		return 1.0
	if inicio < valor < fin:
		return (fin - valor) / (fin - inicio)
	return 0.0


def fuzzificar_hombro_derecho(valor, inicio, fin):
	"""Calcula una membresía tipo hombro derecho: 0 al inicio y 1 al final.

	Se usa para imitar la forma de los extremos de la gráfica dibujada a mano.
	"""

	if valor <= inicio:
		return 0.0
	if inicio < valor < fin:
		return (valor - inicio) / (fin - inicio)
	return 1.0


CONFIGURACION_GRAFICA_COMIDA = {
	"mmc": ("izquierdo", 0.0, 2.5),
	"mc": ("triangular", 1.0, 3.0, 5.0),
	"rc": ("triangular", 2.5, 5.0, 7.5),
	"bc": ("triangular", 5.0, 7.0, 9.0),
	"mbc": ("derecho", 7.5, 10.0),
}

CONFIGURACION_GRAFICA_SERVICIO = {
	"mms": ("izquierdo", 0.0, 2.5),
	"ms": ("triangular", 1.0, 3.0, 5.0),
	"rs": ("triangular", 2.5, 5.0, 7.5),
	"bs": ("triangular", 5.0, 7.0, 9.0),
	"mbs": ("derecho", 7.5, 10.0),
}


def fuzzificar_valor_grafica(valor, configuracion):
	"""Convierte un valor nítido en grados de pertenencia siguiendo la gráfica ajustada.

	Esto refleja la interpretación visual de la imagen: hombros en los extremos
	y triángulos en los términos intermedios.
	"""

	grados = {}
	for etiqueta, parametros in configuracion.items():
		tipo = parametros[0]
		if tipo == "izquierdo":
			_, inicio, fin = parametros
			grados[etiqueta] = fuzzificar_hombro_izquierdo(valor, inicio, fin)
		elif tipo == "derecho":
			_, inicio, fin = parametros
			grados[etiqueta] = fuzzificar_hombro_derecho(valor, inicio, fin)
		elif tipo == "triangular":
			_, a, b, c = parametros
			grados[etiqueta] = FuncionPertenenciaTriangular(a, b, c).evaluar(valor)
		else:
			raise ValueError(f"Tipo de función no soportado: {tipo}")
	return grados


def fuzzificar_comida_servicio_grafica(valor_comida, valor_servicio):
	"""Fuzzifica comida y servicio usando la gráfica ajustada de la documentación.

	Se mantiene como referencia visual, pero la salida final actual de consola
	proviene de la unión triangular + trapezoidal en defuzzification.py.
	"""

	grados_comida = fuzzificar_valor_grafica(valor_comida, CONFIGURACION_GRAFICA_COMIDA)
	grados_servicio = fuzzificar_valor_grafica(valor_servicio, CONFIGURACION_GRAFICA_SERVICIO)
	return grados_comida, grados_servicio


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


class FuncionPertenencia_S:
	"""Representa una función de pertenencia en forma de S."""

	def __init__(self, a, b):
		# a es el punto donde la función comienza a aumentar y b es el punto donde alcanza su valor máximo.
		self.a = a
		self.b = b

	def evaluar(self, x):
		# Implementa la función en forma de S usando la fórmula estándar.
		if x <= self.a:
			return 0.0
		if self.a < x <= (self.a + self.b) / 2:
			return 2 * ((x - self.a) / (self.b - self.a)) ** 2
		if (self.a + self.b) / 2 < x < self.b:
			return 1 - 2 * ((x - self.b) / (self.b - self.a)) ** 2
		return 1.0


def mostrar_resultados_S(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


class FuncionPertenencia_Z:
	"""Representa una función de pertenencia en forma de Z."""

	def __init__(self, a, b):
		# a es el punto donde la función comienza a disminuir y b es el punto donde alcanza su valor mínimo.
		self.a = a
		self.b = b

	def evaluar(self, x):
		# Implementa la función en forma de Z usando la fórmula estándar.
		if x <= self.a:
			return 1.0
		if self.a < x <= (self.a + self.b) / 2:
			return 1 - 2 * ((x - self.a) / (self.b - self.a)) ** 2
		if (self.a + self.b) / 2 < x < self.b:
			return 2 * ((x - self.b) / (self.b - self.a)) ** 2
		return 0.0


def mostrar_resultados_Z(funcion, nombre, valores):
	print(f"\nResultados para {nombre} (a={funcion.a}, b={funcion.b}):")
	for valor in valores:
		print(f"  x = {valor:>5} -> pertenencia = {funcion.evaluar(valor):.2f}")


class FuncionPertenenciaPi:
	"""Representa una función de pertenencia en forma de Pi."""

	def __init__(self, a, b, c, d):
		# a y d controlan las pendientes, mientras que b y c definen el intervalo donde la función alcanza su valor máximo.
		self.a = a
		self.b = b
		self.c = c
		self.d = d

	def evaluar(self, x):
		# Implementa la función en forma de Pi usando la fórmula estándar.
		if x <= self.a:
			return 0.0
		if self.a < x <= (self.a + self.b) / 2:
			return 2 * (x - self.a) / (self.b - self.a)** 2
		if (self.a + self.b) / 2 < x <= self.b:
			return 1 - 2 * (x - self.b) / (self.b - self.a)** 2
		if self.b <= x <= self.c:
			return 1.0
		if self.c < x <= (self.c + self.d) / 2:
			return 1 - 2 * (x - self.c) / (self.d - self.c)** 2
		if (self.c + self.d) / 2 < x < self.d:
			return 2 * (x - self.d) / (self.d - self.c)** 2
		return 0.0


def mostrar_resultados_Pi(funcion, nombre, valores):
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
	# Se crean instancias de cada tipo de función de pertenencia con parámetros específicos, se obtienen los valores del usuario
	fp1_tri = FuncionPertenenciaTriangular(0, 5, 10)
	fp2_tri = FuncionPertenenciaTriangular(5, 10, 15)
	fp_trap = FuncionPertenenciaTrapezoidal(0, 5, 10, 15)
	fp_gauss = FuncionPertenenciaGaussiana(10, 2)
	fp_campana = FuncionPertenenciaCampanaGeneralizada(5, 10, 2)
	fp_sigmoidal = FuncionPertenenciaSigmoidal(1, 10)
	fp_S = FuncionPertenencia_S(0, 10)
	fp_Z = FuncionPertenencia_Z(0, 10)
	fp_Pi = FuncionPertenenciaPi(0, 5, 10, 15)
	valores = obtener_valores_usuario()

	# Se muestran los resultados de evaluación de cada función de pertenencia para los valores ingresados por el usuario.
	mostrar_resultados(fp1_tri, "fp1_tri", valores)
	mostrar_resultados(fp2_tri, "fp2_tri", valores)
	mostrar_resultados_trapezoidal(fp_trap, "fp_trap", valores)
	mostrar_resultados_gaussiana(fp_gauss, "fp_gauss", valores)
	mostrar_resultados_campana(fp_campana, "fp_campana", valores)
	mostrar_resultados_sigmoidal(fp_sigmoidal, "fp_sigmoidal", valores)
	mostrar_resultados_S(fp_S, "fp_S", valores)
	mostrar_resultados_Z(fp_Z, "fp_Z", valores)
	mostrar_resultados_Pi(fp_Pi, "fp_Pi", valores)