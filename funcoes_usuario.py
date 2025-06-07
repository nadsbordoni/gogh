from usuario import Usuario

usuarios_cadastrados = []

def criar_usuario():
    print("\n--- Cadastro de Novo Usuário ---")

    nome = input("Nome completo: ")
    
    while True:
        try:
            idade = int(input("Idade: "))
            break
        except ValueError:
            print("Idade inválida. Digite um número inteiro.")
    
    email = input("E-mail: ")
    senha = input("Senha: ")

    cidade = input("Cidade: ")
    estado = input("Estado: ")
    cep = input("CEP: ")

    endereco = input("Nome da rua/avenida: ")
    numero = input("Número da residência: ")
    telefone = input("Telefone (com DDD): ")

    # Checar se o e-mail já existe
    for usuario in usuarios_cadastrados:
        if usuario.email == email:
            print("Erro: Já existe um usuário com esse e-mail.")
            return None

    try:
        novo_usuario = Usuario(
            nome=nome,
            idade=idade,
            email=email,
            senha=senha,
            cidade=cidade,
            estado=estado,
            cep=cep,
            endereco=endereco,
            numero=numero,
            telefone=telefone
        )
        usuarios_cadastrados.append(novo_usuario)
        print(f"\n✅ Usuário '{nome}' cadastrado com sucesso!\n")
        return novo_usuario
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        return None

def login_usuario(email, senha):
    for usuario in usuarios_cadastrados:
        if usuario.email == email and usuario.senha == senha:
            print(f"\n🔓 Login realizado com sucesso! Bem-vindo(a), {usuario.nome}.\n")
            return usuario
    print("\n❌ E-mail ou senha inválidos.\n")
    return None
