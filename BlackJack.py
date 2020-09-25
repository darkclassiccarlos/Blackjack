import random
import re
#definir la baraja
def baraja():
    baraja = []
    for i in ["♥","♠","♦","♣"]:
        for v in range(1,14):
            if (v==11):
                str(baraja.append(("J"+i)))
            elif(v ==12):       
                str(baraja.append(("Q"+i)))
            elif(v ==13):
                str(baraja.append(("K"+i)))
            elif(v ==1):
                str(baraja.append(("A"+i)))
            else:
                baraja.append((repr(v)+i))
    return baraja
baraja=baraja()

#restar baraja
def restar_baraja(baraja,juego):
    for x in juego:
        if("".join(x) in baraja):
            baraja.remove("".join(x))
    return baraja
#repartir Baraja
def repartir(baraja):
    repartidor = []
    jugador = []
    while len(repartidor) !=2 and len(jugador) !=2:
        random.shuffle(baraja)
        repartidor.append(baraja[:1])
        restar_baraja(baraja, repartidor)
        random.shuffle(baraja)
        jugador.append(baraja[:1])
        restar_baraja(baraja, jugador)
    print("Inicia el juego")
    print("Cartas de la Casa ", repartidor[1])
    print("Cartas del jugador ", jugador)
    return repartidor, jugador

#aumento de cartas
def aumento(cartas):
    if Juego(repartidor) >= 17:
        #print("repartidor tiene: ", Juego(repartidor))
        return cartas
    else:
        print("Repartidor tiene: ", Juego(repartidor), "con ", repartidor)
        repartidor.append(baraja[:1])
        restar_baraja(baraja, repartidor)
        return aumento(cartas)


#Comparativa
def Juego(juego):
    sum = 0
    for i in juego:
        if (len("".join(i))>2):
            sum += 10
        else:
            for v in "".join(i):
                if(re.findall('\d+', v )):
                    sum += int(v)
                elif ('J' in v) or ('Q' in v) or ('K' in v): 
                    sum += 10
                elif ('A'in v):
                    sum +=11
    return(int(sum))

juegos = repartir(baraja)
repartidor = juegos[0]
jugador = juegos[1]
if Juego(jugador) == 21:
    print("Jugador tiene: ", jugador + "Blackjack Gana")
elif Juego(jugador) > 21:
    print("Jugador tiene: ", jugador + "jugador pierde")
while Juego(jugador) < 21:
    Accion = str(input("Carta o no carta? (responda si o no ) "))
    if Accion == 'si':        
        random.shuffle(baraja)
        jugador.append(baraja[:1])
        restar_baraja(baraja, jugador)
        print("tiene un total de: " + str(Juego(jugador)) + " con: ", jugador)
    else:
        #print("repartidor tiene: ", repartidor)
        #print("jugador tiene: ", jugador)                
        repartidor_aumentado = aumento(repartidor)
        print("Repartidor tiene: " + str(Juego(repartidor)) + " con: ", repartidor)
        if (Juego(repartidor)<21) and (Juego(repartidor)) >= Juego(jugador):
            print("Jugador pierde")
            break
        elif Juego(repartidor) > 21:
            print("Jugador Gana")
            break
        elif Juego(jugador) == 21 and Juego(repartidor) == 21:
            print("Jugador Pierde")
        else:
            #print("Jugador gana")
            break
        
if Juego(repartidor) ==21:
    print("Repartidor tiene 21 gana repartidor")
elif Juego(jugador) > 21:
    print("Jugador pierde")
elif Juego(jugador) == 21:
    print("Repartidor tiene: " + str(Juego(repartidor)) + " con: ", repartidor)
    print("21 Jugador Gana")
