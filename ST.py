from Herramientas import *

def prepareST(funcion):  # Hace la evaluacion inicial de la instruccion #"ldR1,a(R15)"
    funcaux = funcion
    if funcion[-1] == ")" and (funcion[-4] == "(" or funcion[-5] == "("):
        funcion = funcion[2:-1].replace("(",",")
        funcion = funcion.split(",")
        print(funcion)
        if len(funcion) == 3:  # Que contenga 3 Registros se
            i = 0
            for item in funcion:
                if i != 1 and not ifRegistro(item):
                    print("ERROR: Registros Invalidos")
                    return 0

                else:
                    if i == 1:
                        if item in constant:
                            constante = getNum(constant.get(item))
                        else:
                            if valorValido(item):
                                constante = getNum(item)
                            else:
                                print("ERROR: Valor no valido")
                                return 0
                i += 1

            return ST_fun(funcaux, funcion[2], constante, funcion[0])  # Una vez validado el contenido pasa a la operacion

        else:
            print("ERROR: Cantidad de registros erronea")
        print(funcion)
    else:
        print("ERROR: Error en la sintaxis de la instrucción")

def ST_fun(funcion, Rb ,Dd, Rd):  # Recibe la funcion, Rd,Dd,Rb
    tipoi(funcion,"00011",Rb,Dd,Rd)  # Envia los valores para crear
