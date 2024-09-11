import math
import sympy

N=int(input('Dame un número entero\n'))
M=int(input('Dame otro número entero\n'))

division=N/M
division=math.trunc(division)
print(division)

mcm=sympy.factorint(N)
print(mcm)