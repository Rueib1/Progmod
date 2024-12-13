from Kortstokk import *
import random as rnd
import time
Kløver = {
    'Kløver 2': {'valør': '2', 'verdi': 2, 'farge': 'Kløver', 'kort_nr': 1}, 
    'Kløver 3': {'valør': '3', 'verdi': 3, 'farge': 'Kløver', 'kort_nr': 2}, 
    'Kløver 4': {'valør': '4', 'verdi': 4, 'farge': 'Kløver', 'kort_nr': 3}, 
    'Kløver 5': {'valør': '5', 'verdi': 5, 'farge': 'Kløver', 'kort_nr': 4}, 
    'Kløver 6': {'valør': '6', 'verdi': 6, 'farge': 'Kløver', 'kort_nr': 5}, 
    'Kløver 7': {'valør': '7', 'verdi': 7, 'farge': 'Kløver', 'kort_nr': 6}, 
    'Kløver 8': {'valør': '8', 'verdi': 8, 'farge': 'Kløver', 'kort_nr': 7}, 
    'Kløver 9': {'valør': '9', 'verdi': 9, 'farge': 'Kløver', 'kort_nr': 8},
    'Kløver 10': {'valør': '10', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 9}, 
    'Kløver Knekt': {'valør': 'Knekt', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 10}, 
    'Kløver Dronning': {'valør': 'Dronning', 'verdi': 10, 'farge': 'Kløver', 'kort_nr': 11}, 
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
Blackjackcount = 0
a=4

def dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total):
    while totaldealer < 17:
        dealerkort.append(rekkefølge[a])
        dealerkortkey.append(rekkefølgekey[a])
        totaldealer = sum(card["verdi"] for card in dealerkort)
        a+=1
    if totaldealer >= 17 and totaldealer <=21:
        print("Dealer stand")
    elif totaldealer > 21:
        totaldealer = 0
        print("Dealer har over 21")
    print(
        "Dealer:",
        dealerkortkey,
        "\n Du:",
        dinekortkey,
        "Din sum er:", total)
    totaldealer = sum(card["verdi"] for card in dealerkort)
    return totaldealer

def blackjack():
    for kort in dinekort:
        if kort["valør"] in ["10", "Knekt", "Dronning", "Konge",]:
            Blackjackcount += 1
        elif kort["valør"] in ["Ess"]:
            Blackjackcount +=2
    if Blackjackcount >=3:
        print("Blackjack")



for i in range (1):
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
    dealerkort.append(rekkefølge[0])
    dealerkort.append(rekkefølge[1])
    dealerkortkey.append(rekkefølgekey[0])
    dealerkortkey.append(rekkefølgekey[1])
    dinekort.append(rekkefølge[2])
    dinekort.append(rekkefølge[3])
    dinekortkey.append(rekkefølgekey[2])
    dinekortkey.append(rekkefølgekey[3])
    #print(tkort1key, tkort1)
    total = sum(card["verdi"] for card in dinekort)
    totaldealer = sum(card["verdi"] for card in dealerkort)
    print(len(deck), len(dinekort))
    
    blackjack()        
    print(
        "Dealer:",
        dealerkortkey,
        "\n Du:",
        dinekortkey,
        "Din sum er:", total)

    hitorstand = input("Hit or Stand ").lower()
    while total <=21:
        if hitorstand == "hit":
            dinekortkey.append(rekkefølgekey[a])
            dinekort.append(rekkefølge[a])
            total = sum(card["verdi"] for card in dinekort)
            if total > 21:
                total = 0
                print(
                    dinekortkey,
                    "\n Du har over 21")
                hitorstand = "0"
            else:
                print(
                    "Dealer:",
                    dealerkortkey,
                    "\n Du:",
                    dinekortkey,
                    "Din sum er:", total)
                hitorstand = input("Hit or Stand ").lower()
            a+=1
        elif hitorstand == "stand":
            print("\n ")
            hitorstand = "0"
            """else:
            print("feil input", hitorstand, total)
            break"""
        elif hitorstand == "0":
            dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total)
            if totaldealer >= total:
                print("\n Dealer har vunnet", totaldealer, ":", total )
                break
            elif total > totaldealer:
                print("\n Du har vunnet", total, ":", totaldealer)
                break
            else:
                print("\n feil med dealer logik")
    #break