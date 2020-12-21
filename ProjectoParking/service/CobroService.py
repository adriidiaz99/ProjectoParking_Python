import datetime

class CobroService():

    def __init__(self, cobroRepository):
        self.__cobroRepository = cobroRepository


    def agregarCobro(self, other):
        self.__cobroRepository.addCobro(other)

    def eliminarCobro(self, other):
        self.__cobroRepository.removeCobro(other)

    def editarCobro(self, other):
        self.__cobroRepository.editCobro(other)

    def encontrarPorId(self, id):
        self.__cobroRepository.encontrarPorId(id)

    def encontrarTodos(self):
        self.__cobroRepository.encontrarTodos()

    def encontrarEntreTramoFecha(self, fechaReciente, fechaAntigua):
        lista = []

        for element in self.encontrarTodos():
            if element.fechaCobro > fechaAntigua and element.fechaCobro < element.fechaReciente:
                lista.append(element)

        return lista

    #Añadir imprimitListaCobros
