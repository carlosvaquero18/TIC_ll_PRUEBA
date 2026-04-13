from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, edad, dni, cargo, salario ):
        super().__init__(nombre, edad, dni)
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        cadena = super().__str__()
        cadena = cadena + " " + self.cargo
        cadena = cadena + " " + str(self.salario)
        return cadena

    def mostrar(self):
        super().mostrar()
        print("Cargo:", self.cargo)
        print("Salario:", self.salario)

    # getter y setters
    def get_salario(self):
        return self.salario

    def set_salario(self, salario):
        if salario >= 0 and salario <= 100000:
            self.salario = salario
        else:
            raise ValueError("Salario inválido")

    def get_cargo(self):
        return self.cargo

    def set_cargo(self, cargo):
        self.cargo = cargo

    # devuelve un portenje del salario
    def bonificacion(self, porcentaje):
        if porcentaje >= 0 and porcentaje <= 100:
            return self.salario * porcentaje / 100
        else:
            raise ValueError("Porcentaje inválido")


if __name__ == "__main__":
    empleado1 = Empleado("Juan", 25, "42342343D", "Gerente", 50000)
    empleado1.mostrar()
    empleado1.set_cargo("Admnistrativo")
    empleado1.mostrar()
    print("Bonificacion 10%: ", empleado1.bonificacion(10))









