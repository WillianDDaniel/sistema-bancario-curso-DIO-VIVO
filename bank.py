def continuar_operacao():
    continuar = input(" => CONTINUAR?  => Para Sim digite [y] | => Para Não digite [n].")
    
    if continuar == "y" or continuar == "Y":
        return True
    elif continuar == "n" or continuar == "N":
        return False
    else: 
        print(" => Digite uma opção válida.")
        return continuar_operacao()

# Menu options
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
controle = True

while controle:

    # Get user input for menu option
    opcao = input(menu)

    # Deposit option
    if opcao == "d" or opcao == "D":
        valor = float(input("Informe o valor do depósito: "))

        # Deposit validation
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("================================================\n")
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!\n")
            print("================================================\n")
            controle = continuar_operacao()
        else:
            print("Operação falhou! O valor informado é inválido.")
            
            controle = continuar_operacao()

    # Withdraw option
    elif opcao == "s" or opcao == "S":
        valor = float(input("Informe o valor do saque: "))

        # Check if withdrawal amount exceeds balance
        excedeu_saldo = valor > saldo

        # Check if withdrawal amount exceeds limit
        excedeu_limite = valor > limite

        # Check if maximum number of withdrawals reached
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # Withdrawal validation
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            
            controle = continuar_operacao()

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            
            controle = continuar_operacao()

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
            
            controle = continuar_operacao()

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            print("================================================\n")
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso!\n")
            print("================================================\n")
            
            controle = continuar_operacao()

        else:
            print("Operação falhou! O valor informado é inválido.")
            
            controle = continuar_operacao()

    # Statement option
    elif opcao == "e" or opcao == "E":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
        
        controle = continuar_operacao()

    # Quit option
    elif opcao == "q" or opcao == "Q":
        break

    # Invalid option
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        
        controle = continuar_operacao()
