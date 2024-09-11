lista=[]

def recibe_cadena_de_texto():
    global frase
    frase=input('Escribe una frase donde pongas algún número.\n')
    
recibe_cadena_de_texto()

x=isinstance(input, int)


for i in frase():
    while x is True:
        lista.append(i)
    
print(lista)