import turtle



def drow_house(
    x=0,
    y=0,
    bass_w=100,
    bass_h=10,
    color_b="black",
    walls_w=250,
    walls_h=250,
    color_w="red",
    roof_w=300,
    roof_h=100,
    color_r="green"
):

    print(x, "левый нижний угол")
    print(y,"левый нижний угол")
    print(bass_w, "ширина фунд")
    print(bass_h, "высота фунд")
    print(color_b, "цвет фунд")
    print(walls_w, "ширина стен")
    print(walls_h, "высота стен")
    print(color_w, "цвет стен")
    print(roof_w, "ширина крыши")
    print(roof_h, "высота крыши")
    print(color_r, "цвет крыши")
    drow_base(x, y, bass_w, bass_h, color_b)
    drow_walls()
    drow_roof()




def drow_base(x, y, bass_w, bass_h, color_b):
    drow_rect(x, y, bass_w, bass_h, color_b)




def drow_rect(x,y, width, height, color_b):
    turtle.fd(width)
    turtle.begin_fill()
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.fd(width)
    turtle.left(90)
    turtle.fd(height)
    turtle.left(90)
    turtle.end_fill()




def drow_walls():
    pass


def drow_roof():
    pass



drow_house(color_b="blue")


turtle.done()