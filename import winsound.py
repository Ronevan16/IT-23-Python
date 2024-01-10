import winsound
import random
def aratus(nr):
    for i in range(nr):
        winsound.Beep(2500, 200)
        print("Tõuse ja sära!")




""" jänes"""

def porgandid(r):
    joostud_ringid = 0
    porgandid = 0
    while joostud_ringid < r:
        joostud_ringid+=1
        if joostud_ringid%2==0:
            porgandid += joostud_ringid
    print(f"Jänkukene saab: {porgandid} porgandit!")


ringid = int(input("Ringide arv : "))
porgandid(ringid)



"""täringud"""

def taringud(arv):
    for i in range(arv):
        print(random.randint(1,6))


#taringud(6)




"""male"""
def male(arv):
    ruut = 1
    nisuterad = 1
    while ruut < arv:
        nisuterad = nisuterad*2
        ruut+=1
    print(nisuterad)

male(10)

"""Lumivalgekesed oli 14 õuna ja ta tahtis neid pöialpoistega jagada. Ta sai aru, et kui kõik seitse pöialpoissi tahavad õunu ja ta annaks kõigile kaks õuna, jääks ta ise üldse ilma. Nüüd otsustas ta õunu jagada nii, et küsib mitu pöialpoissi tahab õuna, ja seejärel loosib isa soovija korral, kas anda talle üks või kaks õuna. Koostada programm!"""

import random

def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad-=pounad
        print(pounad)
    print(f"Lumivalgekesele jäi {ounad} õuna")

lumivalgeke(6)    
