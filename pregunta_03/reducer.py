#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    lista = []
    #lista_clave = []
    for linea in sys.stdin:
        lista.append(linea)
    
    lista = [fila.replace("\r","") for fila in lista]
    lista = [fila.replace("\n","") for fila in lista]
    lista = [fila.split(',') for fila in lista]
  
    ordenados = sorted(lista, key = lambda valor: valor[1])

    
    for linea in ordenados:
        sys.stdout.write("{},{}\n".format(linea[0], linea[1]))