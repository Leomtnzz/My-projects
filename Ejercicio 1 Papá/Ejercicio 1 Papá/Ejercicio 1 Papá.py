milista=('Luissssssss','Leo','Nora','Maria','Ollie')

# def papa():
#     for i in range(0, 5):
#         #print(milista[i])
#         l=len(milista[i])
#         #print(l)
#         #print(milista[len(milista[i])])
#         #print(milista[i][l-1])
#         vocals=('a','e','i','o','u')

#         if milista[i][l-1] in vocals :
#             print(milista[i][l-1])
#         elif milista[i][l-2] in vocals:
#             print(milista[i][l-2])
#         elif milista[i][l-3] in vocals:
#             print(milista[i][l-3])
#         elif milista[i][l-4] in vocals:
#             print(milista[i][l-4])
#         elif milista[i][l-5] in vocals:
#             print(milista[i][l-5])
#         elif milista[i][l-6] in vocals:
#             print(milista[i][l-6])
#         else :
#             print('No hay vocales')

# papa()



encontrada=0
l=len(milista)
for i in range(0, l):
        encontrada=0
        long=len(milista[i])
        vocals=('a','e','i','o','u')
        for j in range (1,long):
                if milista[i][long-j] in vocals and encontrada==0:
                    print(milista[i][long-j])
                    encontrada=1