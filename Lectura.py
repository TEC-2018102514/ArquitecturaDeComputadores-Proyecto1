from Herramientas import *
from Instrucciones import leerInstrucciones


def programa(txt):              # hace la lectura inicial del programa a cargar
    global punto_Program, comandos
    prog_op = open(txt, 'r', encoding='utf-8')
    prog = prog_op.readlines()

    estado = -1                     # Empieza en -1 para revisar que no hayan errores

    for i in prog:
        linea = espComent(i)
        if linea != '':
            if ".program" in linea:
                linea.find(".program")
                punto_Program = linea[9:]       # toma el nombre del programa luego del .program (8 letras) y cambia el estado a 0
                estado = 0
            elif ((estado == 1) or (".const" in linea)) and (".text" not in linea): # Si existen constantes, enctra al if y cambia de estado a 1
                if estado ==-1:
                    print("ERROR: archivo no contiene '.program' ")
                    return 0
                if estado == 1:
                    constantDicc(linea)          # Envia a linea para agregar al diccionario, en caso de que la linea
                if ".const" in linea:     # contenga un .const seguido de la constante, verifica y envia la linea
                    linea = linea.replace(".const", "")  # solo en caso de que luego de remplazar el espaciado, la linea tenga
                    linea = noSpace(linea)       # un tama;o mayor a 2 (a=1)
                    if len(linea) >= 2:
                        constantDicc(linea)
                    elif (len(linea) < 3) and (len(linea) > 0):
                        print("ERROR: Formato incorrecto en las constantes")
                estado = 1
            elif estado == 2 or ".text" in linea:
                if estado == -1:
                    print("ERROR: archivo no contiene '.program' ")
                    return 0
                if estado == 2:
                    comandos += [linea]          # arega los comandos a la lista luego de encontrar el .text, se utiliza
                if ".text" in linea:
                    linea = linea.replace(".text", "")  # aux para verificar que no hayan instrucciones en la misma linea del .text
                    aux = noSpace(linea)
                    if len(aux) >= 1:
                        comandos += [linea]
                estado = 2
            else:
                print("ERROR: declaracion de constantes sin un .const o sin .program")
                return 0
    if len(comandos) == 0:
        print("ERROR, archivo no contiene '.text' ")
        return 0
    print(punto_Program, "\n", constant, "\n", comandos)
    leerInstrucciones(comandos)                 #Una vez revisado el programa, envia la lista de comandos a evaluar

programa("Programa_Ejemplo.txt")
