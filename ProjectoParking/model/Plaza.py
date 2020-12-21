from model.Vehiculo import Vehiculo


class Plaza:

    def __init__(self, nPlaza, cliente, pin, estado):
        self.__nPlaza = nPlaza
        self.__vehiculo = Vehiculo(0, "", "", 0, "")
        self.__cliente = cliente
        self.__pin = pin
        self.__estado = estado

    @property
    def nPlaza(self):
        return self.__nPlaza

    @nPlaza.setter
    def nPlaza(self, nPlaza):
        self.__nPlaza = nPlaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado):
        self.__estado = estado



    def __str__(self):
        return "Número de plaza: " +self.nPlaza +" Vehiculo: " +self.vehiculo +" Dueño: " +self.cliente +" Estado: " +self.__estado
