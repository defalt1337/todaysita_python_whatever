from random import *
szamok = [1, 2, 3, 4, 5]
rnd = randint(-10,20)
szamok[0] = rnd
rnd = randint(-10,20)
szamok[2] = rnd
szamok[int(len(szamok) / 2)] = rnd
rnd = randint(-10,20)
szamok[-1] = rnd
print(szamok)

for i in range(len(szamok) - 1, -1, -1):
    print(szamok[i], end=":")
print(szamok[-1])
print(szamok[::-1])

#progtételek

#összegzés_tétele
osszeg = 0
for szam in szamok:
    osszeg += szam
#elso feldat

print("Pozitív e az összeg?")
if osszeg > 0:
    print("Pozitív az összeg")
else:
    print("Negatív")

#második feladat
print("Páros e a szám?")

if osszeg % 2 == 0:
    print("páros")
else:
    print("Páratlan")

#harmadik feladat
print("Mennyi a sorozat átlaga?")

print(osszeg / len(szamok))

#megszámlálás
darab = 0
darabnagyobbtiz = 0
paratlan = 0
for szam in szamok:
    if szam%2 == 0:
        darab += 1
    if szam > 10:
        darabnagyobbtiz += 1
    if paratlan %2 == 1:
        paratlan += 1
#tétel vége

#első feladat
print("Hány darab páros szám van a sorozatban?")
print(darab)
#második feladat
print("Hány 10-nél nagyobb szám van?")
print(darabnagyobbtiz)
#harmadik feladat
print("Páratlanok száma")
print(paratlan)
#szélsőérték(min,max)
miniindex = 0
maxindex = 0
for i in szamok:
    if szam < szamok[miniindex]:
        miniindex = szam
    if szam > szamok[maxindex]:
        maxindex = i
#elsőfeladat
print("Legkisebb érték")
print(miniindex)
#második feladat
print("Legnagyobb érték")
print(maxindex)
#harmadik feladat
print("Legkisebb index",szamok[miniindex])
print("Legnagyobb index",szamok[maxindex])
#end_of_the_tételek