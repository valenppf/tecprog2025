import datetime

class Alumno:
    def __init__(self,nombre,dni,fecha_nac):
        self.nombre=nombre
        self.dni=dni
        self.fecha_nac=fecha_nac

    def _calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha_nac.year

        #ajustar si aún no llegó el cumpleaños este año
        if (hoy.month,hoy.day)<(self.fecha_nac.month,self.fecha_nac.day):
            edad -= 1

        return edad

class Carrera:
    def __init__(self,nombre):
        self.nombre=nombre
        self.inscripciones = []

    def mostrar_alumnos(self):
        print("carrera:",self.nombre)
        print("Alumnos:")
        for i in self.inscripciones:
            print("-",i.alumno.nombre,"-",i.fecha_insc)

class Inscripcion:
    def __init__(self,fecha_insc,alumno):
        self.fecha_insc=fecha_insc
        self.alumno=alumno

class Facultad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.list_carr = []
    
    def mostrar_carr_y_alum(self):
        print("Facultad:",self.nombre)
        for c in self.list_carr:
            c.mostrar_alumnos()
        
class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        facu=Facultad("FICH")
        informatica=Carrera("Ing. Informática")
        recursos_hidricos=Carrera("Ing. RR hídricos")
        alumno1=Alumno("alum1","11.111.111",datetime.date(1990,11,11))
        alumno2=Alumno("alum2","11.122.122",datetime.date(1990,9,9))
        insc1=Inscripcion(datetime.date(2008,12,10),alumno1)
        insc2=Inscripcion(datetime.date(2008,12,11),alumno2)
        informatica.inscripciones=[insc1,insc2]
        facu.list_carr=[informatica,recursos_hidricos]
        facu.mostrar_carr_y_alum()

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()