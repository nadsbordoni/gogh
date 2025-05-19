class Usuario:
    def __init__(self, nome, email, senha, endereco):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
    
    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Endereço: {self.endereco}"

    # função para atualizar o usuario. Ele checa primeiro se a variável é diferente da anterior, se for ele muda.
    def atualizar_usuario(self, nome=None, email=None, senha=None, endereco=None):
        if nome:
            self.nome = nome
        if email:
            self.email = email
        if senha:
            self.senha = senha
        if endereco:
            self.endereco = endereco
        print(f"Usuário {self.nome} atualizado com sucesso!")