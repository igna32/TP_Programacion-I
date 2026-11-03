from modulos.menus import ejecutar_menu_principal, iniciar_sesion, registrar_usuario
from modulos.funciones import es_un_numero, validar_rango

usuarios_registrados = [["angel", "2000"]]
ejecucion_programa = True

while ejecucion_programa:

    print("\n=======================")
    print("  SISTEMA DE USUARIOS  ")
    print("=======================")
    print("1- Iniciar sesión")
    print("2- Registrarte")
    print("3- Salir del programa")
    print("-----------------------")

    entrada_acceso = input("Seleccione una opción: ")

    if not es_un_numero(entrada_acceso):
        print("Por favor, ingrese una opción numérica válida.")
        continue

    acceso = int(entrada_acceso)

    if not validar_rango(acceso, 1, 3):
        print("Opción fuera de rango. Seleccione una opción entre 1 y 3.")
        continue


    if acceso == 1:
        exito = iniciar_sesion(usuarios_registrados)
        if exito:
            ejecutar_menu_principal()

    elif acceso == 2:
        registrar_usuario(usuarios_registrados)

    elif acceso == 3:
        print("Usted salió del programa.")
        ejecucion_programa = False

    else:
        print("Opción inválida.")