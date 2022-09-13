aantal_croissant = int (input('Hoeveel Croissant? '))
prijs_croissant = 0.39

prijs_croissant_totaal = aantal_croissant * prijs_croissant

aantal_stokbrood = int (input('Hoeveel stokbrood? '))
prijs_stokbrood = 2.78

prijs_stokbrood_totaal = aantal_stokbrood * prijs_stokbrood

kortingsbon = 0.50
aantal_kortingsbon = int (input('Hoeveel kortingsbonnen? '))
kortingsbon_totaal = kortingsbon * aantal_kortingsbon

prijs_totaal = float (prijs_croissant_totaal + prijs_stokbrood_totaal - kortingsbon_totaal)

round (prijs_totaal, 2)
print ("De feestlunch kost je bij de bakker", ("%.2f" % prijs_totaal), "euro voor de", aantal_croissant, " croissantjes en de", aantal_stokbrood, "stokbroden als de", aantal_kortingsbon, "kortingsbonnen nog geldig zijn!")