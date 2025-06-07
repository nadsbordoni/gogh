from funcoes_usuario import criar_usuario, login_usuario, usuarios_cadastrados
from funcoes_galeria import interagir_com_usuario
from carrinho import Carrinho
from galeria import Galeria
from funcoes_pagamento import processar_pagamento
from funcoes_artista import cadastrar_artista, artistas, login_artista, adicionar_nova_obra

def menu_login():
    while True:
        print("\n--- Bem-vindo ao Gogh ---")
        print("1 - Criar novo usuário")
        print("2 - Criar novo artista")
        print("3 - Fazer login usuário")
        print("4 - Fazer login artista")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            usuario = criar_usuario()
            if usuario:
                print("Você pode agora fazer login para continuar.")

        elif escolha == '2':
            artista = cadastrar_artista()
            if artista:
                print("Você pode agora fazer login para continuar")

        elif escolha == '3':
            if not usuarios_cadastrados:
                print("\n❌ Nenhum usuário cadastrado ainda.")
                cadastrar_agora = input("Deseja cadastrar um usuário agora? (S/N): ").strip().upper()
                if cadastrar_agora == 'S':
                    criar_usuario()
                continue

            email = input("E-mail: ")
            senha = input("Senha: ")

            usuario = login_usuario(email, senha)
            if usuario:
                menu_usuario(usuario)
            else:
                print("Login falhou. Voltando ao menu inicial.")
                continue    

        elif escolha == '4':
            if not artistas:
                print("\n❌ Nenhum artista cadastrado ainda.")
                cadastrar_agora = input("Deseja cadastrar um artista agora? (S/N): ").strip().upper()
                if cadastrar_agora == 'S':
                    cadastrar_artista()
                continue

            email = input("E-mail: ")
            senha = input("Senha: ")

            artista = login_artista(email, senha)

            if artista:
                menu_artista(artista)
            else:
                print("Login falhou. Voltando ao menu inicial.")
                continue    

        elif escolha == '0':
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

def menu_usuario(usuario):
    print(f"\n🎉 Bem-vindo ao Gogh, {usuario.nome}!")
    galeria = Galeria()
    carrinho = Carrinho(usuario)
    while True:
        print("O que você gostaria de fazer?")
        print("1 - Ver galeria")
        print("2 - Ver carrinho")
        print("3 - Finalizar Compra")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            interagir_com_usuario(galeria, carrinho)
        elif opcao == '2':
            carrinho.exibir_carrinho()
        elif opcao == '3':
           processar_pagamento(carrinho)
        elif opcao == '4':
            print("Saindo do menu principal. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_artista(artista):
    print(f"\n🎉 Bem-vindo ao Gogh, {artista.nome}!")
    
    while True:
        print("O que você gostaria de fazer?")
        print("1 - Ver minhas obras")
        print("2 - Cadastrar obra")
        print("3 - Apagar todas as minhas obras")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            artista.exibir_obras()
        elif opcao == '2':
            adicionar_nova_obra(artista)
        elif opcao == '3':
           artista.apagar_todas_obras()
        elif opcao == '4':
            print("Saindo do menu principal. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu_login()