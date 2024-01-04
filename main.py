import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

player=Player()
car=CarManager()
score=ScoreBoard()

screen.listen()
screen.onkeypress(player.move,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()
    score.level()
    #detect collision with car
    for i in range(len(car.all_cars)):

        if player.distance(car.all_cars[i]) <20:
            score.game_over()
            game_is_on=False
    '''for i in car.all_cars:
        if i.distance(player)<20:
            game_is_on = False'''
    #player crosses finish line
    if player.ycor()>=280:
        player.is_at_finish_line()
        car.move_increment+=5
        score.level_no+=1


screen.exitonclick()