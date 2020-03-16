
def programa():

    prog_op = open('Programa_Ejemplo.txt', 'r', encoding='utf-8')
    prog = prog_op.readlines()
    punto_Program = []
    constantes = []
    comandos =[]
    estado = -1
    for i in prog:
        linea = espComent(i)
        if linea != '':
            if ".program" in linea:
                punto_Program = [linea[0:7],linea[9:]]
                estado = 0
            elif ((estado == 1) or (".const" in linea)) and (".text" not in linea):
                if estado ==-1:
                    print("Error, archivo no contiene '.program' ")
                    return 0
                constantes += [linea]
                estado = 1
            elif estado == 2 or ".text" in linea:
                if estado == -1:
                    print("Error, archivo no contiene '.program' ")
                    return 0
                comandos += [linea]
                estado = 2
            else:
                print("Formato incorrecto, declaracion de constantes sin un .const")
                return 0
    if len(comandos) == 0:
        print("Error, archivo no contiene '.text' ")
        return 0
    print(punto_Program, "\n", constantes, "\n", comandos)


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


programa()


