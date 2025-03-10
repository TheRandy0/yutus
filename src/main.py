from controllers.home_controller import HomeController
from models.youtube import YoutubeModel
from views.view import ViewManager

def main():
    model = YoutubeModel()
    view_manager = ViewManager()
    controller = HomeController(model, view_manager)
    controller.start_mainloop()

if __name__ == "__main__":
    main()
