from tkinter import * 
from tkinter import messagebox
root = Tk()

menuBar = Menu(root)
root.config(menu=menuBar)

def cerrar():
    messagebox.askquestion("Cerrar", message="¿Estás seguro?")

def licencia():
    messagebox.showinfo("Version", message="Version 1.0")

def error():
    messagebox.showerror("¡Error crítico!", message="Se encontró un error fatal")

def atencion():
    messagebox.showwarning("ATENCION", message="Se borrará el actual")


archivoMenu=Menu(menuBar,tearoff=0)

archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir", command=atencion)
archivoMenu.add_command(label="Guardar", command=error)
archivoMenu.add_command(label="Cerrar", command=cerrar)
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=root.quit)

editMenu=Menu(menuBar,tearoff=0)
editMenu.add_command(label="Cortar")
editMenu.add_command(label="Copiar")
editMenu.add_command(label="Pegar")

ayudaMenu=Menu(menuBar,tearoff=0)
ayudaMenu.add_command(label="Licencia", command=licencia)
ayudaMenu.add_separator()

menuBar.add_cascade(label="Archivo",menu=archivoMenu)
menuBar.add_cascade(label="Editar",menu=editMenu)
menuBar.add_cascade(label="Ayuda",menu=ayudaMenu)
root.mainloop()