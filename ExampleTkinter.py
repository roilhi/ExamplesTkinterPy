from tkinter import *
obj = Tk()
obj.title("Example Tkinter Visual Studio")
obj.geometry("300x300")
wintext = Text(obj)
wintext.insert(INSERT, " Hello ....")
wintext.insert(END, "This is an example")
wintext.pack()
obj.mainloop()



