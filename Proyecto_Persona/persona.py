class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"


    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("DNI:", self.dni)

    # getters y setters
    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        if edad >= 0 and edad <= 120:
            self.edad = edad
        else:
            raise ValueError("Edad inválida")
    # len(dni)
    # si la longitud del dni es 9 se guarda caso contrario se lanza una excepción

    def set_dni(self, dni):
        if len(dni) == 9:
            self.dni = dni
        else:
            raise ValueError("DNI inválido")


if __name__ == "__main__":
    persona1 = Persona("Juan", 25, "42342343D")
    persona1.mostrar()
    persona2 = Persona("Maria", 30, "23423423K")
    persona2.mostrar()
    print(persona1.get_edad())
    persona1.set_edad(30)
    persona1.mostrar()
    persona2.set_dni("12345678A")
    persona2.mostrar()

    print(persona1)

# return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

