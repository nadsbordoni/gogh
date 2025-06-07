def mostrar_resumo_pagamento(obras):
    total = sum(obra.preco for obra in obras)

    print("\n🧾 RESUMO DA COMPRA")
    print("-" * 50)
    for obra in obras:
        print(f"{obra.titulo} - R${obra.preco:.2f}")
    print("-" * 50)
    print(f"TOTAL: R${total:.2f}\n")

    return total

def processar_pagamento(carrinho):
    if not carrinho.itens:
        print("\n❌ O carrinho está vazio. Adicione obras antes de finalizar a compra.")
        return False

    obras = carrinho.itens
    total = carrinho.calcular_total()

    mostrar_resumo_pagamento(obras)

    metodos = {
        '1': {'nome': 'Cartão de Crédito', 'parcelas': True},
        '2': {'nome': 'PIX', 'parcelas': False},
        '3': {'nome': 'Boleto', 'parcelas': False}
    }

    print("\n💳 MÉTODOS DE PAGAMENTO:")
    for cod, metodo in metodos.items():
        print(f"{cod} - {metodo['nome']}")

    while True:
        opcao = input("\nEscolha o método (1-3): ")
        if opcao in metodos:
            metodo = metodos[opcao]
            break
        print("Opção inválida!")

    if metodo['parcelas']:
        while True:
            try:
                parcelas = int(input("Número de parcelas (1-12): "))
                if 1 <= parcelas <= 12:
                    valor_parcela = total / parcelas
                    print(f"\nPagamento parcelado em {parcelas}x de R${valor_parcela:.2f}")
                    break
                else:
                    print("Digite um número entre 1 e 12.")
            except ValueError:
                print("Digite um número válido.")

    print(f"\nValor total: R${total:.2f}")
    confirmar = input("Confirmar pagamento? (S/N): ").strip().upper()
    if confirmar == 'S':
        gerar_recibo_pagamento(obras, total, metodo['nome'])
        carrinho.limpar()
        return True
    else:
        print("\n❌ Compra cancelada!")
        return False


def gerar_recibo_pagamento(obras, total, metodo_pagamento):
    print("\n📄 RECIBO DE COMPRA")
    print("=" * 50)
    for obra in obras:
        print(f"- {obra.titulo}: R${obra.preco:.2f}")
    print("=" * 50)
    print(f"Total: R${total:.2f}")
    print(f"Forma de pagamento: {metodo_pagamento}")
    print("\nObrigado por apoiar os artistas!")
