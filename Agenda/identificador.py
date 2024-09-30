archi1=open('fichero.txt','r')
linea=archi1.readline()
n=input('Número de línea a buscar\n')
nombre=[]
numero=[]
acabado=False
acabado2=False
while linea !='':
    linea=archi1.readline()
    m=len(linea)
    cabecera=linea[0:2]
    if cabecera == n:
        resto_linea=linea[2:m]
        resto_linea=list(resto_linea)
        for i in range(len(resto_linea)):
            if resto_linea[i]!= '+' and acabado ==False:
                nombre.append(resto_linea[i])
            else:
                acabado=True
        resto_linea=resto_linea[::-1]
        for i in range(len(resto_linea)):
            if resto_linea[i]!='+' and acabado2==False:
                numero.append(resto_linea[i])
            else:
                acabado2=True
print('Nombre:'+ ''.join(map(str, nombre)))
print('Número: +'+ ''.join(map(str, numero[::-1])))
archi1.close()