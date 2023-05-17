#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        lista_linea = linea.split()
        sys.stdout.write("{} {}\n".format(lista_linea[0],lista_linea[2]))