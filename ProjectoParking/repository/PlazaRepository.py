from model.Plaza import Plaza


class PlazaRepository:

    def __init__(self, listaPlaza):
        self.__listaPlaza = listaPlaza

    @property
    def listaPlaza(self):
        return self.__listaPlaza

    @listaPlaza.setter
    def listaPlaza(self, listaPlaza):
        self.__listaPlaza = listaPlaza

    def __str__(self):
        return " Lista de plazas: " +self.listaPlaza

    def addPlaza(self, other):
        self.__listaPlaza.append(other)

    def removePlaza(self, other):
        self.__listaPlaza.pop(self.__listaPlaza.index(other))

    def editPlaza(self, other):
        self.__listaPlaza[self.__listaPlaza.encontrarPorId(other.idPlaza)] = other

    def encontrarPorId(self, id):

        plaza = Plaza(0, "", 0, False)

        if len(self.__listaPlaza) > 0:
            for element in self.__listaPlaza:
                if element.idPlaza == id:
                    plaza = element

        return plaza

    def encontrarTodos(self):
        return self.__listaPlaza
