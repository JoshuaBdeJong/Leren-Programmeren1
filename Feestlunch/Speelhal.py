#Prijs dagje-uit in speelhal

aantalpersonen = int (input ('Met hoeveel personen? '))

toegangsticket = 7.45
entree = aantalpersonen * toegangsticket

tijd_per_periode = 7
seat_per_periode = 0.37
aantalminuten = int (input ('Hoeveel minuten wil je zitten? '))
aantal_periodes = aantalminuten / tijd_per_periode
kosten_seat = (aantal_periodes * seat_per_periode) * aantalpersonen

betalen = round (entree + kosten_seat, 2)


print (f'Dit geweldige dagje-uit met {aantalpersonen} mensen in de Speelhal met {aantalminuten} minuten VR kost je maar {betalen} euro!')