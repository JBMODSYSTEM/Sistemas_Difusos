# Sistema difuso simple tipo microcontrolador
# Entradas: comida y servicio de 0 a 100
# Salida: propina de 0 a 25 %

comida = 50
servicio = 30

# Función triangular usando enteros
def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 100
    elif x < b:
        return int((x - a) * 100 / (b - a))
    else:
        return int((c - x) * 100 / (c - b))


# Función trapecial usando enteros
def trapecio(x, a, b, c, d):
    if x <= a or x >= d:
        return 0
    elif x >= b and x <= c:
        return 100
    elif x < b:
        return int((x - a) * 100 / (b - a))
    else:
        return int((d - x) * 100 / (d - c))


# Fuzzificación comida
comida_mala = trapecio(comida, 0, 0, 20, 50)
comida_regular = triangular(comida, 20, 50, 80)
comida_buena = trapecio(comida, 50, 80, 100, 100)

# Fuzzificación servicio
servicio_malo = trapecio(servicio, 0, 0, 20, 50)
servicio_regular = triangular(servicio, 20, 50, 80)
servicio_bueno = trapecio(servicio, 50, 80, 100, 100)

# Inferencia Sugeno simple
# Salidas singleton en porcentaje
# baja=5, media=12, alta=18, excelente=25

num = 0
den = 0

# Regla 1: comida mala y servicio malo -> baja
w = min(comida_mala, servicio_malo)
num += w * 5
den += w

# Regla 2: comida mala y servicio regular -> baja
w = min(comida_mala, servicio_regular)
num += w * 8
den += w

# Regla 3: comida mala y servicio bueno -> media
w = min(comida_mala, servicio_bueno)
num += w * 12
den += w

# Regla 4: comida regular y servicio malo -> baja
w = min(comida_regular, servicio_malo)
num += w * 8
den += w

# Regla 5: comida regular y servicio regular -> media
w = min(comida_regular, servicio_regular)
num += w * 12
den += w

# Regla 6: comida regular y servicio bueno -> alta
w = min(comida_regular, servicio_bueno)
num += w * 18
den += w

# Regla 7: comida buena y servicio malo -> media
w = min(comida_buena, servicio_malo)
num += w * 12
den += w

# Regla 8: comida buena y servicio regular -> alta
w = min(comida_buena, servicio_regular)
num += w * 18
den += w

# Regla 9: comida buena y servicio bueno -> excelente
w = min(comida_buena, servicio_bueno)
num += w * 25
den += w

# Defuzzificación
if den == 0:
    propina = 0
else:
    propina = num / den

print("Comida:", comida)
print("Servicio:", servicio)
print("Propina:", propina, "%")