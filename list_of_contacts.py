def adicionar_contato(contatos, nome, telefone, email):  # Função que adiciona um contato
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
    contatos.append(contato)
    print(f"\nContato {nome} foi adicionado com sucesso!")

    return

def ver_contatos(contatos):  # Função que exibe a lista de contatos
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "★" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] Nome: {nome}, Telefone: {telefone}, Email: {email}")

def atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):  # Função que atualiza um contato
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = novo_nome
        contatos[indice_contato_ajustado]["telefone"] = novo_telefone
        contatos[indice_contato_ajustado]["email"] = novo_email
        print(f"Contato {indice_contato} atualizado para Nome: {novo_nome}, Telefone: {novo_telefone}, Email: {novo_email}")
    else:
        print("Índice de contato inválido.")
    return

def marcar_favorito(contatos, indice_contato):  # Função que marca/desmarca um contato como favorito
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
        status = "favorito" if contatos[indice_contato_ajustado]["favorito"] else "não favorito"
        print(f"Contato {indice_contato} marcado como {status}")
    else:
        print("Índice de contato inválido.")
    return

def ver_favoritos(contatos):  # Função que exibe a lista de contatos favoritos
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if contato["favorito"]:
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. Nome: {nome}, Telefone: {telefone}, Email: {email}")

def deletar_contato(contatos, indice_contato):  # Função que deleta um contato
    indice_contato_ajustado = int(indice_contato) - 1
    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contato = contatos.pop(indice_contato_ajustado)
        print(f"Contato {contato['nome']} foi deletado com sucesso!")
    else:
        print("Índice de contato inválido.")
    return

contatos = []  # Lista que armazena os contatos

while True:
    print("\nMenu da Agenda")
    print("1. Adicionar contato")
    print("2. Ver contatos")
    print("3. Atualizar contato")
    print("4. Marcar/Desmarcar favorito")
    print("5. Ver contatos favoritos")
    print("6. Deletar contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":  
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)

    elif escolha == "2":  
        ver_contatos(contatos)

    elif escolha == "3":  
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja atualizar: ")
        novo_nome = input("Digite o novo nome do contato: ")
        novo_telefone = input("Digite o novo telefone do contato: ")
        novo_email = input("Digite o novo email do contato: ")
        atualizar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

    elif escolha == "4":  
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
        marcar_favorito(contatos, indice_contato)

    elif escolha == "5":  
        ver_favoritos(contatos)

    elif escolha == "6":  
        ver_contatos(contatos)
        indice_contato = input("Digite o número do contato que deseja deletar: ")
        deletar_contato(contatos, indice_contato)

    elif escolha == "7": 
        break

print("Programa finalizado")