# Delfín



## datos para la tabla:



##### Calidad:

CC = Calidad de la Comida

CS = Calidad del Servicio



##### Servicio:

mms = muy mal servicio

ms = mal servicio

rs = regular servicio

bs = buen servicio

mbs = muy buen servicio



##### Comida:

mmc = muy mala comida

mc = mala comida

rc = regular comida

bc = buena comida

mbc = muy buena comida



##### Propinas:

n = nada

p = poca

r = regular

b = buena

e = excelente





##### Tabla:

|CC\\CS|mms|ms|rs|bs|mbs|
|-|-|-|-|-|-|
|mmc|n|n|p|p|p|
|mc|n|n|p|p|r|
|rc|n|n|p|r|r|
|bc|p|p|r|r|b|
|mbc|p|r|r|b|e|





##### Reglas para nada de propinas:

R1 = mmc * mms

R2 = mmc * ms

R3 = mc * mms

R4 = mc * ms

R5 = rc * mms

R6 = rc * ms



nada = max(R1,R2,R3,R4,R5,R6) "Para Python"

