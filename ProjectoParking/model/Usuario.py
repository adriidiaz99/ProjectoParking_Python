class Usuario:

    def __init__(self, idUsuario, apellido1, apellido2):

        self.__idUsuario = idUsuario
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2

    @property
    def idUsuario(self):
        return self.__idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsuario):
        self.__idUsuario = idUsuario

    @property
    def apellido1(self):
        return self.__apellido1

    @apellido1.setter
    def apellido1(self, apellido1):
        self.__apellido1 = apellido1

    @property
    def apellido2(self):
        return self.__apellido2

    @apellido2.setter
    def apellido2(self, apellido2):
        self.__apellido2 = apellido2

    def __str__(self):
        return "Id usuario: " +self.idUsuario +" Apellidos: " +self.apellido1 + " " +self.apellido2
