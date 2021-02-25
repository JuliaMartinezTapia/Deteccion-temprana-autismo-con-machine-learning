
from funcionesv2 import *
from const_variablesv2 import *
from funcionesv2 import *
import numpy as np
import time

print("¡¡¡¡¡¡Bienvenido a Hundir la flota!!!!!!\n EL juego consiste en hundir los barcos de tu adversario, en este caso el ordenador.\
Contamos con los siguientes barcos:\n 4 barcos de 1 posición de eslora \n 3 barcos de 2 posiciones de eslora \n 2 barcos de 3 posiciones de eslora\n\
1 barco de 4 posiciones de eslora \n\
Siempre empezarás disparando, si aciertas en tu tablero saldrá una “X”, si disparas al agua saldrá “-“.\n\
Si aciertas a un barco te tocará jugar otra vez. Sino, será el turno del ordenador.\n\
¡¡¡¡Mucha suerte y que gane el MEJOR!!!!\n")

#Esto es la llamada a la función que usamos para colocar los barcos en los tableros.
tab_b_us = pintar_barcos(tab_b_us, esloras, jugador)
tab_b_or = pintar_barcos(tab_b_or, esloras, jugador)

print("Empezamos, este es tu tablero:\n", tab_b_us)
print("Y este es el tablero del ordenador:\n", tab_i_or)
print(tab_i_us)
print(tab_b_or)

while True:

    if jugador == "usuario":
        #Este while true controla la introducción de coordenadas por el usuario.

        while True:
            try:
                x_y = input("Facilita las coordenadas del disparo, separadas por una coma: ")
                coordenadas = x_y.split(",")
                coor_x = int(coordenadas[0])
                coor_y = int(coordenadas[1])

                if coor_x <= 9 and coor_y <= 9:
                    break
                else:
                    print("Error, debes ingresar valores numéricos dentro de la x y la y, entre 0 y 9")
            except:
                print("Error, debes ingresar valores numéricos dentro de la x y la y, entre 0 y 9")

        #Aauí llamamos a la función disparar.
        tab_i_or, acierto = disparar(coor_x, coor_y,tab_b_or,tab_i_or)
        print(acierto)

        suma_or, tab_b_us = flujo_juego(coor_y,coor_x,suma_or,acierto,jugador,tab_b_us,tab_i_or)

        if acierto:

            print("Vuelves a jugar")

            if suma_or == 0:
                print("¡Has ganado el juego!")
                break

        else:
            jugador = "ordenador"

    elif jugador == "ordenador":
        #Las coordenadas del disparo del ordenador son aleatorias y se obtienen aplicando un random.
        coor_x = np.random.randint(10)
        coor_y = np.random.randint(10)

        # Aauí llamamos a la función disparar e introducimos un lapso de tiempo para la ejecución y visualización del tablero.
        tab_i_us, acierto  = disparar(coor_x, coor_y, tab_b_us, tab_i_us)

        #def flujo_juego(coor_y, coor_x, suma, acierto, jugador, tab_b_us):

        print("el ordenador ha disparado a las coordenadas (" + str(coor_x) + "," + str(coor_y) + ")")

        suma_us, tab_b_us = flujo_juego(coor_y,coor_x,suma_us, acierto, jugador,tab_b_us,tab_i_or)

        if acierto:
            print("Vuelves a jugar")

            if suma_us == 0:
                print("¡oops! ¡el ordenador te ha ganado la partida!")
                break

        else:
            jugador = "usuario"

