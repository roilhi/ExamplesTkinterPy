from tkinter import Tk, Text

root= Tk()

root.resizable(False, False)
root.title("Mi bloc de notas")

text = Text(root, height=8)
text.pack()


text.insert('1.0', 'Esto es un ejemplo de block de notas')

root.mainloop()
