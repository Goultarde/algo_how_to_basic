import random
class Player :
    def __init__(self,name):
        self.name = name

    def ia(self): #Permet au bot de choisir une option entre pierre, papier et ciseaux
        choix = random.choice(["pierre","papier","ciseaux"])
        print(choix)
        return (choix)
        

    def choice(self): #Permet de définir si le joueur est un bot ou si c'est un humain
        if self.name =="bot": #c'est un bot
            choice = self.ia()
        else:#c'est un humain
            choice = input("Choisissez entre pierre, papier et ciseaux : ")
            while choice not in ["pierre","papier","ciseaux"]:#Vérifie que le coup est valide
                choice=input("ce choix n'existe pas, Choisissez entre pierre, papier et ciseaux : ")
        return(choice)

