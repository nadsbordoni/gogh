from obra import Obra
from artista import Artista

def criar_obra(artista):
    if not isinstance(artista, Artista):
        print("Erro: O artista informado não é válido.")
        return

    print("\n--- Cadastro de Nova Obra ---")

    titulo = input("Título da obra: ")
    descricao = input("Descrição da obra: ")

    while True:
        try:
            preco = float(input("Preço da obra (R$): "))
            break
        except ValueError:
            print("Por favor, digite um número válido para o preço.")

    categoria = input("Categoria da obra: ")
    
    variacoes_input = input("Variações (cores/tamanhos etc., separadas por vírgula): ")
    variacoes = [v.strip() for v in variacoes_input.split(",")] if variacoes_input else []

    try:
        nova_obra = Obra(
            titulo=titulo,
            artista=artista,
            preco=preco,
            descricao=descricao,
            categoria=categoria,
            variacoes=variacoes
        )
        artista.adicionar_obra(nova_obra)
        print(f"\n✅ Obra '{titulo}' adicionada ao artista {artista.nome} com sucesso!\n")
        return nova_obra
    except Exception as e:
        print(f"Erro ao criar obra: {e}")
        return None
