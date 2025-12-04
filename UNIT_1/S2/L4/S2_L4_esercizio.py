# Traccia: Si scriva un programma in Python che in base alla scelta dellʼutente permetta di calcolare il perimetro di diverse figure geometriche (scegliete pure quelle che volete voi). 
# Per la risoluzione dellʼesercizio abbiamo scelto: 
# ● Quadrato (perimetro = lato*4. 
# ● Cerchio (circonferenza = 2*pi greco*r). 
# ● Rettangolo (perimetro= base*2 + altezza*2.

import math

def calcolo_perimetro ():
    scelta = 0

    while scelta != 4:
        scelta = int(input("Inserisci un valore: \n 1 per calcolare il perimentro del quadrato \n 2 per calcolare la circonferenza del cerchio \n 3 per calcolare il perimetro del rettangolo \n 4 per uscire \n Cosa scegli? "))

        if scelta == 1:
            lato = int(input("Hai scelto il quadrato, inserisci il valore del lato: "))
            risultato = lato * 4
            print(f"\nIl perimetro è : {risultato}\n")

        elif scelta == 2:
            raggio = int(input("Hai scelto il cerchio, inserisci il valore del cerchio: "))
            risultato = 2 * math.pi * raggio
            print(f"\nLa circonferenza è : {risultato}\n")
        
        elif scelta == 3:
            base = int(input("Hai scelto il rettangolo, inserisci il valore della base: "))
            altezza = int(input("inserisci il valore dell'altezza: "))
            risultato = base * 2 + altezza * 2
            print(f"\nIl perimetro è : {risultato}\n")

        elif scelta == 4:
            print("\nArrivederci!")

        else:
            print("\nScelta non valida, puoi inserire solo 1, 2, 3 o 4!\n")
    return 0

calcolo_perimetro()
