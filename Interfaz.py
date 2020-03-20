#importa modulos
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile

#propiedades del menu
menu = Tk()
menu.geometry("500x500")
menu.title("Menu")
menu.config(bg="orange")

#titulos
titulo = Label(menu,text="Ensamblador en Python",fg = "black",bg = "orange",font = "Helvetica 16 bold italic")
titulo2 = Label(menu,text="Menú",fg = "black",bg = "orange",font = "Helvetica 16 bold italic")
titulo.pack()
titulo2.pack()

#botones
cargar = Button(menu,text="Cargar Archivo",fg = "black",bg = "white",font = "Helvetica 16 bold italic", command=lambda: menu.after(200,botoncargar))
cargar.place(x = 160,y = 120)

traducir = Button(menu,text="Ensamblar",fg = "black",bg = "white",font = "Helvetica 16 bold italic", command=lambda: menu.after(200,traducir))
traducir.place(x = 180,y = 190)

salir = Button(menu,text="Salir",fg = "black",bg = "white",font = "Helvetica 16 bold italic", command=lambda: menu.after(200,salir))
salir.place(x = 200,y = 260)

#funciones
def botoncargar():
    file = askopenfile(mode="r", filetypes=[(".txt", ".txt")])
    if file is not None:
        content = file.read() 
        print(content)
        Lectura.programa(file.name)
  

    #menu.directory = tkFileDialog.askdirectory()
    #print (file)
    #print("boton cargar de picha")
def traducir():
    print("boton traducir de picha")
def salir():
    msgBox = messagebox.askquestion ('Salir','Seguro que desea salir de aplicación?',icon = 'warning')
    if msgBox == 'yes':
        sys.exit()
    else:
        messagebox.showinfo('Retorna','Se regresara a la aplicacion')

        
def main():
    menu.mainloop()


main()

        
