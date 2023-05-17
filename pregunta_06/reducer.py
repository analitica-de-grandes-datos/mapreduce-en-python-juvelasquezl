#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    clave_ant = None 
    mayor = 0 
    menor = 9999 
    
    for linea in sys.stdin:
        clave, valor = linea.split(",")        
        valor = float(valor)                      

        if clave != clave_ant and clave_ant is not None:
            sys.stdout.write("{}\t{}\t{}\n".format(clave_ant, mayor, menor))
            mayor = 0
            menor = 9999
        if valor > mayor:
            mayor =  valor
        if valor < menor:
            menor = valor
        clave_ant = clave
    sys.stdout.write("{}\t{}\t{}\n".format(clave_ant, mayor, menor))