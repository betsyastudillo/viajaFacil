# Diccionario para almacenar los datos de los clientes, utilizando la cédula como clave única
clientes_dict = {}

    # MENU ---------------------------------------------------------------------

def mostrar_menu_principal():
    while True:
        print("\n--- Menú Principal de Gestión de Clientes ---")
        print("1. Registrar nuevo cliente")
        print("2. Buscar cliente por cédula")
        print("3. Salir del sistema")
        opcion_seleccionada = input("Seleccione una opción: ")

        if opcion_seleccionada == '1':
            registrar_cliente()
        elif opcion_seleccionada == '2':
            buscar_cliente_por_cedula()
        elif opcion_seleccionada == '3':
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")



# INGRESO DE DATOS ------------------------------------------------------------

def registrar_cliente():
    cedula_cliente = input("Ingrese la cédula del cliente: ")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    telefono_cliente = input("Ingrese el teléfono del cliente: ")
    correo_cliente = input("Ingrese el correo del cliente: ")
    direccion_cliente = input("Ingrese la dirección del cliente (opcional): ")

    
    clientes_dict[cedula_cliente] = {
        'nombre': nombre_cliente,
        'telefono': telefono_cliente,
        'correo': correo_cliente,
        'direccion': direccion_cliente
    }


    if cedula_cliente in clientes_dict:
        print("Esta cédula ya está registrada. Intente con otra.")
        return
    else:
        print("Cliente '" + nombre_cliente + "' registrado exitosamente.")
    
    # BUSCADOR ---------------------------------------------------------------------

def buscar_cliente_por_cedula():
    cedula_cliente_a_buscar = input("Ingrese la cédula del cliente a buscar: ")

    cliente = clientes_dict.get(cedula_cliente_a_buscar)

    if cliente:
        print("\nInformación del cliente con cédula " + cedula_cliente_a_buscar +" :")
        for llave, valor in cliente.items():
            print(" "+ llave.capitalize() + " "+ valor +" " )
    else:
        print("Cliente no encontrado.")


mostrar_menu_principal()

