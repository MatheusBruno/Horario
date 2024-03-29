from time import strftime
from tkinter import *
import os

janela = Tk()
janela.title("Horario")
janela.geometry("800x450")
janela.config(background="#141414")
janela.iconbitmap()

def get_horas():
    data_agora = strftime('%H:%M:%S')
    horas = strftime('%H')
    if int(horas) < 5 or int(horas) > 18 :
        mensagem.config(text=f"Boa Noite, {os.getlogin()}", fg="#b62ff5", bg="#141414")

    if int(horas) >= 5 and int(horas) < 12 :
        mensagem.config(text=f"Bom Dia, {os.getlogin()}", fg="#62e300", bg="#141414")

    if int(horas) >= 12 and int(horas) < 18 :
        mensagem.config(text=f"Boa Tarde, {os.getlogin()}", fg="#db8b00", bg="#141414")

    data.config(text=data_agora)
    data.after(1000,get_horas)
    
Label(width="10", height="4", bg="#141414").pack()
mensagem = Label( font="Arial 50")
mensagem.pack(pady=10)
Label(font="Arial 30", text=f"{strftime('%a, %d %b %Y')}", fg="#b62ff5", bg="#141414").pack()
data = Label(font="Arial 90", fg="#b62ff5", bg="#141414")
data.pack(pady=5)

get_horas()
janela.mainloop()