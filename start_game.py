#!/usr/bin/python
#import dobbelsteen, beker, tafel
#onderstaande manier van importeren verdient de voorkeur
# from dobbelsteen import * (niet aan te bevelen)
from submodule.gameCommand import GameCommand
from dobbelsteen import Dobbelsteen
from beker import Beker
from tafel import Tafel
from scorekaart import ScoreKaart

class Game:
	
	def __init__(self):
		self.noStop = True
		# dit modelleer ik als een set, want geen volgorde.
		# dobbelstenen aanmaken
		self.dobbelstenen = { Dobbelsteen() for x in range(0,5) }
		# beker aanmaken en alle dobbelstenen in de beker stoppen
		self.beker = Beker()
		for dobbelsteen in self.dobbelstenen:
			self.beker.erinStoppen(dobbelsteen)
		#tafel aanmaken
		self.tafel = Tafel()
		#gameCommands
		self.gameCommand = GameCommand(self)
		self.scorekaart = ScoreKaart()
		#beurtCounter
		self.aantalWorpenOver = 3
	
	@staticmethod
	def main():
		game = Game()

		print("Welkom bij Yahtzee. Type voor hulp het commando `help'.")

		while game.noStop:
	
			userinput=input("Geef invoer (" + str(game.aantalWorpenOver) + "): ").lower()

			inputs = userinput.split()
			
			command = inputs.pop(0)
			arguments = inputs
	
			if command in game.gameCommand.commands.keys():
				game.gameCommand.executeCommand(command, arguments)
			else:
				print("Uw commando is niet herkend. Type voor hulp het commando `help'")

if __name__ == "__main__":
	Game.main()
