from administrador import Administrador
from cliente import Cliente

administrador_principal = Administrador()

administrador_principal.criar_usuario_senha()

while True:
    print("="*30)
    print("Bem-vindo ao ATM BANCO!")
    print("="*30)
    print("1. Administrador")
    print("2. Cliente")
    print("3. Sair")

    escolha_inicial = input("Escolha uma opção (1-3): ")

    if escolha_inicial == '1':
        if administrador_principal.autenticar_admin():
            while True:
                print("="*30)
                print("Bem-vindo, Administrador!")
                print("1. Criar Conta")
                print("2. Voltar para o Menu Inicial")
                print("="*30)

                escolha_admin = input("Escolha uma opção (1-2): ")

                if escolha_admin == '1':
                    administrador_principal.criar_conta()
                elif escolha_admin == '2':
                    print("\nEncerrando sessão de administrador.")
                    break
                else:
                    print("\nOpção inválida. Tente novamente.")
        else:
            print("\nAutenticação de administrador falhou. Tente novamente.")

    elif escolha_inicial == '2':
        if administrador_principal.contas:
            numero_conta_cliente = input("\nDigite o número da sua conta: ").strip()

            for conta_cliente in administrador_principal.contas:
                if conta_cliente.numero_conta == numero_conta_cliente:
                    cliente = Cliente(conta_cliente, administrador_principal)
                    cliente.menu_conta()
                    break
            else:
                print("\nConta não encontrada. Verifique o número da conta.")
        else:
            print("\nNenhuma conta cadastrada. Encerrando o programa.")

    elif escolha_inicial == '3':
        print("\nEncerrando o ATM Banco. Até logo!")
        break

    else:
        print("\nOpção inválida. Tente novamente.")
