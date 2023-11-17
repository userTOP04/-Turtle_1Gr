import turtle
from random import randint

turtle.colormode(255)
turtle.speed(0)

def drow_house(
    x=0,
    y=0,
    base_w=100,
    base_h=10,
    color_b="grey",
    walls_w=100,
    walls_h=80,
    color_w="yellow",
    roof_w=150,
    roof_h=70,
    color_r="red"
):


    print(x, "левый нижний угол")
    print(y,"левый нижний угол")
    print(base_w, "ширина фунд")
    print(base_h, "высота фунд")
    print(color_b, "цвет фунд")
    print(walls_w, "ширина стен")
    print(walls_h, "высота стен")
    print(color_w, "цвет стен")
    print(roof_w, "ширина крыши")
    print(roof_h, "высота крыши")
    print(color_r, "цвет крыши")
    drow_base(x, y, base_w, base_h, color_b)
    walls_y = y + base_h
    drow_walls(x, walls_y, walls_w, walls_h, color_w)
    roof_y = walls_y + walls_h
    drow_roof(x, roof_y, roof_w, roof_h, color_r, walls_w)




def drow_base(x, y, base_w, base_h, color_b):
    drow_rect(x, y, base_w, base_h, color_b)



def drow_rect(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.end_fill()




def drow_walls(x, walls_y, walls_w, walls_h, color_w):
    drow_rect(x, walls_y, walls_w, walls_h, color_w)

def drow_door()


def drow_roof(x, y, roof_w, roof_h, color, walls_w):
    top_x = x + walls_w // 2
    top_y = y + roof_h
    top_rw = roof_w // 2
    turtle.goto(x, y)
    turtle.fd(walls_w // 2)
    turtle.fd(roof_w // 2)
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.goto(top_x, top_y)
    left_x = top_x - top_rw
    turtle.goto(left_x, y)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_street(first_house_x=0, first_house_y=0, houses=10):
    counter = 0 
    while counter < houses:
        base_w = randint(50, 100)
        walls_w = randint(base_w - 50, base_w)
        roof_w = randint(walls_w, walls_w + 50)
        drow_house(
            x=first_house_x,
            y=first_house_y,
            base_w=randint(50, 150),
            base_h=randint(10, 40),
            color_b=(randint(0, 255), randint(0, 255), randint(0, 255)),
            walls_w=randint(50, 150),
            walls_h=randint(50, 150),
            color_w=(randint(0, 255), randint(0, 255), randint(0, 255)),
            roof_w=randint(50, 150),
            roof_h=randint(10, 40),
            color_r=(randint(0, 255), randint(0, 255), randint(0, 255))
        )
        counter += 1
        first_house_x += roof_w + base_w


draw_street(-300, 0, 5)

turtle.done()