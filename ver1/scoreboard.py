from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.level = 1
		self.hideturtle()
		self.penup()
		self.goto(-280, 250)
		self.color("white")
		self.up_sc()

	def up_sc(self):
		self.clear()
		self.write(f'Level: {self.level}', align="left", font=FONT)

	def increase_level(self):
		self.level += 1
		self.up_sc()

	def ga_ov(self):
		self.goto(0,0)
		self.write(f'FUCKED', align="center", font=FONT)
