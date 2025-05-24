class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, obra):
        self.itens.append(obra)

    def calcular_total(self):
        return sum(obra.preco for obra in self.itens)

    def exibir_carrinho(self):
        print("\nCarrinho de Compras:")
        if not self.itens:
            print("Carrinho vazio.")
            return
        for obra in self.itens:
            print(f"- {obra}")
        print(f"Total: R${self.calcular_total():.2f}")

