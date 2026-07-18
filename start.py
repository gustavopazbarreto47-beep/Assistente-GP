print("teste")
agendas = []
notas = []
tarefas = []

while True:
    print("""
    =========================
          ASSISTENTE GP
    =========================

    1 - Agenda
    2 - Bloco de notas
    3 - Lista de tarefas
    4 - Configurações
    5 - Sair
        
    """)
    opçao = int(input("Escolha: "))

    if opçao == 1:
        print("""
        Agenda
    1 - Adicionar compromisso
            
    2 - Calendário
            
    3 - Lembretes

    """)
        escolha = int(input("Escolha: "))
        if escolha == 1:
            data = input("Data: ")
            hora = input("Hora: ")
            descriçao = input("Compromisso: ")
            nova_agenda = data,hora,descriçao
            agendas.append(nova_agenda)
            print("Nova agenda adicionda")
        elif escolha == 2:
            if len(agendas) == 0:
                print("Voçê ainda não tem compromisso!")
            else:
                 for i, nova_agenda in enumerate(agendas):
                    data,hora,descriçao = nova_agenda
                    print(f"{i + 1}. {data} - {hora} - {descriçao}")

    elif opçao == 2:
        print("""
    1 - Nova nota 
            
    2 - Mostar notas
            
    3 - Excluir a ultima nota

    """)
        escolha1 = int(input("Escolha: "))
        if escolha1 == 1:
            nota = input("Comece a escrever: ")
            notas.append(nota)
            print("Nova nota adicionda")
        elif escolha1 == 2:
            if len(notas) == 0:
                print("Nenhuma nota salva")
            else:
                for i, nota in enumerate(notas): 
                    print(f"{i + 1}. {nota}")

        elif escolha1 == 3:
            if len(notas) > 0:
                notas.pop()
                print("Nota Removida!")
            else:
               print("Não a nota para exculir! ")
        else:
            print("Escolha invalida!")       
    elif opçao == 3:
        print("""
    1 - Adicionar tarefa
            
    2 - Ver tarefas
            
    3 - Excluir a ultima tarefa

    """)
        escolha2 = int(input("Escolha: "))
        if escolha2 == 1:
            nova_tarefa = input("se progame: ")  
            tarefas.append(nova_tarefa)
            print("Nova Tarefa adiconada!")
        elif escolha2 == 2:
            if len(tarefas) == 0:
                print("Você ainda não tem tarefa!")
            else:
                for i, nova_tarefa in enumerate(tarefas):
                    print(f"{i + 1}. {nova_tarefa}")
        elif escolha2 == 3:
            if len(tarefas) > 0:
                tarefas.pop()
                print("tarefa removida com sucesso!")
            else:
                print("não a tarefa para excluir!")
        else:
            print("Escolha invalida!")
    elif opçao == 4:
        print("""
    1 - Em breve ... 
            
    """)
    elif opçao == 5:
        print("""
    Fim do progama 
    """)
        break
    else:
        print("Opção invalida! tente novamente ")
