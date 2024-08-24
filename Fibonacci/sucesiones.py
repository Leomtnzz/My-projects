# hago un loop y creo una variable que se vaya sumando. cuando esa variable llegue a los n numeros del input hacer " if repeticion<input break"

secuencia=int(input('Cuantos números de la secuencia Fibonacci quieres?\n'))
lista_secuencia=[]
num=0
num2=1
repeticion=0



while repeticion<=secuencia:
    for i in lista_secuencia:
        long=len(lista_secuencia[i])
        fibonacci=num
        num=fibonacci+(lista_secuencia[i][long-1])
        lista_secuencia.append(num)
    print(lista_secuencia)
    repeticion+=1

# a=0
# b=1
# c=1

# while c<=secuencia:
#     if c%2==1:
#         print(a,end=',')
#         a+=b
#     else:
#         print(b, end=',')
#         b+=a
#     c+=1