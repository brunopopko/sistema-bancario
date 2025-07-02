menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Informe o valor a ser depositado: "))

        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        saque = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = saque > saldo

        excedeu_limite = saque > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!")

        elif excedeu_limite:
            print("Limite de saque por operação é de R$ 500,00.")

        elif excedeu_saques:
            print("Quantidade de saques diária já foi atingida! Tente novamente amanhã.")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")        
            
    elif opcao == "e":
        print("\n====================EXTRATO====================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSeu saldo é de R$ {saldo:.2f}")
        print("=================================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        