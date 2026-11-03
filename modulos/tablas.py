
from modulos.funciones import es_un_numero, validar_rango


def crear_tabla() -> list:

    print("\n--- CREACIÓN DE NUEVA TABLA ---")

    nombre_tabla = input("Ingrese el nombre de la tabla: ")

    while len(nombre_tabla) == 0:
        print("El nombre no puede estar vacío.")
        nombre_tabla = input("Ingrese el nombre de la tabla: ")

    cant_col_str = input("Ingrese la cantidad de columnas: ")

    while not es_un_numero(cant_col_str) or int(cant_col_str) <= 0:
        print("Error: ingrese un número entero mayor a 0: ")
        cant_col_str = input("Ingrese la cantidad de columnas: ")

    cant_columnas = int(cant_col_str)

    columnas = []

    for i in range(cant_columnas):

        nombre_col = input(f"Ingrese el nombre de la columna {i + 1}: ")

        while len(nombre_col) == 0:
            print("El nombre no puede estar vacío.")
            nombre_col = input(f"Ingrese el nombre de la columna {i + 1}: ")

        columnas += [nombre_col]

    cant_filas_str = input("Ingrese la cantidad de filas a cargar: ")

    while not es_un_numero(cant_filas_str) or int(cant_filas_str) < 0:
        print("Error: ingrese un número entero mayor o igual a 0.")
        cant_filas_str = input("Ingrese la cantidad de filas a cargar: ")

    cant_filas = int(cant_filas_str)

    matriz = []

    for f in range(cant_filas):

        print(f"\n--- Carga de fila {f + 1} ---")

        nueva_fila = []

        for c in range(cant_columnas):

            dato = input(f"Ingrese dato para '{columnas[c]}': ")

            if es_un_numero(dato):
                nueva_fila += [int(dato)]

            else:
                nueva_fila += [dato]

        matriz += [nueva_fila]

    tabla_creada = [nombre_tabla, columnas, matriz]

    return tabla_creada

def modificar_tablas(tablas_creadas):
    if len(tablas_creadas) == 0:
        print("Error, no hay tablas creadas")
    else:
        
        print("\n--- SELECCIONE UNA TABLA PARA MODIFICAR ---")

        for i in range(len(tablas_creadas)):
            print(f"{i + 1}. {tablas_creadas[i][0]}")

        entrada_tabla = input("Seleccione el numero de la tabla: ")

        while not es_un_numero(entrada_tabla) or not validar_rango(int(entrada_tabla), 1, len(tablas_creadas)):
            print("Error, ingrese una opcion valida")
            entrada_tabla = input("Seleccione el numero de tabla: ")

        indice_tabla = int(entrada_tabla) - 1
        tabla_seleccionada = tablas_creadas[indice_tabla]

        columnas = tabla_seleccionada[1]
        matriz = tabla_seleccionada[2]

        if len(matriz) == 0:
            print("La tabla seleccionada no tiene filas para modificar.")

        else:
            print("/n Que desea modificar? ")
            print("1- Una Fila")
            print("2- Una columna")
            entrada_modo = input("Seleccione una opción: ")
             
            while not es_un_numero(entrada_modo) or not validar_rango(int(entrada_modo), 1, 2):
               print("Error: Seleccione 1 o 2.")
               entrada_modo = input("Seleccione una opción: ")
                
            opcion_modo = int(entrada_modo)

            print("Seleccione el tipo de carga: ")
            