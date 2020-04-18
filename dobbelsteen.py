import random

class Dobbelsteen:
	sides = (1,2,3,4,5,6)
	sideUp = 0
	
	def __init__(self):
		self.rolldice()
	
	def rolldice(self):
		self.sideUp = random.choice(self.sides)
		#print(f"Side up is: {	self.sideup}")
		
	def setSideUp(self,num):
		if num in self.sides:
			self.sideUp = num
		else:
			print("Not admissible {num}")
