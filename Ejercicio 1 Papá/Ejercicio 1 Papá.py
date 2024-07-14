milista=('Luis','Leo','Nora','María','Ollie')

for i in range(0, 5):
    #print(milista[i])
    l=len(milista[i])
    #print(l)
    #print(milista[len(milista[i])])
    #print(milista[i][l-1])
    vocals=('a','e','i','o','u')
    if milista[i][l-1] in vocals :
        print(milista[i][l-1])
    elif milista[i][l-2] in vocals:
        print(milista[i][l-2])
    elif milista[i][l-3] in vocals:
        print(milista[i][l-3])
    else :
        print(milista[i][l-4])