a = int (input('Welk getal is a? '))
b = int (input('Welk getal is b? '))

x = max(a, b)
y = min(a, b)

if a > b:
    print('a is het grootste getal: ', (x))

elif a < b:
    print ('a is het kleinstge getal', (y))
