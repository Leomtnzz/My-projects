milista=('Luis','Leo','Nora','Maria','Ollie')


encontrada=0
l=len(milista)
for i in range(l):
        encontrada=0
        long=len(milista[i])
        vocals=('a','e','i','o','u')
        for j in range (1,long):
                if milista[i][long-j] in vocals and encontrada==0:
                    print(milista[i][long-j])
                    encontrada=1
