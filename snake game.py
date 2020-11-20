#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 13:28:50 2020

@author: mahima
"""

import turtle as t
import time
import random

##### Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
        
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
def toggle_bonus_cereal_active():
    global bonus_cereal_activated
    global bonus_cereal_activation_time
    if bonus_cereal_activated == True:
        bonus_cereal_activated = False
    else:
        bonus_cereal_activated = True
    bonus_cereal_activation_time = int(time.time())

def toggle_bonus_cereal_showing():
    global bonus_cereal_showing
    if bonus_cereal_showing == True:
        bonus_cereal_showing = False
    else:
        bonus_cereal_showing = True
        
def toggle_poison_active():
    global poison_activated
    global poison_activation_time
    if poison_activated == True:
        poison_activated = False
    else:
        poison_activated = True
    poison_activation_time = int(time.time())

def toggle_poison_showing():
    global poison_showing
    if poison_showing == True:
        poison_showing = False
    else:
        poison_showing = True        
# Write score
def write_score(score, high_score):
    pen.goto(0, 260)
    pen.clear()
    pen.write("Score: {}    High Score: {}".format(score, high_score), align="left", font=("Courier", 24, "normal"))
        

def write_time():
    pen_time.goto(150, -260)
    pen_time.clear()
    global game_started
    global end_time

    if game_started == False:
        pen_time.write("Time: {}".format(0), align="left", font=("Courier", 16, "normal"))
    else:
        pen_time.write("Time: {}".format(game_elapsed_time), align="left", font=("Courier", 16, "normal"))
  
delay= 0.1

# Score
score = 0
high_score = 0
game_started = False
game_start_time = 0
game_elapsed_time = 0
running=True
bonus_cereal_activated = False
bonus_cereal_showing = False
bonus_cereal_spawn_time = 0
bonus_cereal_activation_time = 0
bonus_cereal_elapsed_time = 0
poison_activated = False
poison_showing = False
poison_spawn_time = 0
poison_activation_time = 0
poison_elapsed_time = 0

#Screen setup

w= t.Screen()
w.title('Snake Game')
#w.bgcolor("Chartreuse")
w.bgpic('grass.gif')
w.setup(width=600, height=600)
w.tracer(0) #turns off animation on screen

#Snake head
head= t.Turtle()
head.speed(0) #turtle animation speed
head.shape("square")
w.addshape('no face.gif')
head.shape('no face.gif')
head.color('ForestGreen')
head.penup()
head.goto(0,0)
head.direction='stop'

# Snake food
food = t.Turtle()
food.speed(0)
w.addshape('cake.gif')
food.shape('cake.gif')
#food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

# Snake bonus food
bonus = t.Turtle()
bonus.speed(0)
w.addshape('icecream.gif')
bonus.shape('icecream.gif')
bonus.color("red")
bonus.penup()
bonus.goto(1000,1000)

# Poison
poison = t.Turtle()
poison.speed(0)
w.addshape('poison.gif')
poison.shape('poison.gif')
poison.color("red")
poison.penup()
poison.goto(1000,1000)

segments= []

# Pen
pen = t.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

              
# Create pen_time
pen_time = t.Turtle()
pen_time.color("white")
pen_time.speed(0)
pen_time.penup()
pen_time.hideturtle()
write_time()

# Keyboard bindings
w.listen()
w.onkeypress(go_up, "w")
w.onkeypress(go_down, "s")
w.onkeypress(go_left, "a")
w.onkeypress(go_right, "d")
w.onkey(go_up, 'Up')
w.onkey(go_left, 'Left')
w.onkey(go_right, 'Right')
w.onkey(go_down, 'Down')

#Main game loop
while running:
    w.update()
    
    # Start time
    if head.direction == "stop":
            game_started = False
    if game_started == False and head.direction != "stop":
                game_start_time = time.time()
                game_started = True
    game_elapsed_time = int(time.time() - game_start_time)
    write_time()
            
    # Check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        x = random.randrange(-280, 280,20)
        y = random.randrange(-280, 280,20)
        #food.goto(x,y)
        bonus.goto(1000,1000)
        bonus_cereal_activated = False
        bonus_cereal_showing = False
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()
        
        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1
         
        # Increase the score
        if bonus_cereal_activated:
            score += 30
            if score > high_score:
                high_score = score
        
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    
      # Check for a collision with the food
    if head.distance(food) < 20:
        # Move the food to a random spot
        x = random.randrange(-280, 280,20)
        y = random.randrange(-280, 280,20)
        food.goto(x,y)
        
         # Add a segment
        new_segment = t.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("black")
        new_segment.penup()
        segments.append(new_segment)
        
        # Increase the score
        if bonus_cereal_activated:
            score += 30
            if score > high_score:
                high_score = score
        else:
            score += 10
            if score > high_score:
                high_score = score
        
        # Shorten the delay
        delay -= 0.001

        # Increase the score
#        score += 10

        #if score > high_score:
         #   high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 
        
    
    # Spawn bonus cereal
    if game_elapsed_time % 30 == 0 and game_started and game_elapsed_time > 1:
        toggle_bonus_cereal_showing()
        if bonus_cereal_showing is False:
            x = random.randrange(-280, 280,20)
            y = random.randrange(-280, 280,20)
            bonus.goto(x,y)        
            bonus_cereal_spawn_time = time.time()
            
    # Spawn poison
    if game_elapsed_time % 50 == 0 and game_started and game_elapsed_time > 1:
        toggle_poison_showing()
        if poison_showing is False:
            x = random.randrange(-280, 280,20)
            y = random.randrange(-280, 280,20)
            poison.goto(x,y)        
            poison_spawn_time = time.time()         
            
        
    # Check for a collision with the bonus cereal
    if head.distance(bonus) < 20:
            bonus.goto(2000, 2000)
            toggle_bonus_cereal_active()
            toggle_bonus_cereal_showing()
            score += 30
            if score > high_score:
                high_score = score
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
  
      # Check for a collision with the bonus cereal
    if head.distance(poison) < 20:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        x = random.randrange(-280, 280,20)
        y = random.randrange(-280, 280,20)
        food.goto(x,y)
        bonus.goto(1000,1000)
        bonus.goto(1000,1000)
        bonus_cereal_activated = False
        bonus_cereal_showing = False
        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the segments list
        segments.clear()
        
        # Reset the score
        score = 0
        
        # Reset the delay
        delay = 0.1
   
    
              
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
   
                     

    # Hide bonus cereal
    print(bonus_cereal_spawn_time)
    bonus_cereal_elapsed_time= int(time.time()-bonus_cereal_spawn_time)
    
    print(bonus_cereal_elapsed_time)
    
    if bonus_cereal_elapsed_time == 5:
                toggle_bonus_cereal_showing()
                bonus.goto(2000, 2000)

    if bonus_cereal_activated:
        bonus_cereal_elapsed_time = int(time.time())
        if bonus_cereal_elapsed_time >= 5:
            bonus.goto(2000,2000)
        toggle_bonus_cereal_active()
        
        
    # Hide poison
    poison_elapsed_time= int(time.time()-poison_spawn_time)
    
    print(poison_elapsed_time)
    
    if poison_elapsed_time == 5:
                toggle_poison_showing()
                poison.goto(2000, 2000)

    if poison_activated:
        poison_elapsed_time = int(time.time())
        if poison_elapsed_time >= 5:
            poison.goto(2000,2000)
        toggle_poison_active()    
    
                    
        
    move()
    
     # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear the segments list
            segments.clear()
            
             # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1
            #Reposition food at a random place
            x = random.randrange(-280, 280,20)
            y = random.randrange(-280, 280,20)
            #food.goto(x,y)
            #Bonus food should be reset
            bonus.goto(1000,1000)
           
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

         
    
    time.sleep(delay)
    
