from tkinter import *
from datetime import date 
window = Tk()

window.title('Demo Window')
window.geometry('400x300')
# window.mainloop()
lbl = Label(text = "Sample text", fg = "white", bg = "green", height=20, width=5)
name_lbl = Label(text="Full Name", bg ="#000000")
name_entry = Entry()
def display():
     name = name_entry.get()
     message = "We;come to the Application \n Today's date is:"
     greet="hello " "+name+""\n"
     text_box.insert(END,greet)
     text_box.insert(END,message)
     text_box.insert(END, date.today())
text_box=Text(height=3)
btn = Button(text = "Begin", command=display,height=1, bg="#FFFFFF", fg = "white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()