from Herramientas import *


def prepareTESTL(funcion):        #Hace la evaluacion inicial de la instruccion
    funcstr = funcion
    funcion = funcion[5:].split(",")
    print(funcion)
    if len(funcion) == 2:       #Que contenga 3 Registros se
        for item in funcion:
            if ifRegistro(item):        #Que los registros existan
                valor = registros.get(item)
                try:
                    nuevo = bin(valor)
                    registros.setdefault(item, nuevo)
                except:
                    print("no se pudo")
            else:
                print("ERROR: Registro inexistente")

        return TESTL_fun(funcstr,funcion[0], funcion[1])  #Una vez validado el contenido pasa a la operacion

    else:
        print("ERROR: Cantidad de registros erronea")
    print(funcion)


def TESTL_fun(funcion, valor1, valor2):      # Recibe la funcion,Rf1,Rf2
        tipoA(funcion, "00001", valor2, valor1, "0000", "000000", "0", "0101", "0101")     #Envia los valores para crear la funcion
        

        
