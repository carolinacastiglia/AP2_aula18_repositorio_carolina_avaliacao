from Livro import Livro

class Pilha:
    def __init__(self):
       self.topo = None
       self.tamanho = 0
    
    def adicionarLivro(self, valor):
        livro = valor

        if self.topo == None:
            self.topo = livro
        else:
            aux = self.topo
            self.topo = livro
            livro.proximo = aux
        self.tamanho += 1

    def imprimirLivros(self):
        txt = ""
        if self.topo == None:
            txt = "A Pilha de livros está vazia!"
        else:
            aux = self.topo
            txt = "LISTA DE LIVROS: \n"
            while(aux):
                txt += str(aux.titulo)
                txt += " - "
                txt += str(aux.autor.nome)
                txt += "\n"
                aux = aux.proximo
                
        print(txt,"\n")

    def removerLivro(self):
        if self.topo == None:
            print("Não é possível remover, pois a Pilha está vazia!\n")
        else:
            aux = self.topo
            self.topo = aux.proximo

            if self.tamanho != 0:
                if self.tamanho == 1:
                    self.topo == None
                self.tamanho -= 1