#Prijs dagje-uit in speelhal

aantalpersonen = int (input ('Met hoeveel personen? '))

toegangsticket = 7.45
entree = aantalpersonen * toegangsticket

seat_per5minuten = 0.37
aantalminuten = int (input ('Hoeveel minuten wil je zitten? '))
aantal_periodes = aantalminuten / 5
kosten_seat = (aantal_periodes * seat_per5minuten) * aantalpersonen

betalen = float (entree + kosten_seat)

round(betalen, 2)

print (f'Dit geweldige dagje-uit met {aantalpersonen} mensen in de Speelhal met {aantalminuten} minuten VR kost je maar {betalen} euro!')