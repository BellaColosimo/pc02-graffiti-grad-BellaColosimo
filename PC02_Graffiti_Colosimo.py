#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Bella Colosimo
September 7, 2020
'''

# 3D glasses and a triangle earring on Bezos

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

# Move turtle to start position
penup()
lt(90)
fd(120)
pendown()

# Increase pen size, draw a circle around his eye then fill red
pensize(4)
fillcolor(153,0,0)
begin_fill()
circle(30)
end_fill()

# Decrease pen size and move turtle
pensize(1)
goto(72,120)

# Increase pen size, draw a fcircle around other eye then fill blue
pensize(4)
fillcolor("blue")
begin_fill()
circle(30)
end_fill()


# Move turtle
penup()
goto(-70, 60)
pendown()

# Decrease pen size, create an unfilled triangle
pensize(2)
for _ in range(3):
    forward(10)
    right(-120)