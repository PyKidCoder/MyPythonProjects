import turtle
import time
import random





t = turtle.Turtle()

t.shape('circle')
t.color("black")
for i in range (1):
	t.color("brown")
	t.penup()
	def border():
		t.goto(-300,-250)
		t.pendown()
		t.goto(-300,250)
		t.goto(300,250)
		t.goto(300,-250)
		t.goto(-300,-250)
		t.penup()
		t.goto(0,0)
	border()



n_foods = 10
list_of_foods = []

for kk in range(n_foods):
    food = turtle.Turtle()
    print(food)
    food.penup()
    food.speed(0)
    food.shape("square")
    food.color("blue")
    food.goto(random.randint(-200, 200), random.randint(-200, 200))
    list_of_foods.append(food)

pen = turtle.Turtle()
pen.penup()
pen.goto(180, 180)
pen.color("white")
pen.ht()

report = turtle.Turtle()
report.penup()
report.goto(0, 0)
report.color("white")
report.ht()

started = 0

t.forward(20)
def right():
    if t.heading() != 180.0:
        t.setheading(0.0)


def left():
    if t.heading() != 0.0:
        t.setheading(180.0)


def up():
    if t.heading() != 270.0:
        t.setheading(90.0)


def down():
    if t.heading() != 90.0:
        t.setheading(-90.0)

steps = 0





ts = t.screen
ts.bgcolor("khaki")

ts.onkey(right, "Right")
ts.onkey(left, "Left")
ts.onkey(up, "Up")
ts.onkey(down, "Down")
ts.listen()

caught = [False] * n_foods

segments = []

game_over = False

while game_over == False:
	steps = steps + 1
	pen.write(len(segments), align="center", font=("Courier", 24, "normal"))
    
	for kk in range(len(list_of_foods)):
		if not caught[kk]:			
			if t.distance(list_of_foods[kk]) < 20:
				caught[kk] = True
				list_of_foods[kk].color('green')
				segments.append(list_of_foods[kk])
				pen.clear()

   
	for index in range(len(segments) - 1, 0, -1):
		x = segments[index - 1].xcor()
		y = segments[index - 1].ycor()
		segments[index].goto(x, y)

    

	if len(segments) > 0:
		x = t.xcor()
		y = t.ycor()
		segments[0].st()
		segments[0].goto(x, y)
	
	t.forward(20)
    
	
	if t.xcor() > 10:
		started = 1
	if len(segments) == n_foods:
		if abs(t.xcor()) < 20 and abs(t.ycor()) < 20:
			game_over = True
			time.sleep(1)
			t.clear()
			t.ht()
			for kk in range(len(segments)):
				segments[kk].ht()
				
			report.write("Steps Taken: " + str(steps),align="center",font=("Courier", 24, "normal"))
	


	if t.xcor() > 280 and t.heading() == 0:
		t.setheading(180)
	elif t.xcor() < -280 and t.heading() == 180:
		t.setheading(0)
	elif t.ycor() < -230 and t.heading() == 270:
		t.setheading(90)
	elif t.ycor() > 230 and t.heading() == 90:
		t.setheading(270)