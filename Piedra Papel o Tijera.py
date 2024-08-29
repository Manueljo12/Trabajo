import random

def obtener_eleccion_contrincante():
    """Genera una elección aleatoria para la computadora."""
    opciones = ["piedra", "papel", "tijeras"]
    return random.choice(opciones)

def determinar_ganador(eleccion_usuario, eleccion_contrincante):
    """Determina el ganador del juego."""
    if eleccion_usuario == eleccion_contrincante:
        return "¡Es un empate!"
    elif (eleccion_usuario == "piedra" and eleccion_contrincante == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_contrincante == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_contrincante == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def juego_de_piedra_papel_o_tijeras():
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    while True:
        eleccion_usuario = input("Elige entre piedra, papel o tijeras: ").lower()
        
        if eleccion_usuario not in ["piedra", "papel", "tijeras"]:
            print("Por favor, elige entre piedra, papel o tijeras.")
            continue
        
        eleccion_contrincante = obtener_eleccion_contrincante()
        print(f"La computadora eligió: {eleccion_contrincante}")

        resultado = determinar_ganador(eleccion_usuario, eleccion_contrincante)
        print(resultado)
        
        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if jugar_de_nuevo != "s":
            print("¡Gracias por jugar! ¡Hasta la próxima!")
            break

juego_de_piedra_papel_o_tijeras()