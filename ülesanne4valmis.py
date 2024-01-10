# Ron Evan Krüner
#21.11.2023
#Ülesanne 4

"""
Ruut
Kasutaja sisestab ruudu küljed ning programm tuvastab kas tegemist saab olla ruuduga.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

"""

nr1 = int(input("Ruudu 1. külg: "))
nr2 = int(input("Ruudu 2. külg: "))

if nr1 == nr2:
    print("ruut")
else:
    print("mingi muu asi")
    
"""
Matemaatika
Kasutaja sisestab kaks arvu ning programm küsib kasutajalt, mis tehet ta soovib (+-*/) ning viib kasutaja valiku ellu.
Koosta vastab plokkskeem ja salvesta see samasse kataloogi programmiga.

"""
nr1 = int(input("arv1: "))
nr2 = int(input("arv2: "))
tehe = input("Vali tehe + - * /: ")

if tehe == "+":
    vastus = nr1 + nr2
elif tehe == "-":
    vastus = nr1 - nr2
elif tehe == "*":
    vastus = nr1 * nr2
elif tehe == "/":
    vastus = round(nr1 / nr2, 2)
else:
    vastus = "ära pulli mees!"
    
print(f"{nr1} {tehe} {nr2} = {vastus}")



"""       
Pisike korrutustabel
Koosta programm, mis tekitab automaatselt viiega korrutustabeli.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50

"""
for j in range(1,11):
    for i in range(1,11):
        print(f"{j} x {5*i} = {j*i}")


"""

Viisikud
Programm väljastab ainult 5ga jaguvad arvud 1-100

"""
for i in range(1,101):
    if i%5 == 0:
        print(i)
        
input()

"""

Arvamismäng
Kasutaja saab arvata arvuti poolt loodud arvu 3 korda.
Õnnitle kasutajat, kui arvas selle ära.
Kui mitte, siis küsi, kas ta soovib veel arvata.

"""
import random
loop = 1
voidud = 0
while loop == 1:
    print("-----ARVUTIMÄNG-----")
    suv = random.randint(1,10)
    
    for i in range(3):
        arva = int(input("paku arv 1-10: "))
        if suv == arva:
            print("Arvasid ära!")
            voidud += 1
            break
        else:
            print("Proovi veel!")
    print("-----GAME OVER-----")
    print(f"Võidud: {voidud}")
    jätka = input("Soovid jätkata? y/n: ")
    if jätka == "n":
        loop = 0

input()

"""
Pank
Kasutaja soovib panka panna raha teatud aastateks.
Panga intress on 5% summast. Leia kui palju ta summa iga aasta kasvab.
Vorminda tabel tulpades.
Näiteks: paneme panka 10000€ ja 5 aastaks
Aasta   Algsumma    Intress     Aasta lõpuks
1       10000.00    500.00      10500.00
2       10500.00    525.00      11025.00
3       11025.00    551.25      11576.25
4       11576.25    578.81      12155.06
5       12155.06    607.75      12762.82
Summa kokku: 12762.82€
Kasum: 2762.82€

"""

raha = 10000
aasta = 5
konto = raha
intress = 0.05
print("Aasta   Algsumma    Intress     Aasta lõpuks")
for i in range (aasta):
    print(f"{i+1} {konto:>14.2f} {konto*intress:9.2f} {konto + konto * intress:13.2f}")
    konto = konto + konto * intress
    


print(f"Summa kokku: {konto:.2f}€")
print(f"Kasum: {konto-raha:.2f}€")
input()

"""
Ruutude ja kuupide tabel
Programm leiab ja väljastama ruudud ja kuubid arvudele 1..10.
Vorminda tabel tulpades.
Arv Ruut Kuup
1   1    1
2   4    8
3   9    27
4   16   64
jne

"""
"""arv= 1
print("Arv Ruut Kuup")
for i in range (1,11):
    print(arv:5. arv**2)"""
