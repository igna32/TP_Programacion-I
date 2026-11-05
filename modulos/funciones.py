
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



