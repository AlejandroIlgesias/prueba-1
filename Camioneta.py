from Coche import Coche

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada,carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga=carga

    def atributes(self):
        return ["color","ruedas","velocidad","cilindrada","carga"]
    
    def class_name(self):
        return "Camioneta"