class PlazaService():

    def __init__(self, plazaRepository, servicioTicket, servicioVehiculo):
        self.__plazaRepository = plazaRepository


    def agregarPlaza(self, other):
        self.__plazaRepository.addPlaza(other)

    def eliminarPlaza(self, other):
        self.__plazaRepository.removePlaza(other)

    def editarPlaza(self, other):
        self.__plazaRepository.editPlaza(other)

    def encontrarPorId(self, id):
        self.__plazaRepository.encontrarPorId(id)

    def encontrarTodos(self):
        self.__plazaRepository.encontrarTodos()

    def aparcarVehiculoCliente(self, matricula, dni):
        cliente = self.
