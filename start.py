
# listas
notas = []
agendas = []
tarefas = []
# entrar no menu 

RED = "\033[31m"
RESET = "\033[m"

while True:
    print("""
    ====================
       Assistente GP   
    ====================
        
    1 - Bloco de Notas
        
    2 - Agenda
        
    3 - Tarefas

    4 - Sair
    """)
    # Escolher uma das opçoes 
    try:
        escolha_menu = int(input("Escolha: ").strip())
    except ValueError:
        input(f"{RED}Digite Apenas Numeros! {RESET}Pressione <ENTER> Para continuar")
        continue
    # bloco de notas 

    if escolha_menu == 1:
        print("""
    1 - Nova Nota

    2 - Mostrar Notas
            
    3 - Editar
            
    4 - Excluir

    """)
        try:
            escolha_notas = int(input("Escolha: ").strip())
        except ValueError:
            input(f"{RED}Digite Apenas Numeros! {RESET}Pressione <ENTER> Para continuar")
            continue

        if escolha_notas == 1:
            nova_nota = input("Digite: ").strip() 
            notas.append(nova_nota)
            print("Nota Adicionada com sucesso! ")
        elif escolha_notas == 2:
            if len(notas) == 0:
                print("Não há Notas")
            else:
                for i, nova_nota in enumerate(notas):
                    print(f"{i + 1}. {nova_nota}")
        elif escolha_notas == 3:
            print("Em Breve")
        elif escolha_notas == 4:
            if len(notas) == 0:
                input("Não há Nota para Excluir! Pressione <ENTER> Para continuar")
            else:
                for i, nota in enumerate(notas):
                    print(f"{i + 1}. {nota}")
                try:      
                    excluir_nota = int(input("Qual Nota Voçê Que Excluir? ").strip())
                    print(f"'{notas.pop(excluir_nota - 1)}' Excluido(a) com sucesso!")
                except ValueError:
                    input(f"{RED}Opção Invalida{RESET}, Pressione <ENTER> Para continuar")
                except IndexError:
                    input(f"{RED}Opção Invalida{RESET}, Pressione <ENTER> Para continuar")
 
    # agenda 
    elif escolha_menu == 2:
        print("""
    1 - Adicionar Agenda
              
    2 - Mostrar Agendas
              
    3 - Editar
              
    4 - Excluir
              
    """)
        try:
            escolha_agenda = int(input("Escolha: ").strip())
        except ValueError:
            input(f"{RED}Digite Apenas Numeros! {RESET}Pressione <ENTER> Para continuar")
            continue

        if escolha_agenda == 1:
            data = input("Data: ")
            horario = input("Horario: ")
            descricao = input("Compromisso: ")
            nova_agenda = (data, horario, descricao)
            agendas.append(nova_agenda)
            print("Agenda Adicionada com sucesso!")
        elif escolha_agenda == 2:
            if len(agendas) == 0:
                print("Não há Agendas")
            else:
                for i, nova_agenda in enumerate(agendas):
                    print(f"{i + 1}. {data} | {horario} | {descricao}")
        elif escolha_agenda == 3:
            print("Em Breve")
        elif escolha_agenda == 4:
            if len(agendas) == 0:
                input("Não há Nota para Agendas! Para continuar pressione <ENTER>")
            else: 
                for i, agenda in enumerate(agendas):
                    data, horario, descricao = agenda
                    print(f"{i + 1}. {data} | {horario} | {descricao}")  
                excluir_agenda = int(input("Qual Agenda Voçê Que Excluir? ").strip())
                print(f"{agendas.pop(excluir_agenda - 1)} Excluido(a) com sucesso!")
    # tarefas
    elif escolha_menu == 3:
        print("""
    1 - Adicionar Tarefa
              
    2 - Mostrar Tarefas
              
    3 - Editar
              
    4 - Excluir
              
    """)
        try:
            escolha_tarefa = int(input("Escolha: ").strip())
        except ValueError:
            input(f"{RED}Digite Apenas Numeros! {RESET}Pressione <ENTER> Para continuar")
            continue

        if escolha_tarefa == 1:
            nova_tarefa = input("Digite: ").strip()
            tarefas.append(nova_tarefa)
            print("Tarefa Adicionada com sucesso!")
        elif escolha_tarefa == 2:
            if len(tarefas) == 0:
                print("Não há Tarefas")
            else:
                for i, nova_tarefa in enumerate(tarefas):
                    print(f"{i + 1}. {nova_tarefa}")
        elif escolha_tarefa == 3:
            print("Em Breve")
        elif escolha_tarefa == 4:
            if len(tarefas) == 0:
                input("Não há Nota para Agendas! Para continuar pressione <ENTER>")
            else:
                for i, tarefa in enumerate(tarefas):
                    print(f"{i + 1}. {tarefa}")
                excluir_tarefa = int(input("Qual Agenda Voçê Que Excluir? ").strip())
                print(f"'{tarefas.pop(excluir_tarefa -1 )}' Excluido(a) com sucesso!")
            
    elif escolha_menu == 4:
        print("Programa Encerrado ")
        break
        # conectar ao banco de dados
    else:
       input(f"{RED}Opção Invalida{RESET}, Escolha entre 1 a 4 presione <ENTER>")
