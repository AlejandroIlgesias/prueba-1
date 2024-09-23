from Vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo

    def atributes(self):
        return ["color","ruedas","tipo"]
    
    def class_name(self):
        return "Bicicleta"