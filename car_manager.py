from turtle import Turtle
import random

COLORS=["red","orange","blue","green","violet","yellow","purple"]

MOVE_SPEED=10

class CarManager:
    def __init__(self):
        self.all_cars=[]
        self.move_increment=MOVE_SPEED
    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            d=Turtle(shape="square")
            d.color(random.choice(COLORS))
            d.shapesize(stretch_wid=1, stretch_len=2)
            d.penup()
            random_y=random.randint(-250,250)
            d.goto(300,random_y)
            self.all_cars.append(d)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.move_increment)









