import math

x=int(input('Dame la coordenada X de un punto.\n'))
y=int(input('Dame la coordenada Y de un punto.\n'))
puntoA=[x,y]

x2=int(input('Dame la coordenada X de otro punto.\n'))
y2=int(input('Dame la coordenada Y de otro punto.\n'))
puntoB=[x2,y2]

A=x2-x
B=y2-y
vector=[A,B]


Mo=A**2
Du=B**2
Lo=Mo+Du
mdl=math.sqrt(Lo)
mdl=round(mdl, 3)


C=(x+x2)/2
D=(y+y2)/2
CD=[C,D]
punto_medio=CD


print(f'Las coordenadas del punto A son {puntoA}')
print(f'Las coordenadas del punto B son {puntoB}')
print(f'El vector es {vector}')
print(f'El módulo del vector es {mdl}')
print(f'Las coordenadas del punto medio son {punto_medio}')
