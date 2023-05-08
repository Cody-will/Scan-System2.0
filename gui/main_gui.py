import customtkinter as ctk
from tabview import Tabview


class Gui(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry('1000x600')
        self.title('Scan System 2.0')
        self.appearance = self._set_appearance_mode('dark')

        self.home_frame = ctk.CTkFrame(self)
        self.home_frame.grid(row=0, column=0, sticky='nsew')
        self.tabview = Tabview(self.home_frame)
        self.tabview.grid(row=0, column=0, sticky='nsew')

        self.grid_rowconfigure('all', weight=1)
        self.grid_columnconfigure('all', weight=1)

        self.home_frame.grid_rowconfigure('all', weight=1)
        self.home_frame.grid_columnconfigure('all', weight=1)


gooey = Gui()

gooey.mainloop()
