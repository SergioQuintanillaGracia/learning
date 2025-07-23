import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FPS = 165

screen = Screen()
screen.setup(width=600, height=600, startx=900, starty=250)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    frametime = 1/FPS

    car_manager.update(frametime)

    screen.update()

    if car_manager.position_collides_with_car(player.position()):
        game_is_on = False
        scoreboard.game_over()

    if player.is_on_finish_line():
        player.reset_pos()
        scoreboard.increase_score(1)
        car_manager.increase_difficulty()

    time.sleep(frametime)

screen.exitonclick()