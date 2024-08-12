#Quiero que me genere una contraseña aleatoria.

#1º que me la de 

#2 ponerle parametros

import random
#alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s,','t','u','v','w','x','y','z' )
#num=('0','1','2','3','4','5','6','7','8','9')
#password= random.choice('a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z')
#num=('0','1','2','3','4','5','6','7','8','9'')
from random import sample
password=random.sample('AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_#%*çÇ ')
input(str('How long do you want your password to be?\n'))
input=len(password)
print("".join(map(str, password)))