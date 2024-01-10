# Ron Evan Krüner 14.11.2023



import turtle

w = turtle.Screen()
w.setup(500,500)
w.title("R.Krüner kujund 13")

o = turtle.Turtle()
kaugus= 100
kaugus2 = 200
nurk = 120
nurk2 = 72

def kujund2():
    for i in range(5):
        o.forward(kaugus)
        o.left(nurk)
        o.forward(kaugus2)
        o.left(nurk)
        o.forward(kaugus2)
        o.left(nurk)
        o.forward(kaugus)
        o.left(nurk2)
        

    
kujund2()

turtle.exitonclick()