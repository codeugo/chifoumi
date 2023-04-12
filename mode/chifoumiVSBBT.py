#Import
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from mode.library import chifoumiLibraryUsername, chifoumiLibraryResult

#Variables
gamenb = 0
gamenb2 = 0
pointP1 = 0
pointP2 = 0
data = []
choiceMade = 0
usernameNotFound = True
username2NotFound = True
playcounter = 0

#Fonctions
def Quit():
    resultwinnerGUI.destroy()
    global pointP1, pointP2
    global gamenb,gamenb2
    print('pointP1:', pointP1)
    print('pointP1:', pointP2)
    gamenumberTotal = pointP1 + pointP2
    chifoumiLibraryUsername.dataVSWrite(gamenumberTotal, pointP1, pointP2)
    pointP1 = 0
    pointP2 = 0

def changeText():
    if(texte2['text']=='Au tour du joueur 1 :'):
        texte2['text']='Au tour du joueur 2 :'
        texte2['fg']='#FF6600'
    else:
        texte2['text']='Au tour du joueur 1 :'
        texte2['fg']='#99EE99'

def resultChoice(element):
    global playcounter, elementP1, elementP2, pointP2, pointP1
    if(texte2['text']=='Au tour du joueur 1 :'):
        elementP1 = element
        playcounter = playcounter + 1
        print(playcounter)
    elif(texte2['text']=='Au tour du joueur 2 :'):
        elementP2 = element
        playcounter = playcounter + 1
        print(playcounter)
    if not playcounter == 0 and (playcounter % 2) == 0:
        chifoumiLibraryResult.result(elementP1, elementP2)
        resultRetrieve = chifoumiLibraryResult.resultRetrieve()
        resultText = resultRetrieve[0]
        winner = resultRetrieve[1]
        chaine.configure(text = resultText)
        if winner == 'P1':
            pointP1 = pointP1 + 1
        elif winner == 'P2':
            pointP2 = pointP2 + 1
        print(resultText)
        print('PointP1',pointP1)
        print('PointP2',pointP2)
        score.configure(text='Score du joueur 1 : {0}\nScore du joueur 2 :{1}'.format(pointP1,pointP2))
    if pointP1 == 3:
        winnerName = username
        pointP1 = 1
        pointP2 = 0
        resultwinner(winnerName)
    elif pointP2 == 3:
        winnerName = username2
        pointP2 = 1
        pointP1 = 0
        resultwinner(winnerName)

def resultwinner(winnerName):
    global resultwinnerGUI
    gameGUI.destroy()
    resultwinnerGUI = Tk()
    resultwinnerGUI.iconbitmap('chifoumi.ico')
    resultwinnerGUI.geometry('500x300')
    resultwinnerGUI.configure(bg='#3E4149')
    resultwinnerGUI.title(winnerName)
    resultwinnerGUI.resizable(False, False)
    chifoumiImg = ImageTk.PhotoImage(Image.open("chifoumiPicture.png"))
    resultwinnerlabel = Label(resultwinnerGUI,image = chifoumiImg, bg='#3E4149')
    resultwinnerlabel.pack()
    resultwinnerText1 = Label(resultwinnerGUI, text=winnerName, bg='#2F3137', fg='#F5EDF0')
    resultwinnerText1.pack()
    resultwinnerText2 = Label(resultwinnerGUI, text='gagne cette partie, et ce magnifique saucisson !', bg='#2F3137', fg='#F5EDF0')
    resultwinnerText2.pack()
    sausageImg = ImageTk.PhotoImage(Image.open("sausagePicture.png"))
    resultwinnerSausagePicture = Label(resultwinnerGUI,image = sausageImg, bg='#3E4149')
    resultwinnerSausagePicture.pack()
    resultwinnerButtonQuit = Button(resultwinnerGUI, text='Cliquez ici pour quitter le jeu', bg='#2F3137', fg='#fff', command = Quit)
    resultwinnerButtonQuit.pack()
    resultwinnerButtonReplay = Button(resultwinnerGUI, text='Cliquez ici pour rejouer une partie', bg='#2F3137', fg='#fff', command = lambda:[Quit(), maincode()])
    resultwinnerButtonReplay.pack()
    resultwinnerGUI.mainloop()


#Code
def maincode():
    global gameGUI, texte2, chaine, score, username, username2
    gameGUIName = (username,"contre", username2)
    gameGUI = Tk()
    gameGUI.iconbitmap('chifoumi.ico')
    gameGUI.geometry('500x300')
    gameGUI.configure(bg='#3E4149')
    gameGUI.title(gameGUIName)
    gameGUI.resizable(False, False)
    texte2 = Label(gameGUI, text='Au tour du joueur 1 :', bg='#2F3137', fg='#99EE99')
    texte2.pack()
    bouton1 = Button(gameGUI, text="Feuille", bg='#2F3137', fg='#fff', command =lambda:[resultChoice(1), changeText()])
    bouton1.pack()
    bouton2 = Button(gameGUI, text="Pierre", bg='#2F3137', fg='#fff', command =lambda:[resultChoice(2), changeText()])
    bouton2.pack()
    bouton3 = Button(gameGUI, text="Ciseaux", bg='#2F3137', fg='#fff', command =lambda:[resultChoice(3), changeText()])
    bouton3.pack()
    bouton4 = Button(gameGUI, text="Lezard", bg='#2F3137', fg='#fff', command =lambda:[resultChoice(4), changeText()])
    bouton4.pack()
    bouton5 = Button(gameGUI, text="Spock", bg='#2F3137', fg='#fff', command =lambda:[resultChoice(5), changeText()])
    bouton5.pack()
    chaine = Label(gameGUI, text='Le match vient de commencer !', bg='#2F3137', fg='#fff')
    chaine.pack()
    score=Label(gameGUI, bg='#2F3137', fg='#fff', text='Score du joueur 1 : {0}\nScore du joueur 2 : {1}'.format(pointP1,pointP2))
    score.pack()
    gameGUIPercentText = Label(gameGUI, text='Pourcentage de victoires du joueur 1 et du joueur 2 :', bg='#2F3137', fg='#fff')
    gameGUIPercentText.pack()
    gameGUIPercentResultP1 = Label(gameGUI, text=victorypercentageP1, bg='#2F3137', fg='#fff')
    gameGUIPercentResultP1.pack()
    gameGUIPercentResultP2 = Label(gameGUI, text=victorypercentageP2, bg='#2F3137', fg='#fff')
    gameGUIPercentResultP2.pack()
    gameGUI.mainloop()

retrieve = []
chifoumiLibraryUsername.usernameGUIDef()
retrieve = chifoumiLibraryUsername.usernamedataRetrieve()
print(retrieve)
username = retrieve[0]
username2 = retrieve[1]

percent = []
percent = chifoumiLibraryUsername.percent()
gamenb = percent[0]
gamenb2 = percent[1]
victoires = percent[2]
victoires2 = percent[3]
if not victoires == 0:
    victorypercentageP1 = round(victoires / gamenb * 100)
else:
    victorypercentageP1 = 0
if not victoires2 == 0:
    victorypercentageP2 = round(victoires2 / gamenb2 * 100)
else:
    victorypercentageP2 = 0
print(victorypercentageP1)
print(victorypercentageP2)

maincode()