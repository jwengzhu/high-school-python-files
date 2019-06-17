import turtle
from turtle import *
import time
from random import randint
import Tkinter as tk
from Tkinter import *

bg = turtle.Screen()
bg.bgcolor("greenyellow")
x = randint(1,10)
y = randint(1,10)

line = turtle.Turtle()
bob = turtle.Turtle()
ray = turtle.Turtle()
line.color('black')
bob.color('blue')
ray.color('red')
bob.shape('turtle')
ray.shape('turtle')


line.up()
line.goto(-200, 220)
line.write("Turtle Competition", font=("Arial",50,"normal"))
time.sleep(3)
line.clear()

line.goto(300,300)
line.rt(90)
line.down()
line.forward(600)

bob.up()
ray.up()
bob.goto (-300, 20)
ray.goto(-300,-20)

a = bob.xcor()
b = ray.xcor()


while a <= 300 and b <= 300:
    bob.forward(randint(1,10)) #move blue forward if it hasn't reached the line
    a = bob.xcor()

    ray.forward(randint(1,10)) #move red forward if it hasn't reached the line
    b = ray.xcor() 

while a >= -300: #setting that this loop will be repeated throughout the race
    if a > 300 and b < 300: #if blue reached the line and red not
        while b <= 300:
            ray.forward(randint(1,10))
            b = ray.xcor()
        bob.pendown()
        bob.circle(50)
        bob.circle(60)
        bob.circle(70)
        line.up()
        line.goto(-250,100)
        line.color("blue")
        line.write("Blue Wins!", font=("Arial",100,"normal"))
        break


    if b > 300 and a < 300: #if red reached line and blue not
        while a <= 300:
            bob.forward(randint(1,10))
            a = bob.xcor()
        ray.pendown()
        ray.circle(50)
        ray.circle(60)
        ray.circle(70)
        line.up()
        line.goto(-250,100)
        line.color("Red")
        line.write("Red Wins!", font=("Arial",100,"normal"))
        break

            
    if a > 300 and b > 300 and a == b:
        line.up()
        line.goto(-100,100)
        line.write("Tie!", font=("Arial", 100, "normal"))
        break


bg.exitonclick()

