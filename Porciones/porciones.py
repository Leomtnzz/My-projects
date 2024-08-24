print('Escribe un número')
num=int(input())
lista=[]

while num !=0:
    lista.append(num)
    print('Escribe otro número')
    num=int(input())
    print(lista)

split_lista=lista[::2]
dividida_lista=lista[1::2]


print(split_lista)
print(split_lista[1:-1])
print(dividida_lista)
print(min(dividida_lista))
print(max(dividida_lista))