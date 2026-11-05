from modulos.funciones import es_un_numero, validar_rango
from modulos.tablas import crear_tabla, modificar_tablas, mostrar_tablas


def ejecutar_menu_principal() -> bool:

    sesion = True
    tablas_creadas = []

    while sesion:

        print("\n///// MENU PRINCIPAL /////")
        print("1. Proyectos")
        print("2. Tablas")
        print("3. Variables")
        print("4. Mostrar")
        print("5. Estadística")
        print("6. Validaciones")
        print("7. Cerrar sesión")
        print("//////////////////////////")

        entrada_menu = input("Seleccione una opción del menú: ")

        if not es_un_numero(entrada_menu):
            print("Opción no válida. Ingrese un número.")
            continue

        opcion_menu = int(entrada_menu)

        if not validar_rango(opcion_menu, 1, 7):
            print("Opción fuera de rango. Seleccione una opción entre 1 y 7.")
            continue

        if opcion_menu == 1:

            print("Bienvenido a proyectos")

        elif opcion_menu == 2:

            tabla = crear_tabla()
            tablas_creadas += [tabla]

            print("Tabla creada correctamente.")

        elif opcion_menu == 3:

            modificar_tablas(tablas_creadas)

        elif opcion_menu == 4:

            mostrar_tablas(tablas_creadas)

        elif opcion_menu == 5:

            print("Bienvenido a estadística")

        elif opcion_menu == 6:

            print("Sesión cerrada con éxito.")
            sesion = False

        else:

            print("Opción no válida.")

    return sesion


def iniciar_sesion(usuarios_registrados: list) -> bool:
    """
    Gestiona el intento de inicio de sesión con un máximo de 3 intentos.
    Retorna True si la sesión se inició con éxito, o False en caso contrario.
    """
    intentos = 0
    max_intentos = 3
    sesion_iniciada = False

    while intentos < max_intentos and not sesion_iniciada:
        print(f"\n--- Inicio de sesión (Intento {intentos + 1} de {max_intentos}) ---")

        verificacion_usuario = input("USUARIO: ")
        verificacion_contrasenia = input("CONTRASEÑA: ")

        usuario_encontrado = False

        for i in range(len(usuarios_registrados)):
            if usuarios_registrados[i][0] == verificacion_usuario and usuarios_registrados[i][1] == verificacion_contrasenia:
                usuario_encontrado = True

        if usuario_encontrado:
            sesion_iniciada = True
        else:
            intentos += 1
            if intentos < max_intentos:
                print(f"Usuario o contraseña incorrectos. Te quedan {max_intentos - intentos} intento(s).")
            else:
                print("Ha superado el límite máximo de 3 intentos fallidos.")

    return sesion_iniciada


def registrar_usuario(usuarios_registrados: list):
    """
    Valida y registra un nuevo usuario en la lista recibida.
    """
    print("\n--- Registro de usuario ---")

    nuevo_usuario = input("Cree su nombre de usuario: ")
    nueva_contra = input("Cree su contraseña: ")

    if len(nuevo_usuario) > 0 and len(nueva_contra) > 0:
        usuario_existente = False

        for i in range(len(usuarios_registrados)):
            if usuarios_registrados[i][0] == nuevo_usuario:
                usuario_existente = True

        if usuario_existente:
            print("Ese nombre de usuario ya está registrado.")
        else:
            nuevo_registro = [nuevo_usuario, nueva_contra]
            usuarios_registrados += [nuevo_registro]
            print("¡Usuario registrado exitosamente!")
    else:
        print("El usuario o la contraseña no pueden estar vacíos.")