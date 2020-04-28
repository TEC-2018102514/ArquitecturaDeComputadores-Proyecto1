from Herramientas import espComent, noSpace
from AND import prepareAND
from ADC import prepareADC
from ADD import prepareADD
from LDcambios import prepareLd



def leerInstrucciones(comandos):    # Se utiliza para evaluar as funciones una a una
    if len(comandos) >= 0:
        for item in comandos:
            item = espComent(item)
            item = noSpace(item)
            if "and" in item:
                prepareAND(item)
            elif "adc" in item:        #CHES
                prepareADC(item)

            elif "add" in item:        #SANTI
                prepareADD(item)
            #elif "jump" in item:

            #elif "st" in item:         #PIA

            elif "ld" in item:
                prepareLd(item)
            #DANI
            #elif "tstl" in item:

            #else:  (el unico caso que se puede presentar es que este marcando el inicio de un jump)

