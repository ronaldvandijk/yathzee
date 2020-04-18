import time
class GameCommand:

	#def help(*args):
	#  print("Argumenten: ", args)
 
	# commands = {
	#  "help": help
	# }	
 
	# user = "help spel"
	# def not_found(*args)
	#	print("command not found")
	# commands.get(command, not_found)(*user)

	def __init__(self, game):
		self.game = game # hierdoor beschikt gameCommands over alle instantievariabelen van het spel.
		self.commands = { 'kijk' 		: self.kijk
						, 'stop' 	 	: self.stop
						, 'help' 		: self.help
						, 'inbeker'		: self.inbeker
						, 'schud' 		: self.schud
						, 'scorekaart' 	: self.scorekaart
						, 'save'		: 'self.save'
		}
		
	def kijk(self,*args):
		self.game.tafel.drukAf()
		if self.game.beker.aantalInBeker() > 0:
			print("")
			print("In de beker zitten " + str(self.game.beker.aantalInBeker()) + " dobbelstenen." )

	def help(self,*args):

		helpLines = []
		record = False
		if args:
			argument = args[0]
		else:
			argument = "help"
		with open('help.txt') as f:
			for line in f:
				
				if line.strip() == "<begin:"+argument+">":
					record = True
				elif line.strip() == "<end:"+argument+">":
					record = False

				if record:
					helpLines.append(line)	
		# de eerste regel kan weg
		helpLines.pop(0)
		for line in helpLines:
			print(line)

	def stop(self, *args):
		print("Bedankt voor het spelen. Tot een volgende keer.")
		self.game.noStop = False

	def inbeker(self, *args):
		
		if self.game.aantalWorpenOver == 0:
			print("Je moet de score noteren.")
			return
		
		# args is een tupel. Het eerste element in het tupel is een string met dobbelsteennummers die van de tafel moeten
		# deze gaan in de beker
		# *args komt binnen als een string.
		if len(args)>0:
			argumentenString = args[0]
			indexDobbelstenenNaarBeker = [int(s) for s in argumentenString.split(',')]
		else:
			#codesmell. Dit moet beter.
			indexDobbelstenenNaarBeker = range(0,5)

		#truuk: sorteer de lijst van groot naar klein, anders geeft onderstaande pop een probleem

		for index in reversed(indexDobbelstenenNaarBeker):
		 	dobbelsteen = self.game.tafel.veld.pop(index)
		 	self.game.beker.erinStoppen(dobbelsteen)
	
	def schud(self):

		if self.game.beker.aantalInBeker()>0:
			print("Schudden", end='', flush=True)
			
			for i in range(0,6):
				print(".", end='', flush=True)
				time.sleep(0.3)

			self.game.beker.schudden()
			
			bekerInhoud = self.game.beker.legen()
			for dobbelsteen in bekerInhoud:
				self.game.tafel.veld.append(dobbelsteen)

			if bekerInhoud:
				print("en legen", end='', flush=True)

				for i in range(0,6):
					print(".", end='', flush=True)
					time.sleep(0.1)

			print()
			self.kijk()
			self.game.aantalWorpenOver -=1
		else:
			print("Er zitten geen dobbelstenen in de beker.")

	def scorekaart(self, *args):
		if len(args) != 0:
			None
		print(self.game.scorekaart)

	def executeCommand(self,command,arguments):
		self.commands[command](*arguments)
		#print("Command given:" + command)
		#eval(command)

	