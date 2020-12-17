class VehiculoRepository:

    def __init__(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    @property
    def listaVehiculos(self):
        return self.__listaVehiculos

    @listaVehiculos.setter
    def listaVehiculos(self, listaVehiculos):
        self.__listaVehiculos = listaVehiculos

    def __str__(self):
        return " Lista de vehiculos: " +self.listaVehiculos

    def addVehiculo(self):
        self.__listaVehiculos.append()
