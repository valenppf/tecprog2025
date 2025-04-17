class Empleado:
    def __init__(self,apellido_nombre,direccion,dni)
        self.apellido_nombre=apellido_nombre
        self.direccion=direccion
        self.dni=dni
        
class Mensualizado(Empleado):
    def __init__(self,apellido_nombre,direccion,dni,categoria)
        super().__init__(apellido_nombre,direccion,dni)
        self.categoria=categoria