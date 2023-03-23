
import tkinter
from tkinter import*
import random
questions = [
    "In which year, Partition of Bengal was annulled?",
    "On which date, India's Constituent Assembly adopted the National Flag of India?",
    "Which among the following is not a power of RBI?",
    "Which among the following planets revolves around the sun from east to west?",
    "Which day is celebrated as World Peace and Understanding Day?",
    "The FIFA Football World Cup is normally held every how many years?",
    "Which of the following languages are directly executable by a computer's CPU?",
    "The Punjab National Bank (PNB) has signed an agreement with which telecom company to roll out open mobile wallet Speedpay?",
    "Which city hosted the Shanghai Cooperation Organization (SCO) Film Festival 2023?",
    "Amazon recently partnered with which leading retail Group of India, to deepen its market presence?",
]

answer_choice =[
    ["1909","1910","1911","1912",],
    ["26 January,1947","26 November,1947"," 22 July,1947"," 26 January,1950",],
    ["inspection of banks","Nationalization of Banks","Call of returns","Control the lending policies of the banks",],
    ["Venus","Mercury","Earth","Jupiter",],
    ["23 February","29 January","10 March","17 July",],
    ["2","3","4","5",],
    ["Machine Language","High Language","Assembly Language","Second generation Language",],
    ["Vodafone India","BSNL","Reliance Jio","Idea Cellular",],
    ["Gandhinagar","Mumbai","Mysuru","Kochi",],
    ["Future Group","D-Mart","Mahindra Retail","Big Basket",],
]
answers = [2,2,1,0,0,2,0,1,1,0]
user_answer = []


indexes =[]
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblquestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50,3))


    labelresulttext = Label(
        root,
        font = ("consolas",25), 
        background="#ffffff",
        border=0,  
    )
    labelresulttext.pack(pady=(50,4))
    labelscore = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelscore.pack()
    labelresult = Label(
        root, 
        font = ("consolas",25),
        background="#ffffff",
        border=0,
    )
    labelresult.pack()
if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img 
        labelresulttext.configure(text="You Are Excellent !!")
        img = PhotoImage(file="score.png")
        labelscore.configure(image=img)
        labelscore.image = img 
        labelresult.configure(text=score)
       
    elif (score >= 10 and score <20):
        img = PhotoImage(file="abc.png")
        labelimage.configure(image=img)
        labelimage.image = img
        img = PhotoImage(file="score.png")
        labelscore.configure(image=img)
        labelscore.image = img 
        labelresulttext.configure(text="You Are Better !!")
        labelresult.configure(text=score)
        
    else:
        img = PhotoImage(file="fail.png")
        labelimage.configure(image=img)
        labelimage.image = img 
        labelresulttext.configure(text="Better Luck Next Time !! ")
        img = PhotoImage(file="score.png")
        labelscore.configure(image=img)
        labelscore.image = img 
        labelresult.configure(text=score)
      

def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score =  score + 5
        x += 1    
    print(score)
    showresult(score)
ques = 1
def selected():
    global radiovar,user_answer
    global lblquestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblquestion.config(text=questions[indexes[ques]])
        r1['text']= answer_choice[indexes[ques]][0]
        r2['text']= answer_choice[indexes[ques]][1]
        r3['text']= answer_choice[indexes[ques]][2]
        r4['text']= answer_choice[indexes[ques]][3]
        ques += 1
    else:
          print(indexes)
          print(user_answer)
          calc()



def startquiz():
    global lblquestion,r1,r2,r3,r4
    lblquestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas",18),
        width=500,
        justify="center",
        wraplength=500,
        background="#ffffff",
    )
    lblquestion.pack(pady=(100,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text= answer_choice[indexes[0]][0],
        font=("Times",12),
        value = 0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)
    r2 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][1],
        font=("Times",12),
        value = 1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)
    r3 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][2],
        font=("Times",12),
        value = 2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)
    r4 = Radiobutton(
        root,
        text=answer_choice[indexes[0]][3],
        font=("Times",12),
        value = 3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)
def startIspressed():
    image_label.destroy()
    labeltext.destroy()
    btnstart.destroy()
    gen()
    startquiz()
root = tkinter.Tk()
root.title("Interactive Quiz")
root.geometry("700x600")
root.configure(bg='white')
Photo1 = PhotoImage(file="2.png")
image_label = Label(
    root,
    background="#ffffff",
    image = Photo1
    )

image_label.pack()

labeltext = Label(
    root,
    text = "Interactive Quiz",
    font = ("comic sans MS",24,"bold"),
    background="#ffffff",

)
labeltext.pack()

Photo = PhotoImage(file="3.png")
btnstart = Button(
    root,
    image=Photo,
    command=startIspressed,
)
btnstart.pack(pady=(20,0))
root.mainloop()
