
from Asistentes import *
from Funciones import *
import numpy as np

lista_asistente = []
num_asiento = 0

arreglo = np.full(10,10)
ciclo = True

def AgregarAsistente(arreglo,num_asiento):
    a = Asistente()
    a.rut = int(input("Ingrese Rut:"))
    a.Nombre = int(input("Ingrese Nombre:"))
    a.Num_asiento = num_asiento
    if num_asiento >= 1 and num_asiento <= 20:
        a.valor = 120000
    if num_asiento >= 21 and num_asiento <= 50:
        a.valor = 80000
    if num_asiento >= 51 and num_asiento <= 100:
        a.valor = 50000
    lista_asistente.append(a,)

def ComprarEntrada(arreglo, lista_asistente):
    try:
        can_asientos = int(input("Seleccione Cantidad de Asientos:"))
        if can_asientos >=1 and can_asientos <= 3:
            compra = 0
            while compra < can_asientos:
                mostrar(arreglo)
                num_asiento = int(input("seleccione Asientos:"))
                if num_asiento >= 1 and num_asiento <= 100:
                    disponible = ComprobarAsiento(arreglo, num_asiento)
                    if disponible == True:
                        ComprarEntrada(lista_asistente)
                        compra(arreglo)
                    else:
                        print("No disponible")
                else:
                    print("No disponible")
        else:
            print("Ubicaciones entre 1 y 3")
    except BaseException as error:
        print(f"Error{error}")

ComprobarAsiento(arreglo,num_asiento)

def ListadoAsistentes(lista_asistente):
    for a in lista_asistente:
        print(f"Nombr:  {a.Nombre}")
        print(f"Valor:  {a.valor}")
        print(f"asiento:{a.asiento}")

def MostrarGanacias(lista_asistente):
    P = 0
    g = 0
    s = 0
    tot_p = 0
    tot_g = 0
    tot_s = 0
    for f in lista_asistente:
        if int(f.valor) == 120000:
            p = p + 1
            tot_p = tot_p + 120000
        if int(f.valor) == 80000:
            g = g + 1
            tot_g = tot_g + 80000
        if int(f.valor) == 50000:
            s = s + 1
            tot_s = tot_s + 50000
    print(f"pla: cantidad{p}  total:{tot_p}")
    print(f"gol: cantidad{g}  total:{tot_g}")
    print(f"sil: cantidad{s}  total:{tot_s}")

def salir():
    print(".....")
    return False

while ciclo:
    print("Menu Principal")
    print("1) Comprar Entrada")
    print("2) Mostrar Ubicaciones disponibles")
    print("3) Ver Listado de Asistentes")
    print("4) Mostrar Ganancias Totales")
    print("5) Salir")
    try:
        op = int(input("Seleccione (1-5):"))
        match op:
            case 1:
                ComprarEntrada(arreglo,lista_asistente)
            case 3:
                ListadoAsistentes(lista_asistente)
            case 4:
                MostrarGanacias(lista_asistente)
            case 5:
                ciclo = salir()
    except BaseException as error:
        print(f"Error{error}")

