#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

def ordenar(miLista):
    return (miLista.split()[0], int(miLista.split()[2]))

if __name__ == '__main__':

    lista = []
    
    for linea in sys.stdin:
        lista.append(linea)
    resultado = sorted(lista, key = ordenar)
        
    for linea in resultado:
        sys.stdout.write("{}".format(linea))
