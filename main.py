import customtkinter as ctk
import functionality as func

root = ctk.CTk()

ctk.set_appearance_mode("Dark")

inputFrame = ctk.CTkFrame(root)
inputFrame.pack(padx=5, pady=5)

scanPassLabel = ctk.CTkLabel(inputFrame, text="Scan Pass")
scanPassLabel.pack()

scanPassEntry = ctk.CTkEntry(inputFrame)
scanPassEntry.pack(padx=5, pady=5)

scanBadgeLabel = ctk.CTkLabel(inputFrame, text="Scan Badge")
scanBadgeLabel.pack()

scanBadgeEntry = ctk.CTkEntry(inputFrame)
scanBadgeEntry.pack(padx=5, pady=5)

checkedInList = ctk.CTkScrollableFrame(root)
checkedInList.pack()

addButton = ctk.CTkButton(root, text="Add")
addButton.pack(padx=5, pady=5)

searchButton = ctk.CTkButton(root, text="Search")
searchButton.pack(padx=5, pady=5)

if __name__ == '__main__':
    root.mainloop()
