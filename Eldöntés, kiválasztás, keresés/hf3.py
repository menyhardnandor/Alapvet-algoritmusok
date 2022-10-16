szo = 'alma'
szo2 = input('Adj meg egy betűt: ')

talalat = False
index = 0

while index < len(szo) and not talalat:
    if szo[index] == szo2:
        talalat = True
    index = index + 1
print(szo)
if talalat:
    print('Van benne! ')
else:
    print('Nincs benne!')