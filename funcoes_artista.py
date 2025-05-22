# Importa artista porque vai usar o objeto
from artista import Artista

# Função para criar artista
# Aqui ele tenta criar um um Artista que foi definido em outra classe (artista.py), caso ele consiga ele retorna um objeto to tipo artista
# Se ele não conseguir ele manda um erro dizendo que não conseguiu.
        def cadastrar_artista():
    print("\n--- Cadastro de Artista ---")
    nome = input("Nome do artista: ")
    tipo_arte = input("Tipo de arte: ")
    bio = input("Biografia curta: ")
    redes_sociais = input("Redes sociais (ex: @usuario): ")

    artista = Artista(nome, tipo_arte, bio, redes_sociais)

    while True:
        adicionar = input("Deseja adicionar uma obra? (s/n): ").lower()
        if adicionar == 's':
            obra = input("Nome da obra: ")
            artista.adicionar_obra(obra)
        elif adicionar == 'n':
            break
        else:
            print("Opção inválida. Digite 's' para sim ou 'n' para não.")

    artistas.append(artista)
    print(f"Artista '{nome}' cadastrado com sucesso!\n")

