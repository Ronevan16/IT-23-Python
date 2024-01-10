#Hindeline harjutus
# Ron Evan Krüner
# 28.11.23

"""
Hinne: Kilpkonn (IF, FOR)
- funktsioon, mis loob erineva suuruse ja asukohaga viisnurga kogu platsi ulatuses (üle ääre ei tohi minna)
- funktsioon, mis loob erineva suuruse ja asukohaga kolmnurki kogu platsi ulatuses
- funktsioon, mis kasutab eelmisi funktsioone, et luua suvaliselt viisnurki ja kolmnurki
- menüü -> küsib kasutajalt, millist kujundit soovib, küsib kogust ja kui ära joonistab, siis küsib jälle. EXIT võimalus.
"""

import turtle
import random

w = turtle.Screen()
w.setup(600,600)

def looviisnurk():
    a = random.randint(100,200)
    x = random.randint(-300,300-a)
    y = random.randint(-300-(a//2),300-(a//2))
    john = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,100))
    for i in range(5):
        john.fd(a)
        john.rt(144)
def lookolmnurk():
    a = random.randint(100,200)
    x = random.randint(-300,300-a)
    y = random.randint(-300-(a//2),300-(a//2))
    john = turtle.Turtle()
    john.hideturtle()
    john.speed("fastest")
    john.penup()
    john.goto(x,y)
    john.pendown()
    john.left(random.randint(0,360))
    for i in range(3):
        john.fd(a)
        john.rt(120)
def loosuvaline():
    suv = random.randint(1,2)
    print(suv)
    if suv ==1:
        looviisnurk()
    else:
        lookolmnurk()

        
def kuvamenyy():
    loop = 1
    while loop==1:
        valikujund = w.numinput("Kujundi valik","1; vali viisnurk \n2. vali kolmnurk \n3. vali suvaline \n4. EXIT")
        if valikujund >= 4:
            exit()
        valiKogus = int(w.numinput("Kujundi arv","vali kujundite arv: "))
        for i in range(valiKogus):
            if valikujund == 1:
                looviisnurk()
            elif valikujund == 2:
                lookolmnurk()
            elif valikujund == 3:
                loosuvaline()
            else:
                print("EXIT")
        
kuvamenyy()


turtle.exitonclick()
