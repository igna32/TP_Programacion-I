from modulos.funciones import es_un_numero, validar_rango


def calcular_estadisticas(tablas_creadas: list):

    if len(tablas_creadas) == 0:
        print("Error: no hay tablas creadas para analizar.")

    else:

        print("\n--- SELECCIONE UNA TABLA PARA ESTADÍSTICAS ---")

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

            columna_valida = False
            while columna_valida == False:
                entrada_columna = input(f"Seleccione la columna a analizar (1 a {len(columnas)}): ")

                if es_un_numero(entrada_columna) and validar_rango(int(entrada_columna), 1, len(columnas)):
                    k_col = int(entrada_columna) - 1
                    columna_valida = True
                else:
                    print("Error: ingrese un número de columna válido.")

            valores = []
            for j in range(len(matriz)):
                dato = matriz[j][k_col]
                dato_str = str(dato)
                
                if es_un_numero(dato_str):
                    valores += [int(dato_str)]

            n = len(valores)

            if n == 0:
                print("La columna seleccionada no contiene datos numéricos válidos.")

            else:
                print("\n=============================================")
                print(f"      REPORTE ESTADÍSTICO: {columnas[k_col]}")
                print("=============================================")

                # A. CONTEO TOTAL Y FRECUENCIAS (Sin diccionarios)
                print(f"• Conteo total de datos (n): {n}")

                valores_unicos = []
                conteo_frecuencias = []

                for j in range(n):
                    val = valores[j]
                    encontrado = False

                    for k in range(len(valores_unicos)):
                        if valores_unicos[k] == val:
                            conteo_frecuencias[k] += 1
                            encontrado = True

                    if encontrado == False:
                        valores_unicos += [val]
                        conteo_frecuencias += [1]

                print("  Frecuencias individuales:")
                for k in range(len(valores_unicos)):
                    print(f"    - Valor {valores_unicos[k]}: aparece {conteo_frecuencias[k]} vez/veces")

                val_max = valores[0]
                val_min = valores[0]

                for j in range(1, n):
                    if valores[j] > val_max:
                        val_max = valores[j]
                    if valores[j] < val_min:
                        val_min = valores[j]

                rango = val_max - val_min

                print("\n• Máximos y Mínimos:")
                print(f"  - Mínimo: {val_min}")
                print(f"  - Máximo: {val_max}")
                print(f"  - Rango: {rango}")

                suma_total = 0
                producto = 1

                for j in range(n):
                    suma_total += valores[j]
                    producto *= valores[j]

                prom_aritmetico = suma_total / n
                prom_geometrico = producto ** (1 / n)

                print("\n• Medidas de Tendencia Central:")
                print(f"  - Promedio Aritmético: {prom_aritmetico}")
                print(f"  - Promedio Geométrico: {prom_geometrico}")

                suma_cuadrados = 0
                for j in range(n):
                    diferencia = valores[j] - prom_aritmetico
                    suma_cuadrados += diferencia * diferencia

                varianza = suma_cuadrados / n
                desviacion_estandar = varianza ** 0.5

                print("\n• Medidas de Dispersión:")
                print(f"  - Varianza: {varianza}")
                print(f"  - Desviación Estándar: {desviacion_estandar}")

                valores_ordenados = []
                for j in range(n):
                    valores_ordenados += [valores[j]]

                for j in range(n - 1):
                    for k in range(n - 1 - j):
                        if valores_ordenados[k] > valores_ordenados[k + 1]:
                            aux = valores_ordenados[k]
                            valores_ordenados[k] = valores_ordenados[k + 1]
                            valores_ordenados[k + 1] = aux

                mitad = n // 2
                if n % 2 != 0:
                    mediana = valores_ordenados[mitad]
                else:
                    mediana = (valores_ordenados[mitad - 1] + valores_ordenados[mitad]) / 2

                print("\n• Medidas de Posición:")
                print(f"  - Mediana: {mediana}")
                print("=============================================")