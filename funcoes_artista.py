from artista import Artista
from obra import Obra

artistas = []

def cadastrar_artista():
    print("\n--- Cadastro de Artista ---")
    nome = input("Nome do artista: ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")

    email = input("Email: ").strip()
    senha = input("Senha: ").strip()

    local = input("Local (cidade - estado): ")
    descricao = input("Descrição ou biografia do artista: ")

    # Perguntar quantos tipos de obra o artista trabalha
    while True:
        try:
            qtd_tipos = int(input("Com quantos tipos de obra você trabalha? "))
            if qtd_tipos > 0:
                break
            else:
                print("Digite um número maior que zero.")
        except ValueError:
            print("Digite um número válido.")

    tipos_obra = []
    for i in range(qtd_tipos):
        tipo = input(f"Digite o tipo de obra #{i+1}: ").strip()
        while not tipo:
            print("Tipo inválido, não pode ser vazio.")
            tipo = input(f"Digite o tipo de obra #{i+1}: ").strip()
        tipos_obra.append(tipo)

    artista = Artista(nome, idade, local, descricao, tipos_obra, email, senha)

    while True:
        adicionar = input("Deseja adicionar uma obra agora? (s/n): ").lower()
        if adicionar == 's':
            adicionar_nova_obra(artista)
        elif adicionar == 'n':
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    artistas.append(artista)
    print(f"\n✅ Artista '{nome}' cadastrado com sucesso com {len(artista.obras)} obra(s)!\n")
    return artista

def adicionar_nova_obra(artista):
    print("\n--- Cadastro de Obra ---")
    titulo = input("Título da obra: ")
    while True:
        try:
            preco = float(input("Preço da obra (R$): "))
            break
        except ValueError:
            print("Preço inválido. Digite um número válido.")

    descricao_obra = input("Descrição da obra: ")
    categoria = input("Categoria da obra: ")
    variacoes_input = input("Variações (cores/tamanhos etc., separadas por vírgula): ")
    variacoes = [v.strip() for v in variacoes_input.split(",")] if variacoes_input else []

    nova_obra = Obra(
        titulo=titulo,
        artista=artista,
        preco=preco,
        descricao=descricao_obra,
        categoria=categoria,
        variacoes=variacoes
        )
    artista.adicionar_obra(nova_obra)
    print(f"Obra '{titulo}' adicionada com sucesso!")

def login_artista(email, senha):
    for artista in artistas:
        if artista.email == email and artista.senha == senha:
            print(f"\n🔓 Login realizado com sucesso! Bem-vindo(a), {artista.nome}.\n")
            return artista
    print("\n❌ E-mail ou senha inválidos.\n")
    return None
