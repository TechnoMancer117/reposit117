tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append({"nome": tarefa, "status": "Pendente"})

def listar_tarefas():
    for i, t in enumerate(tarefas):
        print(f"{i + 1}. {t['nome']} - {t['status']}")

def concluir_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas[indice]["status"] = "Concluída"

# Exemplo de uso
while True:
    print("\n1. Adicionar Tarefa\n2. Listar Tarefas\n3. Concluir Tarefa\n4. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        tarefa = input("Digite a tarefa: ")
        adicionar_tarefa(tarefa)
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        indice = int(input("Digite o número da tarefa para concluir: ")) - 1
        concluir_tarefa(indice)
    elif opcao == 4:
        break