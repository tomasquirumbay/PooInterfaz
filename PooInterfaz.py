from tkinter import *
from tkinter import messagebox

#volver

ventana=Tk()
ventana.title("Bibloteca Virtual Santo Domingo")
ventana.geometry("500x250")
ventana.config(bg="light green")
ventana.resizable(1,1)
tituloPrincipal=Label(ventana,text="Bienvenido a la bibloteca",fg="blue",highlightbackground="light green")
tituloPrincipal.grid(column=0,row=1)
def accionRegistro():
    accion()
registro=Button(ventana,text="Registrarse",fg="black",highlightbackground="light green",command=accionRegistro)
registro.grid(column=0,row=2)

inicio=Button(ventana,text="Inicio de sesion",fg="black",highlightbackground="light green")
inicio.grid(column=0,row=3)
def accion():
    tituloPrincipal.configure(text="Registrate",fg="black",highlightbackground="light green")
    tituloPrincipal.grid(column=0,row=1)
    registro.configure(text="Volver")
    registro.grid(column=0,row=20)


    inicio.configure(text="Guardar")
    inicio.grid(column=1,row=20)
    titulo1=Label(ventana,text="Nombre",fg="black",highlightbackground="light green")
    titulo1.grid(column=0,row=2)
    campo1=Entry(ventana,width=20,highlightbackground="light green")
    campo1.grid(column=1,row=2)
    titulo2=Label(ventana,text="Apellido",fg="black",highlightbackground="light green")
    titulo2.grid(column=0,row=3)
    campo2=Entry(ventana,width=20,highlightbackground="light green")
    campo2.grid(column=1,row=3)
    titulo3=Label(ventana,text="Gmail",fg="black",highlightbackground="light green")
    titulo3.grid(column=0,row=4)
    campo3=Entry(ventana,width=20,highlightbackground="light green")
    campo3.grid(column=1,row=4)

ventana.mainloop()

