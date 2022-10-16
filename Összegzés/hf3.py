szam = 0
lista = []

while szam >= -5 and szam <= 5:
    szam = int(input('Adj meg egy számot: '))
    if szam >= -5 and szam <= 5:
        lista.append(szam)

osszeg = 0
for szam2 in lista:
    osszeg = osszeg + szam2
print(lista)
print(osszeg)