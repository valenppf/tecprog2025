class Asiento:
    # Un asiento tiene un numero(identificador) y un estado(está ocupado o no)
    def __init__(self, numero:int, ocupado:bool):
        self._numero = numero
        self._ocupado = ocupado