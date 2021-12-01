from tkinter import *
from dbb import *


# cores -----------------------------
cor0 = "#000000"   # Preto
cor1 = "#59656F"   # azul acinzentado
cor2 = "#feffff"   # branco
cor3 = "#0074eb"   # azul
cor4 = "#f04141"   # vermelho
cor5 = "#59b356"   # cinza

janela=Tk()
janela.title('To-Do APP')
janela.geometry('500x225')
janela.resizable(width=FALSE, height=FALSE)
janela.configure(background=cor1)


#Divisao da janela

frame_esquerda = Frame(janela, width=300, height=200, bg=cor2, relief="flat")
frame_esquerda.grid(row=0, column=0, sticky=NSEW)
frame_direita = Frame(janela, width=200, height=250, bg=cor2, relief="flat")
frame_direita.grid(row=0, column=1, sticky=NSEW)

#Divisao do frame a esquerda em duas partes

frame_e_cima = Frame(frame_esquerda, width=300, height=50, bg=cor2, relief="flat")
frame_e_cima.grid(row=0, column=0, sticky=NSEW)
frame_e_baixo = Frame(frame_esquerda, width=300, height=150, bg=cor2, relief="flat")
frame_e_baixo.grid(row=1, column=0, sticky=NSEW)

#Criando botoes

b_novo = Button(frame_e_cima, text="Novo", width=10, height=1, bg=cor3, fg="white", font="5", anchor=CENTER, relief=RAISED)
b_novo.grid(row=0, column=0, sticky=NSEW, pady=1)
b_remover = Button(frame_e_cima, text="Remover", width=10, height=1, bg=cor4, fg="white", font="5", anchor=CENTER, relief=RAISED)
b_remover.grid(row=0, column=1, sticky=NSEW, pady=1)
b_novo = Button(frame_e_cima, text="Atualizar", width=10, height=1, bg=cor5, fg="white", font="5", anchor=CENTER, relief=RAISED)
b_novo.grid(row=0, column=2, sticky=NSEW, pady=1)

#Adicionando Listbox e Label
Label = Label(frame_direita, text="Tarefas", width=37, height=1, pady=7, padx=0, relief="flat", anchor=W, font=("Courier 20 bold"), fg=cor0)
Label.grid(row=0, column=0, sticky=NSEW, pady=1)

Listbox=Listbox(frame_direita, font=("Courier 9 bold"), width=1)
Listbox.grid(row=1, column=0, sticky=NSEW, pady=5)

#Adicionando tarefas na listbox

tarefas= ["Pagar contas", "Assistir Série", "Reunião de Trabalho", "Estudar", "Tomar remédio"]
for item in tarefas:
    Listbox.insert(END, item)


janela.mainloop()