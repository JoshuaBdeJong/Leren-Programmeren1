print ("Welkom bij 'Pizza Calculator'")

while True:
    try:
        aantal_small = int (input("Hoeveel small pizza's? "))
        break
    except: 
        print ('Dat is geen aantal in nummers!')

while True:
    try:
        aantal_medium = int (input("Hoeveel medium pizza's? "))
        break
    except:
        print ('Dat is geen aantal in nummers!')

while True:
    try:
        aantal_large = int (input("Hoeveel large pizza's? "))
        break
    except:
        print('Dat is geen aantal in nummers!')

prijs_small = 4.99
prijs_medium = 7.99
prijs_large = 9.99

prijs_totaal_small = prijs_small * aantal_small
prijs_totaal_medium = prijs_medium * aantal_medium
prijs_totaal_large = prijs_large * aantal_large
prijs_totaal = prijs_totaal_small + prijs_totaal_medium + prijs_totaal_large

# Bonnetje
print (f"""
--------------------------------------------------------------------
| {aantal_small} small X {prijs_small}
| {aantal_medium} medium X {prijs_medium}
| {aantal_large} large X {prijs_large}
--------------------------------------------------------------------
| Totaalprijs: {prijs_totaal}
--------------------------------------------------------------------""")