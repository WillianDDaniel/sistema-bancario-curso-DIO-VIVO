## Projeto do Bootcamp Python Backend Developer pela DIO + VIVO

Este é um projeto prático desenvolvido durante as aulas do Bootcamp Python Backend Developer, oferecido pela DIO em parceria com a VIVO.

### Descrição do Desafio
**Entendendo o Desafio**

Agora é a sua vez de brilhar e construir um perfil de destaque na DIO! Explore todos os conceitos aprendidos até aqui e reproduza (ou até mesmo aprimore) este projeto prático. Para isso, crie seu próprio repositório e amplie seu portfólio de projetos no GitHub, o que pode fazer toda a diferença em suas entrevistas técnicas 😎

### Minha Versão do Projeto

Para facilitar a compreensão do meu primeiro código em Python, mantive a base original do projeto e fiz algumas melhorias significativas. Apesar de já programar em PHP, JavaScript e TypeScript, adaptar-me à sintaxe do Python foi um desafio, mas gratificante!

Deixei os nomes das variáveis em português propositalmente para agilizar o processo de criação da minha tarefa. No entanto, os comentários estão em inglês, pois é um hábito pessoal. Apesar dessa mistura um tanto peculiar, trata-se de um projeto simples e básico para o curso.

Por isso, peço a compreensão de todos.

## Confira o projeto original

Para ficar mais claras as mudanças feitas no projeto, aqui está o link com o projeto original.

 - [Projeto Original](https://github.com/digitalinnovationone/trilha-python-dio/blob/main/00%20-%20Fundamentos/desafio.py)

## Novas funcionalidades e mudanças

- Introduzi uma função chamada **continuar_operacao()** para lidar com a lógica de continuar ou encerrar a operação. No projeto original, essa lógica estava dentro do loop principal, o que tornava o código mais difícil de acompanhar. Ao extrair essa lógica para uma função separada, chamada continuar_operacao(), tornei o código mais modular e legível.

- Além disso, fiz uma melhoria importante no tratamento das opções do menu. No projeto original, as opções eram verificadas apenas em minúsculas, o que limitava a entrada do usuário. Na minha versão, implementei a verificação tanto em minúsculas quanto em maiúsculas, aumentando a robustez do programa e permitindo que o usuário insira letras em qualquer caso.

- Para melhorar a experiência do usuário, adicionei mensagens de feedback mais informativas, como confirmações de depósito e saque bem-sucedidos. Isso tornou a interação com o programa mais agradável e compreensível.

- Uma das mudanças mais significativas que fiz foi usar recursão na função continuar_operacao(). Isso garante que o usuário sempre insira uma opção válida, mesmo em caso de entrada inválida. Isso eliminou a necessidade de repetir a solicitação de entrada no loop principal, tornando o código mais conciso e fácil de entender.

- Por fim, mesmo mantendo a estrutura geral do loop principal, simplifiquei algumas partes do código, removendo duplicações e tornando-o mais claro e legível. Essas melhorias tornaram o código mais modular, robusto e fácil de entender, o que é fundamental para um projeto básico como este.


## Requisitos para rodar o projeto

- Python 3.6 ou superior
- IDE de sua preferência (eu usei o VsCode, mas você pode usar o que quiser)