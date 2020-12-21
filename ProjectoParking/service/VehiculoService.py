class VehiculoService():

    def __init__(self, vehiculoRepository):
        self.__vehiculoRepository = vehiculoRepository


    def agregarVehiculo(self, other):
        self.__vehiculoRepository.addVehiculo(other)

    def eliminarVehiculo(self, other):
        self.__vehiculoRepository.removeVehiculo(other)

    def editarVehiculo(self, other):
        self.__vehiculoRepository.editVehiculo(other)

    def encontrarPorId(self, id):
        self.__vehiculoRepository.encontrarPorId(id)

    def encontrarTodos(self):
        self.__vehiculoRepository.encontrarTodos()
