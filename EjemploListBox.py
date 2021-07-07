from tkinter import *

root = Tk()
root.geometry("400x400")

productos = Label(root, text="Productos")

def agregar():
    listaProductos.insert(END, entrada.get())

def eliminar():
    selection = listaProductos.curselection()
    listaProductos.delete(selection)

opcion = IntVar()

listaProductos = Listbox(root, width=50)
listaProductos.insert(0, "Carne")
listaProductos.insert(1, "Pollo")
listaProductos.insert(2, "Verdura")
listaProductos.insert(3, "Jugo")
listaProductos.pack()

# Eliminar productos
#listaProductos.delete(0)

entrada = Entry(root, bd=10)
entrada.pack()

boton = Button(root, text=" Agregar Producto", command=agregar)
boton.pack()

botonDel = Button(root, text="Eliminar Producto",command=eliminar)
botonDel.pack()



root.mainloop()