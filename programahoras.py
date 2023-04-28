from time import strftime
from tkinter import *
import os

janela = Tk()
janela.title("Horario")
janela.geometry("800x450")
janela.config(background="#110d04")

def get_horas():
    data_agora = strftime('%H:%M:%S')
    horas = strftime('%H')
    if int(horas) < 5 or int(horas) > 18 :
        mensagem.config(text="Boa Noite")

    if int(horas) >= 5 and int(horas) < 12 :
        mensagem.config(text="Bom Dia")

    if int(horas) >= 12 and int(horas) < 18 :
        mensagem.config(text="Boa Tarde")

    data.config(text=data_agora)
    data.after(1000,get_horas)
    

Label(font="Arial 50", text=f"Olá, {os.getlogin()}", fg="Pink", bg="#110d04").pack()
Label(font="Arial 30", text=f"{strftime('%a, %d %b %Y')}", fg="Pink", bg="#110d04").pack()
data = Label(font="Arial 90", fg="Pink", bg="#110d04")
data.pack()
mensagem = Label( font="Arial 50", fg="Pink", bg="#110d04")
mensagem.pack()
get_horas()
janela.mainloop()