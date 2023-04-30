from time import strftime
from tkinter import *
import os

janela = Tk()
janela.title("Horario")

screen_width = janela.winfo_screenwidth()
screen_height = janela.winfo_screenheight()
position_top = int(screen_height/2 - 600/2)
position_lat = int(screen_width/2 - 600/2)

print(screen_height)
print(screen_width)

janela.geometry(f"650x500+{position_lat}+{position_top}")
janela.config(background="#141414")
janela.iconbitmap("matheus.ico")

def get_horas():
    data_agora = strftime('%H:%M:%S')
    horas = strftime('%H')
    if int(horas) < 5 or int(horas) > 18 :
        mensagem.config(text=f"Boa Noite, {os.getlogin()}", fg="#b62ff5", bg="#141414")

    if int(horas) >= 5 and int(horas) <= 12 :
        mensagem.config(text=f"Bom Dia, {os.getlogin()}", fg="#62e300", bg="#141414")

    if int(horas) > 12 and int(horas) < 18 :
        mensagem.config(text=f"Boa Tarde, {os.getlogin()}", fg="#db8b00", bg="#141414")

    data.config(text=data_agora)
    data.after(1000,get_horas)
    
# # Label(width="10", height="4", bg="#141414").place(relx = 0.5, rely = 0.5,anchor=CENTER)
mensagem = Label( font="Arial 50")
mensagem.place(relx = 0.5, rely = 0.15,anchor=CENTER)
Label(font="Arial 30", text=f"{strftime('%a, %d %b %Y')}", fg="#b62ff5", bg="#141414").place(relx = 0.5, rely = 0.3,anchor=CENTER)
data = Label(font="Arial 90", fg="#b62ff5", bg="#141414")
data.place(relx = 0.5, rely = 0.5,anchor=CENTER)

get_horas()
janela.resizable(0,0)
janela.mainloop()

#pyinstaller --onefile --noconsole --icon=C:/Users/Matheus/Documents/horas/matheus.ico .\programahoras.py