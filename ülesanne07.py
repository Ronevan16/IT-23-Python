#funktsioonid
#05.12.2023
#Ron Evan Krüner

def tervita(nimi, keel="de"):
    if keel == "en":
        print(f"Hi {nimi}")
    elif keel == "et":
        print(f"Tere {nimi}")
    else:
        print(f"Hallo {nimi}")

tervita("Jürid!","en")   
tervita("Jüri!","et")


"""
Koosta ruumalade leidmise programm. Kasutajalt küsitakse, millise kujundi ruumala on vaja leida ja siis vajalikke argumente. Kasutada tuleb funktsioone. Tore, kui programm ei lõpetaks kohe töö vaid lubab valida teisi ruumalasid.

"""
import math
def kuup(a,b,c):
    v = a*b*c
print("F kuubi ruumala on: {v} ")

def kera (r):
    v = round(4*math.pi*r**2,2)
    print(f"Kera ruumala on: {v}")

def koonus():
    print("koonus")

def silinder():
    print("silinder")


loop = 1
print("\n----------\nMatemaatika funktsioonid\n----------")
while loop ==1:
    print("vali kujund:\n1 Kera \n2 Kuup \n3 Koonus \n4 Silinder\n5 EXIT\n----------")
    valik  = int(input("Tee valik: "))
if valik ==1:
    r = int(input("Siesta kera raadius"))
    kera(r)
if valik==2:
    a = int(input("Lisa kuubi külg"))
    b = int(input("Lisa kuubi külg"))
    c = int(input("Lisa kuubi külg"))
    kuup (a,b,c)
elif valik==3:
    Koonus()
if valik==4:
    silinder()