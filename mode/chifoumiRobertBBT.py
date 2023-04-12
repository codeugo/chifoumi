 #import

from msilib import sequence
from random import randrange
from tkinter import *
from os import path
import tkinter as tk

 #variables
gamenb=0
victoires=0
dico=[0]
username =""
feuille = 0
pierre = 0
ciseau = 0
spock = 0
lezard = 0
feuilleb =0
pierrexb = 0  
ciseaub = 0
spockb = 0
lezardb = 0
BOT = 0
testif= 0
pointJ = 0
pointB = 0
data = []

 #Demande Username

def afficheZoneSaisie():
    testif=0
    global entree
    global username
    username =entree.get()
    with open ("data.txt", "r") as f:  
        for li in f :
            s = li.strip ("\n\r")
            l = s.split (";")
            l[1]=int(l[1])
            l[2]=int(l[2])
            data.append (l)
    for i in data :
        if username in i :
            break
        else : 
            testif=testif+1
    if testif == len(data) :
        data.append([username,0,0])
    f.close ()
    jeu.destroy()
    return(username)

for i in data:
    if username in i :
        gamenb=i[1]
        victoires=i[2]

 #definiton des fonctions

jeu = Tk()
jeu.iconbitmap('chifoumi.ico')
cadre = Frame(jeu)
cadre.pack(padx=5, pady=5)

etiquette = Label(cadre, text='Username :')
etiquette.pack(padx=5, pady=5, side=LEFT)

entree = Entry(cadre, width=50)
entree.pack(padx=5, pady=5, side=LEFT)
entree.focus_force()

btnAffiche = Button(jeu, text='Valider', command=afficheZoneSaisie)
btnAffiche.pack(padx=5, pady=5)

jeu.mainloop()

def close_window():
    fenetre.destroy()
    global gamenb,victoires
    gamenb = gamenb + pointJ + pointB
    victoires = victoires + pointJ
    for i in data:
        if username in i :
            i[1]=gamenb
            i[2]=victoires
        f = open ("data.txt", "w")
    for i in range (0,len (data)) : 
        for j in range (0, 2) :
            f.write ( str (data [i][j]) + ";")
        f.write ( str (data [i][2]))
        f.write ("\n")
    f.close ()
def choix(element):
    global pointJ,pointB

#BOT

    BOT = randrange(1,6) # 1->feuille, 2->pierre, 3->ciseaux
    if BOT == 1 :
        feuilleb = 1
    elif BOT == 2 :
        pierrexb = 1
    elif BOT == 3:
        ciseaub = 1
    elif BOT == 4:
        sopckb = 1
    else :
        lezardb = 1

#feuille

    if element == 1 : 
         if BOT == 2 :
            chaine.configure(text ='La feuille recouvre la pierre, vous gagnez')
            pointJ += 1
         elif BOT == 4 :
            chaine.configure(text ='La feuille discrédite spock, vous gagnez')
            pointJ += 1
         elif BOT == 3:
            chaine.configure(text ='Les cisaux coupent la feuille, vous perdez')
            pointB += 1
         else :
            chaine.configure(text ='Le lezard mange la feuille, vous perdez')
            pointB += 1 

#pierre

    elif element == 2 : 
        if BOT ==1 :
            chaine.configure(text ='La feuille recouvre la pierre, Vous perdez')
            pointB += 1
        elif BOT ==4 :
            chaine.configure(text ='Spock vaporise la pierre, vous perdez')
            pointB += 1
        elif BOT == 3:
            chaine.configure(text ='La pierre émousse les cisaux, vous gagnez')
            pointJ += 1
        else : 
            chaine.configure(text ='La pierre écrase le lezard, vous gagnez')
            pointJ += 1

#ciseau

    elif element == 3 : 
        if BOT == 2 :
            chaine.configure(text ='Les cisaux coupent la feuille, vous gagnez')
            pointJ += 1
        elif BOT == 5 :
            chaine.configure(text ='les cisaux décapitent le lezard, vous gagnez')
            pointJ += 1
        elif BOT == 2:
            chaine.configure(text ='La pierre émousse les cisaux, vous perdez')
            pointB += 1
        else :
            chaine.configure(text ='Spock casse les cisaux, vous perdez')
            pointB += 1
    score.configure(text='Votre score : {0}\nScore du BOT :{1}'.format(pointJ,pointB))

#spock

    if element == 4 : 
        if BOT == 3 :
            chaine.configure(text ='Spock casse les cisaux, vous gagnez')
            pointJ += 1
        elif BOT == 2    :
            chaine.configure(text ='Spock vaporise la pierre, vous gagnez')
            pointJ += 1
        elif BOT == 1:
            chaine.configure(text ='La feuille discrédite spock, vous perdez')
            pointB += 1
        else :
            chaine.configure(text ='Le lezard empoisonne spock, vous perdez')
            pointB += 1
    score.configure(text='Votre score : {0}\nScore du BOT :{1}'.format(pointJ,pointB))

#lezard

    if element == 5 : 
        if BOT == 4 :
            chaine.configure(text ='Le lezard empoisonne spock, vous gagnez')
            pointJ += 1
        elif BOT == 1    :
            chaine.configure(text ='Le lezard mange la feuille, vous gagnez')
            pointJ += 1
        elif BOT == 2:
            chaine.configure(text ='La pierre écrase le lezard, vous perdez')
            pointB += 1
        else:
            chaine.configure(text ='Les cisaux décapitent le lezard, vous perdez')
            pointB += 1
    score.configure(text='Votre score : {0}\nScore du BOT :{1}'.format(pointJ,pointB))

#PvM
textnom = (username," Vs Bot")
pointJ,poinB=0,0
fenetre = Tk()
fenetre.iconbitmap('bot.ico')
fenetre.geometry('370x250')
fenetre.title(textnom)
texte1 = Label(fenetre, text='Pierre, Feuille, Cisaux')
texte1.pack()
bouton1 = Button(fenetre, text="Feuille", command = (lambda: choix(1)))
bouton1.pack()
bouton2 = Button(fenetre, text="Pierre", command = (lambda: choix(2)))
bouton2.pack()
bouton3 = Button(fenetre, text="Ciseau", command = (lambda: choix(3)))
bouton3.pack()
bouton4 = Button(fenetre, text="spock", command = (lambda: choix(4)))
bouton4.pack()
bouton5 = Button(fenetre, text="Lezard", command = (lambda: choix(5)))
bouton5.pack()
chaine = Label(fenetre)
chaine.pack()
score=Label(fenetre,text='Votre score : {0}\nScore du BOT :{1}'.format(pointJ,pointB))
score.pack()
button = tk.Button(text = "Cliquer pour quitter", 
                   command = close_window)
button.pack()
fenetre.mainloop()
#http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_io/files.html