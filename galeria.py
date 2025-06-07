from obra import Obra

class Galeria:
    def __init__(self):
        self.obras = [
            Obra("Noite Estrelada", "Van Gogh", 250.00, "Clássico da pintura pós-impressionista", "Pintura"),
            Obra("Girassóis", "Van Gogh", 180.00, "Obra vibrante com girassóis amarelos", "Pintura"),
            Obra("O Grito", "Edvard Munch", 300.00, "Expressão intensa de angústia existencial", "Expressionismo"),
            Obra("A Persistência da Memória", "Dalí", 275.00, "Relógios derretendo no deserto surreal", "Surrealismo")
        ]

    def mostrar_galeria(self):
        print("\n" + "═" * 50)
        print("GALERIA DE ARTE".center(50))
        print("═" * 50 + "\n")

        for i, obra in enumerate(self.obras, 1):
            print(f"{i}. {obra.titulo.upper()}")
            print(f"Artista: {obra.artista}")
            print(f"Preço: R${obra.preco:.2f}")
            if obra.nota is not None:
                print(f"Avaliação: {obra.nota}/10")
            print("\n" + "─" * 45)

    def avaliar_obras(self):
        print("\nAVALIE AS OBRAS (0-10):\n")
        for obra in self.obras:
            while True:
                try:
                    nota = float(input(f'Qual a sua nota para "{obra.titulo}"?: '))
                    if 0 <= nota <= 10:
                        obra.avaliar(nota)
                        break
                    print("Digite um valor entre 0 e 10")
                except ValueError:
                    print("Por favor, digite apenas números")

    def adicionar_ao_carrinho(self, carrinho):
        while True:
            escolha = input("\nDigite o número da obra para adicionar ao carrinho (ou '0' para voltar): ")
            if escolha == '0':
                break
            try:
                indice = int(escolha) - 1
                if 0 <= indice < len(self.obras):
                    carrinho.adicionar_obra(self.obras[indice])
                else:
                    print("Número inválido, tente novamente.")
            except ValueError:
                print("Por favor, digite um número válido.")
