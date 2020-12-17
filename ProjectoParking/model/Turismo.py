from model.Vehiculo import Vehiculo


class Turismo(Vehiculo):

    def __init__(self, idVehiculo, nombre, matricula, combustible, duenyo, nPuertas):
        super().__init__(self, idVehiculo, nombre, matricula, combustible, duenyo)
        self.__nPuertas = nPuertas


    @property
    def nPuertas(self):
        return self.__nPuertas

    @nPuertas.setter
    def nPuertas(self, nPuertas):
        self.__nPuertas = nPuertas

    def __str__(self):
        return super.__str__() +" Número de puertas: " +self.nPuertas


