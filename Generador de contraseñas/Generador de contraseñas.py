#Quiero que me genere una contraseña aleatoria.

#1º que me la de 

#2 ponerle parametros
alfabeto=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s,','t','u','v','w','x','y','z',1,2,3,4,5,6,7,8,9,'-''_''#''%''*''ç''Ç')


import random

# num=input(('How long do you want your password to be?\n'))
password=random.sample(alfabeto,10)
num=len(password)
#('AaBbCcDdEeFfGgHhIiJjKkLlMmNnÑñOoPpQqRrSsTtUuVvWwXxYyZz0123456789-_#%*çÇ ' 10)
print("".join(map(str, password)))




#num=('0','1','2','3','4','5','6','7','8','9')
#password= random.choice('a,b,c,d,e,f,g,h,i,j,k,l,m,n,ñ,o,p,q,r,s,t,u,v,w,x,y,z')
#num=('0','1','2','3','4','5','6','7','8','9'')