from model.Ticket import Ticket


class TicketRepository:

    def __init__(self, listaTicket):
        self.__listaTicket = listaTicket

    @property
    def listaTicket(self):
        return self.__listaTicket

    @listaTicket.setter
    def listaTicket(self, listaTicket):
        self.__listaTicket = listaTicket

    def __str__(self):
        return " Lista de tickets: " +self.listaTicket

    def addTicket(self, other):
        self.__listaTicket.append(other)

    def removeTicket(self, other):
        self.__listaTicket.pop(self.__listaTicket.index(other))

    def editTicket(self, other):
        self.__listaTicket[self.__listaTicket.encontrarPorId(other.idTicket)] = other

    def encontrarPorId(self, id):

        ticket = Ticket(0, 0, "", 0, "")

        if len(self.__listaTicket) > 0:
            for element in self.__listaTicket:
                if element.idTicket == id:
                    ticket = element

        return ticket

    def encontrarTodos(self):
        return self.__listaTicket
