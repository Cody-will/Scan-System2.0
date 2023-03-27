import customtkinter as ctk
import functionality as func

root = ctk.CTk()
root.geometry('800x600')
root.title('Scan System')

ctk.set_appearance_mode("Dark")

mainPage = ctk.CTkTabview(root)
mainPage.pack(fill="both")

'''Creates the pages for the tabview'''

home = mainPage.add("Home")
search = mainPage.add("Search")
addNew = mainPage.add("Add")

'''Main home page frame'''

scanPassEntry = ctk.CTkEntry(mainPage.tab('Home'), placeholder_text='Scan Pass')
scanPassEntry.pack(padx=10, pady=(15, 0))

scanBadgeEntry = ctk.CTkEntry(mainPage.tab('Home'), placeholder_text='Scan Badge')
scanBadgeEntry.pack(padx=10, pady=10)

checkedIn = ctk.CTkScrollableFrame(mainPage.tab('Home'))
checkedIn.pack(padx=0, pady=5, fill="both")

'''Search page frame'''

searchByLabel = ctk.CTkLabel(mainPage.tab('Search'), text="Select Option")
searchByLabel.pack(padx=5, pady=(15, 0))

searchBy = ctk.CTkComboBox(mainPage.tab('Search'), values=['Name', 'Pass Number', 'Associate Number'])
searchBy.pack(padx=5, pady=(0, 10))

searchData = ctk.CTkEntry(mainPage.tab("Search"))
searchData.pack(padx=5, pady=10)

searchButton = ctk.CTkButton(mainPage.tab('Search'), text='Search')
searchButton.pack(padx=5, pady=10)

resultsFrame = ctk.CTkScrollableFrame(mainPage.tab('Search'))
resultsFrame.pack(padx=5, pady=10, fill='both')

'''Add frame. Frame for adding new people or property to the database to give them the ability to be checked in'''

firstNameInput = ctk.CTkEntry(mainPage.tab('Add'), placeholder_text='First Name')
firstNameInput.pack(padx=10, pady=10)

lastNameInput = ctk.CTkEntry(mainPage.tab('Add'), placeholder_text='Last Name')
lastNameInput.pack(padx=10, pady=10)

assocNumInput = ctk.CTkEntry(mainPage.tab('Add'), placeholder_text='Associate Number')
assocNumInput.pack(padx=10, pady=10)

passNumInput = ctk.CTkEntry(mainPage.tab('Add'), placeholder_text='Pass Number')
passNumInput.pack(padx=10, pady=10)

descriptionInput = ctk.CTkEntry(mainPage.tab('Add'), placeholder_text='Description')
descriptionInput.pack(padx=10, pady=10)

addButton = ctk.CTkButton(mainPage.tab('Add'), text='Add')
addButton.pack(padx=10, pady=10)

clearButton = ctk.CTkButton(mainPage.tab('Add'), text='Clear')
clearButton.pack(padx=10, pady=10)






if __name__ == '__main__':
    root.mainloop()
