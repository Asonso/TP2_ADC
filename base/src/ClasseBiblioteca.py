class Biblioteca:
    def __init__(self):
        # Inicializa a coleção de livros como uma lista vazia
        self.colecao = []

    def adicionar_livro(self, titulo, autor, ano):
        # Cria um dicionário para representar o livro
        livro = {
            'titulo': titulo,
            'autor': autor,
            'ano': ano
        }
        # Adiciona o livro à coleção
        self.colecao.append(livro)
        print(f'O livro "{titulo}" foi adicionado à coleção.')

    def listar_livros(self):
        # Lista todos os livros da coleção
        if not self.colecao:
            print("A coleção está vazia.")
        else:
            print("Livros na coleção:")
            for i, livro in enumerate(self.colecao, start=1):
                print(f'{i}. {livro["titulo"]} por {livro["autor"]} ({livro["ano"]})')


# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605)
biblioteca.adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967)
biblioteca.listar_livros()
