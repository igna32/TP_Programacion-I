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


def mostrar_tablas(tablas_creadas: list):

    if len(tablas_creadas) == 0:
        print("Todavía no hay tablas creadas.")

    else:

        for i in range(len(tablas_creadas)):

            tabla_actual = tablas_creadas[i]
            nombre = tabla_actual[0]
            columnas = tabla_actual[1]
            matriz = tabla_actual[2]

            print(f"\nTabla: {nombre}")

            linea_columnas = ""
            for k in range(len(columnas)):
                linea_columnas += str(columnas[k])
                if k < len(columnas) - 1:
                    linea_columnas += " | "
            print(linea_columnas)

            for j in range(len(matriz)):
                linea_fila = ""
                fila = matriz[j]
                for k in range(len(fila)):
                    linea_fila += str(fila[k])
                    if k < len(fila) - 1:
                        linea_fila += " | "
                print(linea_fila)


def modificar_tablas(tablas_creadas: list):

    if len(tablas_creadas) == 0:
        print("Error: no hay tablas creadas.")

    else:

        print("\n--- SELECCIONE UNA TABLA PARA MODIFICAR ---")

        for i in range(len(tablas_creadas)):
            print(f"{i + 1}. {tablas_creadas[i][0]}")


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

            valor_actual = matriz[j][k]
            print(f"\nValor actual en Fila {j + 1}, Columna '{columnas[k]}': {valor_actual}")

            nuevo_dato = input("Ingrese el nuevo valor: ")

            if es_un_numero(nuevo_dato):
                matriz[j][k] = int(nuevo_dato)
            else:
                matriz[j][k] = nuevo_dato

            print("El dato fue modificado.")

"""aca dejo como hacer maso estadisticas, lo podes modificar, esto lo hice mientras tomo te lol"""


"""
def calcular_estadisticas(tablas_creadas: list):
    if len(tablas_creadas) == 0:
        print("Error: no hay tablas creadas para analizar.")
    else:
        print("\n--- SELECCIONE UNA TABLA PARA ESTADÍSTICAS ---")
        
        # 1. Mostrar tablas disponibles 
        for i in range(len(tablas_creadas)):
            print(f"{i + 1}. {tablas_creadas[i][0]}")

        # 2. Validación de selección de tabla
        tabla_valida = False
        while tabla_valida == False:
            entrada_tabla = input("Seleccione el número de tabla: ")

            if es_un_numero(entrada_tabla) and validar_rango(int(entrada_tabla), 1, len(tablas_creadas)):
                indice_tabla = int(entrada_tabla) - 1
                tabla_valida = True
            else:
                print("Error: ingrese una opción válida.")

        tabla_seleccionada = tablas_creadas[indice_tabla]
        nombre = tabla_seleccionada[0]
        columnas = tabla_seleccionada[1]
        matriz = tabla_seleccionada[2]

        if len(matriz) == 0:
            print("La tabla seleccionada no tiene filas para analizar.")
        else:
            print(f"\nAnalizando la tabla: {nombre}")
            print("\nColumnas disponibles:")
            for k in range(len(columnas)):
                print(f"{k + 1}. {columnas[k]}")

            # 3. Selección de la columna a evaluar estadísticamente
            columna_valida = False
            while columna_valida == False:
                entrada_columna = input(f"Seleccione el número de la columna numérica a analizar (1 a {len(columnas)}): ")

                if es_un_numero(entrada_columna) and validar_rango(int(entrada_columna), 1, len(columnas)):
                    k_col = int(entrada_columna) - 1
                    columna_valida = True
                else:
                    print("Error: ingrese un número de columna válido.")

            # 4. EXTRACCIÓN DE DATOS
            # Creamos la lista de valores de esa columna recorriendo la matriz por índice
            valores = [0] * len(matriz)
            for j in range(len(matriz)):
                # Intentamos convertir a float por si son notas o números decimales/enteros
                dato = matriz[j][k_col]
                if es_un_numero(str(dato)):
                    valores[j] = float(dato)
                else:
                    valores[j] = 0.0 # Por si no hay texto

            n = len(valores)
            
            print("\n" + "=" * 45)
            print(f"      REPORTE ESTADÍSTICO: {columnas[k_col]}")
            print("=" * 45)

            # A. CONTEOS O FRECUENCIAS
            print(f"• Conteo total de datos (n): {n}")
            
            frecuencias = {}
            for x in range(len(valores)):
                val = valores[x]
                if val in frecuencias:
                    frecuencias[val] += 1
                else:
                    frecuencias[val] = 1
            
            print("  Frecuencias individuales:")
            for val, freq in frecuencias.items():
                print(f"    - Valor {val}: aparece {freq} vez/veces")

            # B. MÁXIMOS Y MÍNIMOS
            val_max = max(valores)
            val_min = min(valores)
            rango = val_max - val_min
            print(f"\n• Máximos y Mínimos:")
            print(f"  - Mínimo: {val_min}")
            print(f"  - Máximo: {val_max}")
            print(f"  - Rango: {rango}")

            # C. MEDIDAS DE TENDENCIA CENTRAL
            suma_total = sum(valores)
            prom_aritmetico = suma_total / n

            # Promedio geométrico
            producto = 1
            for x in range(len(valores)):
                producto *= valores[x]
            prom_geometrico = producto ** (1 / n)

            print(f"\n• Medidas de Tendencia Central:")
            print(f"  - Promedio Aritmético: {prom_aritmetico:.2f}")
            print(f"  - Promedio Geométrico: {prom_geometrico:.2f}")

            # D. MEDIDAS DE DISPERSIÓN (Varianza, Desviación Estándar, Rango)
            suma_cuadrados = 0
            for x in range(len(valores)):
                suma_cuadrados += (valores[x] - prom_aritmetico) ** 2
            
            varianza = suma_cuadrados / n
            desviacion_estandar = math.sqrt(varianza)

            print(f"\n• Medidas de Dispersión:")
            print(f"  - Varianza: {varianza:.2f}")
            print(f"  - Desviación Estándar: {desviacion_estandar:.2f}")

            # E. MEDIDAS DE POSICIÓN (Mediana)
            valores_ordenados = sorted(valores)
            mitad = n // 2
            if n % 2 != 0:
                mediana = valores_ordenados[mitad]
            else:
                mediana = (valores_ordenados[mitad - 1] + valores_ordenados[mitad]) / 2

            print(f"\n• Medidas de Posición:")
            print(f"  - Mediana (Posición central): {mediana}")
            print("=" * 45)
            
            
            """