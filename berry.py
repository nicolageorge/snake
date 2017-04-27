import random

class BerryFactory(object):
	def __init__(self):
		pass

	@classmethod
	def spawn_random_berry(self):
		types = ['normal', 'mushroom', 'death']
		b_type = types[random.randint(0,2)]
		print b_type
		return Berry(b_type)


class Berry:
	def __init__(self, type):
		self.size = [10, 10]
		self.size_window = [800,600]
		self.type = type
		
		if self.type == 'normal':
			self.color = (0, 255, 0)
			
		if self.type == "mushroom":
			self.color = (0, 0, 255)

		if self.type == "death":
			self.color = (255, 0, 0)

		self.reset_position()


	def get_new_position(self):
		x = random.randint(0, self.size_window[0]/10)
		y = random.randint(0, self.size_window[1]/10)
		return [x*self.size[0],y*self.size[0]]


	def reset_position(self):
		self.position = self.get_new_position()


	def reset_to_normal(self):
		self.type = "normal"
		self.color = (0, 255, 0)