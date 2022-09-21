# examenmiercoles

El enlace al repositorio de GitHub de este proyecto es el siguiente: [GitHub](https://github.com/jzazooro/examenmiercoles.git)

He realizado los ejercicios del examen sorpresa en relacion a puntos, vectores, y espacio vectorial en R2. Desafortunadamente mi ordenador no me importa algunas funciones y no he podido comprobar si el programa funciona correctamente.

El codigo creado es el siguiente: 
### main
```
import math
from clases.punto import crear_punto
from clases.cuadrantes import localizar_cuadrantes
from clases.vector import vector
from clases.distancia import distancia
from clases.rectangulo import rectangulo, obteneraltura, obtenerbase

if __name__ == "__main__":
    crear_punto(2, 3)
    crear_punto(5, 5)
    crear_punto(-3, -3)
    crear_punto(0, 0)
    localizar_cuadrantes(2, 3)
    localizar_cuadrantes(-3, -1)
    localizar_cuadrantes(0, 0)
    vector(2, 3, 5, 5)
    vector(5, 5, 2, 3)
    distancia(2, 3, 5, 5)
    distancia(5, 5, 2, 3)
    distancia(2, 3, 0, 0)
    distancia(5, 5, 0, 0)
    distancia(-3, -1, 0, 0)
    obtenerbase(2, 3, 5, 5)
    obteneraltura(2, 3, 5, 5)
```
