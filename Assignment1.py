from turtle import *
import random

speed(0)
side_length = 10
angle = 120
spiral_turns = 60  #

for i in range(spiral_turns):
    pencolor(random.random(),random.random(),random.random())
    for _ in range(3):
        forward(side_length)
        left(angle)
    left(10)
    side_length += 5
done()



