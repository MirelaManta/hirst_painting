#import colorgram
import random
import turtle
# Extracting the colors from the painting and saving them in a color list

# rgb_colors = []
# colors = colorgram.extract("dots_painting.jpg", 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

color_list = [(43, 2, 176), (79, 253, 174), (226, 149, 109), (230, 225, 253), (160, 3, 82), (4, 211, 101), (3, 138, 64),
              (246, 42, 127), (109, 108, 247), (252, 253, 53), (184, 184, 251), (211, 106, 5), (35, 35, 252),
              (177, 112, 248), (139, 1, 0), (252, 36, 35), (50, 240, 56), (216, 114, 171), (16, 127, 144),
              (85, 248, 252), (188, 39, 109), (23, 5, 107), (8, 209, 215), (99, 8, 50), (231, 163, 205), (204, 119, 35),
              (112, 6, 4)]
petri = t.Turtle()
t.colormode(255)
petri.speed("fastest")
petri.penup()
petri.hideturtle()

petri.setheading(225)
petri.forward(300)
petri.setheading(0)
numbers_of_dots = 100

for dot_counts in range(1, numbers_of_dots + 1):
    petri.dot(20, random.choice(color_list))
    petri.forward(50)
    if dot_counts % 10 == 0:
        petri.setheading(90)
        petri.forward(50)
        petri.setheading(180)
        petri.forward(500)
        petri.setheading(0)

screen = t.Screen()
screen.exitonclick()