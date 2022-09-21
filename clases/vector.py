from clases.punto import crear_punto
def vector(x,y, c, d):
    crear_punto(x,y)
    crear_punto(c, d)
    print("has creado los siguientes vectores:")
    vectorresultanteejex=x-c
    vectorresultanteejey=y-d
    vectorresultante=(vectorresultanteejex, vectorresultanteejey)
    print("el vector resultante de los dos anteriores es el: ", vectorresultante)