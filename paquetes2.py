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

try:
    i = int(input("Ingrese la opción de su preferencia (1-5): "))
except ValueError:
    print("Entrada inválida. Por favor, ingrese un número del 1 al 5.")
    exit()

def paquete(i):
    seleccion = {
        1: "Perfecto, haz seleccionado: "+Paquete1["1"],
        2: "Perfecto, haz seleccionado: "+Paquete2["2"],
        3: "Perfecto, haz seleccionado: "+Paquete3["3"],
        4: "Perfecto, haz seleccionado: "+Paquete4["4"],
        5: "Perfecto, haz seleccionado: "+Paquete5["5"]
    }
    return seleccion.get(i, "Opcion no disponible")

print(paquete(i))

