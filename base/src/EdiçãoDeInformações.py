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

    def editar_livro(self, titulo, novo_titulo=None, novo_autor=None, novo_ano=None, nova_categoria=None):
        for livro in self.colecao:
            if livro['titulo'].lower() == titulo.lower():  # Busca case-insensitive
                if novo_titulo:
                    livro['titulo'] = novo_titulo
                if novo_autor:
                    livro['autor'] = novo_autor
                if novo_ano:
                    livro['ano'] = novo_ano
                if nova_categoria:
                    livro['categoria'] = nova_categoria
                print(f'O livro "{titulo}" foi atualizado com sucesso.')
                return
        print(f'O livro "{titulo}" não foi encontrado na coleção.')

# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.adicionar_livro("Dom Quixote", "Miguel de Cervantes", 1605, "Romance")
biblioteca.adicionar_livro("Cem Anos de Solidão", "Gabriel García Márquez", 1967, "Realismo Mágico")

# Editando as informações de um livro
biblioteca.editar_livro("Dom Quixote", novo_titulo="Dom Quixote de La Mancha", nova_categoria="Clássico")
biblioteca.listar_livros()
