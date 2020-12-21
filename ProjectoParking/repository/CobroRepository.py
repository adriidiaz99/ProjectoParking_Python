from model.Cobro import Cobro


class CobroRepository:

    def __init__(self, listaCobro):
        self.__listaCobro = listaCobro

    @property
    def listaCobro(self):
        return self.__listaCobro

    @listaCobro.setter
    def listaCobro(self, listaCobro):
        self.__listaCobro = listaCobro

    def __str__(self):
        return " Lista de cobros: " +self.listaCobro

    def addCobro(self, other):
        self.__listaCobro.append(other)

    def removeCobro(self, other):
        self.__listaCobro.pop(self.__listaCobro.index(other))

    def editCobro(self, other):
        self.__listaCobro[self.__listaCobro.encontrarPorId(other.idCobro)] = other

    def encontrarPorId(self, id):

        cobro = Cobro(0, 0, "", 0)

        if len(self.__listaCobro) > 0:
            for element in self.__listaCobro:
                if element.idCobro == id:
                    cobro = element

        return cobro

    def encontrarTodos(self):
        return self.__listaCobro
