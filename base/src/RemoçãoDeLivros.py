class Biblioteca:
    def __init__(self):
        self.colecao = []

    def adicionar_livro(self, titulo, autor, ano, categoria):
        livro = {
            'titulo': titulo,
            'autor': autor,
            'ano': ano,
            'categoria': categoria
        }
        self.colecao.append(livro)
        print(f'O livro "{titulo}" foi adicionado à coleção.')

    def listar_livros(self):
        if not self.colecao:
            print("A coleção está vazia.")
        else:
            print("Livros na coleção:")
            for i, livro in enumerate(self.colecao, start=1):
                print(f'{i}. {livro["titulo"]} por {livro["autor"]} ({livro["ano"]}), Categoria: {livro["categoria"]}')

    def remover_livro(self, titulo):
        for livro in self.colecao:
            if livro['titulo'].lower() == titulo.lower():  # Busca case-insensitive
                self.colecao.remove(livro)
                print(f'O livro "{titulo}" foi removido da coleção.')
                return
        print(f'O livro "{titulo}" não foi encontrado na coleção.')

# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605, "Romance")
biblioteca.adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Realismo Mágico")

# Removendo um livro
biblioteca.remover_livro("Dom Quixote")
biblioteca.listar_livros()
