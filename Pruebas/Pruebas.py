lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print(lista[::-3])
# print(lista[::3])
# print(lista[5:-2:3])
# print(lista[-1:3:-2])
# print(lista[9:1:-2])

copia=lista[:]
#rint(id(lista), id(copia))

invertida=copia[::-1]
#print(invertida)


lista = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# del lista[::2]
# del lista[1::2]
# del lista[3:]
# del lista[:8]

# lista[2:3]=[4,5,-1]
# lista[-1:2]=[4,5,-1]
# lista[2:5]=[4,-1]
# print(lista)

#lista[1:9:3]=['x','y','z']
#lista[2:8:2]=['a','b','c']
lista[2:8]=[]
#print(lista)


#Muy curioso
txt = "The binary version of {0} is {0:b}"
print(txt.format(7))    


import math
import sympy

N=int(input('Dame un número entero\n'))
M=int(input('Dame otro número entero\n'))

division=N/M
division=math.trunc(division)
print(division)

mcm=sympy.factorint