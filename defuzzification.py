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


# Devuelve la etiqueta de propina para una combinacion dada.
def obtener_propina(calidad_comida, calidad_servicio):
    return TABLA_PROPINAS[calidad_comida][calidad_servicio]

# Calcula la fuerza de una regla usando producto entre antecedentes.
def evaluar_regla(comida, servicio, grados_comida, grados_servicio):
    return grados_comida[comida] * grados_servicio[servicio]

# Devuelve la activacion maxima de un grupo de reglas de salida.
def evaluar_grupo_reglas(reglas, grados_comida, grados_servicio):
    activaciones = []
    for _, comida, servicio in reglas:
        activaciones.append(evaluar_regla(comida, servicio, grados_comida, grados_servicio))
    if not activaciones:
        return 0.0
    return max(activaciones)

# Funcion que evalua y agrupa las 25 reglas por salida difusa. y devuelve un diccionario con la activacion de cada etiqueta de propina.
def evaluar_reglas(grados_comida, grados_servicio):
    return {
        "nada": evaluar_grupo_reglas(REGLAS_NADA, grados_comida, grados_servicio),
        "poca": evaluar_grupo_reglas(REGLAS_POCA, grados_comida, grados_servicio),
        "regular": evaluar_grupo_reglas(REGLAS_REGULAR, grados_comida, grados_servicio),
        "buena": evaluar_grupo_reglas(REGLAS_BUENA, grados_comida, grados_servicio),
        "excelente": evaluar_grupo_reglas(REGLAS_EXCELENTE, grados_comida, grados_servicio),
    }

# Funcion para calcular el valor nitido usando un promedio ponderado de salidas singleton.
def defuzzificar_por_promedio_ponderado(agregados, valores_salida = None):
    if valores_salida is None:
        valores_salida = VALORES_SALIDA
    
    # Numerador acumula la suma de valor_salida * grado para cada etiqueta, mientras que denominador acumula la suma de los grados.
    numerador = 0.0
    denominador = 0.0

    # Iteramos sobre cada etiqueta de propina y su grado de activación, multiplicando el valor numérico asociado a esa etiqueta 
    # por su grado y sumándolo al numerador, mientras que el grado se suma al denominador.
    for etiqueta, grado in agregados.items():
        valor_salida = valores_salida[etiqueta]
        numerador += valor_salida * grado
        denominador += grado

    # Si el denominador es cero, significa que no se activó ninguna regla, por lo que devolvemos un valor por defecto (0.0).
    if denominador == 0.0:
        return 0.0

    # De lo contrario, calculamos el promedio ponderado dividiendo el numerador por el denominador.
    # El resultado es un valor nitido que representa la propina recomendada basada en las reglas difusas y sus grados de activación.
    # valor_nitido = sum(valor_salida_i * grado_i) / sum(grado_i)
    return numerador / denominador


# Función principal que integra la evaluación de reglas y la defuzzificación para 
# obtener el valor nitido de propina basado en los grados de activación de comida y servicio.   
def inferir_y_defuzzificar(grados_comida, grados_servicio, valores_salida = None):
    # Evaluamos las reglas para obtener los grados de activación de cada etiqueta de propina.
    resultados_reglas = evaluar_reglas(grados_comida, grados_servicio)
    # Calculamos el valor nitido usando un promedio ponderado de salidas singleton.
    nitido = defuzzificar_por_promedio_ponderado(resultados_reglas, valores_salida)
    # Devolvemos tanto los grados de activación de cada etiqueta de propina como el valor nitido resultante.
    return resultados_reglas, nitido

# Función para imprimir los resultados de los grados de activación y el valor nitido de propina recomendado.
def imprimir_resultados(resultados_reglas, nitido):
    print("\nGrados de activación para cada etiqueta de propina:")
    for etiqueta, grado in resultados_reglas.items():
        print(f"  {etiqueta}: {grado:.4f}")
    print(f"\nValor nitido de propina recomendado: {nitido:.4f}")


if __name__ == "__main__":
    # Ejemplo de uso: se pueden definir grados de activación para comida y servicio, luego inferir y defuzzificar para obtener la propina recomendada.
    grados_comida = {"mmc": 0.1, "mc": 0.5, "rc": 0.8, "bc": 0.3, "mbc": 0.1}
    grados_servicio = {"mms": 0.1, "ms": 0.4, "rs": 0.7, "bs": 0.5, "mbs": 0.2}

    # Evaluamos las reglas y obtenemos el valor nitido de propina recomendado.
    resultados_reglas, nitido = inferir_y_defuzzificar(grados_comida, grados_servicio)
    imprimir_resultados(resultados_reglas, nitido)
