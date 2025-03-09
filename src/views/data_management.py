from tkinter import Tk, ttk, Button, messagebox, Frame
from models.youtube import YoutubeModel

class DataManagementView(Frame):
    def __init__(self, url_youtube:str):
        # root.geometry('500x500')
        # vsr = ttk.Frame(root, padding=10)
        # vsr.grid()
        # root.resizable(False, False)
        fuente = "Roboco Cn"
        
        Button(self, text="1080p", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '1080p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=0)
        Button(self, text="720p", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '720p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=1)
        Button(self, text="480", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '480p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=2)
        Button(self, text="360", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '360p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=3)
        Button(self, text="240", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '240p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=4)
        Button(self, text="144", command=lambda: YoutubeModel.descargar_video_mp4("", url_youtube, '144p'), width=25, height=1, font=(fuente,11)).grid(column=0, row=5)

    def draw(self):
        self.root.mainloop()

    def comprobar_dato_input(self, direccion_video:str):
        print(direccion_video)
        # Preguntar si el link está vacío
        if direccion_video == "" or direccion_video == None:
            messagebox.showerror("Error", "No se ingresó la URL del video")

        elif "clip" in direccion_video:
            print(direccion_video, " Video Clips")

        elif "shorts" in direccion_video:
            print(direccion_video, " Video shorts")
            YoutubeModel.descargar_shorts("", direccion_video)

        elif "playlist" in direccion_video:
            print(direccion_video, " Video Playlist")
            YoutubeModel.descargar_playlist("", direccion_video)

        # Preguntar si el video es de youtube
        elif "youtube.com" in direccion_video or "youtu.be" in direccion_video:
            print(direccion_video, " Video Youtube")
            DataManagementView.ventana_seleccion_resolucion("", direccion_video)
