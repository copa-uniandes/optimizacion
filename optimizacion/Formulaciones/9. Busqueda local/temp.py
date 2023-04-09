import busquedaLocal as bl


# Función que retorna el valor de la función objetivo, para un punto (x1,x2)
def f(x1, x2):
    return 20 * x1 + 15 * x2


x1, x2 = 6000, 3500
print(f"El valor de la función objetivo en el punto ({x1}, {x2}) es {f(x1, x2)}.")


def R1(x1, x2):
    return 0.3 * x1 + 0.4 * x2 >= 2000


x1, x2 = 1000, 6000
print(f"R1({x1}, {x2}) retorna: {R1(x1, x2)}.")


# Función booleana para la restricción (3)
def R2(x1, x2):
    return 0.4 * x1 + 0.2 * x2 >= 1500


# Función booleana para la restricción (4)
def R3(x1, x2):
    return 0.2 * x1 + 0.3 * x2 >= 500


# Función booleana para la restricción (5)
def R4(x1, x2):
    return x1 <= 9000


# Función booleana para la restricción (6)
def R5(x1, x2):
    return x2 <= 6000


# Función booleana para la restricción (7)
def R6(x1, x2):
    return x1 >= 0


# Función booleana para la restricción (8)
def R7(x1, x2):
    return x2 >= 0


restricciones = [R1, R2, R3, R4, R5, R6, R7]
x0 = (9000, 6000)
d0 = 500
xStar = bl.busquedaLocal(f, restricciones, bl.miRadar, x0, d0)

x1Star, x2Star = xStar
print(f"El costo total de esta solución es de ${f(x1Star, x2Star)}.")

bl.busquedaLocalGrafica(
    f, restricciones, bl.miRadar, x0, d0, xlim=[-20, 10000], ylim=[-200, 7000]
)
