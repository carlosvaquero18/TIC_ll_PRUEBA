from persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, edad, dni, curso):
        super().__init__(nombre, edad, dni)
        # Usamos guion bajo para indicar que es un atributo "protegido" o interno
        self._curso = curso

    # @property define el "getter" (obtener el valor)
    @property
    def curso(self):
        """Getter para el atributo curso."""
        return self._curso

    # @nombre_de_la_propiedad.setter define el "setter" (modificar el valor)
    @curso.setter
    def curso(self, nuevo_curso):
        """Setter para el atributo curso."""
        # Aquí también podrías poner validaciones como: if type(nuevo_curso) == str:
        self._curso = nuevo_curso

    def __str__(self):
        # Al poner self.curso (sin paréntesis) estamos llamando automáticamente al @property getter
        return super().__str__() + f", Curso: {self.curso}"

    def mostrar(self):
        super().mostrar()
        print("Curso:", self.curso)

if __name__ == "__main__":
    alumno1 = Alumno("Ana", 16, "12345678B", "1º Bachillerato")
    
    print("--- Datos iniciales ---")
    alumno1.mostrar()
    
    print("\n--- Modificando el curso usando el setter ---")
    # Al asignar con el signo =, se llama automáticamente al @curso.setter
    alumno1.curso = "2º Bachillerato"
    
    # Al leer el valor, se llama automáticamente al @property
    print(f"El nuevo curso de {alumno1.nombre} es: {alumno1.curso}")
    
    print("\n--- Resultado final ---")
    print(alumno1)
