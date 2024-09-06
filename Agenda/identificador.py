# with open('fichero.txt', 'r') as archivo:
#     lineas = archivo.readlines()

# numero_linea = int(input('Dime el numero del contacto que quieres'))
# if numero_linea < len(lineas):
#     linea_seleccionada = lineas[numero_linea]
#     print(f"El contacto seleccionada es:\n{linea_seleccionada}")
# else:
#     print("El número de línea está fuera del rango del archivo.")


def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            # Leer todas las líneas y guardarlas en una lista en memoria
            lineas = archivo.readlines()
        return lineas
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontró.")
        return None
    except IOError:
        print(f"Hubo un error al leer el archivo '{nombre_archivo}'.")
        return None

def seleccionar_linea(lineas, numero_linea):
    if lineas is None:
        return None
    
    if 0 <= numero_linea < len(lineas):
        return lineas[numero_linea]
    else:
        print("El número de línea está fuera del rango del archivo.")
        return llamada()


nombre_archivo = 'fichero.txt'
contenido = leer_archivo(nombre_archivo)

def llamada():
    if contenido:
            try:
                numero_linea = int(input("Ingrese el número del contacto que desea leer: "))
                linea = seleccionar_linea(contenido, numero_linea)
                if linea:
                    print(f"El contacto seleccionada es: {linea}")
            except ValueError:
                print("Por favor, ingrese un número válido.")

llamada()