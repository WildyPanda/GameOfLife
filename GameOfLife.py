import tkinter as tk
import time

fenetre = tk.Tk()
fenetre.title("Jeu de la vie")


case=[]
fini = 0
nbcase = 50
largeur = 780
hauteur = 780
canvas = tk.Canvas(fenetre,width = largeur ,height = hauteur ,bg='white')
canvas.pack(padx = 5, pady = 5)

class Case:
    couleur = 0 #0 blanc 1 noir
    puissance = 0
    def __init__(self,x0,y0,x1,y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.X = int(((self.x0 + self.x1) / 2) // ( largeur / nbcase) + 1)
        self.Y = int(((self.y0 + self.y1) / 2) // ( largeur / nbcase) + 1)
        canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1)
        canvas.addtag_overlapping(str(self.X)+str(self.Y), ((self.x0 * 2) + self.x1) / 3, ((self.y0 * 2) + self.y1) / 3, ((self.x1 * 2) + self.x0) / 3, ((self.y1 * 2) + self.y0) / 3)
    
    def changeCoul(self):
        if(self.couleur == 0):
            self.couleur = 1
            canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill = "black")
        else:
            self.couleur = 0
            canvas.create_rectangle(self.x0,self.y0,self.x1,self.y1,fill = "white")

    def getPuissance(self,Puissance):
        self.puissance = Puissance
    
    def retPuissance(self,i):
        self.puissance = 0
        HG = i - nbcase - 1
        H = i - nbcase
        HD = i - nbcase + 1
        D = i + 1
        BD = i + nbcase + 1
        B = i + nbcase
        BG = i + nbcase - 1
        G = i - 1
        if(BD >= len(case)  and B < len(case)):
            if ( case[HG].X == case[i].X - 1 and case[HG].Y == case[i].Y - 1 and case[HG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[H].X == case[i].X and case[H].Y == case[i].Y - 1 and case[H].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[HD].X == case[i].X + 1 and case[HD].Y == case[i].Y - 1 and case[HD].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[D].X == case[i].X + 1 and case[D].Y == case[i].Y and case[D].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[B].X == case[i].X and case[B].Y == case[i].Y + 1 and case[B].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[BG].X == case[i].X - 1 and case[BG].Y == case[i].Y + 1 and case[BG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        elif ( D >= len(case) ):
            if ( case[HG].X == case[i].X - 1 and case[HG].Y == case[i].Y - 1 and case[HG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[H].X == case[i].X and case[H].Y == case[i].Y - 1 and case[H].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        elif ( H >= 0 and B < len(case) ):
            if ( case[HG].X == case[i].X - 1 and case[HG].Y == case[i].Y - 1 and case[HG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[H].X == case[i].X and case[H].Y == case[i].Y - 1 and case[H].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[HD].X == case[i].X + 1 and case[HD].Y == case[i].Y - 1 and case[HD].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[D].X == case[i].X + 1 and case[D].Y == case[i].Y and case[D].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[BD].X == case[i].X + 1 and case[BD].Y == case[i].Y + 1 and case[BD].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[B].X == case[i].X and case[B].Y == case[i].Y + 1 and case[B].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[BG].X == case[i].X - 1 and case[BG].Y == case[i].Y + 1 and case[BG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        elif( H >= 0 and B >= len(case) ):
            if ( case[HG].X == case[i].X - 1 and case[HG].Y == case[i].Y - 1 and case[HG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[H].X == case[i].X and case[H].Y == case[i].Y - 1 and case[H].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[HD].X == case[i].X + 1 and case[HD].Y == case[i].Y - 1 and case[HD].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[D].X == case[i].X + 1 and case[D].Y == case[i].Y and case[D].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        elif( H < 0 and B < len(case) ):
            if ( case[D].X == case[i].X + 1 and case[D].Y == case[i].Y and case[D].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[BD].X == case[i].X + 1 and case[BD].Y == case[i].Y + 1 and case[BD].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[B].X == case[i].X and case[B].Y == case[i].Y + 1 and case[B].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[BG].X == case[i].X - 1 and case[BG].Y == case[i].Y + 1 and case[BG].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        elif( H < 0 and B >= len(case) ):
            if ( case[D].X == case[i].X + 1 and case[D].Y == case[i].Y and case[D].couleur == 1):
                self.puissance = self.puissance + 1
            if ( case[G].X == case[i].X - 1 and case[G].Y == case[i].Y and case[G].couleur == 1):
                self.puissance = self.puissance + 1
        return self.puissance


for h1 in range(1,nbcase + 1):
    for l1 in range(1,nbcase + 1):
        case.append(Case((largeur / nbcase) * (l1 - 1), (hauteur / nbcase) * (h1 - 1), (largeur / nbcase) * l1, (hauteur / nbcase) * h1))

def changeCouleurT(event):
    X = event.x // ( largeur / nbcase) + 1
    Y = event.y // ( hauteur / nbcase) + 1
    posCase = int( ( (Y - 1) * nbcase ) + X - 1 )
    case[posCase].changeCoul()

fenetre.bind_class('Canvas','<Button-1>',changeCouleurT)

def activer():
    global fini
    for i in range(len(case)):
        case[i].retPuissance(i)
    for i in range(len(case)):
        if(case[i].couleur == 0 and case[i].puissance == 3):
            case[i].changeCoul()
        elif(case[i].couleur == 1 and case[i].puissance != 2 and case[i].puissance != 3):
            case[i].changeCoul()
    if (fini == 0):
        fenetre.after(10,activer)
    else:
        fini = 0

def arreter():
    global fini
    fini = 1

boutonStart = tk.Button(fenetre, text = "commencer",command = activer)
boutonStop = tk.Button(fenetre, text = "arreter", command = arreter)
boutonStart.pack()
boutonStop.pack()

fenetre.mainloop()
