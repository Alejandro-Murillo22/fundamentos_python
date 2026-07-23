# Algoritmo 1

p1 = float(input("Digite los puntos obtenidos en el nivel 1: "))
p2 = float(input("Digite los puntos obtenidos en el nivel 2: "))
p3 = float(input("Digite los puntos obtenidos en el nivel 3: "))

sum = p1 + p2 + p3

print("El puntaje total obtenido es:", sum)

print("-----------------------------------------------------------------")

# Algoritmo 2

h = float(input("Digite las horas jugadas: "))
m = float(input("Digite los minutos jugados: "))
s = float(input("Digite los segundos jugados: "))

ht = h * 3600
mt = m * 60

st = ht + mt + s

print("Los segundos totales jugados son:", st)

print("-----------------------------------------------------------------")

# Algoritmo 3

d1 = float(input("Digite el primer daño causado: "))
d2 = float(input("Digite el segundo daño causado: "))
d3 = float(input("Digite el tercer daño causado: "))

total = d1 + d2 + d3

print("El total de daño causado es:", total)

print("-----------------------------------------------------------------")

# Algoritmo 4

xp1 = float(input("Digite la experiencia de la mision 1: "))
xp2 = float(input("Digite la experiencia de la mision 2: "))
xp3 = float(input("Digite la experiencia de la mision 3: "))

xptotal = xp1 + xp2 + xp3

print("La experiencia total obtenida es:", xptotal)

print("-----------------------------------------------------------------")

# Algoritmo 5 

vt = float(input("Digite la vida maxima: "))
va = float(input("Digite su vida actual: "))

pv = (va / vt) * 100

print(f"El porcentaje de vida del jugador es: {pv}%")

print("-----------------------------------------------------------------")

# Algoritmo 6

o1 = float(input("Digite el oro recolectado en la mision 1: "))
o2 = float(input("Digite el oro recolectado en la mision 2: "))
o3 = float(input("Digite el oro recolectado en la mision 3: "))

total = o1 + o2 + o3

print("El total de oro obtenido es:", total)

print("-----------------------------------------------------------------")

# Algoritmo 7

dr = float(input("Digite la distancia recorrida: "))
tt = float(input("Digite el tiempo tomado: "))

vp = dr / tt

print("La velocidad promedio del vehiculo es:", vp)

print("-----------------------------------------------------------------")

# Algoritmo 8

m1 = float(input("Digite el costo de la mejora 1: "))
m2 = float(input("Digite el costo de la mejora 2: "))
m3 = float(input("Digite el costo de la mejora 3: "))

total = m1 + m2 + m3

print("El costo total de las mejoras:", total)

print("-----------------------------------------------------------------")

# Algoritmo 9

tm = float(input("Digite el tiempo total de la mision (minutos): "))
tt = float(input("Digite el tiempo transcurrido en la mision (minutos): "))

tr = tm - tt 

print("El tiempo restante para completar la mision es:", tr)

print("-----------------------------------------------------------------")

# Algoritmo 10

n1 = float(input("Digite el nivel del jugador 1: "))
n2 = float(input("Digite el nivel del jugador 2: "))
n3 = float(input("Digite el nivel del jugador 3: "))

pt = (n1 + n2 + n3) / 3

print("El promedio de nivel de los jugadores del equipo es:", pt)

print("-----------------------------------------------------------------")

# Algoritmo 11

db = float(input("Digite el daño base: "))
ct = float(input("Digite el multiplicador del critico: "))

dc = db * ct

print("El daño critico es:", dc)

print("-----------------------------------------------------------------")

# Algoritmo 12

mt = int(input("Digite el tiempo total jugado en minutos: "))

horas = mt // 60
mr = mt % 60

print("El tiempo total de juego es:", horas, "horas y", mr, "minutos")

print("-----------------------------------------------------------------")

# Algoritmo 13

mt = float(input("Digite el número total de misiones: "))
mc = float(input("Digite el número de misiones completadas: "))

pm = (mc / mt) * 100

print("El porcentaje de misiones completadas es:", pm, "%")

print("-----------------------------------------------------------------")

# Algoritmo 14

c1 = float(input("Digite el costo del primer objeto: "))
c2 = float(input("Digite el costo del segundo objeto: "))
c3 = float(input("Digite el costo del tercer objeto: "))

ct = c1 + c2 + c3

print("El costo total de la compra es:", ct)

print("-----------------------------------------------------------------")

# Algoritmo 15

p1 = float(input("Digite el tiempo de la primera partida en minutos: "))
p2 = float(input("Digite el tiempo de la segunda partida en minutos: "))
p3 = float(input("Digite el tiempo de la tercera partida en minutos: "))

pp = (p1 + p2 + p3) / 3

print("El tiempo promedio por partida es:", pp, "minutos")

print("-----------------------------------------------------------------")

# Algoritmo 16

et = float(input("Digite el número total de enemigos: "))
ed = float(input("Digite el número de enemigos derrotados: "))

pe = (ed / et) * 100

print("El porcentaje de enemigos derrotados es:", pe, "%")

print("-----------------------------------------------------------------")