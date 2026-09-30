#Sheily Alejandra Charuc Revolorio 5to. Perito Contador "C"
import random

# Requisitos: Tupla con niveles y Lista para aliados
NIVELES = ("Bosque", "Cueva", "Aldea", "Castillo")
aliados = []

# Estadísticas base del jugador y recursos
vida, hambre, sed, monedas, poderes = 100, 100, 100, 0, 0
arma, tiene_escudo, tiene_llave = "Puños", False, False

def pedir_opcion(max_op):
    """Manejo de errores para evitar que el juego se cierre con letras"""
    while True:
        try:
            op = int(input("Elige una opción: "))
            if 1 <= op <= max_op: return op
            print(f"⚠️ Elige entre 1 y {max_op}.")
        except ValueError:
            print("❌ Pon un número entero.")

def combate(nombre, v_enemigo, at_enemigo):
    """Sistema de combate simplificado por turnos"""
    global vida
    print(f"\n⚔️ ¡Batalla contra {nombre}!")
    while v_enemigo > 0 and vida > 0:
        print(f"❤️ Tu Vida: {vida} | 👾 Vida {nombre}: {v_enemigo}")
        print("1. Atacar  |  2. Usar Poción")
        if pedir_opcion(2) == 1:
            daño = 10 if arma == "Puños" else (20 if arma == "Madera" else 35)
            if poderes > 0: daño += 20
            v_enemigo -= daño
            print(f"💥 Hiciste {daño} de daño.")
        else:
            vida = min(100, vida + 40)
            print("🧪 Recuperas 40 de vida.")
        
        if v_enemigo > 0:
            daño_recibido = max(2, at_enemigo - (5 if tiene_escudo else 0))
            vida -= daño_recibido
            print(f"👹 Enemigo te quita {daño_recibido} de vida.")
    return vida > 0

def bajar_supervivencia():
    """Sistema de supervivencia"""
    global hambre, sed, vida
    hambre, sed = hambre - 25, sed - 25
    if hambre <= 0 or sed <= 0:
        vida -= 20
        print("⚠️ Hambre/sed extrema. Pierdes 20 de vida.")

# --- NIVELES DEL JUEGO ---
def nivel_1():
    global hambre, sed, arma
    print(f"\n--- NIVEL 1: {NIVELES[0]} ---")
    print("1. Buscar comida y agua\n2. Avanzar con hambre")
    if pedir_opcion(2) == 1:
        hambre, sed = 100, 100
        print("🍎 Comiste y recuperaste energías.")
    print("1. Fabricar espada madera\n2. Seguir desarmado")
    if pedir_opcion(2) == 1:
        arma = "Madera"
        print("⚔️ Tienes una Espada de Madera.")
    return combate("Monstruo de las Ramas", 30, 8)

def nivel_2():
    global vida, monedas, arma
    print(f"\n--- NIVEL 2: {NIVELES[1]} ---")
    bajar_supervivencia()
    if vida <= 0: return False
    print("❓ Acertijo: Vuelo sin alas, lloro sin ojos. ¿Qué soy?\n1. El viento\n2. La nube")
    if pedir_opcion(2) == 2:
        print("🔓 ¡Correcto! Puerta abierta.")
    else:
        vida -= 25
        print("❌ Malo. Trampa de rocas te quita 25 de vida.")
    if vida <= 0: return False
    print("1. Picar hierro y ganar 20 monedas\n2. Pasar de largo")
    if pedir_opcion(2) == 1:
        monedas += 20
        arma = "Hierro"
        print("💎 Mejoras tu arma a Espada de Hierro y ganas 20 monedas.")
    return True

def nivel_3():
    global tiene_llave, monedas, tiene_escudo, vida
    print(f"\n--- NIVEL 3: {NIVELES[2]} ---")
    bajar_supervivencia()
    if vida <= 0: return False
    print("1. Hablar con Anciano\n2. Hablar con Guerrero en taberna")
    if pedir_opcion(2) == 1:
        tiene_llave = True
        print("🧓 Anciano te da la Llave Especial.")
    else:
        if monedas >= 10:
            monedas -= 10
            aliados.append("Guerrero Errante")
            print("👥 Reclutaste al Guerrero Errante.")
    print(f"🏪 TIENDA (Tienes {monedas} monedas):\n1. Comprar Escudo (10 mon)\n2. Salir")
    if pedir_opcion(2) == 1 and monedas >= 10:
        tiene_escudo = True
        print("🛡️ Compraste un Escudo.")
    return True

def nivel_4():
    global poderes, vida
    print(f"\n--- NIVEL 4: {NIVELES[3]} ---")
    daño_g = 6 if "Guerrero Errante" in aliados else 12
    if "Guerrero Errante" in aliados: print("👥 Tu aliado debilita a los guardias.")
    if not combate("Guardia Sombrío", 40, daño_g): return False
    
    print("\n✨ ¡Rompes el hechizo! Recuperas tus Súper Poderes y máxima salud.")
    poderes, vida = 3, 100
    return combate("Hechicero Oscuro", 80, 18)

# --- FLUJO PRINCIPAL ---
if __name__ == "__main__":
    print("🎮 ¡INICIA EL JUEGO DE SHEILY! Rescata a tu madre. 🎮")
    if nivel_1() and nivel_2() and nivel_3() and nivel_4():
        print("\n🏆 ¡VICTORIA ABSOLUTA! 🏆")
        print("Salvaste a tu madre y recuperaste tus poderes.")
        print("🔓 [FINAL ESPECIAL]: El héroe regresa a casa como una leyenda.")
    else:
        print("\n❌ FIN DEL JUEGO. El hechicero ganó.")
