x = 1
y = 2
z = -5.5

#IMPORT DE FUNCIONS MATEMÀTIQUES 
from math import * 

#imprimir el resultat 1+2
print(x+y)

#imprimir el resultat 1-2
print(x-y)

#imprimir el resultat 1 * 2
print(x * y)

#imprimir el resultat de 1 / 2
print(x/y)

#imprimir el residu de 1 / 2
print(x % y)

#imprimir un numero en un string
print(str(x) + " és una variable")

#imprimir el valor absolut de z
print(abs(z))

#imprimir y^z
print(pow(y, z))

#imprimir el numero més gran entre -5.5, 1 i 2
print(max(x, y, z))

#imprimir el numero més petit entre -5.5, 1 i 2
print(min(x, y, z))

#imprimir l'arrolodiment de z
print(round(z))

'''
Aquestes funcions només apareixen amb s'import de funcions
'''
#imprimir z arrodonit cap a petit
print(floor(z))

#imprimir z arrodonit cap a gran
print(ceil(z))

#imprimir arrel quadrada de y
print(sqrt(y))
