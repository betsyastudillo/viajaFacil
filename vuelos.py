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


inicio = input("Bienvenid@ al área de vuelos")


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
print("\n Resumen de su compra:")
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

