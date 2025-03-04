print("\nExemplo de encapsulamento:")

# Definindo uma classe chamada ContaBancaria
class ContaBancaria:
    def __init__(self, saldo) -> None:
        # Atributo privado que armazena o saldo da conta
        self.__saldo = saldo

    # Método para depositar um valor na conta
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    # Método para sacar um valor da conta
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    # Método para consultar o saldo da conta
    def consultar_saldo(self):
        return self.__saldo

# Criando uma instância da classe ContaBancaria com saldo inicial de 1000
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# Depositando 500 na conta
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# Depositando 500 na conta
conta.depositar(valor=-500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

# Sacando 200 da conta
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

