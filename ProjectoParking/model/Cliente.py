from model.Usuario import Usuario


class Cliente(Usuario):

    def __init__(self, idUsuario, apellido1, apellido2, vehiculo, dni, nTarjetaCredito, tipoAbono, nPlaza, email):
        super().__init__(idUsuario, apellido1, apellido2)
        self.__vehiculo = vehiculo
        self.__dni = dni
        self.__nTarjetaCredito = nTarjetaCredito
        self.__tipoAbono = tipoAbono
        self.__nPlaza = nPlaza
        self.__email = email

    @property
    def idVehiculo(self):
        return self.__idVehiculo

    @idVehiculo.setter
    def idVehiculo(self, idVehiculo):
        self.__idVehiculo = idVehiculo

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

