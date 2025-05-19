class Artista:
    # É obrigatório ter um init nas classes. O init vai inicializar cada uma dessas variaveis que a classe tem, de forma a essa classe poder ser reutilizada.
    def __init__(self, nome, tipo_arte, bio, redes_sociais):
        self.nome = nome
        self.tipo_arte = tipo_arte
        self.bio = bio
        self.redes_sociais = redes_sociais
        self.obras = []

    # essa função adiciona uma nova obra dentro da array obras.
    def adicionar_obra(self, obra):
        self.obras.append(obra)

    # Basicamente vai converter um objeto em uma string, tipo um print formatado.
    def __str__(self):
        return f"Nome: {self.nome}, Tipo de Arte: {self.tipo_arte}, Redes Sociais: {self.redes_sociais}"

    # função que perpassa a cada um dos objetos da array e printa.
    # Se a array tiver objetos, ele printa. Se não ele não tenta pra não quebrar o codigo.
    def exibir_obras(self):
        if self.obras:
            for obra in self.obras:
                print(obra)
        else:
            print("Este artista ainda não tem obras cadastradas.")