import datetime
class Cliente:
    def __init__(self,nombre,rubro,cuit):
        self.nombre=nombre
        self.rubro=rubro
        self.cuit=cuit

class Empresa:
    def __init__(self,nombre,tipo):
        self.nombre=nombre
        self.tipo=tipo

class DetalleFactura:
    def __init__(self,producto,cantidad,totalItem):
        self.producto=producto
        self.cantidad=cantidad
        self.totalItem=totalItem

    def mostrarDetalle(self):
        print(self.producto," ",self.cantidad," unid. Total item: ",self.totalItem)
        
class Factura:
    def __init__(self,nro,cliente,fecha:datetime.date):
        self.nro=nro
        self.cliente=cliente
        self.fecha=fecha
        self.listaDetalles=[]

    def obtener_total(self):
        suma=0
        for d in self.listaDetalles:
            suma+=d.totalItem
        return suma
    
    def mostrar(self):
        print("factura nro ",self.nro)
        print("Cliente ",self.cliente.nombre,"-",self.cliente.rubro,"-",self.cliente.cuit)
        print("total $",self.obtener_total())
        for d in self.listaDetalles:
            d.mostrarDetalle()

class SistemaFacturacion:
    def __init__(self,empresa):
        self.empresa=empresa
        self.listaFacturas=[]

    def sumarFacturas(self):
        suma=0
        for f in self.listaFacturas:
            suma+=f.obtener_total()
        return suma
        
class Principal:
    def __init__(self):
        pass

    def ejecutar(self):
        empresa=Empresa("Mayorista S.A","IVA monotributo")
        cliente1=Cliente("Gilcomat SRL","R.I","30-12345678-1")
        d1=DetalleFactura("porcelanato 45x45",100,690)
        d2=DetalleFactura("griferia FV 6 piezas",1,400)
        factura=Factura("0001 0100",cliente1,datetime.date(2015,5,1))
        factura.listaDetalles=[d1,d2]
        factura2=factura
        factura.mostrar()
        sistema=SistemaFacturacion(empresa)
        sistema.listaFacturas=[factura,factura2]
        print("nombre de la empresa: ",empresa.nombre,"-",empresa.tipo)
        print(sistema.sumarFacturas())
        
        

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()



