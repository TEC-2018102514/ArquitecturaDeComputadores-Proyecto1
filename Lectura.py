constant = {}
punto_Program = ''
comandos = []
comandosBase = ["ld", "st", "add", "adc", "and", "jmp", "testl"]


def programa(txt):
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
                print("ERROR: declaracion de constantes sin un .const")
                return 0
    if len(comandos) == 0:
        print("ERROR, archivo no contiene '.text' ")
        return 0
    print(punto_Program, "\n", constant, "\n", comandos)


def noSpace(linea):
    linea = linea.replace("➝", "")
    linea = linea.replace("🖵", "")
    return linea


def espComent(linea):
    linea = linea.replace("    ", "➝")
    linea = linea.replace(" ", "🖵")
    a = b = 0
    if ';' in linea:
        a = linea.find(";")
        b = linea.find("\n")
    linea = linea.replace(linea[a:b], "")
    linea = linea.replace("\n", "")
    return linea


def constantDicc(linea):            # Elimina los espacios y tabs y toma usando el = el nombre de la variable y el valor
    global constant                 # se maneja en string por que el valor puede ser de formato 0x000
    linea = linea.replace("➝", "")
    linea = linea.replace("🖵", "")
    igual = linea.find("=")
    if ("=" in linea) and (igual > 0) and (igual < len(linea)):
        var = constant.get(linea[igual-1])
        if type(var) == type(""):
            constant.pop(linea[igual-1])
            constant.setdefault(linea[igual-1], linea[igual+1:])
        else:
            constant.setdefault(linea[igual-1], linea[igual+1:])
    else:
        print("ERROR: Formato de constante incorrecto")
