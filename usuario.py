class Usuario:
    def __init__(self, nome, idade, email, senha, cidade, estado, cep, endereco, numero, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.senha = senha
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.endereco = endereco
        self.numero = numero
        self.telefone = telefone

    def atualizar_usuario(self, nome=None, idade=None, email=None, senha=None,
                          cidade=None, estado=None, cep=None,
                          endereco=None, numero=None, telefone=None):
        if nome: self.nome = nome
        if idade: self.idade = idade
        if email: self.email = email
        if senha: self.senha = senha
        if cidade: self.cidade = cidade
        if estado: self.estado = estado
        if cep: self.cep = cep
        if endereco: self.endereco = endereco
        if numero: self.numero = numero
        if telefone: self.telefone = telefone

        print(f"Usuário {self.nome} atualizado com sucesso!")

    def __str__(self):
        return (
            f"Usuário: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Email: {self.email}\n"
            f"Telefone: {self.telefone}\n"
            f"Endereço: {self.endereco}, Nº {self.numero}, {self.cidade} - {self.estado}, CEP: {self.cep}"
        )