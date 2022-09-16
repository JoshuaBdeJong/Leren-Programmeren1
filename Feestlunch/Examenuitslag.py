# score van je examen bereken

score_E = int (input('Hoeveel excellente punten behaald? (0 - 6) ')) 
score_P = int (input('Hoeveel professionele punten behaald? (0 - 8) '))
score_O = int (input('Hoeveel onprofessionele punten behaald? (0 - 5) '))
score_S = int (input('Hoeveel slechte punten behaald? (0 - 2) '))

totale_score = int (score_E + score_P - score_O - score_S)

if score_P == 8 and score_E >= 4 and score_O == 0 and score_S == 0:
    print('Uw uitslag is: goed! ')
elif score_S == 0 and totale_score >= 7 and totale_score <= 13 or score_S == 1 and totale_score >= 9:
    print ('Uw uitslag is: voldoende! ')
else: 
    print ('Uw uitslag is: onvoldoende! ')
