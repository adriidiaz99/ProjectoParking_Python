class TicketService():

    def __init__(self, ticketRepository):
        self.__ticketRepository = ticketRepository


    def agregarTicket(self, other):
        self.__ticketRepository.addTicket(other)

    def eliminarTicket(self, other):
        self.__ticketRepository.removeTicket(other)

    def editarTicket(self, other):
        self.__ticketRepository.editTicket(other)

    def encontrarPorId(self, id):
        self.__ticketRepository.encontrarPorId(id)

    def encontrarTodos(self):
        self.__ticketRepository.encontrarTodos()
