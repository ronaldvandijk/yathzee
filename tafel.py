# tafel geldt als een tijdelijke opslag voor dobbelstenen.
# op de tafel hebben dobbelstenen een volgorde, namelijk de volgorde
# van links naar rechts. Vandaar dat we de dobbelstenen opslaan
# in een LIST
class Tafel:
	
	veld = []
	
	def __init__(self):
		# dit is een voorbeeld van een list comprehension
		#self.veld = [x for x in dobbelstenen]
		None
	
	def drukAf(self):
		i = 0
		if self.veld:
			tekst = "Dobbelstenen van links naar rechts op tafel: \n"
			for dobbelsteen in self.veld:
				tekst = tekst + "\t" + "Dobbelsteen " + str(i) + ", is een " + str(dobbelsteen.sideUp) + "\n"
				i = i + 1
		else:
			tekst= "Er liggen geen dobbelstenen op de tafel.\n"
		print(tekst)