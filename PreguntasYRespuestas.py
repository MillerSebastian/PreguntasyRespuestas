from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

preguntas = [
    {
        "pregunta": "¿Cuál es la capital de Colombia?",
        "opciones": ["Barranquilla", "Bogota", "Santa Marta", "Medellín"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Cuánto es 5 x 6?",
        "opciones": ["187187", "25", "11", "56"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Donde la gente es muy gei?",
        "opciones": ["En bogota", "En medellin", "En cucuta", "Cachacos"],
        "respuesta_correcta": 4
    },

    # agregadadas las 3 preguntas faltantes
    # att: Forlan Pri Pra
    {
        "pregunta": "¿Quien fue el responsable de la muerte de Pablo Escobar?",
        "opciones": ["La Guerrilla de las Farc", "El cartel de Cali", "La DEA", "El bloque de busqueda"],
        "respuesta_correcta": 4
    },
    {
        "pregunta": "¿De dónde es el sombrero vueltiao?",
        "opciones": ["La Guajira", "Magdalena", "Sucre", "Cordoba"],
        "respuesta_correcta": 4
    },
     {
        "pregunta": "¿Cuál es el río más largo que pasa por Colombia'?",
        "opciones": ["Cauca", "Sinu", "Amazonas", "Magdalena"],
        "respuesta_correcta": 3
    }
]

respuestas_usuario = []
correctas = 0

print(Fore.CYAN + Style.BRIGHT + "\n========== PREGUNTAS Y RESPUESTAS COSTENAS JUNIOR TU PAPA==========\n")

"""
append: agrega elementos a la lista
indice: guarda la opcion en el for
enumerate: recorre la lista dando el indice y el valor
start: hace que se inicialice en 1 y no en 0
zip: es una funcion que combina dos o mas listas al mismo tiempo, emparejando los elementos posicion por posicion.
"""

for i, pregunta in enumerate(preguntas, start=1):
    print(Fore.YELLOW + f"Pregunta numero {i}: {pregunta['pregunta']}")
    for indice, opcion in enumerate(pregunta["opciones"], start=1):
        print(Fore.BLUE + f"  {indice}. {opcion}")
    
    while True:
        try:
            respuesta = int(input(Fore.WHITE + "Ingrese la respuesta correcta (1-4): "))
            if respuesta < 1 or respuesta > 4:
                print(Fore.RED + "Por favor, ingrese un numero entre 1 y 4.")
                continue
            break
        except ValueError:
            print(Fore.RED + "Entrada inválida. Debe ingresar un numero.")
    
    respuestas_usuario.append(respuesta)
    
    if respuesta == pregunta["respuesta_correcta"]:
        print(Fore.GREEN + "¡Respuesta correcta!\n")
        correctas += 1
    else:
        print(Fore.RED + f"Respuesta incorrecta. La correcta era: {pregunta['respuesta_correcta']}. {pregunta['opciones'][pregunta['respuesta_correcta'] - 1]}\n")

# Mostrar resumen
print(Fore.MAGENTA + "\n========== RESULTADOS ==========")
for i, (pregunta, respuesta) in enumerate(zip(preguntas, respuestas_usuario), start=1):
    correcta = pregunta["respuesta_correcta"]
    texto = f"{i}. {pregunta['pregunta']}"
    if respuesta == correcta:
        print(Fore.GREEN + texto + f" ✅ (Tu respuesta: {pregunta['opciones'][respuesta-1]})")
    else:
        print(Fore.RED + texto + f" ❌ (Tu respuesta: {pregunta['opciones'][respuesta-1]} | Correcta: {pregunta['opciones'][correcta-1]})")

porcentaje = (correctas / len(preguntas)) * 100
print(Fore.CYAN + f"\nHas acertado {correctas} de {len(preguntas)} preguntas.")
print(Fore.CYAN + f"Tu porcentaje de exito fue: {porcentaje:.0f}%")

print(Fore.LIGHTGREEN_EX + "\n¡Gracias por jugar! 👋\n")
