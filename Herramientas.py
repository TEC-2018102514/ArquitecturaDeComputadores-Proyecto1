registros = dict.fromkeys(["R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11",
                           "R12", "R13", "R14", "R15"], 0)  #Todos los registros se inicializan en 0
constant = {}

punto_Program = ''
comandos = []
comandosBase = ["ld", "st", "add", "adc", "and", "jmp", "testl"]
salida = []


def noSpace(linea):             #Elimina todos simbolos que representan espacios y tabs
    linea = linea.replace("➝", "")
    linea = linea.replace("🖵", "")
    return linea


def espComent(linea):           # Cambia todos los espacios y tabs por su representacion
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
        valor = linea[igual+1:]
        literal = linea[:igual]
        if type(literal) == type("") and valorValido(valor):
            constant.pop(literal, valor)
            constant.setdefault(literal, valor)
        else:
            if valorValido(valor):
                constant.setdefault(literal, valor)
            else:
                print("ERROR: valor del literal no valido para la operacion")
    else:
        print("ERROR: Formato de constante incorrecto")


def tipoA(inst, IC, Rf2, Rf1, Rd, K, Tipo, Condicion, f):           #Traduce la instruccion a binario y hexadecimal,
    salida_indiv= {'instruccion': inst, 'binario': '', 'hexa': ''}  # recibe los valores delos datos, exceptuando los
    Rd = regist_strbin(Rd)                                          # registros, que se traducen dentro de la funcion
    Rf1 = regist_strbin(Rf1)
    if Tipo != "1":                 # En caso de que sea tipo 1, un adc, el valor de Rf2 sera "0000"
        Rf2 = regist_strbin(Rf2)
        K = "000000"
    else:
        Rf2 = "0000"
        K = BinToStr(str(bin(K)), 6)           # Envia el valor de k en binario, con el tama;o indicado para instruccion
    inst_bin = f + Condicion + Tipo + K + Rd + Rf1 + Rf2 + IC   # Se agregan los valores en el orden correcto a un string
    salida_indiv['binario'] = inst_bin          #En el diccionario de la instruccion se agregan los valores de salida,
    dec = int(inst_bin,2)                       #Esta salida individual se debe agregar a una lista en donde esten
    salida_indiv["hexa"] = hex(dec)[2:]         #Todos los diccionarios con sus valores de instrucciones
    print(salida_indiv)

def tipoi(funcion,IC,Rb,Dd,Rd):
    salida_indiv = {'instruccion': funcion, 'binario': '', 'hexa': ''}
    Rb = regist_strbin(Rb)
    Dd = BinToStr(bin(Dd),19)
    Rd = regist_strbin(Rd)


    inst_bin = Dd + Rd + Rb + IC
    salida_indiv["binario"] = inst_bin
    dec = int(inst_bin,2)
    salida_indiv["hexa"] = hex(dec)[2:]
    print(salida_indiv)

def tipoJ(inst, Dc, IC):
    salida_indiv= {'instruccion': inst, 'binario': '', 'hexa' : ''}
    Dc = str(Dc)
    binfinal = Dc+IC
    salida_indiv["binario"] = binfinal
    dec = int(binfinal, 2)
    salida_indiv["hexa"] = hex(dec)[2:]
    print(salida_indiv)
    


def regist_strbin(registro):            # Recibe un registro y lo pasa al formato de str, por ejemplo
    RBin = bin(int(registro[1:]))       # regist_strbin("R2") = "0010"
    RBin = str(RBin[2:])
    while len(RBin) < 4:
        RBin = "0" + RBin
    return RBin


def ifRegistro(registro):               # Revisa que el registro exista
    if registro in registros:
        return True
    else:
        return False


def BinToStr(numero, tamaño):           # Recibe un numero binario y lo convierte a string con 0s del tama;o esperado
    nueva = numero[2:]
    i= len(nueva)
    while i< tamaño:
        nueva = "0" + nueva
        i += 1
    return nueva

def BinBase2ToStr(numero, tamaño):           # Recibe un numero binario y lo convierte a string con 1s del tama;o esperado
    nueva = numero[2:]
    i= len(nueva)
    while i< tamaño:
        nueva = "1" + nueva
        i += 1
    return nueva


def valorValido(numero):                #Verifica que el valor sea un hexadecimal, binario o decimal valido, recibe strings
    if ifBin(numero) | ifHex(numero) | numero.isdigit():
        return True
    else:
        return False


def ifBin(numero):                      #Revisa que el valor sea un binario valido, incluyendo que contenga "0b"
    if numero[:2] == "0b":
        numero = numero[2:]

        try:
            int(numero, 2)
            return True
        except:
            print("ERROR: Numero binario incorrecto")
            return False
    else:
        return False


def ifHex(numero):                      # Revisa que el valor sea u hexadecimal valido, incluyendo que contenga "0x"
    if numero[:2] == "0x":
        numero = numero[2:]
        try:
            int(numero, 16)
            return True
        except:
            print("ERROR: Numero hexadecimal incorrecto")
            return False
    else:
        return False


def getNum(numero):
    if ifHex(numero):
        return int(numero[2:], 16)
    elif numero.isdigit():
        return int(numero)
    elif ifBin(numero):
        return int(numero[2:],2)
    else:
        print("ERROR: Valor No Valido")
