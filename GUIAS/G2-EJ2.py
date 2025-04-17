import datetime

class Persona:
    def __init__(self,nombre,apellido,fecha_nac:datetime.date):
        self.m_nombre=nombre
        self.m_apellido=apellido
        self.m_fecha_nac=fecha_nac

    def __eq__(self, value):
        return self.m_nombre==value.m_nombre and self.m_fecha_nac==value.m_fecha_nac
    
    def _calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.m_fecha_nac.year

        #ajustar si aún no llegó el cumpleaños este año
        if (hoy.month,hoy.day)<(self.m_fecha_nac.month,self.m_fecha_nac.day):
            edad -= 1

        return edad

    def mostrar(self):
        edad=self._calcular_edad()
        print(self.m_apellido,",",self.m_nombre,":",edad,"años. Cumple el",self.m_fecha_nac.day,"del",self.m_fecha_nac.month)

class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        persona1 = Persona("Adolf","Stalin",datetime.date(1969,10,19))
        persona2 = Persona("Adolf","Stalin",datetime.date(1969,10,19))
        print("identidad de persona1:",id(persona1))
        print("identidad de persona2:",id(persona2))
        print("tienen igual id?",persona1 is persona2)
        print("son iguales?", persona1 == persona2)
        persona1.mostrar()
        persona2.mostrar()
        

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()