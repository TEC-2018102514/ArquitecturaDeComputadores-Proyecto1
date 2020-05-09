from Herramientas import espComent, noSpace
from AND import prepareAND
from ADC import prepareADC
from ADD import prepareADD
from JMP import prepareJMP
from LDcambios import prepareLd



def leerInstrucciones(comandos):    # Se utiliza para evaluar as funciones una a una
    if len(comandos) >= 0:
        cont=0
        for item in comandos:
            item = espComent(item)
            item = noSpace(item)
            if "and" in item:
                prepareAND(item)
                cont+=4
            elif "adc" in item:        #CHES
                prepareADC(item)
                cont+=4

            elif "add" in item:        #SANTI
                prepareADD(item)
                cont+=4
            elif "jmp" in item:
                cont+=4
                prepareJMP(item, cont)

            #elif "st" in item:         #PIA

            elif "ld" in item:
                prepareLd(item)
                cont+=4
            #DANI
            #elif "tstl" in item:

            #else:  #(el unico caso que se puede presentar es que este marcando el inicio de un jump)
                

