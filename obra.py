# Essa classe é responsável por criar um tipo obra. Esse tipo obra tem algumas caracteristicas especificas.
class Obra:
    # Init é obrigatorio em class.
    def __init__(self, titulo, descricao, preco, categoria):
        self.titulo = titulo
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria

    def __str__(self):
        return f"Título: {self.titulo}, Descrição: {self.descricao}, Preço: {self.preco}, Categoria: {self.categoria}"

    # Essa função é caso a pessoa queira fazer um edit em obra, colocar novo nome, ou valor ou tudo mais.
    def atualizar_obra(self, novo_titulo=None, nova_descricao=None, novo_preco=None, nova_categoria=None):
        if novo_titulo and novo_titulo != self.titulo:
            self.titulo = novo_titulo
        if nova_descricao and nova_descricao != self.descricao:
            self.descricao = nova_descricao
        if novo_preco and novo_preco != self.preco:
            self.preco = novo_preco
        if nova_categoria and nova_categoria != self.categoria:
            self.categoria = nova_categoria

        print(f"Obra '{self.titulo}' atualizada com sucesso!")
