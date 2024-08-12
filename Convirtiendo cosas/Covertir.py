num=13 
txt='La versión binaria de {0} es {0:b}'
#print(txt.format(num))

binario=10101
decimal=int(str(binario), 2)
print(f'El numero {binario} en decimal es {decimal}')

hexanum=hex(num)
print(f'La version hexadecimal de {num} es {hexanum}')

octnum=oct(num)
print(f'La version octal de {num} es {octnum}')