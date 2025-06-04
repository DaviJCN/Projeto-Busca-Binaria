📚 Sistema de Gerenciamento de Notas de Alunos

Este projeto é um sistema simples de gerenciamento de notas de alunos desenvolvido em Python com interface gráfica (GUI) usando Tkinter. Ele permite adicionar, visualizar, pesquisar e excluir registros de alunos e suas respectivas notas em diferentes disciplinas.
✨ Funcionalidades

    Adicionar Aluno: Insira o nome do aluno, três notas e a disciplina para adicionar um novo registro.
    Cálculo de Média: A média das notas é calculada automaticamente.
    Ordenação Automática: A lista de alunos é automaticamente ordenada por média (crescente) utilizando o algoritmo Bubble Sort sempre que um novo aluno é adicionado.
    Pesquisa de Aluno: Realize buscas por nome de aluno utilizando o algoritmo de Busca Binária.
    Excluir Aluno: Remova um aluno da lista.
    Validação de Entrada: Campos numéricos aceitam apenas números (inteiros ou decimais) e campos de texto aceitam apenas letras.
    Interface Gráfica (GUI): Desenvolvida com Tkinter, proporcionando uma experiência de usuário intuitiva.

🎯 Algoritmos Utilizados

    Bubble Sort: Implementado para ordenar a lista de alunos com base em suas médias ou nomes.
    Busca Binária: Utilizado para localizar rapidamente um aluno específico na lista ordenada pelo nome.

🛠️ Tecnologias

    Python 3.x
    Tkinter (biblioteca padrão para GUI em Python)

🚀 Como Rodar o Projeto

    Clone o Repositório:
    Bash

git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
cd SEU-REPOSITORIO

(Lembre-se de substituir SEU-USUARIO e SEU-REPOSITORIO pelo seu próprio nome de usuário e pelo nome que você escolher para o repositório.)

Execute o Programa:
Bash

    python main.py

    Isso abrirá a janela do aplicativo.

📄 Estrutura do Código

O projeto é dividido em três arquivos Python para melhor organização:

    main.py: O ponto de entrada principal do aplicativo, que chama a função principal() do módulo overlay.
    overlay.py: Contém a lógica da interface gráfica do usuário (GUI) com Tkinter, definindo os widgets, layout e chamadas para as funções de manipulação de dados.
    configuracao.py: Contém as funções de lógica de negócios, como salvar_dados, bubblesort, busca_binaria_por_nome, atualizar_listbox e funções de validação de entrada.
