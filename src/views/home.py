from tkinter import Frame, PhotoImage, Entry, Label, Button
from models.youtube import YoutubeModel
from utils.files import manejo_carpetas
from views.data_management import DataManagementView

class HomeView(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight=1)

        # root.geometry("500x500")
        # root.iconbitmap("Icons/apple.ico")
        # root.iconphoto(False, PhotoImage(file="Icons/apple.png"))
        # root.resizable(False, False)
        # root.title("Yutus V1.2")

        # bgImage = PhotoImage(file="BackGround/minecraft.png")
        # bgLabel = Label(root, image=bgImage)
        # bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        direccionVideoUniversal = Entry(self)
        direccionVideoUniversal.place(x= 1, y = 0, height=28, width=190)

        direccionAudio = Entry(self)
        direccionAudio.place(x= 1, y = 60, height=28, width=190)

        # self.bgImage = bgImage
        # self.bgLabel = bgLabel
        self.direccionVideoUniversal = direccionVideoUniversal
        self.direccionAudio = direccionAudio

        btnSelectFolder = Button(self, text="Seleccionar carpeta de descarga")
        btnSelectFolder.place(x = 1, y = 90, width=190, height=28)

        btnDownload = Button(self, text="Descarga univesal", width=25, height=1, font=("Roboto Cn", 11))
        btnDownload.place(x=265, y=0)

        btnDownloadAudio = Button(self, text="Descargar Audio", width=25, height=1, font=("Roboco Cn", 11))
        btnDownloadAudio.place(x=265, y=60)

        #Button(root, text="Seleccionar carpeta de descarga", command=lambda: manejo_carpetas.asignar_carpeta("")).place(x = 1, y = 90, width=190, height=28)
        #Button(root, text="Descarga univesal", command=lambda: DataManagementView.comprobar_dato_input("", self.nada_de_nada(self)), width=25, height=1, font=("Roboto Cn", 11)).place(x=265, y=0)
        #Button(root, text="Descargar Audio", command=lambda: YoutubeModel.descargar_audio("", self.nada_audio(self)), width=25, height=1, font=("Roboco Cn", 11)).place(x=265, y=60)

        self.btnSelectFolder = btnSelectFolder
        self.btnDownload = btnDownload
        self.btnDownloadAudio = btnDownloadAudio

    def draw(self):
        self.root.mainloop()

    def nada_de_nada(self):
        direccion_video = self.direccionVideoUniversal.get().strip()
        print(self.direccionVideoUniversal)
        return direccion_video

    def nada_audio(self):
        direccion_video = self.direccionAudio.get().strip()
        print(direccion_video)
        return direccion_video
