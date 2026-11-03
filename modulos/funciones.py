
def validar_rango(numero: int, minimo: int, maximo: int) -> bool:

    if minimo > maximo:
        respuesta = False

    elif numero == minimo:
        respuesta = True

    else:
        respuesta = validar_rango(numero, minimo + 1, maximo)

    return respuesta


def es_par(numero: int) -> bool:

    if numero < 0:
        respuesta = es_par(-numero)

    elif numero == 0:
        respuesta = True

    elif numero == 1:
        respuesta = False

    else:
        respuesta = es_par(numero - 2)

    return respuesta


def es_primo(numero: int, divisor: int = 0) -> bool:

    if numero < 0:
        numero = -numero

    if numero <= 1:
        respuesta = False

    else:

        if divisor == 0:
            divisor = numero - 1

        if divisor == 1:
            respuesta = True

        elif numero % divisor == 0:
            respuesta = False

        else:
            respuesta = es_primo(numero, divisor - 1)

    return respuesta


def es_multiplo(numero_1: int, numero_2: int) -> bool:

    if numero_1 < 0:
        respuesta = es_multiplo(-numero_1, numero_2)

    elif numero_2 < 0:
        respuesta = es_multiplo(numero_1, -numero_2)

    elif numero_2 == 0:
        respuesta = False

    elif numero_1 == 0:
        respuesta = True

    elif numero_1 < numero_2:
        respuesta = False

    else:
        respuesta = es_multiplo(numero_1 - numero_2, numero_2)

    return respuesta


def es_un_numero(cadena: str) -> bool:

    respuesta = True

    if len(cadena) == 0:
        respuesta = False

    else:

        inicio = 0

        if cadena[0] == '-':

            if len(cadena) == 1:
                respuesta = False

            inicio = 1

        for i in range(inicio, len(cadena)):

            if cadena[i] < '0' or cadena[i] > '9':
                respuesta = False

    return respuesta











"""

def validaciones():

    menu_validaciones = True

    while menu_validaciones:

        print("\n--- VALIDACIONES ---")
        print("1. Validar rango")
        print("2. Verificar si es par")
        print("3. Verificar si es primo")
        print("4. Verificar múltiplo")
        print("5. Volver al menú principal")

        entrada_sub = input("Seleccione una opción: ")

        if not es_un_numero(entrada_sub):
            print("Opción no válida. Ingrese un número entero.")
            continue

        sub_opcion = int(entrada_sub)

        if sub_opcion == 1:

            ent_num = input("Ingrese el número: ")
            ent_min = input("Ingrese el límite mínimo: ")
            ent_max = input("Ingrese el límite máximo: ")

            if es_un_numero(ent_num) and es_un_numero(ent_min) and es_un_numero(ent_max):

                num_rango = int(ent_num)
                minimo = int(ent_min)
                maximo = int(ent_max)

                if validar_rango(num_rango, minimo, maximo):
                    print(f"{num_rango} está dentro del rango [{minimo}-{maximo}].")

                else:
                    print(f"{num_rango} está FUERA del rango [{minimo}-{maximo}].")

            else:
                print("Error: todos los datos deben ser números enteros.")

        elif sub_opcion == 2:

            ent_par = input("Ingrese un número: ")

            if es_un_numero(ent_par):

                num_par = int(ent_par)

                if es_par(num_par):
                    print(f"El número {num_par} es PAR.")

                else:
                    print(f"El número {num_par} es IMPAR.")

            else:
                print("Error: debe ingresar un número entero.")

        elif sub_opcion == 3:

            ent_primo = input("Ingrese un número: ")

            if es_un_numero(ent_primo):

                num_primo = int(ent_primo)

                if es_primo(num_primo):
                    print(f"El número {num_primo} es PRIMO.")

                else:
                    print(f"El número {num_primo} NO es primo.")

            else:
                print("Error: debe ingresar un número entero.")

        elif sub_opcion == 4:

            ent_n1 = input("Ingrese el primer número: ")
            ent_n2 = input("Ingrese el segundo número: ")

            if es_un_numero(ent_n1) and es_un_numero(ent_n2):

                n1 = int(ent_n1)
                n2 = int(ent_n2)

                if es_multiplo(n1, n2):
                    print(f"{n1} es múltiplo de {n2}.")

                else:
                    print(f"{n1} NO es múltiplo de {n2}.")

            else:
                print("Error: ambos valores deben ser números enteros.")

        elif sub_opcion == 5:

            print("Volviendo al menú principal...")
            menu_validaciones = False

        else:
            print("Opción inválida.")
"""