## Preguntas y Respuestas - Caso 2

Pregunta: ¿Cuál cree que es el objetivo del programa?  
Respuesta: Simular un juego de Blackjack (21) entre un jugador y la casa (dealer), donde el jugador puede pedir cartas adicionales o plantarse, y la casa juega automáticamente según reglas predefinidas para determinar el ganador basado en los puntos (sin exceder 21).

Pregunta: ¿Qué información tendrá que suministrar el usuario que ejecute el programa?  
Respuesta: El usuario debe seleccionar opciones en el menú: 1 para pedir otra carta o 2 para no querer más cartas. No se requieren otros inputs directos, ya que el juego maneja las cartas automáticamente.

Pregunta: ¿Cuál es el objetivo de cada bloque?  
Respuesta:  
- `mostrar_menu()`: Muestra opciones al jugador y valida la selección (1 o 2).  
- `mostrar_primera_carta()`: Muestra solo la primera carta de la mano (usado para la casa inicialmente).  
- `mostrar_mano_abierta()`: Muestra todas las cartas y puntos de una mano.  
- `mostrar_juego_actual()`: Muestra el estado actual de las manos del jugador y la casa.  
- `turno_jugador()`: Maneja el turno del jugador, permitiendo pedir cartas y verificando condiciones de victoria/derrota.  
- `turno_casa()`: Maneja el turno de la casa, decidiendo si pedir cartas según reglas y verificando resultados.  
- `iniciar_aplicacion()`: Función principal que inicia el juego, reparte cartas iniciales y controla el flujo de turnos.

Pregunta: ¿Qué es lo que primero se ejecuta?  
Respuesta: La llamada a `iniciar_aplicacion()` al final del archivo, que inicia el juego creando manos nuevas y comenzando los turnos.