print ('Wat voor soort kaas is het? ')

kaas = str (input('is de kaas geel? ').lower())
if kaas in ('ja'):
    str (input('zitten er gaten in? '))
    if ('nee'):
        str (input('is de kaas hard als steen? ')) 
        if ('ja'):
            print ('Parmigiano Reggiano')
        elif ('nee'):
            print ('Goudse Kaas')
    elif ('ja'):
        str (input('is de kaas belagelijk duur? '))
        if ('ja'):
            print ('Emmentaler')
        elif ('nee'):
            print('Leerdammer')
if kaas in ('nee'):
    str (input('heeft de kaas blauwe schimmel? '))
    if ('ja'):
        str (input('heeft de kaas een korst? '))
        if ('ja'):
            print('Blue de Rochbaron')
        elif ('nee'):
            print("Foume d'Ambert")
    elif ('nee'):
        str (input('heeft de kaas een korst? '))
        if ('ja'):
            print('Camembert')
        elif ('nee'):
            print('Mozzarella')
        