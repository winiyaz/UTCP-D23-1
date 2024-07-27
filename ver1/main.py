import time
from turtle import Screen

from car_manager import CarManager
from player import Player

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("pantySmeller")
screen.bgcolor("#020617")

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
	time.sleep(0.1)
	screen.update()

	car_manager.create_car()
	car_manager.move_car()

	# Detect Colliision
	for c in car_manager.all_cars:
		if c.distance(player) < 20:
			game_is_on = False

	# Detect successful crossing
	if player.is_at_fin():
		player.go_ts()
		car_manager.level_up()


# Keep Screen open
screen.exitonclick()
