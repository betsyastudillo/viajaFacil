bienvenida = "\n Bienvenido a Nuestro Menu de Paquetes, por favor elige cual opcion te interesa mas: \n"
print(bienvenida)

Paquete1 = {
        "1": "Paquete de Aventura y Naturaleza en el Eje Cafeteron \n",
        "  DURACION": "4 días / 3 noches \n",
        "  INCLUYE": "\n  -Alojamiento en hoteles boutique en Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorrido por el Parque Nacional Natural Los Nevados \n  -Caminatas y senderismo en la Reserva Natural de Otún Quimbaya \n  -Visitas a fincas cafeteras con cata de café \n  -Actividades como canopy y avistamiento de aves \n",
        "  PRECIO": "1,800,000 \n"
}

Paquete2 = {
        "2": "Tour Cultural y Gastronómico del Eje Cafetero \n",
        "  DURACION": "5 días / 4 noches \n",
        "  INCLUYE": "\n  -Alojamiento en Salento y Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorrido por pueblos tradicionales \n  -Experiencia gastronómica con almuerzos y clase de cocina \n  -Tour por una finca cafetera \n  -Visitas a mercados locales y museos \n",
        "  PRECIO": "2,000,000 \n"
}

Paquete3 = {
        "3": "Paquete de Relax y Bienestar en el Eje Cafetero \n",
        "  DURACION": "3 días / 2 noches \n",
        "  INCLUYE": "\n  -Alojamiento en un resort con spa en Manizales \n  -Transporte terrestre desde Bogotá o Medellín al Eje Cafetero \n  -Sesiones de masaje y tratamientos de bienestar \n  -Acceso a áreas de relajación y piscinas \n  -Excursión a los Termales de Santa Rosa de Cabal \n  -Desayunos y cenas gourmet \n",
        "  PRECIO": "1,500,000 \n"
}

Paquete4 = {
        "4": "Tour de Ecoturismo y Aventura en la Zona Cafetera \n",
        "  DURACION": "6 días / 5 noches \n",
        "  INCLUYE": "\n  -Alojamiento en hoteles ecológicos en Salento y Manizales \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Caminatas por el Valle de Cocora y la Selva de Intag \n  -Descenso en rafting en el río La Vieja \n  -Paseos en jeep por el Paisaje Cultural Cafetero \n  -Senderismo y avistamiento de aves en la Reserva Natural de Río Blanco \n",
        "  PRECIO": "2,200,000 \n"
}

Paquete5 = {
        "5": "Paquete Familiar en el Eje Cafetero \n",
        "  DURACION": "4 días / 3 noches \n",
        "  INCLUYE": "\n  -Alojamiento en un hotel familiar en Salento \n  -Transporte terrestre desde Cali al Eje Cafetero \n  -Recorridos y actividades para todas las edades \n  -Excursión a una finca cafetera con actividades interactivas para niños \n  -Visitas al Jardín Botánico del Quindío y al Mariposario de Salento \n  -Comidas y cenas familiares \n",
        "  PRECIO": "1,800,000 \n"
}

for paquete in [Paquete1, Paquete2, Paquete3, Paquete4, Paquete5]:
    for key, value in paquete.items():
        print(f"{key}: {value}")
    print()

i = 0

while i < 1 or i > 5:
    i = int(input("Ingrese la opción de su preferencia: "))

    if i == 1:
        print("Perfecto, has seleccionado:")
        for key, value in Paquete1.items():
            print(f"{key}: {value}")
    elif i == 2:
        print("Perfecto, has seleccionado:")
        for key, value in Paquete2.items():
            print(f"{key}: {value}")
    elif i == 3:
        print("Perfecto, has seleccionado:")
        for key, value in Paquete3.items():
            print(f"{key}: {value}")
    elif i == 4:
        print("Perfecto, has seleccionado:")
        for key, value in Paquete4.items():
            print(f"{key}: {value}")
    elif i == 5:
        print("Perfecto, has seleccionado:")
        for key, value in Paquete5.items():
            print(f"{key}: {value}")
    else:
        print("Respuesta no válida. Inténtelo de nuevo.")