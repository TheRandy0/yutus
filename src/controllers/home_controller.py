from views.view import View
from models.youtube import YoutubeModel

class HomeController:
    def __init__(self, model: YoutubeModel, view: View):
        self.view = view
        self.model = model
        self.frame = self.view.frames["home"]
        self._bind(self)

    def start_mainloop(self):
        self.view.start_mainloop()

    def _bind(self):
        self.frame.btnSelectFolder.configure(command=lambda: self.on_click_btn_select_folder(self))

    def on_click_btn_select_folder(self):
        print("Click!")

    def on_click_btn_download(self):
        pass

    def on_click_btn_download_audio(self):
        pass
