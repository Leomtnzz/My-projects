# What this is for is to check if a password is valid or not. It's valid when it has at least a capital letter and a normal letter, a special character and a number, and also it has to be 10 charcters long.



contraseña=input('Escribe una contraseña que contenga al menos una mayuscula, una minuscula, un número y un caracter como \'#\', \'*\' o \'@\' y que tenga más de 10 caracteres\n')

min_letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
may_letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caracteres=['#','*','@']
numeros=['0','1','2','3','4','5','6','7','8','9']

l=len(contraseña)

tiene_minuscula = False
tiene_mayuscula = False
tiene_caracter = False
tiene_numero = False

for i in contraseña:
    if i in min_letras:
        tiene_minuscula = True
    elif i in may_letras:
        tiene_mayuscula = True
    elif i in caracteres:
        tiene_caracter = True
    elif i in numeros:
        tiene_numero = True

if l>10:
    if tiene_minuscula and tiene_mayuscula and tiene_caracter and tiene_numero:
        print('Contraseña válida.')
    else:
        print('Contraseña no valida.')    
else:
    print('Contraseña demasiado corta.')






# for i in range(0,l):
#     if contraseña[i] not in caracteres and contraseña[i] not in numeros and contraseña[i]not in min_letras and contraseña[i] not in may_letras:
#         print('Contraseña incompleta.')
        
#     else:
#         print('Contraseña válida.')
