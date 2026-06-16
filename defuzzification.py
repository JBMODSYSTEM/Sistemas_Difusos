"""Base de 25 reglas difusas para el problema de propinas."""

# Calidad de la comida (CC) y calidad del servicio (CS) son las variables de entrada.
CALIDAD = {
	"CC": "Calidad de la Comida",
	"CS": "Calidad del Servicio",
}


# Funciones de pertenencia para cada etiqueta difusa de calidad del servicio.
SERVICIO = {
	"mms": "muy mal servicio",
	"ms": "mal servicio",
	"rs": "regular servicio",
	"bs": "buen servicio",
	"mbs": "muy buen servicio",
}


# Funciones de pertenencia para cada etiqueta difusa de calidad de comida y servicio.
COMIDA = {
	"mmc": "muy mala comida",
	"mc": "mala comida",
	"rc": "regular comida",
	"bc": "buena comida",
	"mbc": "muy buena comida",
}


# Valores de salida para cada etiqueta difusa de propina, usados en defuzzificación.
PROPINAS = {
	"n": "nada",
	"p": "poca",
	"r": "regular",
	"b": "buena",
	"e": "excelente",
}


# Reglas difusas para Nada de Propina: cada tupla representa una regla con su etiqueta, calidad de comida y calidad de servicio.
REGLAS_NADA = [
	("R1", "mmc", "mms"),
	("R2", "mmc", "ms"),
	("R3", "mc", "mms"),
	("R4", "mc", "ms"),
	("R5", "rc", "mms"),
	("R6", "rc", "ms"),
]


# Reglas difusas para Poca Propina: cada tupla representa una regla con su etiqueta, calidad de comida y calidad de servicio.
REGLAS_POCA = [
	("R7", "mmc", "rs"),
	("R8", "mmc", "bs"),
	("R9", "mmc", "mbs"),
	("R10", "mc", "rs"),
	("R11", "mc", "bs"),
	("R12", "rc", "rs"),
	("R13", "bc", "mms"),
	("R14", "bc", "ms"),
	("R15", "mbc", "mms"),
]


# Reglas difusas para Regular Propina: cada tupla representa una regla con su etiqueta, calidad de comida y calidad de servicio.
REGLAS_REGULAR = [
	("R16", "mc", "mbs"),
	("R17", "rc", "bs"),
	("R18", "rc", "mbs"),
	("R19", "bc", "rs"),
	("R20", "bc", "bs"),
	("R21", "mbc", "ms"),
	("R22", "mbc", "rs"),
]


# Reglas difusas para Buena Propina: cada tupla representa una regla con su etiqueta, calidad de comida y calidad de servicio.
REGLAS_BUENA = [
	("R23", "bc", "mbs"),
	("R24", "mbc", "bs"),
]


# Reglas difusas para Excelente Propina: cada tupla representa una regla con su etiqueta, calidad de comida y calidad de servicio.
REGLAS_EXCELENTE = [
	("R25", "mbc", "mbs"),
]


# Agrupamos las reglas por salida para facilitar su evaluación.
REGLAS_POR_SALIDA = {
	"nada": REGLAS_NADA,
	"poca": REGLAS_POCA,
	"regular": REGLAS_REGULAR,
	"buena": REGLAS_BUENA,
	"excelente": REGLAS_EXCELENTE,
}


# Tabla de propinas que relaciona cada combinación de calidad de comida y servicio con una etiqueta de propina.
TABLA_PROPINAS = {
	"mmc": {"mms": "n", "ms": "n", "rs": "p", "bs": "p", "mbs": "p"},
	"mc": {"mms": "n", "ms": "n", "rs": "p", "bs": "p", "mbs": "r"},
	"rc": {"mms": "n", "ms": "n", "rs": "p", "bs": "r", "mbs": "r"},
	"bc": {"mms": "p", "ms": "p", "rs": "r", "bs": "r", "mbs": "b"},
	"mbc": {"mms": "p", "ms": "r", "rs": "r", "bs": "b", "mbs": "e"},
}


# Valores numéricos asociados a cada etiqueta de propina, usados para la defuzzificación por promedio ponderado.
VALORES_SALIDA = {
	"nada": 0.0,
	"poca": 2.5,
	"regular": 5.0,
	"buena": 7.5,
	"excelente": 10.0,
}


class Defuzzification:
    """Esta será la clase para el sistema difuso de propinas, que implementará la lógica de defuzzificación."""
    
    # Inicializamos la clase con los valores de salida para cada etiqueta de propina, 
	# que se pueden personalizar o usar los valores por defecto.
    def __init__(self, valores_salida = None):
        # Si no se proporcionan valores de salida personalizados, 
		# usamos los valores por defecto definidos en VALORES_SALIDA.
        self.valores_salida = valores_salida or VALORES_SALIDA
    
	
	# Esta función toma la calidad de la comida y del servicio como 
	# entrada, obtiene la etiqueta de propina correspondiente
    def obtener_propina(self, calidad_comida, calidad_servicio):
		# Validamos que las entradas sean válidas, que existan en la tabla de propinas.
        return TABLA_PROPINAS[calidad_comida][calidad_servicio]
    

    @staticmethod
    def evaluar_regla(comida, servicio, grados_comida, grados_servicio):
        # Esta función evalúa una regla difusa específica, tomando la calidad de comida y servicio,
		# y los grados de pertenencia para cada uno, y devuelve el grado de activación de la regla.
        return grados_comida[comida] * grados_servicio[servicio]
    

    def evaluar_grupo_reglas(self, reglas, grados_comida, grados_servicio):
        
		# Creamos una lista para almacenar los grados de activación de cada regla en el grupo.
        activaciones = []
        
        # Iteramos sobre cada regla en el grupo, evaluando su activación y almacenándola en la lista.
        for _, comida, servicio in reglas:
            # Evaluamos la regla usando la función evaluar_regla, que calcula el grado de 
			# activación multiplicando los grados de pertenencia de la comida y el servicio.
            activaciones.append(self.evaluar_regla(comida, servicio, grados_comida, grados_servicio))
        
		# Si no hay activaciones (lo que podría ocurrir si el grupo de reglas está vacío), 
		# retornamos 0.0 para evitar errores.
        if not activaciones:
            return 0.0
        return max(activaciones)  # Retornamos el grado de activación máximo entre las reglas del grupo.
    

	# Esta función evalúa todas las reglas para cada etiqueta de propina, 
	# tomando los grados de pertenencia de la comida y el servicio, y devuelve un 
	# diccionario con el grado de activación para cada etiqueta de propina.
    def evaluar_reglas(self, grados_comida, grados_servicio):
        
		# Creamos un diccionario para almacenar los grados de activación para cada etiqueta de propina,
		# evaluando cada grupo de reglas correspondiente a cada etiqueta.
        return {
            "nada": self.evaluar_grupo_reglas(REGLAS_NADA, grados_comida, grados_servicio),
            "poca": self.evaluar_grupo_reglas(REGLAS_POCA, grados_comida, grados_servicio),
            "regular": self.evaluar_grupo_reglas(REGLAS_REGULAR, grados_comida, grados_servicio),
			"buena": self.evaluar_grupo_reglas(REGLAS_BUENA, grados_comida, grados_servicio),
			"excelente": self.evaluar_grupo_reglas(REGLAS_EXCELENTE, grados_comida, grados_servicio),
		}
    

	# Esta función realiza la defuzzificación utilizando el método de promedio ponderado,
	# tomando los grados de activación para cada etiqueta de propina y los valores numéricos 
	# correspondientes, y devuelve el valor nítido de la propina recomendada.
    def defuzzificar_por_promedio_ponderado(self, grados, valores_salida = None):
        # Calcularemos el valor nitido de la propina utilizando el método de promedio ponderado, 
		# multiplicando cada grado de activación por su valor numérico 
		# correspondiente y sumando los resultados.
        
		# Si no se proporcionan valores de salida personalizados, usamos los valores por defecto.
        if valores_salida is None:
            valores_salida = self.valores_salida
        
		# Inicializamos el numerador y denominador para el cálculo del promedio ponderado.
        # Numerador = sum(grado_activacion * valor_salida) para cada etiqueta de propina.
        numerador = 0.0
        # Denominador = sum(grado_activacion) para cada etiqueta de propina, 
		# que se usará para normalizar el resultado.
        denominador = 0.0

        # Iteramos sobre cada etiqueta de propina y su grado de activación,
		# multiplicando el grado de activación por el valor numérico correspondiente y sumando al numerador,
		# y sumando el grado de activación al denominador.
        for etiqueta, grado in grados.items():
            valor_salida = valores_salida[etiqueta]
            numerador += grado * valor_salida
            denominador += grado
        
		# Si el denominador es cero (lo que podría ocurrir si no hay activaciones),
		# retornamos 0.0 para evitar división por cero, lo que indica que no se recomienda ninguna propina.
        if denominador == 0.0:
            return 0.0  # Retornamos 0.0 para evitar división por cero.
        
        return numerador / denominador  # Retornamos el resultado del promedio ponderado, que es el valor nítido de la propina recomendada.	


	# Esta función combina la inferencia de reglas y la defuzzificación en un solo paso, 
	# tomando los grados de pertenencia de la comida y el servicio, evaluando las 
	# reglas para obtener los grados de activación, y luego realizando la defuzzificación 
	# para obtener el valor nítido de la propina recomendada.
    def inferir_y_defuzzificar(self, grados_comida, grados_servicio, valores_salida = None):
		
		# Evaluamos las reglas para obtener los grados de activación.
        resultados_reglas = self.evaluar_reglas(grados_comida, grados_servicio)
        
		# Realizamos la defuzzificación utilizando el método de promedio ponderado para 
		# obtener el valor nítido de la propina recomendada.
        nitido = self.defuzzificar_por_promedio_ponderado(resultados_reglas, valores_salida)
        
    	# Retornamos tanto los resultados de las reglas como el valor nítido de la propina recomendada.
        return resultados_reglas, nitido
        
        