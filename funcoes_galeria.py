def interagir_com_usuario(galeria, carrinho):
    while True:
        galeria.mostrar_galeria()
        print("O que você deseja fazer?")
        print("1 - Avaliar obras")
        print("2 - Adicionar obra ao carrinho")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            galeria.avaliar_obras()
        elif opcao == '2':
            galeria.adicionar_ao_carrinho(carrinho)
        elif opcao == '0':
            print("Voltando...")
            break
        else:
            print("Opção inválida, tente novamente.")