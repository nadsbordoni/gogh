from obra import Obra
from artista import Artista


# Função para criar obra
# Lembrando que ele usa a função .adicionar_obra porque a gente criou essa função em outro arquivo (no artista.py). É tipo um append.
# Aqui ele faz duas checagens. Primeiro ele checa se artista é um objeto do tipo artista, se for ele tenta. Se não for ele já diz que o artista não é valido.
# No segundo erro realmente não deu pra criar a obra.
def criar_obra(artista, titulo, descricao, preco, categoria):
    try:
        if isinstance(artista, Artista):  # Verifica se o artista é uma instância da classe Artista
            obra = Obra(titulo, descricao, preco, categoria)
            artista.adicionar_obra(obra)  # Adiciona a obra ao artista
            print(f"Obra '{titulo}' adicionada ao artista {artista.nome}.")
        else:
            print("Erro: O artista informado não é válido.")
    except Exception as e:
        print(f"Erro ao criar obra: {e}")
