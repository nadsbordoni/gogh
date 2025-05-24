class Obra:
    def __init__(self, id, titulo, artista, preco):
        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.preco = preco

class Galeria:
    def __init__(self):
        self.obras = [
            Obra(1, "Noite Estrelada", "Van Gogh", 250.00),
            Obra(2, "Girassóis", "Van Gogh", 180.00),
            Obra(3, "O Grito", "Edvard Munch", 300.00),
            Obra(4, "A Persistência da Memória", "Dalí", 275.00)
        ]
    
    def mostrar_obras(self):
        print("\nOBRAS DISPONÍVEIS:")
        print("-"*50)
        for obra in self.obras:
            print(f"{obra.id}. {obra.titulo} - {obra.artista}")
            print(f"   Preço: R${obra.preco:.2f}\n")

class PagamentoGogh:
    def __init__(self, obras_selecionadas):
        self.obras = obras_selecionadas
        self.total = sum(obra.preco for obra in obras_selecionadas)
        self.metodos = {
            '1': {'nome': 'Cartão de Crédito', 'parcelas': True},
            '2': {'nome': 'PIX', 'parcelas': False},
            '3': {'nome': 'Boleto', 'parcelas': False}
        }
    
    def mostrar_resumo(self):
        print("\nSUA COMPRA:")
        print("-"*50)
        for obra in self.obras:
            print(f"{obra.titulo} - R${obra.preco:.2f}")
        print("-"*50)
        print(f"TOTAL: R${self.total:.2f}\n")

    def processar_pagamento(self):
        print("\nMÉTODOS DE PAGAMENTO:")
        for cod, metodo in self.metodos.items():
            print(f"{cod} - {metodo['nome']}")
        
        while True:
            opcao = input("\nEscolha o método (1-3): ")
            if opcao in self.metodos:
                metodo = self.metodos[opcao]
                break
            print("\n Opção inválida!")
        
        if metodo['parcelas']:
            parcelas = int(input("Número de parcelas (1-12): "))
            valor_parcela = self.total / parcelas
            print(f"\nPagamento parcelado em {parcelas}x de R${valor_parcela:.2f}")
        
        print(f"\nValor total: R${self.total:.2f}")
        if input("Confirmar pagamento? (S/N): ").upper() == 'S':
            print("\n Compra realizada com sucesso!")
            self.gerar_recibo(metodo['nome'])
        else:
            print("\n Compra cancelada!")

    def gerar_recibo(self, metodo):
        print("\nRECIBO DE COMPRA")
        print("="*50)
        for obra in self.obras:
            print(f"- {obra.titulo}: R${obra.preco:.2f}")
        print("="*50)
        print(f"Total: R${self.total:.2f}")
        print(f"Forma de pagamento: {metodo}")
        print("\nObrigado por apoiar os artistas!")

def main():
    galeria = Galeria()
    carrinho = []
    
    while True:
        galeria.mostrar_obras()
        try:
            escolha = int(input("\nDigite o número da obra que deseja (0 para finalizar): "))
            if escolha == 0:
                break
            obra_selecionada = next((obra for obra in galeria.obras if obra.id == escolha), None)
            if obra_selecionada:
                carrinho.append(obra_selecionada)
                print(f"\n✅ {obra_selecionada.titulo} adicionada ao carrinho!")
            else:
                print("Número inválido!")
        except ValueError:
            print("Digite apenas números!")
    
    if carrinho:
        pagamento = PagamentoGogh(carrinho)
        pagamento.mostrar_resumo()
        pagamento.processar_pagamento()
    else:
        print("\nNenhuma obra selecionada. Até logo!")

if __name__ == "__main__":
    main()
