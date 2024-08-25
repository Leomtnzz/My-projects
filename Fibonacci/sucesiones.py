secuencia=int(input('Cuantos números de la secuencia Fibonacci quieres?\n'))
lista_secuencia=[]

def fibonacci(secuencia):
    sequence = [0, 1]
    while len(sequence) < secuencia:
        sequence.append(sequence[-1] + sequence[-2])
        print(sequence)
    return sequence
fibonacci(secuencia)


# MÍO, NO FUNCIONA

# while repeticion<=secuencia:
#     for i in lista_secuencia:
#         long=len(lista_secuencia[i])
#         fibonacci=num
#         num=fibonacci+(lista_secuencia[i][long-1])
#         lista_secuencia.append(num)
#     print(lista_secuencia)
#     repeticion+=1

# NO MÍO, FUNCIONA.

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