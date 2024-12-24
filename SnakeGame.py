import turtle as trtl, time, random
delay, score, high_score = 0.1, 0, 0
wn = trtl.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(False)
def up():
    global direction
    if direction != "down":
        direction = "up"
def down():
    global direction
    if direction != "up":
        direction = "down"
def left():
    global direction
    if direction != "right":
        direction = "left"
def right():
    global direction
    if direction != "left":
        direction = "right"
def move():
    if direction == "up":
        head.sety(head.ycor() + 20)
    elif direction == "down":
        head.sety(head.ycor() - 20)
    elif direction == "left":
        head.setx(head.xcor() - 20)
    elif direction == "right":
        head.setx(head.xcor() + 20)
wn.listen()
wn.onkeypress(up, "w")
wn.onkeypress(down, "s")
wn.onkeypress(left, "a")
wn.onkeypress(right, "d")
def game(snakeColor, point):
    global direction, delay, score, high_score, segments
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        direction = "stop"
        for segment in segments:
            segment.hideturtle()
        segments.clear()
        score, delay = 0, 0.1
        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                   font=("Courier", 24, "normal"))
    if head.distance(food) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        new_segment = create_snake("square", snakeColor, 0, 0)
        segments.append(new_segment)
        score += point
        if score > high_score:
            high_score = score
        text.clear()
        text.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                   font=("Courier", 24, "normal"))
        delay -= 0.005
    for index in range(len(segments) - 1, 0, -1):
        x,y = segments[index - 1].pos()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x, y = head.pos()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score, delay = 0, 0.05
            text.clear()
            text.write("Score: {}  High Score: {}".format(score, high_score), align="center",
                       font=("Courier", 24, "normal"))
    time.sleep(delay)
def create_snake(shape, color, x, y):
    t = trtl.Turtle()
    t.penup()
    t.shape(shape)
    t.color(color)
    t.goto(x, y)
    return t
head = create_snake("square", (headColor := input("What color do you want the snake head to be? \n>  ").lower().strip()), 0, 0)
food = create_snake("circle", (foodColor := input("What color do you want the food to be? \n> ").lower().strip()), 0, 100)
text = create_snake("square", "white", 0, 260)
snakeColor = input("What color do you want the snake body to be? \n> ").lower().strip();point = int(input("How many points do you want per apple? \n> ").lower().strip())
text.hideturtle()
direction, segments= "stop", []
text.write("Score: 0  High Score: 0", align="center", font=("Comic Sans", 24, "normal"))
while True:
    game(snakeColor, point)