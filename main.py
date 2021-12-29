import random
import colorgram
import turtle
from turtle import Screen, Turtle

turtle.colormode(255)

# def rand_color():
#     r=random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

timmy = Turtle()
timmy.shape("classic")
direction = [0, 90, 180, 270]

counter = 0
timmy.speed(0)

# # random walk
# for i in range(800):
#     timmy.pencolor(rand_color())
#     timmy.fd(25)
#     timmy.setheading(random.choice(direction))


# # spirograpgh
# for _ in range(36):
#     timmy.circle(100, None, 12)
#     timmy.right(10)
#     timmy.pencolor(rand_color())



# Extract 6 colors from an image.
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb=(r, g, b)
#     rgb_colors.append(new_rgb)
#
# print(rgb_colors)

color_list=[
    (230, 207, 91), (225, 149, 91), (122, 167, 187), (35, 110, 158), (163, 13, 22), (127, 177, 145),
    (233, 81, 49), (202, 67, 27), (192, 186, 23), (174, 18, 13), (33, 129, 49), (7, 99, 37), (13, 64, 39),
    (12, 41, 76), (242, 203, 4), (139, 79, 92), (88, 13, 20), (53, 166, 76), (51, 23, 19), (180, 134, 146),
    (6, 64, 137), (213, 68, 75), (230, 170, 161), (49, 151, 191), (77, 133, 186), (175, 204, 176)
]
timmy.penup()
timmy.hideturtle()
x=-200
for i in range(10):
    timmy.setx(-200)
    timmy.sety(x)
    x += 50
    for j in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.fd(50)


screen = Screen()
screen.exitonclick()