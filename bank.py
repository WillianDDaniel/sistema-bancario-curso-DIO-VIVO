# Constant for withdrawal limit
WITHDRAWAL_LIMIT = 500
# Constant for max withdrawals per day
MAX_WITHDRAWALS = 3

# Function to ask the user if they want to continue
def continue_operation():
    msg = "Deseja continuar? (s/n) => "
    continue_op = input(msg)
    
    if continue_op in ["s", "S"]:
        return True
    elif continue_op in ["n", "N"]:
        return False
    else:
        print(" => Digite uma opção válida.")
        
        return continue_operation()

# Function to handle deposits
def deposit(balance, statement, /,):
    
    amount = float(input("Informe o valor do depósito: "))
    
    # Deposit validation
    if amount > 0:
        balance += amount
        statement += f"Depósito: R$ {amount:.2f}\n"
        
        format_response(f"Depósito de R$ {amount:.2f} efetuado com sucesso!\n")
        
        should_continue = continue_operation()
        return [should_continue, balance, statement]
    
    else:
        format_response("Operação falhou! O valor informado é inválido.")
        should_continue = continue_operation()
        return [should_continue, balance, statement]

# Function to handle withdrawals
def withdraw(*, balance, statement, num_withdrawals):
    amount = float(input("Informe o valor do saque: "))

    # Check for insufficient balance, exceeding limit, or exceeding max withdrawals
    exceeded_balance = amount > balance
    exceeded_limit = amount > WITHDRAWAL_LIMIT
    exceeded_withdrawals = num_withdrawals >= MAX_WITHDRAWALS

    # Withdrawal validation
    if exceeded_balance:
        format_response("Operação falhou! Você não tem saldo suficiente.")
        
        should_continue = continue_operation()
        
        return [should_continue, balance, statement, num_withdrawals]
    
    elif exceeded_limit:
        format_response("Operação falhou! O valor do saque excede o limite.")
        
        should_continue = continue_operation()
        
        return [should_continue, balance, statement, num_withdrawals]
    
    elif exceeded_withdrawals:
        format_response("Operação falhou! Número máximo de saques excedido.")
        
        should_continue = continue_operation()
        
        return [should_continue, balance, statement, num_withdrawals]
    
    elif amount > 0:
        balance -= amount
        statement += f"Saque: R$ {amount:.2f}\n"
        num_withdrawals += 1
        
        format_response(f"Saque de R$ {amount:.2f} efetuado com sucesso!\n")
    
        should_continue = continue_operation()
        
        return [should_continue, balance, statement, num_withdrawals]
    
    else:
        format_response("Operação falhou! O valor informado é inválido.")
        
        should_continue = continue_operation()
        
        return [should_continue, balance, statement, num_withdrawals]

# Function to print account statement
def print_statement(balance, /, *, statement):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not statement else statement)
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")
    
    should_continue = continue_operation()
    
    return [should_continue, statement]

# Function to find a user by CPF
def filter_user(cpf, users):
    for user in users:
        if user["cpf"] == cpf:
            return user
    return None

# Function to register a new user
def register_user(users):
    cpf = input("Digite seu CPF: ")
    existing_user =filter_user(cpf, users)
    if existing_user:
        format_response("CPF já cadastrado!")
        
        should_continue = continue_operation()
        
        return [should_continue, users]

    name = input("Digite seu nome completo: ")
    birthdate = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    address = input("Digite seu endereço: ")
    user = {
        "nome": name,
        "data_nascimento": birthdate,
        "cpf": cpf,
        "endereco": address
    }
    users.append(user)
    
    format_response("Usuário cadastrado com sucesso!")
    
    should_continue = continue_operation()
    
    return [should_continue, users]

# Function to create a new account
def create_account(accounts, users):
    cpf = input("Digite seu CPF: ")
    existing_user = filter_user(cpf, users)
    if not existing_user:
        format_response("Usuário não cadastrado!")
        
        should_continue = continue_operation()
        
        return [should_continue, accounts, users]
    
    account_number = len(accounts) + 1
    new_account = {"Agência": "0001", "nro_conta": account_number, "usuario": existing_user}
    accounts.append(new_account)
    format_response("Conta criada com sucesso!")
    
    should_continue = continue_operation()
    
    return [should_continue, accounts, users]

# Function to format responses in a consistent way
def format_response(message):
    print("================================================\n")
    print(message)
    print("================================================\n")

# Main function to run the program
def main():
    print(" => Bem vindo ao sistema de cadastro de clientes")
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Novo Cliente
    [cc] Criar conta
    [q] Sair
    
    => """

    balance = 0
    statement = ""
    num_withdrawals = 0
    should_continue = True
    users = []
    accounts = []
    
    while should_continue:
        option = input(menu)
        if option in ["d", "D"]:
            should_continue, balance, statement = deposit(balance, statement)
            
        elif option in ["s", "S"]:
            
            should_continue, balance, statement, num_withdrawals = withdraw(
                balance=balance, statement=statement, num_withdrawals=num_withdrawals
            )
            
        elif option in ["e", "E"]:
            should_continue, statement = print_statement(balance, statement=statement)
            
        elif option in ["nc", "NC"]:
            should_continue, users = register_user(users)
            
        elif option in ["cc", "CC"]:
            should_continue, accounts, users = create_account(accounts, users)
            
        elif option in ["q", "Q"]:
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
            should_continue = continue_operation()

main()
