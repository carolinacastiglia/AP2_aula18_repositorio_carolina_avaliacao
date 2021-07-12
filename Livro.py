class Livro:

    def __init__(self):
        self.id = None
        self.titulo = None
        self.autor = None
        self.proximo = None
    
    def cadastrarLivro(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
    
    def imprimirLivroExemplar(self):
        print("AUTOR:", self.autor.nome, "- TÍTULO:", self.titulo)