# Importar a biblioteca do Tkinter que faz a interface

from tkinter import *
from tkinter import ttk

# Colocando cores na janela

cor1 = "#1e1f1e"  # Preto
cor2 = "#feffff"  # Branco
cor3 = "#38576b"  # Azul escuro
cor4 = "#ECEFF1"  # cinza
cor5 = "#FFAB40"  # Laranja

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")
janela.config(bg=cor1)

# Criando Frames

# TELA COMPLETA
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

# CORPO DA CALCULADOR

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)

# Criando Botões

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

#BOTÕES 7; 8; 9

b_5 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=52)

b_6 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=59, y=52)

b_7 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=118, y=52)

b_8 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=177, y=52)

#BOTÕES 4; 5; 6

b_9 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=0, y=52)

b_10 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=59, y=52)

b_11 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=118, y=52)

b_12 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=177, y=52)

#BOTÕES 1; 2; 3

b_13 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=0, y=52)

b_14 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=59, y=52)

b_15 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=118, y=52)

b_16 = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=177, y=52)

#BOTÕES 0; .; =

b_1 = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

b_2 = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)




janela.mainloop()
