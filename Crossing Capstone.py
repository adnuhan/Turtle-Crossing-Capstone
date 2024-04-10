from turtle import Turtle, Screen
import random
import time

COLORS = ["Aquamarine", "Brown", "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenrod", "DarkGray", "DarkGreen",
          "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid", "DarkRed", "DarkSeaGreen", "DarkViolet", "Gold",
          "Pink", "Purple", "Silver", "Teal", "Turquoise", "Yellow"]


class Cars:
    """ Constructs a rectangular shape and moves it backward from SOUTH to NORTH. """

    def __init__(self):
        self.all_cars = []
        self.speed = 5

    def new_car(self):
        """ Constructs a rectangular shape. """
        random_chance = random.randint(1, 6)  # Reduces the number of cars that are being made
        if random_chance == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move_car(self):
        """ Moves the rectangle backward from SOUTH to NORTH """
        for car in self.all_cars:
            car.backward(self.speed)

    def level_up(self):
        """ Speeds up the movement of the squares by 5 """
        self.speed += 5


class Player(Turtle):
    """ Creates the turtle that the player is going to move. """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("#FFFFFF")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def move_up(self):
        """ Moves the turtle 10 pixels upward EAST. """
        self.forward(10)

    def move_down(self):
        """ Moves the turtle 10 pixels downward WEST. """
        self.forward(-10)

    def rest_turtle(self):
        """ rests the position of the turtle back to the starting point when the player goes to the next level. """
        self.goto(0, -280)


class Score:
    """ Displays the current level of the player and as the player progresses to new level it increments the level to
    show their advancement. """

    def __init__(self):
        self.scoreboard = Turtle()
        self.level = 1
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.hideturtle()
        self.scoreboard.goto(-280, 250)
        self.scoreboard.write(f"Level: {self.level}", font=("courier", 24, "normal"))

    def new_level(self):
        """ Increments the level upon successful completion of the initial level. """
        self.level += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"level: {self.level}", font=("courier", 24, "normal"))


def homepage():
    """“ Implements "PLAY" and "QUIT" buttons on the interface, designed for immediate response to user clicks. ”"""

    # Main Screen Frame
    screen = Screen()
    screen.setup(600, 600)
    screen.title("Crossing Capstone")
    screen.bgcolor("#000000")
    screen.tracer(0)
    screen.listen()

    # Play Button
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("#FFFFFF")
    turtle.penup()
    turtle.goto(-45, 50)
    turtle.write("PLAY", move=False, font=("Courier", 25, "normal"))
    turtle.goto(-50, 50)
    turtle.pendown()

    for i in range(2):
        turtle.forward(90)
        turtle.left(90)
        turtle.forward(38)
        turtle.left(90)

    # Quit Button
    turtle.penup()
    turtle.goto(-44, -50)
    turtle.write("QUIT", move=False, font=("Courier", 25, "normal"))
    turtle.goto(-49, -50)
    turtle.pendown()

    for j in range(2):
        turtle.forward(88)
        turtle.left(90)
        turtle.forward(38)
        turtle.left(90)

    turtle.penup()

    def screen_click(x, y):
        """ Detects the user's mouse click and executes actions based on the pinpointed screen locations. """
        if -50 <= x <= 50 <= y <= 88:
            play()
        elif -49 <= x <= 49 and -49 <= y <= -12:
            screen.bye()

    screen.onscreenclick(screen_click)
    screen.mainloop()


def game_over():
    """ Upon the player's loss, it Implements "RESTART" and "QUIT" buttons on the interface. """

    # Main Screen Frame
    screen = Screen()
    screen.setup(600, 600)
    screen.title("Crossing Capstone")
    screen.bgcolor("#000000")
    screen.tracer(0)
    screen.listen()

    # Restart Button
    turtle = Turtle()
    turtle.hideturtle()
    turtle.color("#FFFFFF")
    turtle.penup()
    turtle.goto(-74, 50)
    turtle.write("RESTART", move=False, font=("Courier", 25, "normal"))
    turtle.goto(-79, 50)
    turtle.pendown()

    for i in range(2):
        turtle.forward(148)
        turtle.left(90)
        turtle.forward(38)
        turtle.left(90)

    # Quit Button
    turtle.penup()
    turtle.goto(-44, -50)
    turtle.write("QUIT", move=False, font=("Courier", 25, "normal"))
    turtle.goto(-49, -50)
    turtle.pendown()

    for j in range(2):
        turtle.forward(88)
        turtle.left(90)
        turtle.forward(38)
        turtle.left(90)

    turtle.penup()

    def screen_click(x, y):
        """ Detects the user's mouse click and executes actions based on the pinpointed screen locations. """
        if -50 <= x <= 50 <= y <= 88:
            play()
        elif -49 <= x <= 49 and -49 <= y <= -12:
            screen.bye()

    screen.onscreenclick(screen_click)


def play():
    """ Assembles the elements of the capstone project, which includes the turtle, scoreboard, and dynamic rectangle to
    Construct the central framework of the capstone project. """

    # Refreshes the display prior to setting up a new screen
    screen = Screen()
    screen.clear()
    screen.bgcolor("#000000")
    screen.tracer(0)

    player = Player()
    score = Score()
    car = Cars()

    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")

    performing = True

    while performing:
        time.sleep(0.1)
        screen.update()
        car.new_car()
        car.move_car()

        for cars in car.all_cars:
            if cars.distance(player) < 22:
                performing = False
                game_over()

        if player.ycor() >= 285:
            score.new_level()
            player.rest_turtle()
            car.level_up()

        if player.ycor() <= -285:
            player.rest_turtle()


homepage()
