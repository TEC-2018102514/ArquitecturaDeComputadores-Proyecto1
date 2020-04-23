from Herramientas import *

def prepareADC(funcion):
    funcstr = funcion
    funcion = funcion[3:].split(",")
    print(funcion)
    if len(funcion) == 3:
        for item in funcion:
            i = 0
            if i == 0 and not ifRegistro(item):
                print("ERROR: Registro Destino Invalido")
                return 0

            if i == 1 and ifRegistro(item):
                valorR1 = registros.get(item)
            else:
                print("ERROR: Registro 1 No Valido")
                return 0
            #if i == 2:
                #if item in constant:
                    #if :

            i += 1
        #return AND_fun(funcstr, funcion[0], funcion[1], funcion[2])

    else:
        print("ERROR: Cantidad de elementos erronea")
        return 0
    print(funcion)

