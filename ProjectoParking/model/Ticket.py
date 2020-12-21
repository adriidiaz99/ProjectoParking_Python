import datetime

class Ticket:

    def __init__(self, idTicket, nPlaza, matricula, pin, duenyo):
        self.__idTicket = idTicket
        self.__nPlaza = nPlaza
        self.__matricula = matricula
        self.__pin = pin
        self.__duenyo = duenyo
        self.__fechaDeposito = datetime.datetime.now()

    @property
    def idTicket(self):
        return self.__idTicket

    @idTicket.setter
    def idTicket(self, idTicket):
        self.__idTicket = idTicket

    @property
    def fechaDeposito(self):
        return self.__fechaDeposito

    @fechaDeposito.setter
    def fechaDeposito(self, fechaDeposito):
        self.__fechaDeposito = fechaDeposito

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
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def duenyo(self):
        return self.__duenyo

    @duenyo.setter
    def duenyo(self, duenyo):
        self.__duenyo = duenyo

    def __str__(self):
        return "Id ticket: " +self.idTicket +" Matricula: " +self.matricula +" Dueño: " +self.duenyo +" Fecha de deposito: " +self.fechaDeposito
