from empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, edad, dni, salario, departamento, equipo=None ):
        super().__init__(nombre, edad, dni, "Gerente", salario)
        self.departamento = departamento
        self.equipo = equipo or []

    def bonificacion(self, porcentaje):
        if porcentaje >= 0 and porcentaje <= 100:
            return self.salario * porcentaje / 100 + 1500
        else:
            raise ValueError("Porcentaje erroneo")

    def agregar_empleado(self, emp):
        self.equipo.append(emp)

    def mostrar(self):
        super().mostrar()
        print("Departamento:", self.departamento)
        print("Equipo:")
        for emp in self.equipo:
            print(emp)

if __name__ == "__main__":
    g1 = Gerente("José", 50, "12345678A", 10000, "Contabilidad")
    e1 = Empleado("Juan", 25, "42342343D", "Administrativo", 2000)
    e2 = Empleado("María", 20, "87654321B", "Auxiliar", 1500)
    g1.agregar_empleado(e1)
    g1.agregar_empleado(e2)
    g1.mostrar()
