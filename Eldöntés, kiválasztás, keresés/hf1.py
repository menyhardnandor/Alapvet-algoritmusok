import random
szam = 0
lista = []
i = 1

while i <= 5:
    szam = random.randint(1,7)
    lista.append(szam)
    i = i+1

ertek = False
index = 0
szam2 = int(input('Adj meg egy számot 1 és 7 között: '))
while index < len(lista) and not ertek:
    
    if lista[index] == szam2:
        ertek = True
        
    index = index + 1
if ertek:
    print(lista)
    print('Van benne!')
else:
    print(lista)
    print('Nincs benne!')

