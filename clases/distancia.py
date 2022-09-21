from clases.vector import vector
from clases.punto import crear_punto
import math
def distancia(x, y, c, d):
    crear_punto(x, y)
    crear_punto(c, d)
    distancia=math.sqrt((c-x)**2 + (d-y)**2)
    print("la distancia entre los dos vectores es: ", distancia)