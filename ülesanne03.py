# Ron Evan Krüner
#21.11.2023
#Ülesanne 3

"""

Korralik nimi
Küsi kasutajalt nime
Tervita teda ja sinu programm väljastab nime kirjapildi õigesti – suure algustähega ja eemaldab ülearused tühikud
Näiteks: sisend–>mARiO; väljund–>Tere, Mario!

"""
ask = input("Sisesta nimi: ")
vanus = 28



print(f"Tere {ask.strip().capitalize()}!")


"""

Vandumine
Kui kasutaja sisestab “kogemata” teksti, kus leidub sõna ‘kurat’, siis sinu programm asendab need tärnidega.
Näiteks: sisend–>Kurat küll!; väljund–>*** küll!

"""


ask = input("Sisesta nimi: ")
print(f"{ask.replace('kurat','***')}!")

"""
Email
Küsi kasutajalt emaili ja kontrolli, kas see sisaldas @-märki.
Näiteks: sisend–>minu@mail.ee; väljund–> True või False

"""
ask = input("Sisesta nimi: ")
print("@" in ask)



"""

Tundide ajad
Kasutaja sisestab tundide alguse ja lõpu. Näiteks 8:30 ja 14:15
Sinu programm leiab, kui pikk oli õpilase päev
Väljasta täislause ja kasuta vormindamisel format() meetodit.

"""

algus = input("sisesta tundide algus: ")
lopp = input("sisesta tundide lõpp: ")

hh1,mm1 =algus.split(":")
hh2,mm2 =lopp.split(":")

algus_minutid = int(hh1) * 60 + int(mm1)
lopu_minutid = int(hh2) * 60 + int(mm2)

ajavahe = lopu_minutid - algus_minutid

tunnid = ajavahe // 60
minutid = ajavahe % 60

print(f"{tunnid}:{minutid}")

"""
Palindroom
Mis on palindroom?
Sinu programm peab kontrollima, kas minu sisestatud tekst on palindroom või mitte.
Leia abi Pythoni dokumentatsioonist

"""
tekst = input("Sisesta tekst: ")
print(tekst == tekst [:: -1])

























