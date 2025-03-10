from utils.files import obtener_direccion_carpeta, asignar_carpeta
from views.view import ViewManager
from models.youtube import YoutubeModel

class HomeController:
    def __init__(self, model: YoutubeModel, views: ViewManager):
        self.views = views
        self.model = model
        self._bind()

    def start_mainloop(self):
        self.views.view["home"].draw()

    def _bind(self):
        self.views.view["home"].btnSelectFolder.configure(command=self.on_click_btn_select_folder)

    def on_click_btn_select_folder(self):
        asignar_carpeta()

    def on_click_btn_download(self):
        urlVideo = self.views.view["home"].direccionVideoUniversal.get()
        carpeta = obtener_direccion_carpeta()
        print("Click!", urlVideo, carpeta)
        # ...

    def on_click_btn_download_audio(self):
        pass
