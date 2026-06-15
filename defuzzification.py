"""Base de 25 reglas difusas para el problema de propinas."""


CALIDAD = {
	"CC": "Calidad de la Comida",
	"CS": "Calidad del Servicio",
}

SERVICIO = {
	"mms": "muy mal servicio",
	"ms": "mal servicio",
	"rs": "regular servicio",
	"bs": "buen servicio",
	"mbs": "muy buen servicio",
}

COMIDA = {
	"mmc": "muy mala comida",
	"mc": "mala comida",
	"rc": "regular comida",
	"bc": "buena comida",
	"mbc": "muy buena comida",
}

PROPINAS = {
	"n": "nada",
	"p": "poca",
	"r": "regular",
	"b": "buena",
	"e": "excelente",
}


REGLAS_NADA = [
	("R1", "mmc", "mms"),
	("R2", "mmc", "ms"),
	("R3", "mc", "mms"),
	("R4", "mc", "ms"),
	("R5", "rc", "mms"),
	("R6", "rc", "ms"),
]

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

REGLAS_REGULAR = [
	("R16", "mc", "mbs"),
	("R17", "rc", "bs"),
	("R18", "rc", "mbs"),
	("R19", "bc", "rs"),
	("R20", "bc", "bs"),
	("R21", "mbc", "ms"),
	("R22", "mbc", "rs"),
]

REGLAS_BUENA = [
	("R23", "bc", "mbs"),
	("R24", "mbc", "bs"),
]

REGLAS_EXCELENTE = [
	("R25", "mbc", "mbs"),
]

REGLAS_POR_SALIDA = {
	"nada": REGLAS_NADA,
	"poca": REGLAS_POCA,
	"regular": REGLAS_REGULAR,
	"buena": REGLAS_BUENA,
	"excelente": REGLAS_EXCELENTE,
}

TABLA_PROPINAS = {
	"mmc": {"mms": "n", "ms": "n", "rs": "p", "bs": "p", "mbs": "p"},
	"mc": {"mms": "n", "ms": "n", "rs": "p", "bs": "p", "mbs": "r"},
	"rc": {"mms": "n", "ms": "n", "rs": "p", "bs": "r", "mbs": "r"},
	"bc": {"mms": "p", "ms": "p", "rs": "r", "bs": "r", "mbs": "b"},
	"mbc": {"mms": "p", "ms": "r", "rs": "r", "bs": "b", "mbs": "e"},
}


VALORES_SALIDA = {
	"nada": 0.0,
	"poca": 2.5,
	"regular": 5.0,
	"buena": 7.5,
	"excelente": 10.0,
}

