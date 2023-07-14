import json

agenda = {}

def adicionar_compromisso():
    data = input("Digite a data do compromisso (formato DD/MM/AAAA): ")
    hora = input("Digite a hora do compromisso (formato HH:MM): ")
    descricao = input("Digite a descrição do compromisso: ")

    compromisso = {"Hora": hora, "Descrição": descricao}

    if data in agenda:
        agenda[data].append(compromisso)
    else:
        agenda[data] = [compromisso]

    print("Compromisso adicionado com sucesso!")

def visualizar_compromissos():
    data = input("Digite a data para visualizar os compromissos (formato DD/MM/AAAA): ")

    if data in agenda:
        print("Compromissos para a data", data + ":")
        for compromisso in agenda[data]:
            print("Hora:", compromisso["Hora"])
            print("Descrição:", compromisso["Descrição"])
            print("------------------------")
    else:
        print("Não há compromissos agendados para essa data.")

def editar_compromisso():
    data = input("Digite a data do compromisso a ser editado (formato DD/MM/AAAA): ")

    if data in agenda:
        print("Compromissos para a data", data + ":")
        for i, compromisso in enumerate(agenda[data]):
            print(i+1, "- Hora:", compromisso["Hora"])
            print("   Descrição:", compromisso["Descrição"])
            print("------------------------")

        opcao = int(input("Digite o número do compromisso a ser editado: ")) - 1
        if 0 <= opcao < len(agenda[data]):
            hora = input("Digite a nova hora do compromisso (formato HH:MM): ")
            descricao = input("Digite a nova descrição do compromisso: ")
            agenda[data][opcao] = {"Hora": hora, "Descrição": descricao}
            print("Compromisso editado com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("Não há compromissos agendados para essa data.")

def remover_compromisso():
    data = input("Digite a data do compromisso a ser removido (formato DD/MM/AAAA): ")

    if data in agenda:
        print("Compromissos para a data", data + ":")
        for i, compromisso in enumerate(agenda[data]):
            print(i+1, "- Hora:", compromisso["Hora"])
            print("   Descrição:", compromisso["Descrição"])
            print("------------------------")

        opcao = int(input("Digite o número do compromisso a ser removido: ")) - 1
        if 0 <= opcao < len(agenda[data]):
            agenda[data].pop(opcao)
            if len(agenda[data]) == 0:
                del agenda[data]
            print("Compromisso removido com sucesso!")
        else:
            print("Opção inválida.")
    else:
        print("Não há compromissos agendados para essa data.")

def mostrar_agenda():
    if len(agenda) == 0:
        print("Não há compromissos agendados.")
    else:
        print("Compromissos agendados:")
        for data, compromissos in agenda.items():
            print("Data:", data)
            for compromisso in compromissos:
                print("Hora:", compromisso["Hora"])
                print("Descrição:", compromisso["Descrição"])
                print("------------------------")

#salvamos num json
def salvar_agenda():
    with open("agenda.json", "w") as arquivo:
        json.dump(agenda, arquivo)

# Carregar a agenda salva anteriormente (se existir)
def carregar_agenda():
    global agenda
    try:
        with open("agenda.json", "r") as arquivo:
            agenda = json.load(arquivo)
    except FileNotFoundError:
        agenda = {}

carregar_agenda()

# Loop principal do programa
while True:
    print("\n---- Agenda de Compromissos ----")
    print("1 - Adicionar compromisso")
    print("2 - Visualizar compromissos por data")
    print("3 - Editar compromisso")
    print("4 - Remover compromisso")
    print("5 - Mostrar todos os compromissos")
    print("0 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adicionar_compromisso()
        salvar_agenda()  # Salvar a agenda após adicionar um compromisso
    elif opcao == "2":
        visualizar_compromissos()
    elif opcao == "3":
        editar_compromisso()
        salvar_agenda()  # Salvar a agenda após editar um compromisso
    elif opcao == "4":
        remover_compromisso()
        salvar_agenda()  # Salvar a agenda após remover um compromisso
    elif opcao == "5":
        mostrar_agenda()
    elif opcao == "0":
        salvar_agenda()  # Salvar a agenda antes de encerrar o programa
        break
    else:
        print("Opção inválida. Tente novamente.")
