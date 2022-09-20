print ('Wat voor soort kaas is het? ')

kaas = input('is de kaas geel? ').lower()
if kaas in ('ja', 'j'):
    gaten = input('zitten er gaten in? ').lower()
    if gaten in ('nee', 'n'):
        hard_steen = input('is de kaas hard als steen? ')
        if hard_steen in ('ja', 'j'):
            print ('Parmigiano Reggiano')
        elif hard_steen in ('nee', 'n'):
            print ('Goudse Kaas')
    elif gaten in ('ja', 'j'):
        duur = input('is de kaas belagelijk duur? ')
        if duur in ('ja', 'j'):
            print ('Emmentaler')
        elif duur in ('nee', 'n'):
            print('Leerdammer')
if kaas in ('nee', 'n'):
    schimmel = input('heeft de kaas blauwe schimmel? ')
    if schimmel in ('ja', 'j'):
        korst = input('heeft de kaas een korst? ')
        if korst in ('ja', 'j'):
            print('Blue de Rochbaron')
        elif korst in ('nee', 'n'):
            print("Foume d'Ambert")
    elif schimmel in ('nee', 'n'):
        korst2 = input('heeft de kaas een korst? ')
        if korst2 in ('ja', 'j'):
            print('Camembert')
        elif korst2 in ('nee', 'n'):
            print('Mozzarella')
        