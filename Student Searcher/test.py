
from tkinter import *
window = Tk()

window.title("Student searcher")
def submit():
    username = entry.get()
    print("Hello " + username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1, END)

entry = Entry (window, 
               font=("sans-serif", 50),
               fg="#134123",
               bg="cyan")
entry.insert(0, "spongebob")
entry.pack(side=LEFT)



entry.pack(side=LEFT)

submit_button = Button(window,text="Submit",command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text="Delete",command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text="Backspace",command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()