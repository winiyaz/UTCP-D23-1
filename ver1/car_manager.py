import random as rp
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NEONC = ["#39FF14", "#FF00FF", "#FF0000", "#00FFFF", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#FF00FF", "#800080"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

	def __init__(self):
		self.all_cars = []
		self.car_speed = STARTING_MOVE_DISTANCE

	def create_car(self):
		random_chance = rp.randint(1, 6)
		if random_chance == 1:
			new_car = Turtle("square")
			new_car.shapesize(stretch_wid=1, stretch_len=2)
			new_car.penup()
			new_car.color(rp.choice(NEONC))
			random_y = rp.randint(-200, 200)
			new_car.goto(300, random_y)
			self.all_cars.append(new_car)

	def move_car(self):
		for car in self.all_cars:
			car.backward(self.car_speed)

	def level_up(self):
		self.car_speed += MOVE_INCREMENT
