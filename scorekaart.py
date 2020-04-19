from spel import Spel
class ScoreKaart:
    #op een scorekaart kunnen de scores van 6 spellen genoteerd worden
    # op dit moment kunnen we de score van 1 spel bijhouden.
    
    def __init__(self,game):
        self.spellen = [Spel() for i in range(0,6)]
        self.game = game
        self.actiefspel = 0

    def __str__(self):
        # de __str__ methode geeft aan hoe een instantiatie in het geval van print() moet worden afgedrukt.
        # op dit moment wordt alleen de score van 1 spel getoond.
        output = f"U speelt op dit moment met spel {self.actiefspel} \n"
        alleSpelScores = self.spellen[0].score
        
        for spelScore in list(alleSpelScores):
            output = output + f"{spelScore} \t\t: {alleSpelScores[spelScore]} \n"
        
        return output

    def vakjeIsLeeg(self, naam, spel):
        if spel[naam]:
            return False
        else:
            return True

    def noteer_bovenhelft(self,vakje, waarde):
        spelScore = self.spellen[0].score
        i = 0
        if self.vakjeIsLeeg(vakje, spelScore):
            for dobbelsteen in self.game.tafel.veld:
                if dobbelsteen.sideUp == waarde:
                    i += 1
            spelScore[vakje] = waarde * i
        else: 
            print('Deze score is al genoteerd, mag niet nog een score noteren')
        
        self.game.reset_round()

    