def adicionar_tarefa(tarefas, nome_tarefa):  # Função que adiciona a tarefa
    tarefa = {"tarefa": nome_tarefa, "concluida": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")

    return

def ver_tarefas(tarefas):  # Função que exibe a lista de tarefas
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["concluida"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")

def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome_tarefa):  # Função que atualiza o nome de uma tarefa
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido.")
    return

def completar_tarefa(tarefas, indice_tarefa):  # Função que marca uma tarefa como completada
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["concluida"] = True
        print(f"Tarefa {indice_tarefa} marcada como completada")
    else:
        print("Indice de tarefa inválido.")
    return

def deletar_tarefas_completadas(tarefas):  # Função que deleta as tarefas completadas
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["concluida"]]
    print("Tarefas completadas foram deletadas.")
    return

tarefas = []  # Lista que armazena as tarefas

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

    elif escolha == "3":  
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":  
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":  
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6": 
        break

print("Programa finalizado")