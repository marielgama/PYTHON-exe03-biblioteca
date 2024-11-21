
from Livro import Livro

class Biblioteca:
   def __init__(self, nome):
      self.nome = nome
      self.livros = []

   def adicionar_livro(self, livro):
       self.livros.append(livro)
       print(f'Livro "{livro.titulo}" adicionado à biblioteca "{self.nome}".')

   def remover_livro(self, isbn):
       for livro in self.livros:
           if livro.isbn == isbn:
               self.livros.remove(livro)
               print(f'Livro "{livro.titulo}" removido da biblioteca "{self.nome}".')
               return
       print(f'Livro com ISBN {isbn} não encontrado na biblioteca "{self.nome}".')

   def listar_livros(self):
       if not self.livros:
           print(f'A biblioteca "{self.nome}" não tem livros.')
       else:
           print(f'Livros na biblioteca "{self.nome}":')
           for livro in self.livros:
               print(f'- {livro.titulo} por {livro.autor} (ISBN: {livro.isbn})')


# Testando as classes

# Criando alguns livros
livro1 = Livro('O Senhor dos Anéis', 'J.R.R. Tolkien', '1234567890')
livro2 = Livro('1984', 'George Orwell', '0987654321')
livro3 = Livro('O Apanhador no Campo de Centeio', 'J.D. Salinger', '1122334455')

# Criando uma Biblioteca
biblioteca = Biblioteca('Biblioteca Central')

# Adicionando Livros a Biblioteca
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)
print(f'....................................................................................')
# Listando os livros da Biblioteca
biblioteca.listar_livros()
print(f'....................................................................................')
# Removendo Livro da Biblioteca
biblioteca.remover_livro('0987654321')