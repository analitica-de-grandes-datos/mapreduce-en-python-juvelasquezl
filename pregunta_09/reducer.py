#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

def ordenar(miLista):
    return (int(miLista.split()[2]))

if __name__ == '__main__':

    lista = []
   
    for linea in sys.stdin:
        lista.append(linea)
    resultado = sorted(lista, key = ordenar)
       
    for linea in resultado[:6]:
        sys.stdout.write("{}".format(linea))