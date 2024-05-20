import random

VALOR_CARTAS = [2,3,4,5,6,7,8,9,10,'J','Q','K','AS']

VALOR_NUM_CARTAS = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10, 'AS':11}

def repartir_carta(mazo_cartas):

    tam_mazo = len(mazo_cartas)
    rand_index = random.randint(0, tam_mazo - 1)
    carta = mazo_cartas.pop(rand_index)

    return carta

def iniciar_partida():

    mazo_cartas = [carta for carta in VALOR_CARTAS for j in range(4)]

    mano_jugador = []
    mano_casa = []

    for j in range(2):
        mano_jugador.append(repartir_carta(mazo_cartas))
        mano_casa.append(repartir_carta(mazo_cartas))

    return mano_jugador, mano_casa, mazo_cartas

def sigueJugando():
    pass

def suma_cartas(mano):
    suma = 0
    for carta in mano:
        suma += VALOR_NUM_CARTAS[carta]
    
    if 'AS' in mano:
        num_ases = sum([1 for j in mano if j == 'AS'])
        contador = 0
        while contador < num_ases and suma > 21:
            suma -= 10
            contador += 1

    return suma

def sigueJugando(mano_jugador):

    if suma_cartas(mano_jugador) <= 21:
        return True
    
    return False

def determinar_ganador(mano_jugador, mano_casa):
    if (suma_cartas(mano_casa) > 21) or suma_cartas(mano_jugador) <= 21 and suma_cartas(mano_jugador) > suma_cartas(mano_casa):
        return 'El jugador'
    else:
        return 'La casa'

while True:

    print(' ')
    print('Bienvenido al Blackjack!')

    # Iniciar la partida - reparte manos al jugador y a casa, resetea el maso de cartas
    mano_jugador, mano_casa, mazo_cartas = iniciar_partida()

    # empieza bucle - hasta que se cumple una condicion 
    while sigueJugando(mano_jugador):

        print('')
        print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
        print('Cartas de la casa: ', mano_casa, suma_cartas(mano_casa))
        print('')

        ### se le pregunta al jugador si pide o se plant
        print('Quieres pedir (P) o Plantarte (S)?')
        pide_o_planta = input()

        ### si pide, se le reparte una carta
        if(pide_o_planta == 'P'):
            mano_jugador.append(repartir_carta(mazo_cartas))

        ### si se planta, la casa se reparte a si misma hasta cumplir una condicion
        elif(pide_o_planta == 'S'):
            while suma_cartas(mano_casa) <= 16:
                mano_casa.append(repartir_carta(mazo_cartas))
            break  #salimso del bucle y pasamos a determonar ganador

    print('')
    print('Tus cartas: ', mano_jugador, suma_cartas(mano_jugador))
    print('Cartas de la casa: ', mano_casa, suma_cartas(mano_casa))
    print('')

    # determinar el ganador
    ganador  = determinar_ganador(mano_jugador, mano_casa)
    
    print('Ha ganado: ',  ganador)

