from spel import Spel
class ScoreKaart:
    #op een scorekaart kunnen de scores van 6 spellen genoteerd worden
    # op dit moment kunnen we de score van 1 spel bijhouden.
    
    def __init__(self,game):
        self.spellen = [Spel() for i in range(0,6)]
        self.game = game
        self.setActiefspel(0)

    def __str__(self):
        # de __str__ methode geeft aan hoe een instantiatie in het geval van print() moet worden afgedrukt.
        # op dit moment wordt alleen de score van 1 spel getoond.
        output = f"U speelt op dit moment met spel {self.getActiefspel()} \n"
        alleSpelScores = self.spellen[self.getActiefspel()].score
        totaalscore =0
        bonusscore =0
        score = 0

        #bovenhelft = self.spellen[self.getActiefSpel()].bovenhelft
        bovenhelft = {'enen', 'tweeen', 'drieen', 'vieren', 'vijven', 'zessen'}
        bovenhelftscore = 0
        for spelScore in list(bovenhelft):
            if alleSpelScores[spelScore]:
                bovenhelftscore += alleSpelScores[spelScore]

        if bovenhelftscore >= 63:
            bonusscore = 35

        for spelScore in list(alleSpelScores):
            output = output + f"{spelScore}     \t\t: {alleSpelScores[spelScore]} \n"
            if alleSpelScores[spelScore]:
                score += alleSpelScores[spelScore]
        
        output = output + f"Score           \t\t: {score}\n"
        output = output + f"Bonus           \t\t: {bonusscore}\n"
        totaalscore = score + bonusscore
        output = output + f"Totaal          \t\t: {totaalscore}\n"

        print(alleSpelScores)

        return output

    def setActiefspel(self, spelnummer):
        self.actiefspel = int(spelnummer)
    
    def getActiefspel(self):
        return(int(self.actiefspel))

    def vakjeIsLeeg(self, naam, spel):
        if spel[naam]:
            return False
        else:
            return True

    def noteer_bovenhelft(self,vakje, waarde):
        spelScore = self.spellen[self.getActiefspel()].score
        i = 0
        noProblem = True
        if self.vakjeIsLeeg(vakje, spelScore):
            for dobbelsteen in self.game.tafel.veld:
                if dobbelsteen.sideUp == waarde:
                    i += 1
            spelScore[vakje] = waarde * i
        else: 
            print('Deze score is al genoteerd, mag niet nog een score noteren')
            noProblem = False

        if noProblem:
            self.game.reset_round()
    
    def noteer_onderhelft(self, vakje):
        spelScore = self.spellen[self.getActiefspel()].score
        noProblem = True
        if vakje == 'threeofakind':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidThreeofkind = False
                
                #print("threeofakind")
                # controleer of het een valide threeofakind is 
                scoreList = [dobbelsteen.sideUp for dobbelsteen in dobbelstenen]
                hoogsteAantalvanEenSoort = max({scoreList.count(x) for x in scoreList})
                isValidThreeofkind = (hoogsteAantalvanEenSoort >= 3)
               
                totaal = 0
                             
                if isValidThreeofkind:
                    for dobbelsteen in dobbelstenen:
                        totaal += dobbelsteen.sideUp
                    spelScore[vakje] = totaal
                else:
                    print("Geen valide three-of-a-kind, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
            # totaal van de vijf stenen
        
        if vakje == 'carre':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidThreeofkind = False
                
                #print("threeofakind")
                # controleer of het een valide threeofakind is 
                scoreList = [dobbelsteen.sideUp for dobbelsteen in dobbelstenen]
                hoogsteAantalvanEenSoort = max({scoreList.count(x) for x in scoreList})
                isValidCarre = (hoogsteAantalvanEenSoort >=4)
               
                totaal = 0
                             
                if isValidCarre:
                    for dobbelsteen in dobbelstenen:
                        totaal += dobbelsteen.sideUp
                    spelScore[vakje] = totaal
                else:
                    print("Geen valide carre, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
            # totaal van de vijf stenen
        
        
        if vakje == 'fullhouse':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidFullhouse = False
                
                # controleer of het een valide threeofakind is 
                scoreList = [dobbelsteen.sideUp for dobbelsteen in dobbelstenen]
                resultSet = {scoreList.count(x) for x in scoreList}
                isValidFullhouse = (resultSet == {2,3})
               
                totaal = 0
                             
                if isValidFullhouse:
                    spelScore[vakje] = 25
                else:
                    print("Geen valide fullhouse, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
            # totaal van de vijf stenen
        
        if vakje == 'yathzee':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidYathzee = False
                
                #print("threeofakind")
                # controleer of het een valide threeofakind is 
                scoreList = [dobbelsteen.sideUp for dobbelsteen in dobbelstenen]
                hoogsteAantalvanEenSoort = max({scoreList.count(x) for x in scoreList})
                isValidYathzee = (hoogsteAantalvanEenSoort ==5)
               
                totaal = 0
                             
                if isValidYathzee:
                    spelScore[vakje] = 50
                else:
                    print("Geen valide yathzee, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
            # totaal van de vijf stenen

    
        if vakje == 'chance':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                          
                totaal = 0  
                
                for dobbelsteen in dobbelstenen:
                    totaal += dobbelsteen.sideUp
                spelScore[vakje] = totaal
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
        
        if vakje == 'kleinestraat':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidKleinestraat = False
                
                scoreList = {dobbelsteen.sideUp for dobbelsteen in dobbelstenen}
                variantA = {1,2,3,4}
                variantB = {2,3,4,5}
                variantC = {3,4,5,6}

                isValidKleinestraat = (variantA.issubset(scoreList) or variantB.issubset(scoreList) or variantC.issubset(scoreList))
               
                totaal = 0
                             
                if isValidKleinestraat:
                    spelScore[vakje] = 30
                else:
                    print("Geen valide kleinestraat, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False

        if vakje == 'grotestraat':
            if self.vakjeIsLeeg(vakje, spelScore):
                dobbelstenen = self.game.tafel.veld
                isValidGrotestraat = False
                
                scoreList = {dobbelsteen.sideUp for dobbelsteen in dobbelstenen}
                variantA = {1,2,3,4,5}
                variantB = {2,3,4,5,6}

                isValidGrotestraat = (variantA.issubset(scoreList) or variantB.issubset(scoreList))
               
                totaal = 0
                             
                if isValidGrotestraat:
                    spelScore[vakje] = 40
                else:
                    print("Geen valide grotestraat, nulscore genoteerd in het vakje.")
                    spelScore[vakje] = 0
            else: 
                print('Deze score is al genoteerd, mag niet nog een score noteren')
                noProblem = False
            

        if noProblem:
            self.game.reset_round()

    