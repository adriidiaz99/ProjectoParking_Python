class Vehiculo:
    def __init__(self, idVehiculo, nombre, matricula, combustible, duenyo):
        self.__idVehiculo = idVehiculo
        self.__nombre = nombre
        self.__matricula = matricula
        self.__combustible = combustible
        self.__duenyo = duenyo

    @property
    def idVehiculo(self):
        return self.__idVehiculo

    @id.setter
    def idVehiculo(self, idVehiculo):
        self.__idVehiculo = idVehiculo

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def combustible(self):
        return self.__combustible

    @combustible.setter
    def combustible(self, combustible):
        self.__combustible = combustible

    @property
    def duenyo(self):
        return self.__duenyo

    @duenyo.setter
    def duenyo(self, duenyo):
        self.__duenyo = duenyo

    def __str__(self):
        return " Nombre: " +self.nombre +" Matricula: " +self.matricula +" Combustible: " +self.combustible +" Dueño: " +self.duenyo

    def __eq__(self, other):
        if((self.idVehiculo == other.idVehiculo) or (self.matricula == other.matricula)):
            return True

        return False




