from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT_DIRECTION = 0
LEFT_DIRECTION = 180
TOP_DIRECTION = 90
BOTTOM_DIRECTION = 270

class Snake:

    # reference will be saved
    def __init__(self):
        self.body_segments = []
        self.createSnake()
        self.head = self.body_segments[0]

    def createSnake(self):
        x_pos = 0
        y_pos = 0
        for i in range(3):
            self.add_segment((x_pos, y_pos))
            x_pos -= MOVE_DISTANCE

    def add_segment(self, position):
        turtle = Turtle()
        turtle.penup()
        turtle.shape("square")
        turtle.color("white")
        turtle.goto(position)
        self.body_segments.append(turtle)

    def extend(self):
        self.add_segment(self.body_segments[-1].position())

    '''
        The algorithm is to move:
        it will move from last position into the position of the index in front of it
        [3][2][1] -> [3][1] -> [3][2] -> segment[0].forward(20) -> [3][2][1]
    '''
    def move(self):
        # Can't use param keyword argument cos internally it's C implementation
        for seg_num in range(len(self.body_segments) - 1, 0, -1):
            dest = self.body_segments[seg_num - 1]
            self.body_segments[seg_num].goto(dest.xcor(), dest.ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != BOTTOM_DIRECTION:
            self.head.setheading(TOP_DIRECTION)

    def down(self):
        if self.head.heading() != TOP_DIRECTION:
            self.head.setheading(BOTTOM_DIRECTION)

    def left(self):
        if self.head.heading() != RIGHT_DIRECTION:
            self.head.setheading(LEFT_DIRECTION)

    def right(self):
        print(self.head.heading)
        if self.head.heading() != LEFT_DIRECTION:
            self.head.setheading(RIGHT_DIRECTION)

