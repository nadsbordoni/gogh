class Obra:
    id_counter = 1

    def __init__(self, titulo, artista, preco, descricao, categoria, variacoes=None, nota=None):
        self.id = Obra.id_counter
        Obra.id_counter += 1

        self.titulo = titulo
        self.artista = artista
        self.preco = preco
        self.descricao = descricao
        self.categoria = categoria
        self.variacoes = variacoes or []
        self.nota = nota

    def __str__(self):
        variacoes_str = ", ".join(self.variacoes) if self.variacoes else "Nenhuma"
        return (
            f"Obra: {self.titulo} (ID: {self.id})\n"
            f"Artista: {self.artista}\n"
            f"Preço: R${self.preco:.2f}\n"
            f"Categoria: {self.categoria}\n"
            f"Descrição: {self.descricao}\n"
            f"Variações: {variacoes_str}"
        )

    def avaliar(self, nota):
        if 0 <= nota <= 10:
            self.nota = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 10.")