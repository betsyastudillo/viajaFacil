import random


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
  "horarioSalidaVuelta": {
        '1': '05:30 am', '2': '09:30 am', '3': '01:20 pm', '4': '05:20 pm', '5': '09:20 pm'
      },
}


inicio = input("Bienvenid@ al área de vuelos. Seleccione la opción que busca: 1. Buscar Vuelos, 2. Ver Boletos: ")

if inicio == '1':
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
  hora_aleat = random.sample(list(vueloCompra['horarioSalidaIda'].items()), 5)
  for key, value in hora_aleat:
    print(f"{key}. {value}")
  
  hora_ida = input("Ingrese la opción de horario de ida que desea:\n")
  vueloCompra['horarioSalidaIda'] = dict(hora_aleat).get(hora_ida, "Horario no válido") 
  
  # Escoge los horarios del vuelo de ida:
  print("Seleccione una hora de salida para el vuelo de regreso:")
  hora_aleat_vuelta = random.sample(list(vueloCompra['horarioSalidaVuelta'].items()), 5)
  for key, value in hora_aleat:
    print(f"{key}. {value}")
  
  hora_vuelta = input("Ingrese la opción de horario de regreso que desea:\n")
  vueloCompra['horarioSalidaVuelta'] = dict(hora_aleat_vuelta).get(hora_vuelta, "Horario no válido") 


  # Confirmemos la compra:
  print("\n Resumen de su compra:")
  print(f"Ciudad de origen: {vueloCompra['ciudadOrigen']}")
  print(f"Ciudad de destino: {vueloCompra['ciudadDestino']}")
  print(f"Fecha ida: {vueloCompra['fechaIda']}")
  print(f"Fecha de regreso: {vueloCompra['fechaRegreso']}")
  print(f"Horario de salida viaje de ida: {vueloCompra['horarioSalidaIda']}")
  print(f"Horario de salida viaje de regreso: {vueloCompra['horarioSalidaVuelta']}")
  print(f"Horario de salida viaje de regreso: {vueloCompra['horarioSalidaVuelta']}")

  if vueloCompra['ciudadOrigen'] == 'cali':
    print("El costo de sus vuelos tiene un total de $80.000")
  elif vueloCompra['ciudadOrigen'] == 'medellin':
    print("El costo de sus vuelos tiene un total de $100.000")
  elif vueloCompra['ciudadOrigen'] == 'bogota':
    print("El costo de sus vuelos tiene un total de $120.000")
  elif vueloCompra['ciudadOrigen'] == 'barranquilla':
    print("El costo de sus vuelos tiene un total de $150.000")

