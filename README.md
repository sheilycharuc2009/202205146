# Rescate
programador junior sheily charuc

# Fase 1. Analisis
Documento donde realizamos nuestro análisis sobre el juego conteniendo información la idea, que usamos, objetivo, análisis, aspectos, minijuegos, requerimientos funcionales y no funcionales.
mi video juego trata de un superhéroe pierde sus poderes y sufre el secuestro de su madre a manos de un hechicero, lo que lo obliga a emprender una misión de rescate.
Durante la partida, el jugador experimentará el siguiente desarrollo:
• Exploración y combate: Viajar por diversos escenarios enfrentando criaturas y superando desafíos.
• Progresión: Recolectar recursos, conseguir armas, formar un equipo con aliados y recuperar los poderes gradualmente.
• Toma de decisiones: Elegir caminos y opciones que alteran el rumbo de la historia hasta el enfrentamiento final con el villano.


# Fase 2. Diseño
Realizamos un diagrama de flujo sobre nuestro juego y señalamos donde encuentra la clase padre e hij@s.
El proceso funciona de la siguiente manera:
• Inicio: Se declaran las variables de estado y se anuncia la aparición del enemigo en pantalla.
• Bucle de combate: Mientras el jugador y el enemigo tengan vida (HP > 0), el juego muestra la vida actual de ambos y pide elegir una acción.
• Acción 1 (Atacar): Resta el daño del jugador a la vida del enemigo. Si el enemigo sobrevive, este contraataca reduciendo la vida del jugador.
• Acción 2 (Usar Poción): Si quedan pociones, consume una y cura 40 HP al jugador (máximo 100 HP). Si no quedan, avisa que no hay disponibles.
• Desenlace: Cuando uno se queda sin vida, termina el bucle. Si el jugador sobrevivió, se anuncia su victoria y la función devuelve "Verdadero" (sigue vivo); si murió, devuelve "Falso".

# Fase 3. Dasarrollo
Basándonos en el análisis y diagrama de flujo se realizo el código para ver nuestro resultado del juego.
Sus funciones principales son:
• Mecánicas: El jugador gestiona su vida, hambre y sed. Avanzar consume recursos y, si se agotan, se pierde vida.
• Combate por turnos: Permite atacar (el daño varía según el arma: puños, madera o hierro) o curarse con pociones.
• Niveles (1 al 4): El jugador progresa tomando decisiones como recolectar recursos, resolver un acertijo, comprar equipo (escudo), reclutar un aliado y recuperar sus poderes.
• Fin del juego: Si el jugador se queda sin vida en cualquier punto, pierde; si derrota al jefe en el nivel 4, logra la victoria.
