import turtle
t = turtle.Turtle()


def draw_line(x0, y0, x1, y1):
    t.penup()
    t.goto(x0, y0)
    t.pendown()
    t.goto(x1, y1)


def draw_rectangle(x0, y0, len, hgt, clr):
    t.fillcolor(clr)
    t.begin_fill()
    draw_line(x0, y0, x0+len, y0)
    draw_line(x0+len, y0, x0+len, y0+hgt)
    draw_line(x0+len, y0+hgt, x0, y0+hgt)
    draw_line(x0, y0+hgt, x0, y0)
    t.end_fill()


x_val = -200
y_val = 0


# 1. Setup the canvas screen
screen = turtle.Screen()
screen.bgcolor("#E0F0FF")  # Sky blue background
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen.tracer(0)  # Renders instantly

PIXEL_SIZE = 20

# 2. Easy helper function to draw a line of pixel blocks


def draw_row(x, y, count, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):  # Draws a long rectangle to save code lines
        t.forward(count * PIXEL_SIZE)
        t.right(90)
        t.forward(PIXEL_SIZE)
        t.right(90)
    t.end_fill()


# 3. Simple list of coordinates: [X, Y, Number of blocks, Color]
fruit_basket_pixels = [

    [-40, 60, 2, "green"],    # Apple leaves
    [-60, 40, 4, "red"],      # Apple top row
    [-60, 20, 4, "red"],      # Apple middle row
    [40, 40, 2, "purple"],    # Grapes top row
    [20, 20, 4, "purple"],    # Grapes middle row
    [40, 0, 2, "purple"],     # Grapes bottom row
    [-20, 20, 3, "orange"],   # Orange row
    [-100, 40, 1, "yellow"],  # Banana tip
    [-120, 20, 3, "yellow"],  # Banana body

    # --- THE BASKET ---
    [-140, 0, 15, "black"],
    [-120, -20, 13, "#8B5A2B"],
    [-100, -40, 11, "#8B5A2B"],
    [-80, -60, 9, "#8B5A2B"],
    [-60, -80, 7, "black"]
]

# 4. Loop through the list and paint everything
for block in fruit_basket_pixels:
    draw_row(block[0], block[1], block[2], block[3])

screen.update()
turtle.done()


turtle.mainloop()
