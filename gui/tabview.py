import customtkinter as ctk
from home import HomePage


class Tabview(ctk.CTkTabview):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)

        self.add('Home')
        self.add('Search')
        self.add('Add')
        self.add('Edit')

        # ====== Creating the Home Page =======
        self.pass_entry = ctk.CTkEntry(self.tab('Home'), placeholder_text='Scan Pass')
        self.pass_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
        self.badge_entry = ctk.CTkEntry(self.tab('Home'), placeholder_text='Scan Badge')
        self.badge_entry.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky='nsew')
        self.checked_in = ctk.CTkScrollableFrame(self.tab('Home'))
        self.checked_in.grid(row=1, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
