from .home import HomeView
from .data_management import DataManagementView

class ViewManager:
    def __init__(self):
        self.root = None
        self.view = {
            "home": HomeView(),
            #"data_management": DataManagementView("")
        }
