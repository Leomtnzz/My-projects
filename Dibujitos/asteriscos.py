#Here I want to do figures with the '*' sign.

# Sorry if my instructions are not understandable, i've never done this before.

def escalera():                                        # This code makes a figure like this one for n=5:
    n=input('Dame un número\n')                                 #*****                                               
                                                                #****
    if n.isdigit():  # This cheks if the input is a integer.    #*** 
        n=int(n)                                                #**
        while n>=0:                                             #*
            print(n* '*')
            n-=1
         
    else:
        print('Pon un número válido.')
        return escalera()
    
escalera()



def cuadro():                                               # This one makes a figure like this for x=5.
    x=input('Dame un número\n')                             #*****
    caracter='*'                                            #*   *
    lista1=[]                                               #*   *
    lista2=['*']                                            #*   *
                                                            #*****
    if x.isdigit():
        x=int(x)
        for _ in range(x):    # I do this when I want to iterate through something but I don't care about the index.
            lista1+=caracter
        print(''.join(map(str, lista1)))
        for _ in range(x-2):    # The same thing as the other one but I want it to iterate 2 times less.
            lista2.append(" ")  # This is to add the spaces between the two '*' signs.
        lista2.append('*')      # And to add the last '*' sign.
        for _ in range(x-2):
            print(''.join(map(str, lista2)))
        print(''.join(map(str, lista1)))
    else:
        print('Pon un número válido.')
        return cuadro()
    
# cuadro()

import math
def tresbolillo():   #This works only with odd numbers                  # This one males a figure like this for y=5
    y=input('Dime un número impar.\n')                                                                                        
    if y.isdigit():   # This check that the input is a number           # * * *
        y=int(y)                                                        #  * *
        if y%2==1:    # this checks that the number is odd              # * * *
            operacion=y/2                                               #  * * 
            ceiling=math.ceil(operacion)                                # * * *
            truncado=math.trunc(operacion)
            lista2=[]
            for _ in range(truncado):
                lista=[]
                for _ in range(ceiling):                # This loop appends to the list the lines with three '*' signs
                    lista.append('* ')                                        
                lista.append('\n')
                for _ in range(truncado):               # And this one appends the lines with two '*' signs
                    lista.append(' *')
                print(''.join(map(str, lista)))
            for _ in range(ceiling):                    # And this last one appends the last row of '*' signs
                lista2.append('* ')    
            print(''.join(map(str, lista2)))
        
        else:
            print('Escribe un número inpar.')  
            return tresbolillo()
    
    else:
        print('Escribe un número válido.')
        return tresbolillo()
        
# tresbolillo()



def piramide():
    z=input('Dime un número impar.\n')
    caracter=1
    lista=[]

    if z.isdigit():   
        z=int(z)                                                        
        if z%2==1:
            operacion=z/2
            truncado=math.trunc(operacion)
            ceiling=math.ceil(operacion)
            for _ in range(ceiling):
                lista.append(' ' * truncado)
                truncado-=1
                lista.append('*' * caracter)
                caracter+=2
                lista.append('\n')                
            print(''.join(map(str, lista)))

        else:
            print('Escribe un número impar.')
            return piramide()

    else:
        print('Escribe un número válido.')
        return piramide()

piramide()