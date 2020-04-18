from spel import Spel
class ScoreKaart:
    #op een scorekaart kunnen de scores van 6 spellen genoteerd worden
    
    def __init__(self):
        self.spellen = [Spel() for i in range(0,6)]

    def __str__(self):
        # de __str__ methode geeft aan hoe een instantiatie in het geval van print() moet worden afgedrukt.
        # op dit moment wordt alleen de score van 1 spel getoond.
        output = ""
        alleSpelScores = self.spellen[0].score
        
        for spelScore in list(alleSpelScores):
            output = output + f"{spelScore} \t\t: {alleSpelScores[spelScore]} \n"
        
        return output
