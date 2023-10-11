'''
1. Cadastro de Alunos:
Modifique o programa para que ao cadastrar um aluno, os dados sejam exibidos em uma árvore de exibição (Treeview).
'''
# Importando Tkinter e Ttk


########################################################################
# Importando Tkinter e Ttk
from tkinter import *
from tkinter.ttk import *




# Criando Janela
janela = Tk()
janela.geometry('500x500')

# Label
label_semana = Label(janela, text='Selecione o dia da semana:')

# 
aba_1 = Frame(janela)

tree_aba1 = Treeview(aba_1)
tree_aba1['column'] = [ 'nome', 'sobrenome']
tree_aba1.column('#0', width=50, anchor='w')
tree_aba1.column('nome', width=100, anchor='w')
tree_aba1.column('sobrenome', width=100, anchor='w')
tree_aba1.heading('#0',text= 'ID')
tree_aba1.heading('nome', text= 'Nome')
tree_aba1.heading('sobrenome', text= 'Sobrenome')

nome = [
     ['Pedro', 'Paulo'],
     ['Letticia', 'Betonico'],
     ['Vinicius', 'Araujo']

]

id = 1
for el  in nome:
     tree_aba1.insert('', END, text=(id, el[0], el[1]))
     id += 1




# Grid
aba_1.grid(row= 0, column= 1)
tree_aba1.grid(row= 1, column=0)




janela.mainloop()