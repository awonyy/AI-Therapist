import tkinter
from tkinter import *
import random

with open ('questions.txt') as f:
 questions = f.readlines()


#print(questions)


user_answer = []
indexes = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background = "#ffffff",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "#ffffff",
    )
    labelresulttext.pack()
    labelresulttext.configure(text=score)
    if score >= 30:
        labelresulttext.configure(text="You Are Stressed. Seeking help is advisable")
    elif (score >=0 and score < 30):
        labelresulttext.configure(text="Normal stress levels.")


   


def calc():
    global indexes,user_answer
    x = 0
    score = 0
    for i in indexes:
        ans= int(user_answer[x])
        if i>=14:
            if ans==0:
                score+=4
            elif ans==1:
                score+=3
            elif ans==2:
                score+=2
            elif ans==3:
                score+=1
            elif ans==4:
                score+=0
        else:
            score+= ans
        x += 1
    print(score)
    showresult(score)


ques = 0
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4,r5
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    #for ques in range(0,17)
    if ques < 17:
        lblQuestion.config(text= questions[ques])
        ques += 1
    else:
        # print(indexes)
        # print(user_answer)
        # these two lines were just developement code
        # we don't need them
        calc()
    




def startquiz():
    global lblQuestion,r1,r2,r3,r4,r5
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = '0',
        font = ("Times", 12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = '1',
        font = ("Times", 12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = '2',
        font = ("Times", 12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = '3',
        font = ("Times", 12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)

    r5 = Radiobutton(
        root,
        text = '4',
        font = ("Times", 12),
        value = 4,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r5.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    
    startquiz()



root = tkinter.Tk()
root.title("AI THERAPIST")
root.geometry("700x600")
root.config(background="#89CFF0")
root.resizable(0,0)


img1 = PhotoImage(file="l2.png")

labelimage = Label(
    root,
    image = img1,
    background = "#03018C",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "AI THERAPIST",
    font = ("Times New Roman",24,"bold"),
    background = "#89CFF0",
)
labeltext.pack(pady=(0,50))

img2 = PhotoImage(file="start.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Read the questions and mark one out of the five options \n 0-Never,1-Rarely, 2-Sometimes, 3-Often, 4-Very Often",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "This questionnaire contains 17 questions pertaining to both mood and physical symptoms.",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
