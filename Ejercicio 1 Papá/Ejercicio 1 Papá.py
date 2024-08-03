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


#Funciona

l=len(milista)
for i in range(0, l):
        l=len(milista[i])
        vocals=('a','e','i','o','u')
        for milista[i][l-1] in vocals:
                print(milista[i][l-1])
                if milista[i][l-1] not in vocals:
                    print(milista[i][l-1])
                    l-=1
                # elif milista[i][l-2] in vocals:
                #         print(milista[i][l-2])
                # elif milista[i][l-3] in vocals:
                #         print(milista[i][l-3])
                # elif milista[i][l-4] in vocals:
                #         print(milista[i][l-4])
                # elif milista[i][l-5] in vocals:
                #         print(milista[i][l-5])
                # elif milista[i][l-6] in vocals:
                #         print(milista[i][l-6])



#No funciona

# l=len(milista)
# for i in range(0, l):
#         l=len(milista[i])
#         vocals=('a','e','i','o','u')
#         while milista[i][l==0] in vocals:
#             print(milista[i][l-1])
#             if milista[i][l-1] not in vocals:
#                 print(milista[i][l-2])



#No funciona

# l=len(milista)
# for i in range(0, l):
#         l=len(milista[i])
#         vocals=('a','e','i','o','u')
#         def papa():
#             while milista[i][l==0] in vocals :
#                     if milista[i][l-1] in vocals :
#                         print(milista[i][l-1])
#                     else:
#                           return papa
            
#                     if milista[i][l-2] in vocals :
#                         print(milista[i][l-2])
#                     elif milista[i][l-3] in vocals :
#                         print(milista[i][l-3])
#                     else:
#                         print(milista[i][l-4])
#                     break