import turtle
wn = turtle.Screen()
wn.bgcolor("black")
#Yılan
yılan = turtle.Turtle()
yılan.penup()
yılan.shape("square")
yılan.shapesize(1,1)
yılan.color("white")
yılan.speed(0)

#İleri
def yılan_ileri():
    y = yılan.ycor()
    y =+20
    yılan.sety(y)
#Hareket
    wn.listen()
    wn.onkeypress(yılan_ileri,"w")



while True:
    wn.update()
