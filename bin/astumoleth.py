import PIL
import tkinter as tk
import assetloader as data

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.load_data()
        self.create_widgets()

    def load_data(self):
        pass

    def create_widgets(self):
        pass

if __name__ == '__main__':
    app = Application()
    assets = data.Assets()
    app.master.title("Astumoleth - " + assets["title"])
    app.master.grid(None, None, 8, 16)
    app.master.minsize(1024, 512)
    app.mainloop()
