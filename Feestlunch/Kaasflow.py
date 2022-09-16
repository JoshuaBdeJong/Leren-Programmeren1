print ('Wat voor soort kaas is het? ')

kaas = input('is de kaas geel? ').lower()
if kaas in ('ja', 'j'):
    gaten = input('zitten er gaten in? ').lower()
    if gaten in ('nee', 'n'):
        hard_steen = input('is de kaas hard als steen? ')
        if hard_steen in ('ja'):
            print ('Parmigiano Reggiano')
        elif hard_steen in ('nee'):
            print ('Goudse Kaas')
    elif gaten in ('ja'):
        duur = input('is de kaas belagelijk duur? ')
        if duur in ('ja'):
            print ('Emmentaler')
        elif duur in ('nee'):
            print('Leerdammer')
if kaas in ('nee'):
    schimmel = input('heeft de kaas blauwe schimmel? ')
    if schimmel in ('ja'):
        korst = input('heeft de kaas een korst? ')
        if korst in ('ja'):
            print('Blue de Rochbaron')
        elif korst in ('nee'):
            print("Foume d'Ambert")
    elif schimmel in ('nee'):
        korst2 = input('heeft de kaas een korst? ')
        if korst2 in ('ja'):
            print('Camembert')
        elif korst2 in ('nee'):
            print('Mozzarella')
        