#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys 

if __name__ == '__main__':

    clave_ant = None 
    mayor = 0  
    
    for linea in sys.stdin:
        clave, valor = linea.split("\t")        
        valor = int(valor)                      

        if clave != clave_ant and clave_ant is not None:
            sys.stdout.write("{}\t{}\n".format(clave_ant, mayor))
            mayor = 0
        if valor > mayor:
                mayor =  valor
        clave_ant = clave
    sys.stdout.write("{}\t{}\n".format(clave_ant, mayor))