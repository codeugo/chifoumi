from tkinter import *
from PIL import Image,ImageTk

data = []

usernameNotFound = True
username2NotFound = True

def usernameGUIDef():
    global username1Entry, username2Entry, usernameGUI
    usernameGUI = Tk()
    usernameGUI.geometry('500x300')
    usernameGUI.iconbitmap('chifoumi.ico')
    usernameGUI.title('Chifoumi')
    usernameGUI['bg']='#3E4149'
    chifoumiImg = ImageTk.PhotoImage(Image.open("chifoumiPicture.png"))
    label = Label(usernameGUI,image = chifoumiImg, bg='#3E4149')
    label.pack()
    usernameGUIFrame = Frame(usernameGUI, bg='#3E4149')
    usernameGUI.resizable(False, False)
    usernameGUIFrame.pack()

    username1Label = Label(usernameGUIFrame, text='Username :', fg='#fff', bg='#3E4149')
    username1Label.pack()
    username1Entry = Entry(usernameGUIFrame)
    username1Entry.pack()
    username1Entry.focus_force()
    username2Label = Label(usernameGUIFrame, text='Username2 :', fg='#fff', bg="#3E4149")
    username2Label.pack()
    username2Entry = Entry(usernameGUIFrame)
    username2Entry.pack()
    username2Entry.focus_force()
    print(username2Entry)

    btnAffiche = Button(usernameGUI, text='Valider', command=dataVSRead)
    btnAffiche.pack(padx=5, pady=5)

    usernameGUI.mainloop()

def dataVSRead():
    testif=0
    global username2NotFound
    global usernameNotFound
    global gamenb, victoires, gamenb2, victoires2
    global username,username2
    username =username1Entry.get()
    username2 =username2Entry.get()
    print(username)
    print(username2)
    with open ("data.txt", "r") as f:  
        for li in f :
            s = li.strip ("\n\r")
            l = s.split (";")
            l[1]=int(l[1])
            l[2]=int(l[2])
            data.append (l)
    for i in data :
        if username in i :
            gamenb=i[1]
            victoires=i[2]
            usernameNotFound = False
            print("username1yes")
        elif username2 in i:
            gamenb2=i[1]
            victoires2=i[2]
            username2NotFound = False
            print("username2yes")
        else : 
            testif=testif+1
            print("testif number", testif)
    print(len(data))
    print(testif)
    if not usernameNotFound or not username2NotFound:
        testif = testif+1 
    if testif == len(data):
        print("testifyes")
        if usernameNotFound == True:
            print("testifyesusername1")
            data.append([username,0,0])
            gamenb = 0
            victoires = 0
        if username2NotFound == True:
            print("testifyesusername2")
            data.append([username2,0,0])
            gamenb2 = 0
            victoires2 = 0
    f.close ()
    usernameGUI.destroy()

def percent():
    return[gamenb, gamenb2, victoires, victoires2]

def dataVSWrite(gamenumberTotal, victoires, victoires2):
    print(victoires)
    for i in data:
        if username in i :
            gamenumberP1Old = i[1]
            victoiresOld = i[2]
            i[1]=gamenumberTotal + gamenumberP1Old
            i[2]=victoires + victoiresOld
        elif username2 in i:
            gamenumberP2Old = i[1]
            victoires2Old = i[2]
            i[1]=gamenumberTotal + gamenumberP2Old
            i[2]=victoires2 + victoires2Old
        f = open ("data.txt", "w")
    for i in range (0,len (data)) : 
        for j in range (0, 2) :
            f.write ( str (data [i][j]) + ";")
        f.write ( str (data [i][2]))
        f.write ("\n")
    f.close ()

def usernamedataRetrieve():
    return[username, username2]