from .root import RootView

from .home import HomeView
from .data_management import DataManagementView

class View:
    def __init__(self):
        self.root = RootView()
        self.frames = {}

        self._add_frame(HomeView, "home")
        #self._add_frame(DataManagementView, "data_management")

    def _add_frame(self, Frame, name: str):
        self.frames[name] = Frame(self.root)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name: str):
        # frame = self.frames[name]
        # frame.tkraise()
        pass

    def start_mainloop(self):
        self.root.mainloop()
