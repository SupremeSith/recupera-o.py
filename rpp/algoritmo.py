from class import *
from main import*
import os

def main():

    sair = False
    while sair == False:
        try:
            os.system("cls")
            print("---BEM VINDO---")
            print("01 - CRIAR CONTA")
            print("02 - SACAR")
            print("03 - DEPOSITAR")
            print("04 - TRANSFERIR")
            print("05 - SALDO")
            print("00 - SAIR")
            print("--------")
            print("")

            print("Qual opção deseja?")
            menu = int(input(">> "))
            os.system("pause")

            
            match menu:
                case 1:
                    os.system("cls")
                    print("---CRIAR CONTA---")
                    print("INFORME OS SEUS DADOS")
                    nome = input("Nome \n >>> ")
                    valor = input("Qual seria seu saldo Inicial? \n >")
                    banco.criar_conta(nome, valor)
                    print("CLIENTE CADASTRADO")
                    print(f"Nome = {nome} \n Valor Inserido = {valor}")
                    os.system("pause")

                case 2:
                    os.system("cls")
                    print("--SACAR--")
                    print("Qual seria o valor desejado ? \n >")
                    print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
                    else:
                    print("Saldo insuficiente.")
                    os.system("cls")


                case 3:
                    os.system("cls")
                    print("---DEPOSITAR---")
                    print("---QUAL VALOR DESEJAR DEPOSITAR???---")
                    print(int(">>>"))
                    print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")


                case 4:
                    os.system("cls")
                    print("---TRANFERIR---")
                    print("---QUAL VALOR DESEJA TRANFERIR---")
                    def transferir(self, destino, valor, origem):
                        self.origem = origem
                        if self.saldo >= valor:
                        destino.deposito(valor)
                        origem = print(f"Qual seria a conta a enviar ? \n ")
                        print(f"Transferência de R${valor:.2f} realizada para {destino.nome} na conta de {origem}. Novo saldo: R${self.saldo:.2f}")
                        pass

                case 5:
                    os.system("cls")
                    print("---VER SALDO---")
                    banco.listar_valor()

                case 0:
                    print("emitindo saida")
                    os.system("cls")
                    sair = True

        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)
            print("")


                        
