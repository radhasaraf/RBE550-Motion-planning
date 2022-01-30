import turtle


def have_turtle_draw_star():
    for _ in range(4):
        turtle.forward(200)
        turtle.right(144)
    turtle.forward(200)


if __name__ == '__main__':
    have_turtle_draw_star()
