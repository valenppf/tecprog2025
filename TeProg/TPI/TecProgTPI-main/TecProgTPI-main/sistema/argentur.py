from modelos.servicio import Servicio
from modelos.pasajero import Pasajero

class Argentur:
    # La empresa tiene un estado(está activo o no) y muchos servicios y ¿¿ pasajeros ??
    def __init__(self, sistema_activo:bool, pasajeros:list[Pasajero], servicios:list[Servicio]):
        self._sistema_activo = sistema_activo
        self._pasajeros = pasajeros
        self._servicios = servicios
