import datetime

class Cobro:

    def __init__(self, idCobro, nPlaza, matricula, cCobro):
        self.__idCobro = idCobro
        self.__nPlaza = nPlaza
        self.__matricula = matricula
        self.__cCobro = cCobro
        self.__fechaCobro = datetime.datetime.now()

    @property
    def idCobro(self):
        return self.__idCobro

    @idCobro.setter
    def idCobro(self, idCobro):
        self.__idCobro = idCobro

    @property
    def fechaCobro(self):
        return self.__fechaCobro

    @fechaCobro.setter
    def fechaCobro(self, fechaCobro):
        self.__fechaCobro = fechaCobro

    @property
    def nPlaza(self):
        return self.__nPlaza

    @nPlaza.setter
    def nPlaza(self, nPlaza):
        self.__nPlaza = nPlaza

    @property
    def cCobro(self):
        return self.__cCobro

    @cCobro.setter
    def cCobro(self, cCobro):
        self.__cCobro = cCobro

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return "Id cobro: " +self.idCobro +" Matricula: " +self.matricula +" Fecha de cobro: " +self.fechaCobro +" Cantidad " +self.cCobro
