import tkinter as tk
from configuracao import salvar_dados, validacao, valida_nome,excluir_aluno,pesquisar

def principal():
    #Criando Grafico GUi e Definindo Configurações
    janela = tk.Tk()
    janela.title("Sistema de Alunos")
    janela.geometry("700x400+200+200")
    janela.resizable(True, True)
    #janela.iconbitmap("")

    #configurar peso da coluna
    for i in range(5):
        janela.columnconfigure(i, weight=1)

    # Configurar linhas: só a linha 4 (listbox) cresce!
    for i in range(6):
        janela.rowconfigure(i, weight=0)
    janela.rowconfigure(4, weight=1)  # só listbox cresce

    # ======= FORMULÁRIO (linha 1) =======
    nome_aluno = tk.Label(janela, text="Nome Do Aluno")
    nome_aluno.grid(row=0, column=0, padx=50, pady=5, sticky="w")

    pesquisa_aluno = tk.Label(janela, text="Pesquisar Aluno por Nome")
    pesquisa_aluno. grid(row=2, column=0, padx=20, pady=5, sticky="w")

    pesquisa_aluno = tk.Label(janela, text="Disciplina")
    pesquisa_aluno. grid(row=0, column=4, padx=20, pady=5, sticky="w")

    nota1 = tk.Label(janela, text="NOTA 1")
    nota1.grid(row=0, column=1, padx=20, pady=5, sticky="w")

    nota2 = tk.Label(janela, text="NOTA 2")
    nota2.grid(row=0, column=2, padx=20, pady=5, sticky="w")

    nota3 = tk.Label(janela, text="NOTA 3")
    nota3.grid(row=0, column=3, padx=20, pady=5, sticky="w")
#----------------------------------------------------------------------------------------------

    valido = janela.register(validacao)
    nome_valido = janela.register(valida_nome)

    # ======= FORMULÁRIO (linha 2) =======
    nome_aluno = tk.Entry(janela, width=25, validate='key', validatecommand=(nome_valido, '%P'))
    nome_aluno.grid(row=1, column=0, padx=20, pady=5, sticky="w")

    pesquisa_nome = tk.Entry(janela, width=25, validate='key', validatecommand=(nome_valido,"%P"))
    pesquisa_nome.grid(row=3, column=0, padx=20, pady=5, sticky="w")

    entrada_nota1 = tk.Entry(janela, width=9, validate='key',validatecommand=(valido, '%P'))
    entrada_nota1.grid(row=1, column=1, padx=20, pady=5, sticky="w")

    entrada_nota2 = tk.Entry(janela, width=9, validate='key',validatecommand=(valido, '%P'))
    entrada_nota2.grid(row=1, column=2, padx=20, pady=5, sticky="w")

    entrada_nota3 = tk.Entry(janela, width=9, validate='key',validatecommand=(valido, '%P'))
    entrada_nota3.grid(row=1, column=3, padx=20, pady=5, sticky="w")

    disciplina = tk.Entry(janela, width=25, validate='key', validatecommand=(nome_valido, '%P'))
    disciplina.grid(row=1, column=4, padx=20, pady=5, sticky="w")
#-------------------------------------------------------------------------------------------

    # ======= LISTBOX (linha 4) =======
    listbox = tk.Listbox(janela, width=50, font=("Courier New", 10))
    listbox.grid(row=4, column=0, columnspan=5, sticky="nsew", padx=10, pady=10)
    listbox.insert(tk.END, f'{"NOME DO ALUNO":<20}{"NOTA 1":<10}{"NOTA 2":<10}{"NOTA 3":<10}{"NOTA FINAL":<12}{"DISCIPLINA":<15}')
    #---------------------------------------------------------------------------------------------------


    # ======= BOTÃO (linha 3) =======
    botao = tk.Button(janela, text="Adicionar", command=lambda: salvar_dados(nome_aluno, entrada_nota1, entrada_nota2, entrada_nota3, listbox, disciplina))
    botao.grid(row=3, column=4, sticky="nsew", padx=10, pady=10)

    botao_pesquisar = tk.Button(janela, text="Pesquisar", command=lambda:pesquisar(pesquisa_nome))
    botao_pesquisar.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)

    botao_excluir = tk.Button(janela, text="Excluir da lista", command=lambda: excluir_aluno(listbox))
    botao_excluir.grid(row=3, column=2, sticky="nsew", padx=10, pady=10)





    janela.mainloop()