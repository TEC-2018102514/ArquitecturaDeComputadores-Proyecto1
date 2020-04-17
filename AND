import Lectura

registros = "R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12", "R13", "R14", "R15"


def prepareAND(funcion):
    funcion = Lectura.espComent(funcion)
    funcion = Lectura.noSpace(funcion)
    funcion = funcion[3:].split(",")
    print(registros)
    if len(funcion) == 3:
        for item in funcion:
            if not ifRegistro(item):
                print("ERROR: Registro inexistente")
            else:
                return AND_fun(funcion[0], funcion[1], funcion[2])

    else:
        print("ERROR: Cantidad de registros erronea")
    print(funcion)


def AND_fun(destino, valor1, valor2):
    print(registros.get(valor1))
    valorFinal = int(registros.get(valor1), 2) & int(registros.get(valor2), 2)
    registros[destino] = int(str(valorFinal), 16)
    print(registros.get(destino))


def ifRegistro(registro):
    if registro in registros:
        return True
    else:
        return False


def ifBin(numero):
    try:
        int(numero, 2)
        return True
    except:
        return False


def ifHex(numero):
    try:
        int(numero, 16)
        return True
    except:
        return False
