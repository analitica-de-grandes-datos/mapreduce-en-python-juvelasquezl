#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for linea in sys.stdin:
        clave, valor = linea.split()   
        for letra in valor.split(','):
            sys.stdout.write("{} {}\n".format(letra,clave))   