# datos:
#  * los de persona
#  * es empleado ? empleado
#  * lista de cursos
from empleado import Empleado

class Profesor(Empleado):
    def __init__(self, nombre, edad, dni, cargo, salario, lista_cursos):
        super().__init__(nombre, edad, dni, cargo, salario)
        self.lista_cursos = []

    def __str__(self):
        return super().__str__() + " " + str(self.lista_cursos)

    def añadir_curso(self, curso):
        self.lista_cursos.append(curso)

    def mostrar_cursos(self):
        for curso in self.lista_cursos:
            print(curso)

if __name__ == "__main__":
    # construir un objeto profesor
    profesor1 = Profesor("Juanma", 27, "12345678A", "PROFESOR", 1000, [])
    profesor1.añadir_curso("TIC II")
    profesor1.añadir_curso("CDyPC")
    profesor1.añadir_curso("ROBOTICA 3º")
    profesor1.mostrar_cursos()
    # probar __str__
    print(profesor1)
