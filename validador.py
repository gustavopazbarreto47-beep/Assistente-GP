while True:

    print(
        """
    ------- MENU -------
    1 - Opção mensagem 1
    2 - Opção mensagem 2
    3 - Opção mensagem 3
    """
    )

    opcao = input("Informe uma opção:_").strip()

    if opcao:

        if opcao == "1":
            print("opção 1")
            break

        elif opcao == "2":
            print("opção 2")
            break

        elif opcao == "3":
            print("opção 3")
            break

        else:
            print("Opção incorreta, informe uma opção válida")

    else:
        print("Erro:Necessário informar uma opção!!!")
        eval(1)
