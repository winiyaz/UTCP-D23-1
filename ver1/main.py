import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

# Setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("pantySmeller")
screen.bgcolor("#020617")

# Initialize turtle , carmanager and scoreboard
player = Player()
car_manager = CarManager()
scoreb = Scoreboard()

# Listen for keystrokes
screen.listen()
screen.onkey(player.go_up, "Up")

# Game logic in while loop to keep running
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
		scoreb.increase_level()


# Keep Screen open
screen.exitonclick()
