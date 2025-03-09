from views.home import HomeView
from controllers.home_controller import HomeController
from models.youtube import YoutubeModel
from views.view import View

def main():
    model = YoutubeModel()
    view = View()
    controller = HomeController(model, view)
    controller.start_mainloop()

if __name__ == "__main__":
    main()
