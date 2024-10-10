import random
import pprint
import time
from funciones_hundirlaflota import *


# Aquí empieza el programa principal
nombre_jugador = menu_inicio()

# Se crean los tableros
tablero_jugador = crea_tablero()
tablero_maquina = crea_tablero()
disparos_jugador = crea_tablero()

# Se colocan aleatoriamente los barcos en el tablero de la máquina
colocar_barco_aleatorio(tablero_maquina, 4)
for i in range(2):
    colocar_barco_aleatorio(tablero_maquina, 3)
for i in range(3):
    colocar_barco_aleatorio(tablero_maquina, 2)
for i in range(4):
    colocar_barco_aleatorio(tablero_maquina, 1) 
pprint.pprint(tablero_maquina)   # en el juego real se eliminaría esta línea para que no muestre en pantalla el tablero de la máquina

colocacion = input('Elige como quieres colocar los barcos(manual/aleatorio)')
if colocacion.lower() not in ['manual', 'aleatorio']:
    colocacion = 'aleatorio'
    print('Entrada incorrecta. Se colocarán aleatoriamente los barcos')

if colocacion.lower() == 'aleatorio':                       # Se colocan aleatoriamente los barcos en el tablero del jugador
    colocar_barco_aleatorio(tablero_jugador, 4)
    for i in range(2):
        colocar_barco_aleatorio(tablero_jugador, 3)
    for i in range(3):
        colocar_barco_aleatorio(tablero_jugador, 2)
    for i in range(4):
        colocar_barco_aleatorio(tablero_jugador, 1) 
    print('El tablero con tus barcos:')  
    pprint.pprint(tablero_jugador)

elif colocacion.lower() == 'manual':   
    print('Portaaviones, tamaño 4')                     # Se colocan los barcos manualmente en el tablero del jugador
    colocar_barco_manual(tablero_jugador, 4)
    for i in range(2):
        print('Acorazado, tamaño 3')
        colocar_barco_manual(tablero_jugador, 3)
    for i in range(3):
        print('Destructor, tamaño 2')
        colocar_barco_manual(tablero_jugador, 2)
    for i in range(4):
        print('Fragata, tamaño 1')
        colocar_barco_manual(tablero_jugador, 1) 
    print('El tablero con tus barcos:')  
    pprint.pprint(tablero_jugador)

# Se inician a 0 los marcadores de los jugadores
puntos_jugador = 0
puntos_maquina = 0

# Aquí comienza el bucle principal del juego
fin_juego = False
ronda = 1
while not fin_juego:
    time.sleep(1.8)
    print()
    print()
    print(f'RONDA {ronda}')
    mostrar_marcador(puntos_jugador, puntos_maquina, nombre_jugador)
    print()

    # Turno del jugador
    print('Tu turno:')
    puntos_jugador = disparo_jugador(tablero_maquina, disparos_jugador, puntos_jugador)
    print()
    if puntos_jugador == 20:
        print('¡¡ WIN !! Has hundido todos los barcos del enemigo')
        print('Resultado final:')
        mostrar_marcador(puntos_jugador, puntos_maquina, nombre_jugador)
        fin_juego = True
        break

    # Turno de la máquina
    print('Turno de la máquina:')
    puntos_maquina = disparo_maquina(tablero_jugador, puntos_maquina)
    if puntos_maquina == 20:
        print('¡¡ GAME OVER !! Todos tus barcos están hundidos')
        print('Resultado final:')
        mostrar_marcador(puntos_jugador, puntos_maquina, nombre_jugador)
        fin_juego = True
        break

    ronda = ronda + 1
