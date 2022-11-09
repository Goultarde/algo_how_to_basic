from game import Game #on importe la classe Game
from player import Player #on importe la classe Player

#L'utilisateur choisit entre bot et humain
a=input("Joueur 1 : entrer bot ou entrer un nom pour un humain : ")
b=input("Joueur 2 : entrer bot ou entrer un nom pour un humain : ")
player_n1 = Player(a)
player_n2 = Player(b)
if a == "Aymeric":
    print("Salut Aymeric")
else:
    print("Bonjour et bienvenue joueur")

#On définit les parametres de la class game via les joeurs sélectioné
game_class = Game(player_n1,player_n2)

#On lance le jeu
while True:
    #On définit le gagnant si le nombre de 3 manche est atteint
    if game_class.score_1==3: 
        print (" joueur 1 à gagner la partie") 
        break
    elif game_class.score_2==3:
        print ("Joueur 2 à gagner la partie")
        if a=="Aymeric" and b =="bot" :
            print("...Perdre contre un bot, la honte Aymeric")
        break
    else:
    #Dans le cas contraire le jeu continue
        game_class.choice_player()
