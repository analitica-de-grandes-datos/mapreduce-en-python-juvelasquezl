#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave_actual = None 
    canti = 0  
    
    for linea in sys.stdin:
        clave, valor = linea.split(",")        
        valor = int(valor)                      

        if clave == clave_actual:
            canti += valor
        else:
            if clave_actual is not None:
                sys.stdout.write("{}\t{}\n".format(clave_actual, canti))
            clave_actual = clave
            canti = valor
    sys.stdout.write("{}\t{}\n".format(clave_actual, canti))