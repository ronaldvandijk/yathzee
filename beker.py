#beker
#import dobbelsteen

class Beker:
	
	__maxSize = 5
	__inhoud  = set()
	
	def aantalInBeker(self):
		return len(self.__inhoud)

	def schudden(self):
		#test beker is leeg
		if len(self.__inhoud) > 0:
			for x in self.__inhoud:
				x.rolldice()
		else:
			print("De beker is leeg")
		
	def legen(self):
		result = self.__inhoud
		self.__inhoud = set()
		return result
		
	def erinStoppen(self,dobbelsteen):
		
		if len(self.__inhoud) < self.__maxSize:
			self.__inhoud.add(dobbelsteen)
		else:
			print("De beker is vol")
		
