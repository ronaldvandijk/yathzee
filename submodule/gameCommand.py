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
						, 'noteer'		: self.noteer
						, 'speel'		: self.speel
						, 'save'		: 'self.save'
		}
		
	def kijk(self,*args):
		if len(args)!=0:
			if args[0] == 'scorekaart':
				print(self.game.scorekaart)
		else:
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
		i=0
		for line in helpLines:
			print(line)
			i+=1
			# na 10 afgedrukte regels vragen we de gebruiker om verder te gaan.
			if i%10==0:
				input("Druk op 'enter' om verder te gaan")
				continue

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

	def speel(self, *args):
		if len(args)!=0:
			self.game.scorekaart.actiefspel = args[0]

		actiefspel = self.game.scorekaart.actiefspel
		print(f"U speelt nu met spel {actiefspel}. ")

	def schud(self):

		if self.game.beker.aantalInBeker()==0:
			# stop alle dobbelstenen in de beker
			self.inbeker()
		
		if self.game.beker.aantalInBeker()>0:
			print("Schudden", end='', flush=True)
			
			for i in range(0,6):
				print(".", end='', flush=True)
				time.sleep(0.2)

			self.game.beker.schudden()
			
			bekerInhoud = self.game.beker.legen()
			for dobbelsteen in bekerInhoud:
				self.game.tafel.veld.append(dobbelsteen)

			if bekerInhoud:
				print("en legen", end='', flush=True)

				for i in range(0,6):
					print(".", end='', flush=True)
					time.sleep(0.05)

			print()
			self.kijk()
			self.game.aantalWorpenOver -=1
		else:
			print("Er zitten geen dobbelstenen in de beker.")
		

	def noteer(self, *args):
		if len(args)!=0 and args[0] in self.game.scorekaart.spellen[0].score:


			if len(self.game.tafel.veld) == 0:
				print("Er liggen geen dobbelstenen op de tafel. Schud en leeg de beker.")
				return
			if self.game.beker.aantalInBeker() != 0:
				print("Er zitten nog dobbelstenen in de beker. Schud en leeg de bekerstop")
				return
			
			# noteer de enen die op tafel liggen, maar alleen als er nog geen score is.
			if args[0] == 'enen':
				self.game.scorekaart.noteer_bovenhelft('enen', 1)
				return
			if args[0] == 'tweeen':
				self.game.scorekaart.noteer_bovenhelft('tweeen', 2)
				return
			if args[0] == 'drieen':
				self.game.scorekaart.noteer_bovenhelft('drieen', 3)
				return
			if args[0] == 'vieren':
				self.game.scorekaart.noteer_bovenhelft('vieren', 4)
				return
			if args[0] == 'vijven':
				self.game.scorekaart.noteer_bovenhelft('vijven', 5)
				return
			if args[0] == 'zessen':
				self.game.scorekaart.noteer_bovenhelft('zessen', 6)
				return
			
			#print("Noteer score op onderstehelft")
			self.game.scorekaart.noteer_onderhelft(args[0])
			return
		else:
			print("Noteer wat?")

	def executeCommand(self,command,arguments):
		self.commands[command](*arguments)
		#print("Command given:" + command)
		#eval(command)

	