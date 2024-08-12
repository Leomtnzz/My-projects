import math

D=float(input('Cuanto hay que pagar?\n'))
print(f'Tienes que pagar ${D}')
monedas=[2,1,0.5,0.2,0.1,0.05,0.02,0.01]
lista=[0,0,0,0,0,0,0,0,0]
D=math.trunc(D)
resto=D%2

# if resto==0:
#     A=D/2
#     lista.append(A)
# else:
#     A=D//2
#     B=1
#     lista.append(A)
#     lista.append(B)
# print(lista)

l=len(monedas)
for i in range(0,l):
    M=monedas-lista[i]
    if M>lista[i]:
        M=M-lista[i]
        lista[i]+=1
    else:
        i+=1


















#NO FUNCIONA

# def cambio_dinero(monto):
#     monedas=[2,1,0.5,0.2,0.1,0.05,0.02,0.01]
#     lista=[]
#     if (monto>=1 and monto<=99):
#         for moneda in reversed(monedas):
#             result=monto//moneda
#             if result>0:
#                 lista.append(result)
#                 monto=monto-(moneda*result)
#             else:
#                 lista.append(result)
#         return list(reversed (lista))
#     else:
#         return 'None'
    
# cambio_dinero(87)