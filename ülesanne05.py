#massiivid - array
# 28.11.23
#R.Krüner

"""
Vanused
Loo vanuste loend. Leia numbrite suurim ja väikseim arv, kogusumma, keskmine

"""
vanused = [13,12,5,4,5,4,45,5,5,53,44,4,4,4,4]
print(f"suurim arv on {max(vanused)} ja väikseim arv on {min(vanused)}")
print(f"vanuste summa: {sum(vanused)}")
print(f"vanuste keskmine: {round(sum(vanused)/len(vanused),2)}")
print(vanused[0]*"*")

for vanus in vanused:
    print(vanus * "*")


























"""
Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras. Kuva eraldi viimati lisatud nimi.

"""
nimed = []

for i in range (5):
    nimi = input("Lisa nimi: ")
    nimed.append(nimi)
print("Viimati lisatud nimi:",nimed[-1])
nimed.sort()

print(nimed)


"""
Loo õpilaste nimedest loend. Programm lubab loendis olevaid nimesid muuta.
opilased = ["Juhan,"Kati","Maarja","Mario","Mati"]
"""

opilased = ["Juhan","Kati","Maarja","Mario","Mati"]
            
jrk = 1
for opilane in opilased:
    print(f"{jrk}. {opilane}")
    jrk =+1
valik = int(input("Mitmendat nime tahad muuta: "))
uusnimi = input("Lisa uus nimi: ")
del opilased[valik-1]
opilased.insert(valik-1, uusnimi) 










"""
Duplikaadid
    Tekita loend, kuhu oled lisanud meelega mõned ühesugused nimed.
    Loo kood, mis ei väljasta kordusi.
"""
opilased = ["Juhan","Kati","Mario","Mario","Mati","Mati"]
uus_opilased = []
# Käib käib kõik läbi
for opilane in opilased:
# kontrollib kas on uues loendis olemas
    if opilane in uus_opilased:
        uus_opilased.append(opilane)
print(uus_opilased)


print("")
input()












