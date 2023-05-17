#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    lista = []
    for linea in sys.stdin:
        lista.append(linea)
    
    lista = [fila.replace("\r","") for fila in lista]
    lista = [fila.replace("\n","") for fila in lista]
    lista = [fila.replace("\t",',') for fila in lista]
    lista_aux = ([fila[0] for fila in lista])
    #print(lista_aux)
    for linea in lista_aux:
        sys.stdout.write("{},1\n".format(linea))