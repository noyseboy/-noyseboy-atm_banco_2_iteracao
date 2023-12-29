import getpass

class Conta:
    def __init__(self, nome, cpf, numero_conta, saldo=0.0):
        self.nome = nome
        self.cpf = cpf
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.senha = None

    def cadastrar_senha(self, senha):
        self.senha = senha
        print("\nSenha cadastrada com sucesso.")

    def digitar_senha(self):
        return getpass.getpass("Digite sua senha: ").strip()
