import datetime

class Persona:
    def __init__(self, nombre, fechanac):
        self.nombre = nombre
        self.fechanac = fechanac

    def _calcular_edad():
        edad=datetime.datetime.strptime - self.fechanac.strptime
        return edad%

    def _mostrar():
        fecha= _calcular_edad()
        print(nombre,": ","nacido en ",fecha.day,"/",fecha.month,"/",fecha.year)

class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        p1=Persona("Pepe",datetime.date(1896,4,20))
        p2=Persona("Jose",datetime.date(1869,3,12))

        print("Identidad de 1: ", id(p1))
        print("Identidad de 2: ", id(p2))

        print(id(p1)==id(p1))

        p1._mostrar()
        p2._mostrar()
        

if __name__ == "__main__":
    principal=Principal()
    principal.ejecutar()