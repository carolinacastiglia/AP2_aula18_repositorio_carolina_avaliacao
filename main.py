from Autor import Autor
from Livro import Livro
from Pilha import Pilha

class main:

    print("------- AUTOR -------")
    a1 = Autor()
    a1.cadastrarAutor(1, "Stephen King")

    a2 = Autor()
    a2.cadastrarAutor(2, "Agatha Christie")

    a3 = Autor()
    a3.cadastrarAutor(3, "Jojo Moyes")

    a1.imprimirAutor()
    a2.imprimirAutor()
    a3.imprimirAutor()
    
    print("------- LIVRO -------")
    l1 = Livro()
    l1.cadastrarLivro(1, "It", a1)

    l2 = Livro()
    l2.cadastrarLivro(2, "O Iluminado", a1)

    l3 = Livro()
    l3.cadastrarLivro(3, "O assassinato de Roger Ackroyd", a2)

    l4 = Livro()
    l4.cadastrarLivro(4, "Como eu era antes de você", a3)

    l5 = Livro()
    l5.cadastrarLivro(5, "Depois de você", a3)

    l6 = Livro()
    l6.cadastrarLivro(6, "Ainda sou eu", a3)

    l1.imprimirLivroExemplar()
    l2.imprimirLivroExemplar()
    l3.imprimirLivroExemplar()
    l4.imprimirLivroExemplar()
    l5.imprimirLivroExemplar()
    l6.imprimirLivroExemplar()

    print("------- Pilha -------")

    p = Pilha()
    p.imprimirLivros()
    p.removerLivro()

    p.adicionarLivro(l1)
    p.adicionarLivro(l2)
    p.adicionarLivro(l3)

    p.imprimirLivros()
    p.removerLivro()
    p.imprimirLivros()

    p.adicionarLivro(l4)
    p.adicionarLivro(l5)
    p.adicionarLivro(l6)

    p.imprimirLivros()
    p.removerLivro()
    p.removerLivro()
    p.imprimirLivros()