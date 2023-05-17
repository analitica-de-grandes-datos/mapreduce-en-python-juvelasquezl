#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave_actual = None 
    canti = []  
    
    for linea in sys.stdin:
        clave, valor = linea.split()
        valor = int(valor)        
        if clave == clave_actual:
            canti.append(valor)
        else:
            if clave_actual is not None:
                canti.sort()
                linea = ",".join(str(value) for value in canti)
                sys.stdout.write("{}\t{}\n".format(clave_actual, linea))
                canti = []
            clave_actual = clave
            canti.append(valor)
    canti.sort()
    linea = ",".join(str(value) for value in canti)
    sys.stdout.write("{}\t{}\n".format(clave_actual, linea))
