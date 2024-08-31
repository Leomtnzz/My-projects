#Here I want to do figures with the '*' sign.

# Sorry if my instructions are not understandable i've never done this before.

def escribe_un_numero():                                        # This code makes a figure like this one for n=5:
    n=input('Dame un número\n')                                 #*****
    caracter='*'                                                #****
                                                                #***
    if n.isdigit():  # This cheks if the input is a number.     #**   
        n=int(n)                                                #*
        for _ in range(n):
            resultado=[]
            operacion=n*caracter  # This print this sign '*' n times.
            n=n-1
            resultado.append(operacion)
            print(''.join(map(str, resultado)))  # This prints the list 'resultado' as a string and in the same chain so it enables us to make this figures.
    else:
        print('Pon un número válido.')
        return escribe_un_numero()
    
escribe_un_numero()



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
            lista2.append(" ")  # This is to print the spaces between the two '*' signs.
        lista2.append('*')      # And to add the last '*' sign.
        for _ in range(x-2):
            print(''.join(map(str, lista2)))
        print(''.join(map(str, lista1)))
    else:
        print('Pon un número válido.')
        return cuadro()
    
cuadro()