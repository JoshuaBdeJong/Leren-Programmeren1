# Vacature: Circusdirecteur voor Circus HotelDeBotel

ervaring = int (input('Hoeveel jaar ervaring heeft u met dieren-dressuur? '))
if ervaring <= 4:
    ervaring2 = int (input('Hoeveel jaar ervaring heeft u met jongleren? '))
    if ervaring2 <= 5:
        ervaring3 = int (input('Hoeveel jaar ervaring heeft u met acrobatiek? '))
diploma = input('Heeft u een MBO-4 diploma ondernemen? (J/N) ')
bewijs = input('Heeft u een vrachtwagen rjibewijs? (J/N) ')
hoed = input('Heeft u een hoge hoed? (J/N) ')
man = input('Bent u een man? (J/N) ')

if man == 'j':
    snor = int (input('Hoe breed is uw snor in cm? '))

else:
    haar = input('Is uw haar rood en krullig? (J/N) ')
    haar2 = int (input('Hoe lang is uw haar in cm? '))

lengte = int (input('Hoelang bent u in cm? '))
gewicht = int (input('Hoeveel weegt u in kg? '))
certificaat = input("Heeft u het certificaat, 'overleven met gevaarlijk personeel'? (J/N) ")
fav_eten = str (input('Wat is uw favoriete eten? '))
if fav_eten == 'Kip' or 'kip':
    raise NameError('Kip?!, aangenomen!')

#aantal behaalde punten
s = 0

if ervaring > 4:
    s += 1

if ervaring <= 4:
    if ervaring2 > 5:
        s += 1

if ervaring <= 4:
    if ervaring2 <= 5:
        if ervaring3 > 3:
            s += 1

if diploma == "j":
    s += 1

if bewijs == "j":
    s += 1

if hoed == "j":
    s += 1

if man == "j":
    if snor > 10:
        s += 1

if man == "n":
    if haar == "j":
        s += 1

    if haar2 > 20:
        s += 1

if lengte > 150:
    s += 1

if gewicht > 90:
    s += 1

if certificaat == "j":
    s += 1

if man == "j":
    if s >= 8:
        print("U mag gaan soliciteren!", s)
    else:
        print("U mag helaas niet gaan soliciteren!", s)
