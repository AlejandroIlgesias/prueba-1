from Vehiculo import Vehiculo
    
class Coche(Vehiculo):

    def __init__(self, color, ruedas,velocidad,cilindrada):
        super().__init__(color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def atributes(self):
        return ["color","ruedas","velocidad","cilindrada"]
    
    def class_name(self):
        return  "Coche"






    
