import numpy as np

def llenar(arreglo):
    x = 0
    for d in range (10):
        for c in range (10):
            x = x+1
            if len(str(x)) < 2:
                arreglo[d][c] = '0' + str(x)
            else:
                arreglo[d][c] = str(x)

def mostrar(arreglo):
    for d in range (10):
        fila = ''
        for c in range (10):
            fila = fila + '|' + str(arreglo[d][c])
        print(fila)

def comprar(arreglo,num_asiento):
    x = 0
    for d in range (10):
        for c in range (10):
            x =x+1
            if str(x) == srt(num_asientos):
                arreglo[d][c] = 'XX'

def ComprobarAsiento(arreglo,num_asiento):
    x = 0
    for d in range (10):
        for c in range (10):
            x = x + 1
            if str(x) == str(num_asiento):
                if arreglo[d][c] == 'XX':
                    return False
    return True










