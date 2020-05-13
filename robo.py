import math

class Robo:
	def __init__(self,x ,y):
		self.x=x
		self.y=y

	def move_up(self,axis):
		self.y+= axis

	def move_down(self,axis):
		self.y -= axis

	def move_right(self,axis):
		self.x+= axis

	def move_left(self,axis):
		self.x -= axis

	def get_position(self):
		print(self.x,self.y)
	
	def hypotenuse(self):
		print('distance traveled: ', math.hypot(self.x,self.y))
		print('close approximate distance is: ',round(math.hypot(self.x,self.y)))

		
p1 = Robo(0,0)
p1.get_position()

a = eval(input('UP '))
p1.move_up(a)

b = eval(input('DOWN '))
p1.move_down(b)

c = eval(input('RIGHT '))
p1.move_right(c)

d = eval(input('LEFT '))
p1.move_left(d)

p1.get_position()

p1.hypotenuse()










