# Diccionario para almacenar los datos de los clientes, utilizando la cédula como clave única
nombre_cliente = '',
telefono_cliente = '',
correo_cliente = '',
direccion_cliente = ''


clientes_dict = {
  'nombre': nombre_cliente,
  'telefono': telefono_cliente,
  'correo': correo_cliente,
  'direccion': direccion_cliente
}

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
      print("Gracias por estar aquí. Nos vemos una próxima ocasión")
      mostrar_menu_principal()
      # break
    else:
      print("Opción no válida. Por favor, intente nuevamente.")


    print("\n Bienvenid@ a Nuestro Menu de Paquetes, por favor la opción de tu preferencia: \n")

    paquetes = {
      '1': {
            "NOMBRE DEL PAQUETE": "Paquete de Aventura y Naturaleza en el Eje Cafeteron \n",
            "DURACION": "4 días / 3 noches \n",
            "INCLUYE": "\n  -Alojamiento en hoteles boutique en Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorrido por el Parque Nacional Natural Los Nevados \n  -Caminatas y senderismo en la Reserva Natural de Otún Quimbaya \n  -Visitas a fincas cafeteras con cata de café \n  -Actividades como canopy y avistamiento de aves \n",
            "PRECIO": "1,800,000 \n"
            },
      '2': {
            "NOMBRE DEL PAQUETE": "Tour Cultural y Gastronómico del Eje Cafetero \n",
            "DURACION": "5 días / 4 noches \n",
            "INCLUYE": "\n  -Alojamiento en Salento y Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorrido por pueblos tradicionales \n  -Experiencia gastronómica con almuerzos y clase de cocina \n  -Tour por una finca cafetera \n  -Visitas a mercados locales y museos \n",
            "PRECIO": "2,000,000 \n"
          },
      '3': {
            "NOMBRE DEL PAQUETE": "Paquete de Relax y Bienestar en el Eje Cafetero \n",
            "DURACION": "3 días / 2 noches \n",
            "INCLUYE": "\n  -Alojamiento en un resort con spa en Manizales \n  -Transporte terrestre desde Bogotá o Medellín al Eje Cafetero \n  -Sesiones de masaje y tratamientos de bienestar \n  -Acceso a áreas de relajación y piscinas \n  -Excursión a los Termales de Santa Rosa de Cabal \n  -Desayunos y cenas gourmet \n",
            "PRECIO": "1,500,000 \n"
          },
      '4': {
            "NOMBRE DEL PAQUETE": "Tour de Ecoturismo y Aventura en la Zona Cafetera \n",
            "DURACION": "6 días / 5 noches \n",
            "INCLUYE": "\n  -Alojamiento en hoteles ecológicos en Salento y Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Caminatas por el Valle de Cocora y la Selva de Intag \n  -Descenso en rafting en el río La Vieja \n  -Paseos en jeep por el Paisaje Cultural Cafetero \n  -Senderismo y avistamiento de aves en la Reserva Natural de Río Blanco \n",
            "PRECIO": "2,200,000 \n"
          },
      '5': {
            "NOMBRE DEL PAQUETE": "Paquete Familiar en el Eje Cafetero \n",
            "DURACION": "4 días / 3 noches \n",
            "INCLUYE": "\n  -Alojamiento en un hotel familiar en Salento \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorridos y actividades para todas las edades \n  -Excursión a una finca cafetera con actividades interactivas para niños \n  -Visitas al Jardín Botánico del Quindío y al Mariposario de Salento \n  -Comidas y cenas familiares \n",
            "PRECIO": "1,800,000 \n"
          }
    }


    for key, subdict in paquetes.items():
      print(f"{key}:")
      
      for sub_key, value in subdict.items():
        print(f"{sub_key}: {value}")

    paq = int(input("Ingrese la opción de su preferencia: "))

    if str(paq) in paquetes:
      print("Perfecto, has seleccionado: ")

      for key, value in paquetes[str(paq)].items():
        print(f"{key}: {value}")

    else:
        print("Respuesta no válida. Inténtelo de nuevo.")


    print("\n Bienvenid@ a Nuestro Menu de Hoteles, por favor elige la opción de tu preferencia: \n")

    hoteles = { 
      '1': { 
        "Nombre Habitación": 'Hotel Marulanda',
        "Tipo de Habitación": 'Habitación doble',
        "Accesorios": 'Tina incluida, aire acondicionado, cocina',

        },
      '2': { 
        "Nombre Habitación": 'Hotel Astudillo',
        "Tipo de Habitación": 'Habitación sencilla',
        "Accesorios": 'Aire acondicionado',

        },
      '3': { 
        "Nombre Habitación": 'Hotel Rodriguez',
        "Tipo de Habitación": 'Habitación triple',
        "Accesorios": 'Jacuzzi incluida, aire acondicionado',

        },
      '4': { 
        "Nombre Habitación": 'Hotel Ivanich',
        "Tipo de Habitación": 'Habitación múltiple',
        "Accesorios": 'Jacuzzi incluida, aire acondicionado, cocina, buenas vistas',

        },
      '5': { 
        "Nombre Habitación": 'Hotel Montaño',
        "Tipo de Habitación": 'Habitación suite',
        "Accesorios": 'Tina incluida, aire acondicionado',

        },
      }
    
    for key, subdict in hoteles.items():
      print(f"{key}:")

      for sub_key, value in subdict.items():
        print(f"{sub_key}: {value}")

    hot = int(input("\nIngrese la opción de su preferencia: "))

    if str(hot) in hoteles:
      print("\nPerfecto, has seleccionado: ")

      for key, value in hoteles[str(hot)].items():
        print(f"{key}: {value}")

    else:
        print("Respuesta no válida. Inténtelo de nuevo.")


    print("\n Bienvenid@ a Nuestro Menu de Vuelos, por favor elige la opción de tu preferencia: \n")

    vueloCompra = {
      "ciudadOrigen": '',
      "ciudadDestino": {
            '1': "Armenia: Aeropuerto Internacional El Edén", 
            '2': "Pereira: Aeropuerto Internacional Matecaña", 
            '3': "Manizales: Aeropuerto La Nubia"
      },
      "fechaIda": '',
      "fechaRegreso": '',
      "horarioSalidaIda": {
            '1': '05:30 am', '2': '09:30 am', '3': '01:20 pm', '4': '05:20 pm', '5': '09:20 pm'
      },
      "horarioSeleccionadoIda": '',
      "horarioSalidaVuelta": {
            '1': '05:30 am', '2': '09:30 am', '3': '01:20 pm', '4': '05:20 pm', '5': '09:20 pm'
      },
      "horarioSeleccionadoVuelta": ''
    }


    # Escoge la ciudad de origen
    vueloCompra['ciudadOrigen'] = input("Digite la ciudad de orígen:\n")


    # Escoge la ciudad de destino
    print("Seleccione la ciudad de destino:")
    for key, value in vueloCompra['ciudadDestino'].items():
      print(f"{key}. {value}")

    destino = input("Ingrese el número correspondiente a la ciudad de destino:\n")
    vueloCompra['ciudadDestino'] = vueloCompra["ciudadDestino"].get(destino, "Destino no válido")


    # Escoge la fecha de ida:
    vueloCompra['fechaIda'] = input("Digite la fecha de ida (DD/MM/YYYY):\n")


    # Escoge la fecha de regreso:
    vueloCompra['fechaRegreso'] = input("Digite la fecha de regreso (DD/MM/YYYY):\n")


    # Escoge los horarios del vuelo de ida:
    print("Seleccione una hora de salida para el vuelo de ida:")
    for key, value in vueloCompra['horarioSalidaIda'].items():
      print(f"{key}. {value}")

    hora_ida = input("Ingrese la opción de horario de ida que desea:\n")

    # Lo agregamos a la variable horarioSeleccionadoIda para que no sobreescriba el diccionario
    vueloCompra['horarioSeleccionadoIda'] = vueloCompra['horarioSalidaIda'].get(hora_ida, "Horario no válido")

    # Comprobamos si la opción que ingresó fue válida
    if vueloCompra['horarioSeleccionadoIda'] == "Horario no válido":
      print("Ha seleccionado una hora no válida")

    else:
      print(f"Hora de ida seleccionada: {vueloCompra['horarioSeleccionadoIda']}")


    # Escoge los horarios del vuelo de ida:
    print("Seleccione una hora de salida para el vuelo de regreso:")
    for key, value in vueloCompra['horarioSalidaVuelta'].items():
      print(f"{key}. {value}")

    hora_vuelta = input("Ingrese la opción de horario de regreso que desea:\n")
    vueloCompra['horarioSeleccionadoVuelta'] = vueloCompra['horarioSalidaVuelta'].get(hora_vuelta, "Horario no válido") 

    # Comprobamos si la opción que ingresó fue válida
    if vueloCompra['horarioSeleccionadoVuelta'] == "Horario no válido":
      print("Ha seleccionado una hora no válida")

    else:
      print(f"Hora de ida seleccionada: {vueloCompra['horarioSeleccionadoVuelta']}")


    # Confirmemos la compra:
    print("\n Resumen de su tiquete:")
    print(f"Ciudad de origen: {vueloCompra['ciudadOrigen']}")
    print(f"Ciudad de destino: {vueloCompra['ciudadDestino']}")
    print(f"Fecha ida: {vueloCompra['fechaIda']}")
    print(f"Fecha de regreso: {vueloCompra['fechaRegreso']}")
    print(f"Horario de salida viaje de ida: {vueloCompra['horarioSeleccionadoIda']}")
    print(f"Horario de salida viaje de regreso: {vueloCompra['horarioSeleccionadoVuelta']}")

    if vueloCompra['ciudadOrigen'] == 'cali':
      print("El costo de sus vuelos tiene un total de $80.000")
    elif vueloCompra['ciudadOrigen'] == 'medellin':
      print("El costo de sus vuelos tiene un total de $100.000")
    elif vueloCompra['ciudadOrigen'] == 'bogota':
      print("El costo de sus vuelos tiene un total de $120.000")
    elif vueloCompra['ciudadOrigen'] == 'barranquilla':
      print("El costo de sus vuelos tiene un total de $150.000")


def registrar_cliente():
  cedula_cliente = input("Ingrese la cédula del cliente: ")

  if cedula_cliente in clientes_dict:
    print("Esta cédula ya está registrada. Intente con otra.")
    return
  
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

  print("Cliente '" + nombre_cliente + "' registrado exitosamente.")


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


if __name__ == "__main__": mostrar_menu_principal()

      
