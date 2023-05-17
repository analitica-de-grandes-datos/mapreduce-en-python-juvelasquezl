#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave_actual = None
    canti = 0  
    conta = []
    for linea in sys.stdin:
        clave, valor = linea.split()        
        valor = float(valor)                      

        if clave == clave_actual:
            canti += valor
            conta.append(1)
        else:
            if clave_actual is not None:
                promedio = canti / len(conta)
                sys.stdout.write("{}\t{}\t{}\n".format(clave_actual, canti, promedio))
            clave_actual = clave
            canti = valor
            conta = [1]
    promedio = canti / len(conta)
    sys.stdout.write("{}\t{}\t{}\n".format(clave_actual, canti, promedio))