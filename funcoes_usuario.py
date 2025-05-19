from usuario import Usuario

# Função para criar usuário
# Tenta criar um usuário e retorna ele, se der erro, diz que não conseguiu.
def criar_usuario(nome, email, senha, endereco):
    try:
        usuario = Usuario(nome, email, senha, endereco)
        print(f"Usuário {nome} criado com sucesso!")
        return usuario
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")