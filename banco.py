
def menu():
    texto_menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Novo usuário
    [c] Nova conta
    [lc] Listar contas
    [q] Sair

    => """
    return texto_menu

def listar_contas (contas):
    print("\n-------------------- Contas --------------------\n")
    if not contas:
        print("Nenhuma conta cadastrada ainda.")
    else:
        maior_nome = max(len(conta['Titular']) for conta in contas)
        for conta in contas:
            print(f"Titular:{conta['Titular']:<{maior_nome}}  |  Agência:{conta['Agência']}  |  Número da conta:{conta['Número da conta']}\n")

def depositar (deposito,saldo,extrato, /):
    if deposito > 0:
        saldo += deposito
        extrato += f"DEPÓSITO - R${deposito:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido, tente novamente.")
    return saldo, extrato

def historico (saldo, /, *, extrato):
    print("------------EXTRATO------------")
    print("Nenhuma movimentação bancária foi realizada." if not extrato else extrato)
    print(f"SALDO - R${saldo:.2f}")
    print("-------------------------------")

def sacar (*,saque,saldo,limite,limite_saques,numero_saques,extrato):
    saldo_insuficiente = saque > saldo
    limite_insufiente = saque > limite
    if saldo_insuficiente:
        print("Não será possível sacar o dinheiro por falta de saldo.")
    elif limite_insufiente:
        print("Limite indisponível para saque.")
    elif saque <= limite and saque <= saldo:
        if numero_saques < limite_saques:
            saldo -= saque
            extrato += f"SAQUE - R${saque:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Não será possível sacar, limite diário atingido.")
    return saldo, extrato, numero_saques

def novos_usuarios(usuarios):
    cpf = input("Digite seu CPF (somente números): ")
    if cpf in [usuario["CPF"] for usuario in usuarios]:
        print("Usuário já cadastrado.")
        return

    nome = str(input("Digite o seu nome: "))
    data_nas = input("Digite a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite o seu endereço (endereço, número - bairro - cidade/sigla do estado): ")

    usuarios.append({"Nome": nome, "CPF": cpf, "Data de nascimento": data_nas, "Endereço": endereco})
    print("Usuário cadastrado com sucesso.")

def nova_conta(usuarios, agencia, numero_conta, contas):
    cpf = input("Digite seu CPF (somente números): ")

    usuario = None
    for u in usuarios:
        if u["CPF"] == cpf:
            usuario = u
            break

    if usuario:
        print("Conta criada com sucesso!")
        contas.append({"Titular":usuario["Nome"], "Agência": agencia, "Número da conta": numero_conta })
    else:
        print("Usuário não encontrado")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = input(menu()).lower()

        if opcao == "d":
            deposito = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(deposito,saldo,extrato)

        elif opcao == "s":
            saque = float(input("Digite o valor do saque: "))
            saldo, extrato, numero_saques = sacar (saque=saque, saldo=saldo, extrato=extrato, limite=limite, limite_saques=LIMITE_SAQUES, numero_saques=numero_saques)

        elif opcao == "e":
            historico(saldo,extrato=extrato)

        elif opcao == "u":
            novos_usuarios(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            nova_conta(usuarios, agencia,numero_conta,contas)

        elif opcao == "lc":
            listar_contas(contas)
        
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()
