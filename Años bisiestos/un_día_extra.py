años=int(input('Hasta que año quieres saber los años bisiestos desde el 1d.c.?\n'))
años_bisiestos=[0]

# longitud_de_la_lista=len(años_bisiestos)/4
suma_años_bisiestos=0

if años<=506:
    while años>=len(años_bisiestos):
        suma_años_bisiestos+=4
        años_bisiestos.append(suma_años_bisiestos)
    print(años_bisiestos)



# if años >= 4:  # El primer año bisiesto fue el 4 d.C.
#     while len(años_bisiestos) / 4 < años:
#         suma_años_bisiestos += 4
#         años_bisiestos.append(suma_años_bisiestos)
    
#     print(f"Años bisiestos hasta el año {años}:")
#     print(años_bisiestos)
# else:
#     print("No hay años bisiestos antes del año 4 d.C.")