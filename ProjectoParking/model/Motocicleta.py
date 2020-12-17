from model.Vehiculo import Vehiculo


class Motocicleta(Vehiculo):

    def __init__(self, idVehiculo, nombre, matricula, combustible, duenyo):
        super().__init__(self, idVehiculo, nombre, matricula, combustible, duenyo)
