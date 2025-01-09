"""
En forenklet versjon av Blackjack som også kan hjelpe deg med å holde styr på tellingen av kort.
Laget av Jakob
"""
from Kortstokk import *
import random as rnd
import time
# Noen av kommentarene er generert av ChatGPT, men sett over av meg
# Oppretter tomme lister og variabler for å holde styr på kortene, poengene og spillets tilstand
valgt = []  # Holder oversikt over hvilke kort som allerede er valgt
rekkefølge = []  # Liste for å lagre rekkefølgen av kortene i kortstokken
rekkefølgekey = []  # Nøklene til kortene i rekkefølgen
dinekort = []  # Kortene til spilleren
dinekortkey = []  # Nøklene til spillerens kort
dealerkort = []  # Kortene til dealeren
dealerkortkey = []  # Nøklene til dealerens kort
spill = 1  # Teller antall spill
total = 0  # Summen av kortverdiene til spilleren
totaldealer = 0  # Summen av kortverdiene til dealeren
Blackjackcount_1 = 0  # Telle blackjack-muligheter for spilleren
Blackjackcount_2 = 0  # Telle blackjack-muligheter for dealeren
a = 0  # Indeks for å spore hvor i rekkefølgen vi er
Dine_poeng = 0  # Antall spill spilleren har vunnet
Dealer_poeng = 0  # Antall spill dealeren har vunnet
count = 0
brukte_kort = []

# Funksjon for dealerens logikk
def dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total): #Håndterer dealerens handlinger og oppdaterer dealerens totale poengsum
    if totaldealer < 17:  # Dealer må trekke kort hvis summen er under 17
        print(
            "\n Dealer:",
            dealerkortkey,
            "\n Du:",
            dinekortkey,
            "Din sum er:", total)
    while totaldealer < 17:
        total = juster_for_ess(dinekort, total)  # Justerer for ess
        #print("\n Dealer hit")
        dealerkort.append(rekkefølge[a])
        dealerkortkey.append(rekkefølgekey[a])
        totaldealer = sum(card["verdi"] for card in dealerkort)
        a += 1
    if totaldealer > 21:  # Dealer taper hvis summen overstiger 21
        totaldealer = 0
        print("Dealer har over 21")
    '''        
    print(
        "\n Dealer:",
        dealerkortkey,
        "\n Du:",
        dinekortkey,
        "Din sum er:", total)
    '''
    return totaldealer, a


# Funksjon for å sjekke om en hånd har blackjack
def blackjack(Blackjackcount, bkort): #Sjekker om hånden har blackjack basert på spesifikke kort
    for kort in bkort:
        if kort["valør"] in ["10", "Knekt", "Dronning", "Konge"]:
            Blackjackcount += 1
        elif kort["valør"] in ["Ess"]:
            Blackjackcount += 2
    if Blackjackcount >= 3:  # Blackjack oppnås hvis summen er minst 3
        return True

# Funksjon for å stokke kortstokken
def kortstokk(): #Stokker kortstokken og lagrer resultatet i rekkefølge og rekkefølgekey
    global rekkefølge, rekkefølgekey, valgt
    rekkefølge.clear()
    rekkefølgekey.clear()
    valgt.clear()
    for i in range(len(deck)):
        ttall = rnd.randint(0, len(deck) - 1)
        while ttall in valgt:
            ttall = rnd.randint(0, len(deck) - 1)
        valgt.append(ttall)
        tkort1key = list(deck.keys())[ttall]
        tkort1 = deck[tkort1key]
        rekkefølgekey.append(tkort1key)
        rekkefølge.append(tkort1)

# Funksjon for å distribuere kort til spilleren og dealeren
def kort_disdribusjon(dealerkort, dealerkortkey, dinekort, dinekortkey, a): #Tildeler to kort til både spilleren og dealeren
    dealerkort.append(rekkefølge[a])
    dealerkortkey.append(rekkefølgekey[a])
    a += 1
    dealerkort.append(rekkefølge[a])
    dealerkortkey.append(rekkefølgekey[a])
    a += 1
    dinekort.append(rekkefølge[a])
    dinekortkey.append(rekkefølgekey[a])
    a += 1
    dinekort.append(rekkefølge[a])
    dinekortkey.append(rekkefølgekey[a])
    a += 1
    return dealerkort, dealerkortkey, dinekort, dinekortkey, a

def telling(brukte_kort, count):
    #print("brukte kort", brukte_kort, len(brukte_kort))
    for card in brukte_kort:  #Går gjennom hvert kort i brukte_kort listen
        if card["verdi"] <= 6:
            count += 1
        elif card["verdi"] >= 10:
            count -= 1
    #print(count)
    return count

def juster_for_ess(hånd, total):
    """
    Justerer totalverdien til hånden for å håndtere ess.
    Hvis totalverdien overstiger 21, reduseres verdien til et ess fra 11 til 1 etter behov.
    """
    for kort in hånd:
        if kort["valør"] == "Ess" and total > 21:
            total -= 10  # Reduserer verdien til ess fra 11 til 1
    return total

# Starter spillet ved å stokke kortene
kortstokk()

while True:  # Løkken fortsetter til spilleren avslutter
    # Sjekker om det er færre enn 6 kort igjen i kortstokken for å eventuelt stokke på nytt igjen
    if len(rekkefølge) - a < 6:
        print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++",
              "\n Det er færre enn 6 kort igjen, stokker på nytt! ",
              "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        kortstokk()
        a = 0
    # Tilbakestiller kort og poengsummer for hvert nye spill
    dinekort.clear()
    dinekortkey.clear()
    dealerkort.clear()
    dealerkortkey.clear()
    Blackjackcount_1 = 0
    Blackjackcount_2 = 0
    total = 0
    totaldealer = 0
    hitorstand = 0
    count = 0
    count = telling(brukte_kort, count)
    #print("count", count)

    # Fordeler kort til spiller og dealer
    dealerkort, dealerkortkey, dinekort, dinekortkey, a = kort_disdribusjon(dealerkort, dealerkortkey, dinekort, dinekortkey, a)
    total = sum(card["verdi"] for card in dinekort)
    totaldealer = sum(card["verdi"] for card in dealerkort)

    # Skriver ut poengsummer og kortene
    print(
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        "\n Du har vunnet",
        Dine_poeng,
        "ganger, og dealer har vunnet",
        Dealer_poeng, "ganger \n",
        "Count = ",
        count,
        "\n Dealer:",
        dealerkortkey,
        "\n Du:",
        dinekortkey,
        "Din sum er:", total)

    # Sjekker etter blackjack
    blackjack_spiller = blackjack(Blackjackcount_1, dinekort)
    blackjack_dealer = blackjack(Blackjackcount_2, dealerkort)

    if blackjack_spiller and blackjack_dealer: # Skjekker om begge har blackjack
        print("Du og dealer har blackjack, ingen vinner")
        time.sleep(1)
        continue
    elif blackjack_spiller: # Skjekker om spiller har blackjack
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
              "\nDu har blackjack, og har vunnet",
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        Dine_poeng += 1
        time.sleep(2.5)
        continue
    elif blackjack_dealer: # Skjekker om Dealer har blackjack
        print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
              "\nDealer har blackjack, og har vunnet",
              "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        Dealer_poeng += 1
        time.sleep(1.25)
        continue

    # Lar spilleren velge mellom "hit" eller "stand"
    hitorstand = input("Hit or Stand ").lower()
    while total <= 21:
        if hitorstand in ["hit", "h"]:  # Spilleren velger å trekke et kort
            dinekortkey.append(rekkefølgekey[a]) # Legger til nytt kort i nøkkelen til dine kort
            dinekort.append(rekkefølge[a]) # Legger til det nye kortet i dine kort
            total = sum(card["verdi"] for card in dinekort)
            total = juster_for_ess(dinekort, total)  # Justerer for ess
            a += 1
            if total > 21: # Skjekker om spilleren har over 21
                print(
                    "\n Dealer:",
                    dealerkortkey,
                    "\n Du:",
                    dinekortkey,
                    "Din sum er:", total)
                total = 0
                print(" Du har over 21 \n Dealer har vunnet", totaldealer, ":", total)
                Dealer_poeng += 1
                break
            else: # Fortsetter helt til spilleren sier "stand"
                print(
                    "\n Dealer:",
                    dealerkortkey,
                    "\n Du:",
                    dinekortkey,
                    "Din sum er:", total)
                hitorstand = input("Hit or Stand ").lower()
        elif hitorstand in ["stand", "s"]:  # Spilleren velger å bli værende
            break
        else:
            hitorstand = input("Error, skriv inn på nytt: Hit or Stand ").lower() # Hvis du skulle skrive feil så spør den på nytt i steden for en feilmelding
    for card in dealerkort:
        brukte_kort.append(card)
    for card in dinekort:
        brukte_kort.append(card)
    time.sleep(0.25)
    if total == 0: # Dersom spilleren har gått over, så er det alerede sagt i fra om, og nytt spill begynnes
        continue
    else:
        totaldealer, a = dealer_logikk(dealerkort, dealerkortkey, totaldealer, a, dinekortkey, total)
        if totaldealer > total: #Skjekker om dealer har vunnet
            print("\nDealer har vunnet", totaldealer, ":", total)
            Dealer_poeng += 1
        elif total > totaldealer: # Skjekker om du har vunnet
            print("\nDu har vunnet", total, ":", totaldealer)
            Dine_poeng += 1
        elif total == totaldealer: # Hvis begge har det samme
            print("Ingen vinner", totaldealer, ":", total)
        else:
            print("\n Feil med dealer logikk")
    time.sleep(1)
    a += 1 # Holder styr på hvor mange kort som har blitt brukt