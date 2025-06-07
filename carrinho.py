from obra import Obra
from usuario import Usuario

class Carrinho:
    def __init__(self, usuario):
        self.usuario = usuario
        self.itens = []

    def adicionar_obra(self, obra):
        if isinstance(obra, Obra):
            self.itens.append(obra)
            print(f"Obra '{obra.titulo}' adicionada ao carrinho.")
        else:
            print("Erro: item inválido. Só é possível adicionar objetos do tipo Obra.")

    def calcular_total(self):
        return sum(obra.preco for obra in self.itens)

    def exibir_carrinho(self):
        print(f"\nCarrinho de Compras de {self.usuario.nome}:")
        if not self.itens:
            print("Carrinho vazio.")
            return
        for obra in self.itens:
            print(f"\n{obra}")
        print("\n" + "-" * 40)
        print(f"Total: R${self.calcular_total():.2f}")

    def remover_obra_por_id(self, id_obra):
        for obra in self.itens:
            if obra.id == id_obra:
                self.itens.remove(obra)
                print(f"Obra '{obra.titulo}' removida do carrinho.")
                return
        print(f"Nenhuma obra com ID {id_obra} foi encontrada no carrinho.")

    def limpar(self):
        self.itens.clear()
        print("Carrinho esvaziado com sucesso.")
