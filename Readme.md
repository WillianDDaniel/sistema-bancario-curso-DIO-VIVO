## Projeto do Bootcamp Python Backend Developer pela DIO + VIVO

Este é um projeto prático desenvolvido durante as aulas do Bootcamp Python Backend Developer, oferecido pela DIO em parceria com a VIVO.

### Descrição do Desafio
**Entendendo o Desafio**

O objetivo deste desafio é construir um sistema bancário simplificado em Python. Ele permite que os usuários realizem operações básicas como depósito, saque e visualização de extrato. O projeto original serve como base para que os alunos explorem os conceitos aprendidos e desenvolvam suas próprias soluções. 😎

## Minha Versão do Projeto

Minha versão do projeto mantém a funcionalidade principal do sistema bancário, mas introduz melhorias significativas em termos de organização, legibilidade e experiência do usuário.

### Principais Mudanças e Melhorias:

- **Função continuar_operation():** Extraí a lógica de continuar ou encerrar a operação para uma função separada, tornando o código mais modular e fácil de manter. Essa função usa recursão para garantir que o usuário insira uma opção válida.

- **Tratamento de Opções do Menu:** As opções do menu agora são verificadas tanto em minúsculas quanto em maiúsculas, proporcionando maior flexibilidade para o usuário.

- **Mensagens de Feedback:** Adicionei mensagens de feedback mais claras e informativas para confirmar o sucesso das operações de depósito e saque.

- **Função format_response():** Criei uma função para formatar as respostas na tela de forma consistente, melhorando a legibilidade e a organização do código.

- **Comentários em Inglês:** Os comentários no código estão em inglês para facilitar a compreensão de desenvolvedores de outras nacionalidades.

- **Outras Melhorias:** Fiz ajustes adicionais para simplificar o código, remover duplicações e melhorar a legibilidade geral.

## Estrutura do Projeto
- **WITHDRAWAL_LIMIT:** Constante que define o limite de saque diário.
- **MAX_WITHDRAWALS:** Constante que define o número máximo de saques diários permitidos.
- **continue_operation():** Função que pergunta ao usuário se ele deseja continuar e valida a entrada.
- **format_response():** Função que formata as mensagens de resposta na tela.
- **deposit():** Função que realiza depósitos na conta.
- **withdraw():** Função que realiza saques da conta.
- **print_statement():** Função que imprime o extrato da conta.
- **filter_user():** Função que busca um usuário pelo CPF.
- **register_user():** Função que cadastra um novo usuário.
- **create_account():** Função que cria uma nova conta bancária.
- **main():** Função principal que executa o programa, apresenta o menu e chama as outras funções conforme a escolha do usuário.

## Confira o projeto original

Para ficar mais claras as mudanças feitas no projeto, aqui está o link com o projeto original.

 - [Projeto Original](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)


## Requisitos para rodar o projeto

- Python 3.6 ou superior
- IDE de sua preferência (eu usei o VsCode, mas você pode usar o que quiser)

## Como Executar o Projeto
**1 -** Clone o repositório: Faça o download do código para o seu computador.

**2 -** Abra o terminal: Navegue até o diretório onde você salvou o código.

**3 -** Execute o código: Digite o comando python nome_do_arquivo.py (substituindo "nome_do_arquivo.py" pelo nome real do arquivo) e pressione Enter.

O programa será iniciado e você poderá interagir com o sistema bancário simplificado.