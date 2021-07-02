from tkinter import * 

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

#etiqueta = Label(root, text="Etiqueta")
#etiqueta.grid(row=0, column=0)
#etiqueta.place(x=30, y=40)
#boton1 = Button(root, text="Boton")
#boton1.grid(row=0, column=1)
def saludo():
    print("Hola te saludo")

def minimizar():
    root.iconify()


etiqueta1 = Label(root, text="Saluda desde aquí")
etiqueta1.place(x=30, y=50)

etiqueta2 = Label(root, text="Minimizar desde aquí")
etiqueta2.place(x=30, y=10)

boton1 = Button(root, text="Haz click aquí para saludar",command = saludo)
boton1.place(x=200, y=50)

boton2 = Button(root, text="Haz click aquí para minimizar", command = minimizar)
boton2.place(x=200, y=100)
root.mainloop()