from model.Vehiculo import Vehiculo


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

    def addVehiculo(self, other):
        self.__listaVehiculos.append(other)

    def removeVehiculo(self, other):
        self.__listaVehiculos.pop(self.__listaVehiculos.index(other))

    def editVehiculo(self, other):
        self.__listaVehiculos[self.__listaVehiculos.encontrarPorId(other.idVehiculo)] = other

    def encontrarPorId(self, id):

        vehiculo = Vehiculo(0, "", "", 0, "")

        if len(self.__listaVehiculos) > 0:
            for element in self.__listaVehiculos:
                if element.idVehiculo == id:
                    vehiculo = element

        return vehiculo

    def encontrarTodos(self):
        return self.__listaVehiculos









