from tkinter import Tk, PhotoImage, Entry, Label, Button
from libreriasYutus import descarga_videos_youtube, manejo_carpetas, manejo_datos
import os

root = Tk() 
root.geometry("500x500")
root.iconbitmap("Icons/apple.ico")
root.iconphoto(False, PhotoImage(file="Icons/apple.png"))
root.resizable(False, False)
root.title("Yutus V1.2")

bgImage = PhotoImage(file="BackGround/minecraft.png")
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

direccionVideoUniversal = Entry(root)
direccionVideoUniversal.place(x= 1, y = 0, height=28, width=190)

direccionAudio = Entry(root)
direccionAudio.place(x= 1, y = 60, height=28, width=190)

def nada_de_nada():
    direccion_video = direccionVideoUniversal.get().strip()
    print(direccionVideoUniversal)
    return direccion_video

def nada_audio():
    direccion_video = direccionAudio.get().strip()
    print(direccion_video)
    return direccion_video

Button(root, text="Seleccionar carpeta de descarga", command=lambda: manejo_carpetas.asignar_carpeta("")).place(x = 1, y = 90, width=190, height=28)
Button(root, text="Descarga univesal", command=lambda: manejo_datos.comprobar_dato_input("", nada_de_nada()), width=25, height=1, font=("Roboto Cn", 11)).place(x=265, y=0)
Button(root, text="Descargar Audio", command=lambda: descarga_videos_youtube.descargar_audio("", nada_audio()), width=25, height=1, font=("Roboco Cn", 11)).place(x=265, y=60)

root.mainloop()