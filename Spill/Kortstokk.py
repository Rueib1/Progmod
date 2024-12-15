farge = ['Kløver', 'Ruter', 'Hjerter', 'Spar']
valører  = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'Knekt', 12: 'Dronning', 13: 'Konge', 14: 'Ess'}


deck = {}

card_number = 1
for farge in farge:
    for verdi, valør in valører.items():
        if valør in ['Knekt', 'Dronning', 'Konge']:
            verdi = 10
        elif valør in ['Ess']:
            verdi = 11
        else:
            verdi = verdi
        card = {
            'valør': valør,
            'verdi': verdi,
            'farge': farge,
            'kort_nr': card_number
        }
        deck[f'{farge} {valør}'] = card
        card_number += 1

#print(deck)
