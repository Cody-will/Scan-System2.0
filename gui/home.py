import customtkinter as ctk


class HomePage:
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # creates entry boxes to scan pass and badge
        self.pass_entry = ctk.CTkEntry(self.parent, placeholder_text='Scan Pass')
        self.badge_entry = ctk.CTkEntry(self.parent, placeholder_text='Scan Badge')
        # creates the scrollable frame to put the list of checked in properties
        self.checked_in = ctk.CTkScrollableFrame(self.parent)


