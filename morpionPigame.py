import pygame, sys
from pygame.locals import *

def check(m):
    #on verifie les colonnes
    for i in range(0,3):
        if(m[i][0]==m[i][1]==m[i][2]!=" "):
            print('GG le joueur:',m[i][0])
            return 0

    #on verifie les lignes    
    for i in range(0,3):
        if(m[0][i]==m[1][i]==m[2][i]!=" "):
            print('GG le joueur:',m[0][i])
            return 0

    #on verifie les diagonales
    if(m[0][0]==m[1][1]==m[2][2]!=" "):
        print('GG le joueur:',m[1][1])
        return 0

    if(m[0][2]==m[1][1]==m[2][0]!=" "):
        print('GG le joueur:',m[1][1])
        return 0

    #on verifie qu'il reste des cases a remplir
    for i in range(0,3):
        for j in range(0,3):
            if(m[i][j]==" "):
                return 1
    print("fin du jeu aucun gagnant")
    
    return 0
def bye():

    return 0
def popup(titre,oui,non):
    fen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption(titre)
    return 1
def modifieCase(m,x,y,j):
    if(m[y][x]==' '):
        m[y][x]=j
        return 1
    return 0

def draw(m):
    if(graphic==False):
        print("-------------")
        for i in range(0,3):
            print("|",m[i][0],"|",m[i][1],"|",m[i][2],"|")
            print("-------------")
    else:
        fen.fill((255,255,255))
        for i in range(0,3):
            for j in range(0,3):
                if(m[j][i]=="x"):
                    pygame.draw.line(fen,(0, 0, 255), (100+i*110,100+j*110),(190+i*110,190+j*110),5)
                    #pygame.draw.circle(fen, (0, 0, 255), (150+i*110, 150+j*110),50)
                elif(m[j][i]=="0"):
                    pygame.draw.circle(fen, (255, 0, 0), (150+i*110, 150+j*110),50)
        pygame.display.flip()
    return 1

graphic=False

if __name__== "__main__":
    continuer=True
    try:
        if(sys.argv[1]!= ''):
            graphic=True
    except:
        pass
    if(graphic):
            pygame.init()
            fen = pygame.display.set_mode((500, 500))
            pygame.display.set_caption("morpion")
    nihil=" "
    while(continuer):
        m =[[nihil,nihil,nihil],[nihil,nihil,nihil],[nihil,nihil,nihil]]
        draw(m)
        j='x'
        while(continuer & check(m)):
            if(graphic==False):
                while(1):
                    try:
                        case=int(input("Entrer un numéro de case entre 1 et 9:"))-1
                        break
                    except ValueError:
                        print("rentrer un nombre!!!")
                    except EOFError:
                        print("EOF interdit")
                if(not(-1<case<9)):
                    continue
                x=case%3
                y=int((case-x)/3)
                if modifieCase(m,x,y,j):
                    j='0' if j=='x' else 'x'
            else:
                for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                
                    if event.type == QUIT:     #Si un de ces événements est de type QUIT
                        continuer = False      #On arrête la boucle
                        break
                    if event.type == MOUSEBUTTONDOWN and 100<event.pos[0]<400 and 100<event.pos[1]<400:
                        x=int((event.pos[0]-100)/100)
                        y=int((event.pos[1]-100)/100)
                        if modifieCase(m,x,y,j):
                            j='0' if j=='x' else 'x'
            draw(m)
        if (graphic == False):
            continuer=bool(input("Entrez 0 pour quitter 1 autre chose pour continuer"))
        else:
            continuer=bool(input("Entrez 0 pour quitter 1 autre chose pour continuer"))
            
            
    #print(x,y)
