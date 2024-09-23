from Vehiculo import Vehiculo
from Coche import Coche
from Camioneta import Camioneta
from Bicicleta import Bicicleta
from Motocicleta import Motocicleta

lista_vehiculos=[]

if __name__=="__main__":
    mi_vehiculo=Coche("rojo",4,100,2000)
    lista_vehiculos.append(mi_vehiculo)
    print(mi_vehiculo)
    mi_vehiculo2=Bicicleta("Azul",2,"Montaña")
    lista_vehiculos.append(mi_vehiculo2)
    print(mi_vehiculo2)
    mi_vehiculo3=Camioneta("verde",4,1000,160,2500)
    lista_vehiculos.append(mi_vehiculo3)
    print(mi_vehiculo3)
    mi_vehiculo4=Motocicleta("negra",2,"deportiva",120,2000)
    lista_vehiculos.append(mi_vehiculo4)
    print(mi_vehiculo4)


def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(f"nombre de la clase: {vehiculo.class_name()}, sus atributos son: {vehiculo.atributes()}")


def catalogar_modificada(vehiculos,ruedas):
    cantidad=0
    for vehiculo in vehiculos:
        if vehiculo.ruedas==ruedas:
            cantidad=cantidad+1
    print(f"Se han encontrado {cantidad} vehiculos con {ruedas} ruedas")


catalogar(lista_vehiculos)
catalogar_modificada(lista_vehiculos,4)


