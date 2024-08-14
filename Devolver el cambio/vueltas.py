# What I want to do here is to write an amount of money and receive what would be the minimal amount of coins to pay that.

D=float(input('Cuanto hay que pagar?\n'))
print(f'Tienes que pagar ${D}')
monedas=[2,1,0.5,0.2,0.1,0.05,0.02,0.01]
lista=[0,0,0,0,0,0,0,0]


l=len(monedas)
for i in range(0,l):
    D=round(D,2)
    while D-monedas[i]>=0:
        lista[i]+=1
        D=D-monedas[i]
# print(lista)
        
l=len(lista)
for i in range(0,l):
    if lista[i]!=0: 
        print(f'Necesitas {lista[i]} de {monedas[i]}€')
            








# import math

# Un intento.

# D=math.trunc(D)
# print(D)
# resto=D%2
# if resto==0:
#     A=D/2
#     lista.append(A)
# else:
#     A=D//2
#     B=1
#     lista.append(A)
#     lista.append(B)
# print(lista)