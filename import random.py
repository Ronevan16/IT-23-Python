import random

def lumivalgeke(p):
    ounad = 14
    for i in range(p):
        pounad = random.randint(1,2)
        ounad-=pounad
        print(pounad)
    print(f"Lumivalgekesele jäi {ounad} õuna")

lumivalgeke(6)