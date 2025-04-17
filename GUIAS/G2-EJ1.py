class Persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad

    def __eq__(self, value):
        return self.nombre==value.nombre and self.edad==value.edad

class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        persona1 = Persona("adolf",89)
        persona2 = Persona("adolf",89)
        print("identidad de persona1: ",id(persona1))
        print("identidad de persona2: ",id(persona2))
        print("tienen igual id? ",persona1 is persona2)
        print("son iguales? ", persona1 == persona2)

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()