from empleado import Empleado

class Desarrollador(Empleado):
    def __init__(self, nombre, edad, dni, cargo, salario, lenguaje ):
        super().__init__(nombre, edad, dni, cargo, salario)
        self.lenguaje = lenguaje

    def bonificacion(self, porcentaje):
        if porcentaje >= 0 and porcentaje <= 100:
            return self.salario * porcentaje / 100 + 1000
        else:
            raise ValueError("Porcentaje inválido")

    def __str__(self):
        return super().__str__() + f" Lenguaje: {self.lenguaje}"

if __name__ == "__main__":
    d1 = Desarrollador("Juan", 25, "42342343D", "Gerente", 2000, "C++")
    print(d1.bonificacion(10))
    print(d1)