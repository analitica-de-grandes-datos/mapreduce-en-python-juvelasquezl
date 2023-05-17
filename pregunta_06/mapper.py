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
    lista = [fila.replace("   ",',') for fila in lista]
    lista = [fila.split(',') for fila in lista]
            
    for linea in lista:
       sys.stdout.write("{},{}\n".format(linea[0],linea[2]))