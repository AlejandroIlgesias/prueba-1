from Bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    
    def __init__(self, color, ruedas, tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def atributes(self):
        return ["color","ruedas","tipo","velocidad","cilindrada"]
    
    def class_name(self):
        return "Motocicleta"
