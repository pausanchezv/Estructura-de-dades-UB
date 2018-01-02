# autores: Pau Sanchez Valdivieso y Albert Espin Roman
from Time import *

# dado un tiempo y una lista de tiempos da cuantos tiempos de la lista son menores
def estadisticaFormulaUno(lista,h,m,s):
    tiempoPatron = Time(h,m,s) # creamos un tiempo con los valores temporales de los parametros
    listaMejoresTiempos = [] # lista para guardar los tiempos que estan por debajo al patron
    # iteramos la lista, comparamos los segundos totales de cada tiempo con el tiempo patron, ampliamos la lista con los tiempos mas rapidos y retornamos el numero de pilotos con tiempos por debajo del tiempo patron
    return len([listaMejoresTiempos.append(item) for item in lista if item.time_to_int() < tiempoPatron.time_to_int()])


def ej2(h=1,m=40,s=0):
    lista=[Time(1,38,26),Time(1,39,16),Time(1,39,7),Time(1,39,55), Time(1,39,54), Time(1,40,9),
    Time(1,40,11), Time(1,40,51), Time(1,40,05), Time(1,40,38), Time(1,40,55), Time(1,40,56),
    Time(1,40,55), Time(1,41,46), Time(1,41,52), Time(1,41,15), Time(1,42,36), Time(1,43, 9), Time(1,43,5),
    Time(1,44,37)] # se llena la lista de elementos de tipo tiempo
    print "El numero de deportistas con tiempo menor es: {}".format(estadisticaFormulaUno(lista, h,m,s))
    # encontramos con el tiempo pasado como parametros cuantos deportistas estan por debajo

ej2(1,41)