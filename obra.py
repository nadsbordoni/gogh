obras = [
    {"titulo": "Noite Estrelada", "artista": "Van Gogh", "preco": 250.00, "nota": None},
    {"titulo": "Girassóis", "artista": "Van Gogh", "preco": 180.00, "nota": None},
    {"titulo": "O Grito", "artista": "Edvard Munch", "preco": 300.00, "nota": None},
    {"titulo": "A Persistência da Memória", "artista": "Dalí", "preco": 275.00, "nota": None}
]

def mostrar_galeria():
    print("\n" + "═" * 50)
    print("GALERIA DE ARTE".center(50))
    print("═" * 50 + "\n")
    
    for i, obra in enumerate(obras, 1):
        print(f" {obra['titulo'].upper()}")
        print(f" Artista: {obra['artista']}")
        print(f" Preço: R${obra['preco']:.2f}")
        if obra['nota'] is not None:
            print(f" Sua avaliação: {obra['nota']}/10")
        print("\n" + "─" * 45)

def avaliar_obras():
    print("\nAVALIE AS OBRAS (0-10):\n")
    for obra in obras:
        while True:
            try:
                nota = float(input(f'Qual a sua nota para "{obra["titulo"]}"?: '))
                if 0 <= nota <= 10:
                    obra['nota'] = nota
                    break
                print("Digite um valor entre 0 e 10")
            except ValueError:
                print("Por favor, digite apenas números")


mostrar_galeria()
avaliar_obras()
print("\n" + "═" * 50)
print("OBRIGADO POR VISITAR NOSSA GALERIA!".center(50))
print("═" * 50 + "\n")
mostrar_galeria()