class livro:
    def __init__(self, titulo, autor, ano, paginas):
        self.titulo,self.autor,self.ano,self.paginas,self.disponivel = titulo, autor, ano, paginas, True
        status = "disponivel " if self.disponivel else "indisponivel"
        return f"'{self.titulo} por {self.autor} Ano :{self.ano} Paginas : {self.paginas} Status {status}
class Biblioteca:
    def __init__(self):
        livros = []
    def adicionar_livros(self, livro):
        self.livros.append(livro)
        print("o livro foi adicionado")
    def procurar_livro(self,titulo):
        if titulo
        
        