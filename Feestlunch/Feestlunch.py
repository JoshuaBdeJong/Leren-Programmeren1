aantal_croissant = 17
prijs_croissant = 0.39

prijs_croissant_totaal = aantal_croissant * prijs_croissant

aantal_stokbrood = 2
prijs_stokbrood = 2.78

prijs_stokbrood_totaal = aantal_stokbrood * prijs_stokbrood

kortingsbon = 0.50
aantal_kortingsbon = 3
kortingsbon_totaal = kortingsbon * aantal_kortingsbon

prijs_totaal = prijs_croissant_totaal + prijs_stokbrood_totaal - kortingsbon_totaal
print (prijs_totaal)