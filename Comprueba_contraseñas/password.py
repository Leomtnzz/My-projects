contraseña=False

min_letras=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
may_letras=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
caracteres=['#','*','@']
numeros=['0','1','2','3','4','5','6','7','8','9']

todo=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z','#','$','/','@','0','1','2','3','4','5','6','7','8','9']

password=input('Escribe una contraseña que contenga al menos una mayuscula, una minuscula, un número y un caracter como \'#\', \'*\' o \'@\'\n')

for i in password:
    if any(i in password for i in todo):
        print("Contraseña válida")
    else:
        print('mal')
    
    

    
#     if i==(any(min_letras) and any(may_letras) and any(numeros) and any(caracteres)):
#         contraseña=True
# if contraseña==True:
#     print('Contraseña válida.')
# else:
#     print('Le faltan caracteres a la contraseña.')
            




# for i in range(0,l):
#     if contraseña[i] not in caracteres and contraseña[i] not in numeros and contraseña[i]not in min_letras and contraseña[i] not in may_letras:
#         print('Contraseña incompleta.')
        
#     else:
#         print('Contraseña válida.')