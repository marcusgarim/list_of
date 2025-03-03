def adicionar_tarefa(tarefas, nome_tarefa):  # Função que adiciona a tarefa
    # DICIONÁRIO COM:
    # tarefa: nomes da tarefa
    # status: identificar se essa tarefa está concluída
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")

    return

def ver_tarefas(tarefas):
  print("\nLista de tarefas:")
  for indice, tarefa in enumerate(tarefas, start=1):
    status = "✓" if tarefa["concluida"] else " "
    nome_tarefa = tarefa["tarefa"]
    print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa (tarefas, indic):
    return

tarefas = []
#teste

while True:
    print("\nMenu do Gerenciador da Lista de tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas concluídas")
    print("6. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja armazenar: ")
        adicionar_tarefa(tarefas, nome_tarefa)

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Programa finalizado")