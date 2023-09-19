from algoritmo import*
import os
class banco:
    def __init__(self, conta):
        self.conta = conta

    def depositar(self, valor, conta):
        self.saldo += valor
        self.conta = conta
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

        def criar_conta (self, conta , saldo_inicial, nome):
            self.nome = nome
            self.conta = conta
            self.saldo_incial = valor
            print("---DIGITE SEUS DADOS---")
            nome = print(f"Digite seu nome: \n >>>")
            conta = print(f"Digite o numero da sua agencia: \n >>>")
            print(f"Conta cadastradaca com sucesso! \n Nome : {nome}  Agencia da Conta: {conta}")
            print("Press Enter for Skip")
            os.system("cls")

    def sacar(self, valor, conta):
        self.conta = conta
        if self.saldo >= valor:
            self.saldo -= valor
            os.system("cls")

    def transferir(self, destino, valor, origem):
        self.origem = origem
        if self.saldo >= valor:
            self.saldo -= valor
            destino.deposito(valor)
            origem = print(f"Qual seria a conta a enviar ? \n ")
            print(f"Transferência de R${valor:.2f} realizada para {destino.nome} na conta de {origem}. Novo saldo: R${self.saldo:.2f}")
        else:
            print("O saldo disponível é insuficiente")
            os.system("cls")
            
            def valor(self, listar_valor):
                self.listar_valor = listar_valor

if __name__ == "__main__":
    banco = banco()