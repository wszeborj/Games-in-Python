'''
Created on 13 lut 2020

@author: Boniass
'''

import turtle
import time
import random

delay = 0.1

#score
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by Wszebor")
wn.bgcolor("green")
wn.setup(width = 600, height = 600)
wn.tracer(0) #turn off the screen updates

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

#snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align = "center", font = ("Courier", 24, "normal"))

# functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_right():
    if head.direction != "left":
        head.direction = "right"
def go_left():
    if head.direction != "right":
        head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

#keyboards bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left,"a")

#main game loop
while True:
    wn.update()

# check for a collision with the border
    if (head.xcor() >= 290) or (head.xcor() <= -290) or (head.ycor() >= 290) or (head.ycor() <= -290):
        head.direction = "stop"
        time.sleep(1)
        head.goto(0, 0)
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

    for segment in segments:
        if head.distance(segment) < 20:
            head.direction = "stop"
            time.sleep(1)
            head.goto(0, 0)
            for segment1 in segments:
                segment1.goto(1000, 1000)
            segments.clear()
            #reset the score
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

#check for collision with the food
    if head.distance(food) < 20:
        #move the food to random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)
#add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

#increase score
        score = score + 10
        
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))
#move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

#move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    
    time.sleep(delay)

wn.mainloop()