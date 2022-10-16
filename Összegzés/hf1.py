import random
szam = 1
lista = []
while szam <= 5:
    rand = random.randint(1,10)
    szam = szam + 1
    lista.append(rand)




osszeg = 0
for szam2 in lista:
    osszeg = szam2 + osszeg
print(osszeg)
    