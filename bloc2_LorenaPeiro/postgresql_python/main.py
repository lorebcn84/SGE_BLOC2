import create_registre as cr
import read_registre as rr

#Trucada per executar la funció a l'arxiu create_registre.py
cr.create_reg()

#afegim la trucada a read_reg
results = rr.read_reg()

#Imprimim tipus
print (type(results))

#Imprimim
print(results)

