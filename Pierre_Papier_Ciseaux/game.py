class Game:
    def __init__(self,player_1,player_2):
        self.player_1=player_1
        self.player_2=player_2
        self.score_1, self.score_2,self.nb_partie=0,0,0
    def regles(self,choix1,choix2): #On définit les règles du jeu
        if choix1=="pierre" and choix2=="ciseaux":
            self.score_1+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        elif choix1=="papier" and choix2=="pierre":
            self.score_1+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        elif choix1=="ciseaux" and choix2=="papier":
            self.score_1+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        if choix2=="pierre" and choix1=="ciseaux":
            self.score_2+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        elif choix2=="papier" and choix1=="pierre":
            self.score_2+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        elif choix2=="ciseaux" and choix1=="papier":
            self.score_2+=1
            return(f"score joeur 1 : {self.score_1} \nscore joeur 2 : {self.score_2}")
        if choix2=="pierre" and choix1=="pierre":
            return("egaliter")
        elif choix2=="papier" and choix1=="papier":
            return("egaliter")
        elif choix2=="ciseaux" and choix1=="ciseaux":
            self.score_2+=1
            return("egaliter")

    def choice_player(self): #Permet d'afficher le gagnant de la manche
        choice_1=self.player_1.choice()
        choice_2=self.player_2.choice()
        issue = self.regles(choice_1, choice_2)
        print(f"{choice_1} vs {choice_2}")
        print (issue)
