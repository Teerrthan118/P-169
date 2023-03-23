from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()  
root.geometry("900x600") 
root.title("Classes")

elements = ["Label","Button","Dropdown"]
dropdown = ttk.Combobox(root, state = "readonly", values = elements)
dropdown.pack()

class CreateElements:
    def __init__(self):
        print("This is CreateElements class")
        
    def createLabel(self):
        label = Label(root,text ="A new label is been created using class", fg="red")
        label.pack() 
    def createButton(self):
        class_btn = Button(root, text ="Button", command = self.message)
        class_btn.pack(padx=20, pady = 10) 
    def createDropdown(self):
        numbers = [1,2,3,4]
        combobox = ttk.Combobox(root, state = "readonly", values = numbers)
        combobox.pack() 
    def choose(self):
        global dropdown
        element = dropdown.get()
        if (element == "Label"):
            self.createLabel()
        elif (element == "Button"):
            self.createButton()
        elif (element == "Dropdown"):
            self.createDropdown()
        
    def message(self):
        messagebox.showinfo("showinfo", "You clicked the button created using class")

obj_of_CreateElements = CreateElements()

btn = Button(root, text ="Click to create label and button element", command = obj_of_CreateElements.choose) 
btn.pack(padx=20, pady = 10) 

root.mainloop()
