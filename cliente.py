import getpass
from administrador import Administrador

class Cliente:
    def __init__(self, conta, administrador_principal):
        self.conta = conta
        self.administrador_principal = administrador_principal

    def menu_conta(self):
        if not self.autenticar_cliente():
            print("\nAcesso negado. Certifique-se de fornecer as informações corretas.")
            return

        while True:
            print("="*30)
            print(f"Bem-vindo, {self.conta.nome}!")
            print("Número da conta:", self.conta.numero_conta)
            #print("Saldo atual: R${:.2f}".format(self.conta.saldo))
            print("="*30)
            print("1. Verificar Saldo")
            print("2. Sacar")
            print("3. Transferir")
            print("4. Depositar")
            print("5. Sair")
            print("="*30)

            escolha = input("Escolha uma opção (1-5): ")

            if escolha == '1':
                self.verificar_saldo()
            elif escolha == '2':
                self.sacar()
            elif escolha == '3':
                self.transferir()
            elif escolha == '4':
                self.depositar()
            elif escolha == '5':
                print("\nObrigado por usar nosso ATM. Até logo!")
                break
            else:
                print("\nOpção inválida. Tente novamente.")

    def autenticar_cliente(self):
        senha = getpass.getpass("Digite sua senha: ").strip()
        return senha == self.conta.senha

    def verificar_saldo(self):
        print("="*30)
        print("Verificar Saldo")
        print("="*30)
        print(f"Seu saldo atual é: R${self.conta.saldo:.2f}")

    def sacar(self):
        valor_str = input("\nDigite o valor a sacar: R$").strip()
        try:
            valor = float(valor_str)
        except ValueError:
            print("\nPor favor, insira um valor válido.")
            return

        if 0 < valor <= self.conta.saldo:
            self.conta.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nSaldo insuficiente ou valor inválido.")

    def transferir(self):
        numero_conta_destino = input("\nDigite o número da conta de destino: ").strip()

        for conta_destino in self.administrador_principal.contas:
            if conta_destino.numero_conta == numero_conta_destino:
                print("="*30)
                print("Destinatário da Transferência")
                print("="*30)
                print(f"Nome: {conta_destino.nome}")
                print(f"Número da Conta: {conta_destino.numero_conta}")
                print("="*30)

                valor_str = input("\nDigite o valor a transferir: R$").strip()

                try:
                    valor = float(valor_str)
                except ValueError:
                    print("\nPor favor, insira um valor válido.")
                    return

                if 0 < valor <= self.conta.saldo:
                    self.conta.saldo -= valor
                    conta_destino.saldo += valor
                    print(f"\nTransferência de R${valor:.2f} para {conta_destino.nome} realizada com sucesso.")
                else:
                    print("\nSaldo insuficiente ou valor inválido.")
                break
        else:
            print("\nConta de destino não encontrada. Verifique o número da conta.")

    def depositar(self):
        valor_str = input("\nDigite o valor a depositar: R$").strip()

        try:
            valor = float(valor_str)
        except ValueError:
            print("\nPor favor, insira um valor válido.")
            return

        if valor > 0:
            self.conta.saldo += valor
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("\nValor inválido para depósito.")
