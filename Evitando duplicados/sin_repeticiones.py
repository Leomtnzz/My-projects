lista1=[]

while len(lista1)<=9:
    num=input('Dame 10 numeros, pueden ser repetidos. ')
    lista1.append(num)

lista2=[]
lista3=[]

for i in lista1:
    if i not in lista2:
        lista2.append(i)
    else:
        lista3.append(i)

print(f'Tu lista es esta :{','.join(map(str, lista1))}')
print(f'Tu lista sin duplicados es :{','.join(map(str, lista2))}')
print(f'Tu lista de duplicados es :{','.join(map(str, lista3))}')