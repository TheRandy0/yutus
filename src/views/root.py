from tkinter import Tk, PhotoImage, Label


class RootView(Tk):
    def __init__(self):
        super().__init__()

        # start_width = 500
        # min_width = 400
        # start_height = 300
        # min_height = 250

        # self.geometry(f"{start_width}x{start_height}")
        # self.minsize(width=min_width, height=min_height)
        # self.title("TKinter MVC Multi-frame GUI")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # bgImage = PhotoImage(file="BackGround/minecraft.png")
        # bgLabel = Label(root, image=bgImage)
        # bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.geometry("500x500")
        self.iconbitmap("Icons/apple.ico")
        self.iconphoto(False, PhotoImage(file="Icons/apple.png"))
        self.resizable(False, False)
        self.title("Yutus V1.2")

        bgImage = PhotoImage(file="BackGround/minecraft.png")
        bgLabel = Label(self, image=bgImage)
        bgLabel.place(x=0, y=0, relwidth=1, relheight=1)
