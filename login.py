# -*- coding: utf-8 -
#https://www.youtube.com/watch?v=kliik_Bzk6M&list=PLesCEcYj003QxPQ4vTXkt22-E11aQvoVj&index=98
from tkinter import *

janela = Tk()


lb1 = Label(janela, text='Login')
lb2 = Label(janela, text='Senha')

ed1 = Entry(janela)
ed2 = Entry(janela)

bt1 = Button(janela, text='Confirmar')


#Posicionando na tela
lb1.grid(row=0, column=0)
ed1.grid(row=0, column=1)

lb2.grid(row=1, column=0)
ed2.grid(row=1, column=1)

bt1.grid(row=3, column=1, rowspan=2)

janela.geometry("200x100+100+100")
janela.mainloop()