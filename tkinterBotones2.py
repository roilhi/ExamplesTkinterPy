import tkinter as tk
from tkinter import ttk 

root = tk.Tk()

# recibe un argumento por parametro y recibe lo que el usuario seleccione en los botones

def seleccionar(opcion):
    print(opcion)

# el comando lambda permite que se seleccione lo que el usuario ingresa como argumento o parametro
ttk.Button(root, text="Python", command=lambda:seleccionar("Python")).pack()
ttk.Button(root, text="Java", command=lambda:seleccionar("Java")).pack()
ttk.Button(root, text="Javascript", command=lambda:seleccionar("Javascript")).pack()
root.mainloop()