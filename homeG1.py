import turtle


def drow_house(
    x=0,
    y=0,
    base_w=100,
    base_h=10,
    color_b="grey",
    walls_w=100,
    walls_h=100,
    color_w="yellow",
    roof_w=100,
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
    turtle.goto(x, y)
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


def drow_roof(x, roof_y, roof_w, roof_h, color, walls_w):
    turtle.goto(x, roof_y)
    turtle.fillcolor(color)
    turtle.begin_fill()
    top_x = walls_w // 2
    top_y = roof_y + roof_h
    turtle.goto(top_x, top_y)
    right_x = x + walls_w
    turtle.goto(right_x, roof_y)
    turtle.goto(x, roof_y)
    turtle.end_fill()



drow_house()


turtle.done()