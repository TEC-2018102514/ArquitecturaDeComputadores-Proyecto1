from Herramientas import *


def prepareJMP(funcion):        #Hace la evaluacion inicial de la instruccion
    print("[",funcion[3:],"]")
    #suma = 0
    iniciojmp = 0
    #while (suma < 24):
    suma=24
    print ("hola")
    resta = iniciojmp-suma
                                        #Convierte el decimal negativo de la resta en un binario en base 2 del largo del Dc
    s = bin(resta & int("1"*27, 2))[2:]    
    resultadobin = ("{0:0>%s}" % (27)).format(s)
   
    return JMP_fun(funcion, resultadobin) 

        


def JMP_fun(instru, Dc):    #recibe instr
    tipoJ(instru, Dc, "01001")     #Envia los valores para crear
    


