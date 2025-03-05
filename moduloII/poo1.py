# POO

# Pilares da POO - 
print("\nExemplo de herança: ")

# Definindo uma classe chamada Animal
class Animal:
    # Método construtor que inicializa o objeto com um nome
    def __init__(self, nome) -> None:
        self.nome = nome

    # Método que faz o animal andar
    def andar(self):
        print(f"O animal {self.nome} andou")
        return

    # Método que será sobrescrito pelas subclasses para emitir som
    def emitir_som(self):
        pass

# Definindo uma classe Cachorro que herda de Animal
class Cachorro(Animal):
    # Sobrescrevendo o método emitir_som para o Cachorro
    def emitir_som(self):
        return "Au, au"
    
# Definindo uma classe Gato que herda de Animal
class Gato(Animal):
    # Sobrescrevendo o método emitir_som para o Gato
    def emitir_som(self):
        return "Miau!"
    

dog = Cachorro(nome="Rex")
cat = Gato(nome="Felix")
print("\nExemplo de polimorfismo")

animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")



# Classe de exemplo
class Pessoa:
    # Método construtor que inicializa o objeto com nome e idade
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    # Método que retorna uma saudação com o nome e idade da pessoa
    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Criando um objeto (instância) da classe Pessoa
pessoa1 = Pessoa("Alice", 30)

# Chamando o método saudacao e imprimindo a mensagem
mensagem = pessoa1.saudacao()
print(mensagem)

# Criando outro objeto (instância) da classe Pessoa
pessoa2 = Pessoa(nome="Rodrigo", idade=32)
mensagem2 = pessoa2.saudacao()
print(mensagem2)

# Comentários sobre a classe Carro (exemplo comentado)
# class Carro:
#     def __init__(self, cor, modelo):  # Método especial chamado ao criar o objeto
#         self.cor = cor  # Atributo cor
#         self.modelo = modelo  # Atributo modelo
    
#     def buzinar(self):  # Método para buzinar
#         print("Biii Biii!")