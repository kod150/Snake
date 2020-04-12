

import turtle
import random
import os
import winsound
import time

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("                                                                                 🐍Yılan🐍             ")
wn.setup(width=600, height=600)
wn.tracer(0)
wn.bgcolor("black")
winsound.Beep(659, 125)
winsound.Beep(659, 125)
time.sleep(0.125)
winsound.Beep(659, 125)
time.sleep(0.167)
winsound.Beep(523, 125)
winsound.Beep(659, 125)
time.sleep(0.125)
winsound.Beep(784, 125)
time.sleep(0.375)
winsound.Beep(392, 125)
time.sleep(0.3)




kalem=turtle.Turtle()
kalem.color("white")
kalem.hideturtle()
kalem.penup()
kalem.goto(0,0)
kalem.pendown()

time.sleep(1)
kalem.clear()
kalem.penup()
kalem.goto(0,260)
kalem.pendown()


# Score
score_a = 0
#segmentler
segmentler=[]
segment = turtle.Turtle()
segment.color("blue")
segment.shape("square")
segment.shapesize(1,1)
segmentler.append(segment)
segment.penup()

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(1,1)
paddle_a.penup()
paddle_a.goto(0, 0)
#yem
yem=turtle.Turtle()
yem.color("red")
yem.shape("circle")
yem.penup()
yem.setposition(10,150)
yem.penup()
yem.shapesize(0.5,0.5)
#kalem

kalem.write("Skor:{}".format(score_a), align="center", font=("Courier", 24, "normal"))
# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#Bundan sonrası benim
def paddle_a_right():
    x = paddle_a.xcor()

    x += 20
    paddle_a.setx(x)
def paddle_a_left():
    x=paddle_a.xcor()
    x-=20
    paddle_a.setx(x)
def hile():
    kalem.clear()
    score_b =100
    kalem.write("Skor:{}".format(score_b), align="center", font=("Courier", 24, "normal"))
#def renk():
    #if paddle_a.color =="white":
    #paddle_a.color("green")
    #else:
    #paddle_a.color("white")
    






wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right,"d")
wn.onkeypress(paddle_a_left,"a")
#wn.onkeypress(hile,"j")
#wn.onkeypress(renk,"c")


a=0

while True:
    wn.update()
    wn.delay()

    if paddle_a.distance(yem)<15:
        score_a +=1
        winsound.Beep(1000,100)


        
        
        segment = turtle.Turtle()
        segment.color("blue")
        segment.shape("square")
        segment.shapesize(1,1)
        segment.penup()
        kalem.clear()

        
       
        kalem.write("Skor:{}".format(score_a), align="center", font=("Courier", 24, "normal"))
        segmentler.append(segment)
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        yem.setposition(x,y)

        

        x = random.randint(-290,290)
        y = random.randint(-290,290)
        yem.setposition(x,y)
        
        a= (len(segmentler))
        a*=20
    if (len(segmentler)) == 1:
        segment.setposition(paddle_a.xcor(), paddle_a.ycor()-a)
    else:
        segment.setposition(paddle_a.xcor(),paddle_a.ycor()-a)
        segment.setposition(segment.xcor(),segment.ycor()-a)
    if paddle_a.ycor() > 290 or paddle_a.ycor() < -290:
        print(a)
        y = paddle_a.ycor()
        y -= 20
        paddle_a.sety(y)
        kalem.clear()
        kalem.penup()
        kalem.goto(0,0)
        kalem.pendown()
        paddle_a.hideturtle()
        yem.hideturtle()
        segment.hideturtle()
        wn.clearscreen()
        wn.bgcolor("black")
        
        kalem.write("Alandan dışarı çıkamazsın", align="center", font=("Courier", 24, "normal"))
        winsound.Beep(300,100)
        winsound.Beep(600,100)
        winsound.Beep(900,100)
        winsound.Beep(1200,100)
        winsound.Beep(1500,100)
        winsound.Beep(1800,200)
        winsound.Beep(1500,100)
        winsound.Beep(1200,100)
        winsound.Beep(900,100)
        winsound.Beep(600,100)
        winsound.Beep(300,100)
        winsound.Beep(300,100)
        winsound.Beep(600,100)
        winsound.Beep(900,100)
        winsound.Beep(1200,100)
        winsound.Beep(1500,100)
        winsound.Beep(1800,200)
        winsound.Beep(1500,100)
        winsound.Beep(1200,100)
        winsound.Beep(900,100)
        winsound.Beep(600,100)
        winsound.Beep(300,100)
        winsound.Beep(200,100)
        winsound.Beep(100,100)
        winsound.Beep(50,100)
        time.sleep(0.5)
        wn.bye()
        
    if paddle_a.xcor() > 290 or paddle_a.xcor() < -290:
        print(a)
        x=paddle_a.xcor()
        x-=20
        paddle_a.setx(x)
        kalem.clear()
        kalem.penup()
        kalem.goto(0,0)
        kalem.pendown()
        
        paddle_a.hideturtle()
        yem.hideturtle()
        segment.hideturtle()
        wn.clear()
        wn.bgcolor("black")
        
        kalem.write("Alandan dışarı çıkamazsın", align="center", font=("Courier", 24, "normal"))
        winsound.Beep(300,100)
        winsound.Beep(600,100)
        winsound.Beep(900,100)
        winsound.Beep(1200,100)
        winsound.Beep(1500,100)
        winsound.Beep(1800,200)
        winsound.Beep(1500,100)
        winsound.Beep(1200,100)
        winsound.Beep(900,100)
        winsound.Beep(600,100)
        winsound.Beep(300,100)
        winsound.Beep(300,100)
        winsound.Beep(600,100)
        winsound.Beep(900,100)
        winsound.Beep(1200,100)
        winsound.Beep(1500,100)
        winsound.Beep(1800,200)
        winsound.Beep(1500,100)
        winsound.Beep(1200,100)
        winsound.Beep(900,100)
        winsound.Beep(600,100)
        winsound.Beep(300,100)
        winsound.Beep(200,100)
        winsound.Beep(100,100)
        winsound.Beep(50,100)
        time.sleep(0,5)
        wn.bye()
       
