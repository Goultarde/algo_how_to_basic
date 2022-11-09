board = [       #tableau de jeu
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

def display(board):
    print(board[0])
    print(board[1])
    print(board[2])

def win(board,player): #cette fonction permet d'identifier une victoire
    if board[0][0]==player and board[0][1]==player and board[0][2]==player: #horizontal
        return True
    elif board[1][0]==player and board[1][1]==player and board[1][2]==player: #horizontal
        return True
    elif board[2][0]==player and board[2][1]==player and board[2][2]==player: #horizontal
        return True
    elif board[0][0]==player and board[1][1]==player and board[2][2]==player:#diagonale
        return True
    elif board[0][2]==player and board[1][1]==player and board[2][0]==player:#diagonale
        return True
    elif board[0][0]==player and board[1][0]==player and board[2][0]==player: #verticale
        return True
    elif board[0][1]==player and board[1][1]==player and board[2][1]==player: #verticale
        return True
    elif board[0][2]==player and board[1][2]==player and board[2][2]==player: #verticale
        return True
    return False

def empty(board,a): #cette fonction vérifie que la case est utiliser ou non
    if a==1:
        if board[0][0]==0:
            return True
        else:
            return False
    if a==2:
        if board[0][1]==0:
            return True
        else:
            return False
    if a==3:
        if board[0][2]==0:
            return True
        else:
            return False
    if a==4:
        if board[1][0]==0:
            return True
        else:
            return False
    if a==5:
        if board[1][1]==0:
            return True
        else:
            return False
    if a==6:
        if board[1][2]==0:
            return True
        else:
            return False
    if a==7:
        if board[2][0]==0:
            return True
        else:
            return False
    if a==8:
        if board[2][1]==0:
            return True
        else:
            return False
    if a==9:
        if board[2][2]==0:
            return True
        else:
            return False

def real(a):#Cette fonction permet de vérifier que cette case existe ou non
    if 1<=a<=9:
        return True
    else:
        return False


def game(a,player):#cette fonction définir
    if a==1:
        board[0][0]=player
        display(board)
    if a==2:
        board[0][1]=player
        display(board)
    if a==3:
        board[0][2]=player
        display(board)
    if a==4:
        board[1][0]=player
        display(board)
    if a==5:
        board[1][1]=player
        display(board)
    if a==6:
        board[1][2]=player
        display(board)
    if a==7:
        board[2][0]=player
        display(board)
    if a==8:
        board[2][1]=player
        display(board)
    if a==9:
        board[2][2]=player
        display(board)
    
    
        
def partie(case,n):
    if real(case) and empty(board,case):
        game(case,n)



count=0
print([1,2,3])
print([4,5,6])
print([7,8,9])
while True:
    """
    Joueur 1
    """ 
    while True: #On verifie que le joeur entre bien une valeur entre 1 et 9 et que c'est un chiffre
        case_j1=input("joueur 1 entrée une valeur entre 1 et 9 compris : ")
        try:
            case_j1= int(case_j1)
            break
        except:
            print("Erreur : ce n' est pas un chiffre")
    case_j1=int(case_j1)#on transforme cette valeur en integer


    while not real(case_j1):#On verifie que la case existe et que la veleur entrer est un chiffre
        if case_j1==666:
            print("😈 va de retro satana  😈")
        while True:
            case_j1=input("cette case n'existe pas, entrée en une nouvelle : ")
            try:
                case_j1= int(case_j1)
                break
            except:
                print("Erreur : ce n' est pas un chiffre")
        case_j1=int(case_j1)   
    while not empty(board,case_j1): #On vérifie que la case n'est pas déja utiliser et que la valeur entrer est un chiffre
        while True:
            case_j1=input("cette case est prise, entrée en une nouvelle : ")
            try:
                case_j1= int(case_j1)
                break
            except:
                print("Erreur : ce n' est pas un chiffre")
    partie(case_j1,1)
               
    if win(board,1): #On vérifie que l'utilisateur a gagner ou non
        print("le joueur 1 à gagner")
        break
    count+=1#count permet de conter le nombre de coup pour ainsi mettre fin au jeu quand on aurant jouter 9 coup
    




    """
    Joueur 2
    """ 
    while True: #On verifie que le joeur entre bien une valeur entre 1 et 9 et que c'est un chiffre
        case_j2=input("joueur 2 entrée une valeur entre 1 et 9 compris : ")
        try:
            case_j2= int(case_j2)
            break
        except:
            print("Erreur : ce n' est pas un chiffre")
    case_j2=int(case_j2)#on transforme cette valeur en integer


    while not real(case_j2):#On verifie que la case existe et que la veleur entrer est un chiffre
        if case_j2==666:
            print("😈 va de retro satana  😈")
        while True:
            case_j2=input("cette case n'existe pas, entrée en une nouvelle : ")
            try:
                case_j2= int(case_j2)
                break
            except:
                print("Erreur : ce n' est pas un chiffre")
        case_j2=int(case_j2)   
    while not empty(board,case_j2): #On vérifie que la case n'est pas déja utiliser et que la valeur entrer est un chiffre
        while True:
            case_j2=input("cette case est prise, entrée en une nouvelle : ")
            try:
                case_j2= int(case_j2)
                break
            except:
                print("Erreur : ce n' est pas un chiffre")
    partie(case_j2,2)

    if win(board,2):
        print("le joueur 2 à gagner")
        break
    count+=1
    if count>9:
        print("egaliter !")
        break
