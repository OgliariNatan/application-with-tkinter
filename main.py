# -*- coding: utf-8 -*-

from tkinter import *
def bt_click():
    print("BT Click")
    lb["text"] = 'ESCREVEU EM CIMA'




janela = Tk()

bt = Button(janela, width=10, text="OK", command=bt_click) #Cria o botão diz a quem pertence, ajusta o tamanho e o texto
bt.place(x=100, y=100) #Ajusta a posição do botão na tela

lb = Label(janela, text='Informações', width=20)
lb.place(x=100, y=150)


janela.geometry("300x300+200+200")
janela.mainloop()