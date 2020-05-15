from Herramientas import *
from tkinter import *
from tkinter import messagebox

def prepareADC(funcion):
    funcstr = funcion
    funcion = funcion[3:].split(",")
    print(funcion)
    constante = None
    if len(funcion) == 3:
        i = 0
        for item in funcion:
            if i != 2 and not ifRegistro(item):
                msgBox = messagebox.showinfo('Error',"Registros inválidos", icon = 'warning')
                return 0
            else:
                if i == 2:
                    if item in constant:
                        constante = getNum(constant.get(item))
                    else:
                        if valorValido(item):
                            constante = getNum(item)
                        else:
                            msgBox = messagebox.showinfo('Error',"Valor no válido", icon = 'warning')
                            return 0

            i += 1
    else:
        msgBox = messagebox.showinfo('Error',"Cantidad de elementos errónea", icon = 'warning')
        return 0
    if constante is not None:
        return ADC_fun(funcstr,funcion[0],funcion[1],constante)


def ADC_fun(funcion, Destino, Rf1, K):
    tipoA(funcion, "00001", "0000", Rf1, Destino, K, "1", "0000", "0100")
    registros[Destino] = K + registros.get(Rf1)
    print(registros)
