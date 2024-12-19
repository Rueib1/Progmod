from Kortstokk import *
import random as rnd
import time
Kløver = {
    'Kløver 2': {'valør': '2', 'verdi': 2, 'farge': 'Kløver', 'kort_nr': 1}, 
    'Kløver 3': {'valør': '3', 'verdi': 3, 'farge': 'Kløver', 'kort_nr': 2}, 
    #'Kløver 4': {'valør': '4', 'verdi': 4, 'farge': 'Kløver', 'kort_nr': 3}, 
    #'Kløver 5': {'valør': '5', 'verdi': 5, 'farge': 'Kløver', 'kort_nr': 4}, 
    #'Kløver 6': {'valør': '6', 'verdi': 6, 'farge': 'Kløver', 'kort_nr': 5}, 
    #'Kløver 7': {'valør': '7', 'verdi': 7, 'farge': 'Kløver', 'kort_nr': 6}, 
    #'Kløver 8': {'valør': '8', 'verdi': 8, 'farge': 'Kløver', 'kort_nr': 7}, 
    #'Kløver 9': {'valør': '9', 'verdi': 9, 'farge': 'Kløver', 'kort_nr': 8},
    #'Kløver 10': {'valør': '10', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 9}, 
    #'Kløver Knekt': {'valør': 'Knekt', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 10}, 
    #'Kløver Dronning': {'valør': 'Dronning', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 11}, 
    'Kløver Konge': {'valør': 'Konge', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 12}, 
    'Kløver Ess': {'valør': 'Ess', 'verdi': 11, 'farge': 'Kløver', 'kort_nr': 13}
}

#deck = Kløver
valgt = []
rekkefølge = []
rekkefølgekey = []
dinekort = []
dinekortkey = []
dealerkort = []
dealerkortkey = []
spill=1
tkort2 = []
total = 0
totaldealer = 0
Blackjackcount_1 = 0
Blackjackcount_2 = 0
a=0

def dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total):
    if totaldealer < 17:
        print(
            "\n Dealer:",
            dealerkortkey,
            "\n Du:",
            dinekortkey,
            "Din sum er:", total)
    while totaldealer < 17:
        print("\n Dealer hit")
        dealerkort.append(rekkefølge[a])
        dealerkortkey.append(rekkefølgekey[a])
        #print(dealerkortkey)
        totaldealer = sum(card["verdi"] for card in dealerkort)
        #print(totaldealer)
        print(
            "\n Dealer:",
            dealerkortkey,
            "\n Du:",
            dinekortkey,
            "Din sum er:", total)
        a+=1
    #print(totaldealer)
    if totaldealer > 21:
        totaldealer = 0
        print("Dealer har over 21")
    
    return totaldealer, a

def blackjack(Blackjackcount, bkort):
    for kort in bkort:
        if kort["valør"] in ["10", "Knekt", "Dronning", "Konge"]:
            Blackjackcount += 1
        elif kort["valør"] in ["Ess"]:
            Blackjackcount += 2
    if Blackjackcount >=3:
        return True

def kortstokk ():
    for i in range(len(deck)):
        ttall = rnd.randint(0,len(deck)-1)
        while ttall in valgt:
            ttall = rnd.randint(0,len(deck)-1)
        valgt.append(ttall)
    #    print(ttall)
    #    print(valgt)
        tkort1key = list(deck.keys())[ttall]
        tkort1 = deck[tkort1key]
        rekkefølgekey.append(tkort1key)
        rekkefølge.append(tkort1)
    #print(rekkefølgekey)

def kort_disdribusjon (ealerkort, dealerkortkey, dinekort, dinekortkey, a):
    dealerkort.append(rekkefølge[a])
    dealerkortkey.append(rekkefølgekey[a])
    a+=1
    dealerkort.append(rekkefølge[a])
    dealerkortkey.append(rekkefølgekey[a])
    a+=1
    dinekort.append(rekkefølge[a])
    dinekortkey.append(rekkefølgekey[a])
    a+=1
    dinekort.append(rekkefølge[a])
    dinekortkey.append(rekkefølgekey[a])
    return dealerkort, dealerkortkey, dinekort, dinekortkey, a

kortstokk()

while True:
    if len(rekkefølge) - a < 4:
        print("Færre enn 4 kort i gjen, spillet er over")
        break
    dinekort.clear()
    dinekortkey.clear()
    dealerkort.clear()
    dealerkortkey.clear()
    Blackjackcount_1 = 0
    Blackjackcount_2 = 0 
    total = 0
    totaldealer = 0
    print (a)
    dealerkort, dealerkortkey, dinekort, dinekortkey, a = kort_disdribusjon(dealerkort, dealerkortkey, dinekort, dinekortkey, a)
    print("a", a)
    #print(tkort1key, tkort1)
    total = sum(card["verdi"] for card in dinekort)
    totaldealer = sum(card["verdi"] for card in dealerkort)
    #print(len(deck), len(dinekort))
    
    print(
        "Dealer:",
        dealerkortkey,
        "\n Du:",
        dinekortkey,
        "Din sum er:", total)

    blackjack_spiller = blackjack(Blackjackcount_1, dinekort)
    blackjack_dealer = blackjack(Blackjackcount_2, dealerkort)

    if blackjack_spiller == True and blackjack_dealer == True:
        print("Du og dealer har blackjack, ingen vinner")
        break
    elif blackjack_spiller == True:
        print("Du har blackjack, og har vunnet")
        break
    elif blackjack_dealer == True:
        print("Dealer har blackjack, og har vunnet")
        break

    hitorstand = input("Hit or Stand ").lower()
    while total <=21:
        if hitorstand == "hit":
            dinekortkey.append(rekkefølgekey[a])
            dinekort.append(rekkefølge[a])
            total = sum(card["verdi"] for card in dinekort)
            a+=1
            if total > 21:
                print(
                    "\n Dealer:",
                    dealerkortkey,
                    "\n Du:",
                    dinekortkey,
                    "Din sum er:", total)
                total = 0
                print("Du har over 21 \n Dealer har vunnet", totaldealer, ":", total)
                break
            else:
                print(
                    "\n Dealer:",
                    dealerkortkey,
                    "\n Du:",
                    dinekortkey,
                    "Din sum er:", total)
                hitorstand = input("Hit or Stand ").lower()
        elif hitorstand == "stand":
            break
        else:
            hitorstand = input("Error, skriv inn på nytt: Hit or Stand ").lower()
    if total == 0:
        break
    else:
        totaldealer, a = dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total)
        if totaldealer > total:
            print("\n Dealer har vunnet", totaldealer, ":", total )
        elif total > totaldealer:
            print("\n Du har vunnet", total, ":", totaldealer)
        elif total == totaldealer:
            print("Ingen vinner", totaldealer, ":", total)
        else:
            print("\n Feil med dealer logik")
    