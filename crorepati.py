from tkinter import *
from pygame import mixer
import pyttsx3 as pp
from tkinter.ttk import Progressbar

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

questions = ["Which of these Hindi phrases is used to denote high inflation?",
             "Complete the title of this film starring Anil Kapoor and Kajol, 'Hum Aapke _____ Mein Rehte Hain'",
             "Which one of these four birds has the longest beak and feet?",
             "Which of these formulae is used to calculate the area of a rectangular agriculture field?",
             "Which one of these festivals is celebrated during winter in India?",
             "which of these Hindi idioms means to defame someone ?",
             "The traditional attire 'pheta' is worn on which part of the body ?",
             "Which of the following was once a lifeline on the TV show 'Kaun Banega Crorepati'?",
             "what time corresponds to 23:23 hours ?",
             "Which team has won most number of IPL matches ?",
             "Among the following actors,which actor is commonly recognized as the 'Angry Young Man'?",
             "The death anniversary of which of the following leaders is observed as Martyrs Day?",
             "Bahubali festival is related to ?",
             "Which cricketer has most number of international centuries?",
             "'Itna sannata kyun hai bhai?'is a very famous dialogue. Name the movie."]

first_option = ["Fasal Bikau Mehngaai", "Gali",
                "Heron", "breadth-length",
                "Baisakhi", "Keechad Uchaalna",
                "Arm", "Tridev", "11:23PM", "KKR"
    , "Shah Rukh Khan",

                "Smt. Indira Gandhi", "Islam", "Ricky Ponting",
                "Dabangg"]

second_option = ["Padgi Chor Mehngaai", "Dil",
                 "Parrot", "length + breadth ",
                 "Makar Sankranti", "Paani Daalna",
                 "Head", "Triguni", "11.11PM", "CSK",
                 "Salman Khan", "Pt. jawaharlal Nehru",
                 "Hinduism",
                 "Virat Kohli", "Lagaan"]

third_option = ["Aankhfod Mehngaai", "Kholi",
                "Crow", "length * breadth",
                "Naag Panchami", "Mitti Khodna",
                "Waist", "Trimurti", "7:23PM", "MI",
                "Sanjay Dutt", "Mahatma Gandhi",
                "Buddhism",
                "Rohit Sharma", "Sholey"]

fourth_option = ["Kamartod Mehngai", "Baju",
                 "Pigeon", "breadth/length",
                 "Ganesh Chaturthi", "Rang Lagaana",
                 "Chest", "Trilok", "9.11PM", "RCB",
                 "Amitabh Bachchan",
                 "Bhagat Singh",
                 "Jainism", "Sachin Tendulkar",
                 "Kal Ho Na Ho"]

mixer.init()
mixer.music.load('kbc.mp3')
mixer.music.play(-1)
window = Tk()
window.title(" Who Wants to be a Millionaire")
window.geometry("1352x652+0+0")
window.resizable(0,0)
window.configure(background='black')
#########################Frames##############################
mainFrame = Frame(window, bg='black')
mainFrame.grid()

leftframe = Frame(window, bg='black', bd=20, width=900, height=600)
leftframe.grid(row=0, column=0)
rightframe = Frame(window, bg='black', bd=20, width=452, height=600)
rightframe.grid(row=0, column=1)

topframe = Frame(leftframe, bg='black', bd=20, width=900, height=200, padx=110)
topframe.grid(row=0, column=0)
middleframe = Frame(leftframe, bg='black', bd=20, width=900, height=200)
middleframe.grid(row=1, column=0)
bottomframe = Frame(leftframe, bg='black', bd=20, width=900, height=200)
bottomframe.grid(row=2, column=0)


#########################Image changing ###########################


def change50():
    Live50.config(image=Image50X)
    Live50.config(state=DISABLED)

    if textQuestionEntry.get(1.0, 'end-1c') == questions[0]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[1]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[2]:
        textQuestion3Button.config(text='')
        textQuestion4Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[3]:
        textQuestion2Button.config(text='')
        textQuestion1Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[4]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[5]:
        textQuestion2Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[6]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[7]:
        textQuestion3Button.config(text='')
        textQuestion4Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[8]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[9]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[10]:
        textQuestion1Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[11]:
        textQuestion1Button.config(text='')
        textQuestion2Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[12]:
        textQuestion1Button.config(text='')
        textQuestion2Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[13]:
        textQuestion2Button.config(text='')
        textQuestion3Button.config(text='')

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[14]:
        textQuestion1Button.config(text='')
        textQuestion4Button.config(text='')


def peoplechange():
    audience_polebtn.config(state=DISABLED)

    audience_polebtn.config(image=audience_poleX)

    if textQuestionEntry.get(1.0, 'end-1c') == questions[0]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=60)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=90)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[1]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[1]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[2]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=70)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=50)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=60)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=10)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[3]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=70)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=90)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=50)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[4]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[5]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=80)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=10)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[6]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=10)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[7]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=10)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=70)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=30)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[8]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=90)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=50)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[9]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=10)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=70)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=50)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[10]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=20)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=80)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[11]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=30)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=80)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=90)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=40)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[12]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=20)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=60)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=10)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=90)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[13]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=60)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=35)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=40)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=80)
        progressbar3volumeLabel.place(x=790, y=330)

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[14]:
        progressbarLabel.place(x=660, y=200)
        progressbarvolume.config(value=60)
        progressbarvolumeLabel.place(x=660, y=330)

        progressbar1Label.place(x=700, y=200)
        progressbar1volume.config(value=65)
        progressbar1volumeLabel.place(x=710, y=330)

        progressbar2Label.place(x=740, y=200)
        progressbar2volume.config(value=90)
        progressbar2volumeLabel.place(x=750, y=330)

        progressbar3Label.place(x=780, y=200)
        progressbar3volume.config(value=80)
        progressbar3volumeLabel.place(x=790, y=330)


def phonechange():
    phonebtn.config(image=phoneimageX)
    phonebtn.config(state=DISABLED)
    mixer.music.load('calling.mp3')
    mixer.music.play()
    phoneButton.config(image=phonepic)


def phoneclick():
    mixer.music.load('kbc.mp3')
    mixer.music.play(-1)
    mixer.music.set_volume(0)

    if textQuestionEntry.get(1.0, 'end-1c') == questions[0]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[1]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[2]:
        engine.say('The Answer is A')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[3]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[4]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[5]:
        engine.say('The Answer is A')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[6]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[7]:
        engine.say('The Answer is B')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[8]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[9]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[10]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[11]:
        engine.say('The Answer is C')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[12]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[13]:
        engine.say('The Answer is D')
        engine.runAndWait()

    elif textQuestionEntry.get(1.0, 'end-1c') == questions[14]:
        engine.say('The Answer is C')
        engine.runAndWait()


######################Different millionare pictures###################################
def million1():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture1.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million2():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture2.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million3():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture3.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million4():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture4.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million5():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture5.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million6():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture6.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million7():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture7.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million8():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture8.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million9():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture9.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million10():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture10.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million11():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture11.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million12():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture12.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million13():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture13.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million14():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture14.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


def million15():
    canvas = Canvas(rightframe, bg='black', width=430, height=600)
    canvas.grid(row=0, column=0)
    canvas.delete('all')
    image1 = PhotoImage(file='Picture15.png')
    canvas.create_image(215, 300, image=image1)
    canvas.image = image1


##############################Images##################################
CentreImage = PhotoImage(file="center.png")
LogoCentre = Button(middleframe, image=CentreImage, bg='black', width=300, height=200, activebackground='black', bd=0)
LogoCentre.grid()

Image50 = PhotoImage(file="jpge50.png")
Image50X = PhotoImage(file="jpge50X.png")
Live50 = Button(topframe, image=Image50, bg='black', width=180, cursor='hand2', height=80, command=change50,
                activebackground='black', bd=0)
Live50.grid(row=0, column=0)

audience_pole = PhotoImage(file="jpgePeople.png")
audience_poleX = PhotoImage(file="jpgePeopleX.png")
audience_polebtn = Button(topframe, image=audience_pole, bg='black', cursor='hand2', width=180, height=80,
                          command=peoplechange, activebackground='black', bd=0)
audience_polebtn.grid(row=0, column=1)

phoneimage = PhotoImage(file="jpgePhone.png")
phoneimageX = PhotoImage(file="jpgePhoneX.png")
phonebtn = Button(topframe, image=phoneimage, bg='black', width=180, cursor='hand2', height=80, command=phonechange,
                  activebackground='black', bd=0)
phonebtn.grid(row=0, column=2)

amountimage = PhotoImage(file="Picture01.png")
phonepic = PhotoImage(file="phone.png")
amountbtn = Button(rightframe, image=amountimage, bg='black', width=430, height=600, activebackground='black', bd=0)
amountbtn.grid(row=0, column=0)

phoneButton = Button(window, bg='black', command=phoneclick, bd=0, cursor='hand2', activebackground='black')
phoneButton.place(x=660, y=250)


###################################################questions

def select(event):
    phoneButton.config(image='')
    mixer.music.set_volume(1)

    progressbarLabel.place_forget()
    progressbarvolumeLabel.place_forget()
    progressbar1Label.place_forget()
    progressbar1volumeLabel.place_forget()
    progressbar2Label.place_forget()
    progressbar2volumeLabel.place_forget()
    progressbar3Label.place_forget()
    progressbar3volumeLabel.place_forget()

    b = event.widget

    value = b['text']
    img = b['image']

    if value == 'Kamartod Mehngai':

        million1()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[1])
        textQuestion1Button.config(text=first_option[1])
        textQuestion2Button.config(text=second_option[1])
        textQuestion3Button.config(text=third_option[1])
        textQuestion4Button.config(text=fourth_option[1])

    elif value == 'Dil':
        million2()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[2])
        textQuestion1Button.config(text=first_option[2])
        textQuestion2Button.config(text=second_option[2])
        textQuestion3Button.config(text=third_option[2])
        textQuestion4Button.config(text=fourth_option[2])

    elif value == 'Heron':
        million3()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[3])
        textQuestion1Button.config(text=first_option[3])
        textQuestion2Button.config(text=second_option[3])
        textQuestion3Button.config(text=third_option[3])
        textQuestion4Button.config(text=fourth_option[3])

    elif value == 'length * breadth':
        million4()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[4])
        textQuestion1Button.config(text=first_option[4])
        textQuestion2Button.config(text=second_option[4])
        textQuestion3Button.config(text=third_option[4])
        textQuestion4Button.config(text=fourth_option[4])

    elif value == 'Makar Sankranti':
        million5()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[5])
        textQuestion1Button.config(text=first_option[5])
        textQuestion2Button.config(text=second_option[5])
        textQuestion3Button.config(text=third_option[5])
        textQuestion4Button.config(text=fourth_option[5])

    elif value == 'Keechad Uchaalna':
        million6()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[6])
        textQuestion1Button.config(text=first_option[6])
        textQuestion2Button.config(text=second_option[6])
        textQuestion3Button.config(text=third_option[6])
        textQuestion4Button.config(text=fourth_option[6])

    elif value == 'Head':
        million7()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[7])
        textQuestion1Button.config(text=first_option[7])
        textQuestion2Button.config(text=second_option[7])
        textQuestion3Button.config(text=third_option[7])
        textQuestion4Button.config(text=fourth_option[7])

    elif value == 'Triguni':
        million8()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[8])
        textQuestion1Button.config(text=first_option[8])
        textQuestion2Button.config(text=second_option[8])
        textQuestion3Button.config(text=third_option[8])
        textQuestion4Button.config(text=fourth_option[8])

    elif value == '7:23PM':
        million9()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[9])
        textQuestion1Button.config(text=first_option[9])
        textQuestion2Button.config(text=second_option[9])
        textQuestion3Button.config(text=third_option[9])
        textQuestion4Button.config(text=fourth_option[9])

    elif value == 'MI':
        million10()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[10])
        textQuestion1Button.config(text=first_option[10])
        textQuestion2Button.config(text=second_option[10])
        textQuestion3Button.config(text=third_option[10])
        textQuestion4Button.config(text=fourth_option[10])

    elif value == 'Amitabh Bachchan':
        million11()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[11])
        textQuestion1Button.config(text=first_option[11])
        textQuestion2Button.config(text=second_option[11])
        textQuestion3Button.config(text=third_option[11])
        textQuestion4Button.config(text=fourth_option[11])

    elif value == 'Mahatma Gandhi':
        million12()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[12])
        textQuestion1Button.config(text=first_option[12])
        textQuestion2Button.config(text=second_option[12])
        textQuestion3Button.config(text=third_option[12])
        textQuestion4Button.config(text=fourth_option[12])

    elif value == 'Jainism':
        million13()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[13])
        textQuestion1Button.config(text=first_option[13])
        textQuestion2Button.config(text=second_option[13])
        textQuestion3Button.config(text=third_option[13])
        textQuestion4Button.config(text=fourth_option[13])

    elif value == 'Sachin Tendulkar':
        million14()
        textQuestionEntry.delete(1.0, END)
        textQuestionEntry.insert(END, questions[14])
        textQuestion1Button.config(text=first_option[14])
        textQuestion2Button.config(text=second_option[14])
        textQuestion3Button.config(text=third_option[14])
        textQuestion4Button.config(text=fourth_option[14])

    elif value == 'Sholey':
        def restart():
            phonebtn.config(state=NORMAL)
            Live50.config(state=NORMAL)
            audience_polebtn.config(state=NORMAL)
            Live50.config(image=Image50)
            audience_polebtn.config(image=audience_pole)
            phonebtn.config(image=phoneimage)

            mixer.music.stop()
            canvas = Canvas(rightframe, bg='black', width=430, height=600)
            canvas.grid(row=0, column=0)
            canvas.delete('all')
            image1 = PhotoImage(file='Picture01.png')
            canvas.create_image(215, 300, image=image1)
            canvas.image = image1
            amountbtn.config(image=amountimage)
            textQuestionEntry.delete(1.0, END)
            textQuestionEntry.insert(END, questions[0])
            textQuestion1Button.config(text=first_option[0])
            textQuestion2Button.config(text=second_option[0])
            textQuestion3Button.config(text=third_option[0])
            textQuestion4Button.config(text=fourth_option[0])
            root2.destroy()
            mixer.music.load('kbc.mp3')
            mixer.music.play(-1)

        mixer.music.stop()
        mixer.music.load('Kbcwon.mp3')
        mixer.music.play()
        million15()
        root2 = Toplevel()
        root2.config(bg='black')
        root2.title('You won 1 million pounds')
        root2.geometry('500x400')
        img = PhotoImage(file='center.png')
        imgLabel = Label(root2, image=img, bd=0, activebackground='black')
        imgLabel.pack(pady=30)
        winlabel = Label(root2, text='You Won', font=('arial', 40, 'bold'), bg='black', fg='white')
        winlabel.pack(pady=10)
        happy = PhotoImage(file='happy.png')
        happylabel = Label(root2, image=happy, bg='black')
        happylabel.place(x=400, y=280)
        happy1label = Label(root2, image=happy, bg='black')
        happy1label.place(x=30, y=280)
        tryagainButton = Button(root2, text='Play Again', bd=0, bg='black', fg='white', cursor='hand2',
                                font=('arial', 20, 'bold'),
                                activebackground='black', activeforeground='white', command=restart)
        tryagainButton.pack(pady=10)

        def on_closing():
            root2.destroy()
            window.destroy()

        root2.protocol("WM_DELETE_WINDOW", on_closing)

        root2.mainloop()



    else:
        def restart1():
            phonebtn.config(state=NORMAL)
            Live50.config(state=NORMAL)
            audience_polebtn.config(state=NORMAL)
            Live50.config(image=Image50)
            audience_polebtn.config(image=audience_pole)
            phonebtn.config(image=phoneimage)

            canvas = Canvas(rightframe, bg='black', width=430, height=600)
            canvas.grid(row=0, column=0)
            canvas.delete('all')
            image1 = PhotoImage(file='Picture01.png')
            canvas.create_image(215, 300, image=image1)
            canvas.image = image1
            textQuestionEntry.delete(1.0, END)
            textQuestionEntry.insert(END, questions[0])
            textQuestion1Button.config(text=first_option[0])
            textQuestion2Button.config(text=second_option[0])
            textQuestion3Button.config(text=third_option[0])
            textQuestion4Button.config(text=fourth_option[0])
            root.destroy()
            mixer.music.load('kbc.mp3')
            mixer.music.play(-1)

        mixer.music.stop()
        root = Toplevel()
        root.config(bg='black')
        root.geometry('500x400')
        root.title('You won 0 pound')
        img = PhotoImage(file='center.png')
        imgLabel = Label(root, image=img, bd=0, activebackground='black')
        imgLabel.pack(pady=30)
        loselabel = Label(root, text='You Lose', font=('arial', 40, 'bold'), bg='black', fg='white')
        loselabel.pack(pady=10)
        sad = PhotoImage(file='sad.png')
        sadlabel = Label(root, image=sad, bg='black')
        sadlabel.place(x=400, y=280)
        sad1label = Label(root, image=sad, bg='black')
        sad1label.place(x=30, y=280)

        tryagainButton = Button(root, text='Try Again', bd=0, bg='black', fg='white', cursor='hand2',
                                font=('arial', 20, 'bold'),
                                activebackground='black', activeforeground='white', command=restart1)
        tryagainButton.pack(pady=10)

        def on_closing():
            root.destroy()
            window.destroy()

        root.protocol("WM_DELETE_WINDOW", on_closing)
        root.mainloop()


################################Text,Label,button######################################


textQuestionEntry = Text(bottomframe, font=('arial', '18', 'bold'), bg='blue', fg='white', bd=5, width=44
                         , height=2, wrap='word')
textQuestionEntry.grid(row=0, column=0, columnspan=4, pady=4)
textQuestionEntry.insert(END, questions[0])

lblQuestionA = Label(bottomframe, font=('arial', '14', 'bold'), text="A: ", bg='black', fg='white', bd=5,
                     justify=CENTER)
lblQuestionA.grid(row=1, column=0, pady=4, sticky=W)

textQuestion1Button = Button(bottomframe, text=first_option[0], font=('arial', '14', 'bold'), bg='blue', fg='white',
                             bd=1, width=17, height=2,
                             justify=CENTER, cursor='hand2')
textQuestion1Button.grid(row=1, column=1, pady=4)

lblQuestionB = Label(bottomframe, font=('arial', '14', 'bold'), text="B: ", bg='black', fg='white', justify=LEFT)
lblQuestionB.grid(row=1, column=2, sticky=W)

textQuestion2Button = Button(bottomframe, text=second_option[0], font=('arial', '14', 'bold'), bg='blue', fg='white',
                             bd=1, width=17, height=2,
                             justify=CENTER, cursor='hand2')
textQuestion2Button.grid(row=1, column=3, pady=4)

lblQuestionC = Label(bottomframe, font=('arial', '14', 'bold'), text="C: ", bg='black', fg='white', justify=LEFT)
lblQuestionC.grid(row=2, column=0, sticky=W)

textQuestion3Button = Button(bottomframe, text=third_option[0], font=('arial', '14', 'bold'), bg='blue', fg='white',
                             bd=1, width=17
                             , height=2, justify=CENTER, cursor='hand2')
textQuestion3Button.grid(row=2, column=1, pady=4)

lblQuestionD = Label(bottomframe, font=('arial', '14', 'bold'), text="D: ", bg='black', fg='white', justify=LEFT)
lblQuestionD.grid(row=2, column=2, sticky=W)

textQuestion4Button = Button(bottomframe, text=fourth_option[0], font=('arial', '14', 'bold'), bg='blue', fg='white',
                             bd=1,
                             width=17, height=2, justify=CENTER, cursor='hand2')
textQuestion4Button.grid(row=2, column=3, pady=4)
progressbarLabel = Label(window, text='', bg='black', height=8, width=2)
progressbarLabel.place(x=660, y=200)
progressbarLabel.place_forget()
progressbarvolume = Progressbar(progressbarLabel, orient=VERTICAL, mode='determinate', value=0, length=120, )
progressbarvolume.grid(row=0, column=0, ipadx=5)
progressbarvolumeLabel = Label(window, text='A', bg='black', fg='whitesmoke', font=('arial', 20, 'bold'))
progressbarvolumeLabel.place(x=660, y=330)
progressbarvolumeLabel.place_forget()

progressbar1Label = Label(window, text='', bg='black', height=8, width=2)
progressbar1Label.place(x=700, y=200)
progressbar1Label.place_forget()
progressbar1volume = Progressbar(progressbar1Label, orient=VERTICAL, mode='determinate', value=0, length=120, )
progressbar1volume.grid(row=0, column=0, ipadx=5)
progressbar1volumeLabel = Label(window, text='B', bg='black', fg='whitesmoke', font=('arial', 20, 'bold'))
progressbar1volumeLabel.place(x=710, y=330)
progressbar1volumeLabel.place_forget()

progressbar2Label = Label(window, text='', bg='black', height=8, width=2)
progressbar2Label.place(x=740, y=200)
progressbar2Label.place_forget()
progressbar2volume = Progressbar(progressbar2Label, orient=VERTICAL, mode='determinate', value=0, length=120, )
progressbar2volume.grid(row=0, column=0, ipadx=5)
progressbar2volumeLabel = Label(window, text='C', bg='black', fg='whitesmoke', font=('arial', 20, 'bold'))
progressbar2volumeLabel.place(x=750, y=330)
progressbar2volumeLabel.place_forget()

progressbar3Label = Label(window, text='', bg='black', height=8, width=2)
progressbar3Label.place(x=780, y=200)
progressbar3Label.place_forget()
progressbar3volume = Progressbar(progressbar3Label, orient=VERTICAL, mode='determinate', value=0, length=120, )
progressbar3volume.grid(row=0, column=0, ipadx=5)
progressbar3volumeLabel = Label(window, text='D', bg='black', fg='whitesmoke', font=('arial', 20, 'bold'))
progressbar3volumeLabel.place(x=790, y=330)
progressbar3volumeLabel.place_forget()

textQuestion1Button.bind('<Button-1>', select)
textQuestion2Button.bind('<Button-1>', select)
textQuestion3Button.bind('<Button-1>', select)
textQuestion4Button.bind('<Button-1>', select)

window.mainloop()
