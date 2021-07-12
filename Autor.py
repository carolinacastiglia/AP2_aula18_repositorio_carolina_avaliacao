class Autor:

    def __init_(self):
        self.__id = None
        self.nome = None
    
    def cadastrarAutor(self, id, nome):
        self.__id = id
        self.nome = nome
    
    def imprimirAutor(self):
        print("ID", self.__id, "- NOME AUTOR:", self.nome, )