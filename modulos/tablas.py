from modulos.funciones import es_un_numero, validar_rango


def crear_tabla() -> list:

    print("\n--- CREACIÓN DE NUEVA TABLA ---")

    nombre_tabla = input("Ingrese el nombre de la tabla: ")

    while len(nombre_tabla) == 0:
        print("El nombre no puede estar vacío.")
        nombre_tabla = input("Ingrese el nombre de la tabla: ")

    # Validación de cantidad de columnas con bandera
    cant_col_valida = False
    while cant_col_valida == False:
        cant_col_str = input("Ingrese la cantidad de columnas: ")
        if es_un_numero(cant_col_str) and int(cant_col_str) > 0:
            cant_columnas = int(cant_col_str)
            cant_col_valida = True
        else:
            print("Error: ingrese un número entero mayor a 0.")

    columnas = []

    for i in range(cant_columnas):

        nombre_col = input(f"Ingrese el nombre de la columna {i + 1}: ")

        while len(nombre_col) == 0:
            print("El nombre no puede estar vacío.")
            nombre_col = input(f"Ingrese el nombre de la columna {i + 1}: ")

        columnas += [nombre_col]

    # Validación de cantidad de filas con bandera
    cant_filas_valida = False
    while cant_filas_valida == False:
        cant_filas_str = input("Ingrese la cantidad de filas a cargar: ")
        if es_un_numero(cant_filas_str) and int(cant_filas_str) >= 0:
            cant_filas = int(cant_filas_str)
            cant_filas_valida = True
        else:
            print("Error: ingrese un número entero mayor o igual a 0.")

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


def modificar_tablas(tablas_creadas: list):

    if len(tablas_creadas) == 0:
        print("Error: no hay tablas creadas.")

    else:

        print("\n--- SELECCIONE UNA TABLA PARA MODIFICAR ---")

        for i in range(len(tablas_creadas)):
            print(f"{i + 1}. {tablas_creadas[i][0]}")

        # 1. Selección de Tabla
        tabla_valida = False
        while tabla_valida == False:
            entrada_tabla = input("Seleccione el número de tabla: ")

            if es_un_numero(entrada_tabla) and validar_rango(int(entrada_tabla), 1, len(tablas_creadas)):
                indice_tabla = int(entrada_tabla) - 1
                tabla_valida = True
            else:
                print("Error: ingrese una opción válida.")

        tabla_seleccionada = tablas_creadas[indice_tabla]
        columnas = tabla_seleccionada[1]
        matriz = tabla_seleccionada[2]

        if len(matriz) == 0:
            print("La tabla seleccionada no tiene filas para modificar.")

        else:
            print(f"\nModificando la tabla: {tabla_seleccionada[0]}")
            print(f"La tabla tiene {len(matriz)} fila(s).")

            # 2. Selección de Fila (j)
            fila_valida = False
            while fila_valida == False:
                entrada_fila = input(f"Seleccione el número de fila a modificar (1 a {len(matriz)}): ")

                if es_un_numero(entrada_fila) and validar_rango(int(entrada_fila), 1, len(matriz)):
                    j = int(entrada_fila) - 1
                    fila_valida = True
                else:
                    print("Error: ingrese un número de fila válido.")

            # 3. Selección de Columna (k)
            print("\nColumnas disponibles:")
            for k in range(len(columnas)):
                print(f"{k + 1}. {columnas[k]}")

            columna_valida = False
            while columna_valida == False:
                entrada_columna = input(f"Seleccione la columna a modificar (1 a {len(columnas)}): ")

                if es_un_numero(entrada_columna) and validar_rango(int(entrada_columna), 1, len(columnas)):
                    k = int(entrada_columna) - 1
                    columna_valida = True
                else:
                    print("Error: ingrese un número de columna válido.")

            # 4. Modificación del dato puntual
            valor_actual = matriz[j][k]
            print(f"\nValor actual en Fila {j + 1}, Columna '{columnas[k]}': {valor_actual}")

            nuevo_dato = input("Ingrese el nuevo valor: ")

            if es_un_numero(nuevo_dato):
                matriz[j][k] = int(nuevo_dato)
            else:
                matriz[j][k] = nuevo_dato

            print("¡Dato modificado exitosamente!")