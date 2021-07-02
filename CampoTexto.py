from tkinter import * 
root = Tk()

root.title("Entrada")
root.geometry("300x300")
root.resizable(0,0)
# string var variables de control para asociar los widgets 
nombre   = StringVar()
apellido = StringVar()
saludo = StringVar()
nombre.set("Escribe aquí tu nombre: ")
apellido.set("Escribe aquí tu apellido: ")

#get recibe lo almacenado en la variable nombre y apellido
def saludar():
    saludo.set("Hola "+nombre.get()+ " "+apellido.get())

etiqueta1 = Label(root, text="Escribe aquí tu nombre: ", bd=4, bg="red",font=("Curier 10"))
etiqueta1.place(x=10, y=10)
# Entry es la caja de texto asociada 
entrada1 = Entry(root,textvariable = nombre, bd=5)
entrada1.place(x=170, y=10)


etiqueta2 = Label(root, text="Escribe aquí tu apellido: ", bd=4, bg="red",font=("Curier 10") )
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable = apellido, bd=5)
entrada2.place(x=170, y=40)

boton = Button(root, text="Saludar ahora", command=saludar, bd=5, bg="red")
boton.place(x=112, y=123)

entrada3 = Entry(root, bd=20, font=("Curier 10"), textvariable=saludo, state="disable")
entrada3.place(x=70, y=221)

root.mainloop()