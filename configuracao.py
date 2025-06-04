import tkinter as tk
from tkinter import  messagebox

lista = []

def salvar_dados(nome_aluno, entrada_nota1, entrada_nota2, entrada_nota3, listbox, materia):    
    nome = nome_aluno.get()
    nota1 = entrada_nota1.get()
    nota2 = entrada_nota2.get()
    nota3 = entrada_nota3.get()
    disciplina = materia.get()
    if not nome or not nota1 or not nota2 or not nota3:
        return messagebox.showinfo("Erro", "Preencha todos os campos!")
    else:
        nota1 = float(entrada_nota1.get())
        nota2 = float(entrada_nota2.get())
        nota3 = float(entrada_nota3.get())

    #Obtendo a Media
    media = (nota1+nota2+nota3)/3

    #Truncando a media para nao ter numero quebrados exemplo: 6.9
    media = funcaotruncar(media)
    print(media)

    #Criando um dicionario
    alunos = {'nome':nome,
              'notas': [nota1, nota2, nota3],
              'media': media,
              'disciplina': disciplina
              }
    
    lista.append(alunos)

    bubblesort(lista, 'media')


    print(lista)
    
    atualizar_listbox(listbox)

        # Limpa os campos após salvar
    nome_aluno.delete(0, tk.END)
    entrada_nota1.delete(0, tk.END)
    entrada_nota2.delete(0, tk.END)
    entrada_nota3.delete(0, tk.END)
    materia.delete(0, tk.END)
    

def bubblesort(lista, chave):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            valor1 = lista[j][chave]
            valor2 = lista[j + 1][chave]

            # Se os valores forem strings (ex: 'nome'), normaliza para minúsculas
            if isinstance(valor1, str):
                valor1 = valor1.lower()
                valor2 = valor2.lower()

            if valor1 > valor2:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]


def atualizar_listbox(listbox):
    listbox.delete(0, tk.END)  # Limpa o Listbox
    listbox.insert(tk.END, f'{"NOME DO ALUNO":<20}{"NOTA 1":<10}{"NOTA 2":<10}{"NOTA 3":<10}{"NOTA FINAL":<12}{"DISCIPLINA":<15}')
    for aluno in lista:         # Percorre a lista já ordenada
        nome = aluno['nome']
        notas = aluno['notas']
        media = aluno['media']
        disciplina = aluno['disciplina']
        listbox.insert(tk.END, f'{nome:<20}{notas[0]:<10}{notas[1]:<10}{notas[2]:<10}{media:<12}{disciplina:<15}')


def validacao(valor):
    valor = valor.replace(" ", "")
    
    if valor == "":
        return True  # permite apagar o campo
    
    if valor.isalpha():
        return False  # bloqueia letras

    try:
        float(valor)
        return True  # permite números com ponto ou vírgula
    except ValueError:
        return False  # qualquer outro símbolo


def funcaotruncar(valor):
    return int(valor * 10) / 10

def valida_nome(texto):
      return texto.replace(" ", "").isalpha() or texto == ""

def excluir_aluno(listbox):
    selecionado = listbox.curselection()

    if not selecionado or selecionado[0] == 0:
        # Evita tentar excluir o cabeçalho ou nenhum item
        messagebox.showinfo("Erro", "Selecione um aluno válido para excluir.")
        return

    index = selecionado[0] - 1  # Desconta o cabeçalho (linha 0)

    aluno = lista[index]
    confirmar = messagebox.askyesno("Confirmar Exclusão", f"Deseja excluir o aluno '{aluno['nome']}'?")

    if confirmar:
        lista.pop(index)
        atualizar_listbox(listbox)

def busca_binaria_por_nome(lista, nome_procurado):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        nome_atual = lista[meio]["nome"].lower()

        if nome_atual == nome_procurado.lower():
            return lista[meio]
        elif nome_atual < nome_procurado.lower():
            inicio = meio + 1
        else:
            fim = meio - 1

    return None

def pesquisar(aluno):
    nome = aluno.get()
    if not nome:
        return messagebox.showinfo("Erro", "Digite um nome para pesquisar.")

    bubblesort(lista, 'nome')  # Ordena 

    resultado = busca_binaria_por_nome(lista, nome)

    if resultado:
        messagebox.showinfo("Aluno Encontrado", f"Nome: {resultado['nome']}\nNotas: {resultado['notas']}\nMédia: {resultado['media']}")
    else:
        messagebox.showinfo("Não encontrado", "Aluno não encontrado.")
