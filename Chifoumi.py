#Import
from tkinter import *
from PIL import Image,ImageTk

#Fonctions
def choiceFinal(choiceNumber):
    global choicewindow
    choicewindow.destroy()
    if choiceNumber == 1 :
        exec(open("mode/chifoumiRobertClassic.py").read(), globals())
    elif choiceNumber == 2 :
        exec(open("mode/chifoumiRobertBBT.py").read(), globals())
    elif choiceNumber == 3:
        exec(open('mode/chifoumiVSClassic.py').read(), globals())
    elif choiceNumber == 4:
        exec(open('mode/chifoumiVSBBT.py').read(), globals())

def choiceRobert():
    buttonBot.pack_forget()
    buttonVS.pack_forget()
    buttonOnline.pack_forget()
    buttonRobertClassic = Button(choicewindow, text="Robert Classic", bg='#2F3137', fg='#fff', command=(lambda: choiceFinal(1)))
    buttonRobertClassic.pack()
    space = Label(choicewindow, bg='#3E4149', fg='#fff') #Espace
    space.pack()
    buttonRobertBBT = Button(choicewindow, text="Robert Big Bang Theory", bg='#2F3137', fg='#fff', command=(lambda: choiceFinal(2)))
    buttonRobertBBT.pack()
    
def choiceVS():
    buttonBot.pack_forget()
    buttonVS.pack_forget()
    buttonOnline.pack_forget()
    buttonVSClassic = Button(choicewindow, text="Versus Classic", bg='#2F3137', fg='#fff', command=(lambda: choiceFinal(3)))
    buttonVSClassic.pack()
    space = Label(choicewindow, bg='#3E4149', fg='#fff') #Espace
    space.pack()
    buttonVSBBT = Button(choicewindow, text="Versus Big Bang Theory", bg='#2F3137', fg='#fff', command=(lambda: choiceFinal(4)))
    buttonVSBBT.pack()

#Code
choicewindow = Tk()
choicewindow.geometry('500x300')
choicewindow.iconbitmap('chifoumi.ico')
choicewindow.title('Chifoumi')
choicewindow['bg']='#3E4149'
chifoumiImg = ImageTk.PhotoImage(Image.open("chifoumiPicture.png"))
choicewindowLabel = Label(choicewindow,image = chifoumiImg, bg='#3E4149')
choicewindowLabel.pack()
choicewindowFrame = Frame(choicewindow, bg='#3E4149')
choicewindow.resizable(False, False)
choicewindowFrame.pack()

buttonBot = Button(choicewindow, text="Jouer contre Robert le robot", bg='#2F3137', fg='#fff', command = (choiceRobert))
buttonBot.pack()
chaine = Label(choicewindow, bg='#3E4149', fg='#fff') #Espace
chaine.pack()
buttonVS = Button(choicewindow, text="Jouer en Versus", bg='#2F3137', fg='#fff', command=(choiceVS))
buttonVS.pack()
chaine = Label(choicewindow, bg='#3E4149', fg='#fff') #Espace
chaine.pack()
buttonOnline = Button(choicewindow, text="Jouer en ligne", bg='#2F3137', fg='#fff', command = (choicewindow.destroy))
buttonOnline.pack()
choicewindow.mainloop()