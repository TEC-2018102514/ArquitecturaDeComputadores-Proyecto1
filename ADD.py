#ADD
from Herramientas import *
from tkinter import *
from tkinter import messagebox


def prepareADD(funcion):        #Hace la evaluacion inicial de la instruccion
    funcstr = funcion
    funcion = funcion[3:].split(",")
    print(funcion)
    if len(funcion) == 3:       #Que contenga 3 Registros se
        for item in funcion:
            #HOLAAAA

            if ifRegistro(item):        #Que los registros existan
                valor = registros.get(item)
                try:
                    nuevo = bin(valor)
                    registros.setdefault(item, nuevo)
                except:
                    msgBox = messagebox.showinfo('Error',"Error, vuélvalo a intentar", icon = 'warning')
            else:
                msgBox = messagebox.showinfo('Error',"Registro inexistente", icon = 'warning')

        return AND_fun(funcstr,funcion[0], funcion[1], funcion[2])  #Una vez validado el contenido pasa a la operacion

    else:
        msgBox = messagebox.showinfo('Error',"Cantidad de registros errónea", icon = 'warning')
    print(funcion)


def AND_fun(funcion, destino, valor1, valor2):      # Recibe la funcion, Rd,Rf1,Rf2
    tipoA(funcion, "00001", valor2, valor1, destino, "000000", "0", "0000", "0100")     #Envia los valores para crear
    valor1 = registros.get(valor1)                                  #El codigo binario y exadecimal de la instruccion
    valor2 = registros.get(valor2)
    valorFinal = valor1 & valor2                                    #Realiza la operacion y la carga a los registros
    registros[destino] = valorFinal
    print(registros.get(destino))
