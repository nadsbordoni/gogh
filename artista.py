class Artista:
    def __init__(self, nome, idade, local, descricao, tipos_obra, email, senha):
        self.nome = nome
        self.idade = idade
        self.local = local
        self.descricao = descricao
        self.tipos_obra = tipos_obra
        self.email = email
        self.senha = senha
        self.obras = []

    def adicionar_obra(self, obra):
        self.obras.append(obra)

    def exibir_obras(self):
        if self.obras:
            print(f"\nObras disponíveis de {self.nome}:")
            for obra in self.obras:
                print(obra)
        else:
            print(f"{self.nome} ainda não tem obras cadastradas.")

    def apagar_todas_obras(self):
        confirmacao = input(f"Tem certeza que deseja apagar TODAS as obras de {self.nome}? (s/n): ").lower()
        if confirmacao == 's':
            self.obras.clear()
            print("🗑️ Todas as obras foram removidas com sucesso.")
        else:
            print("❌ Ação cancelada. Nenhuma obra foi removida.")

    def __str__(self):
        tipos = ", ".join(self.tipos_obra)
        return (
            f"Artista: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Local: {self.local}\n"
            f"Email: {self.email}\n"
            f"Descrição: {self.descricao}\n"
            f"Tipos de Obra: {tipos}\n"
            f"Total de Obras: {len(self.obras)}"
        )
