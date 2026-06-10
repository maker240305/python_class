from tkinter import *
from random import *

window = Tk()
window.title('두더지 잡기')

moleFrame = Frame(window)
statFrame = Frame(window)

moleFrame.grid(row=0,column=0)
statFrame.grid(row=0,column=1)

hitLabel = Label(statFrame,text='0 hits')
missLabel = Label(statFrame,text='0 misses')
hitLabel.pack()
missLabel.pack()

moleNum = 3
moleP = PhotoImage(file='gif/mole.png')
nomoleP = PhotoImage(file='gif/no_mole.png')

moleList = []

hitNum = 0
missNum = 0

def mole_hit(c):
    global hitNum,missNum,moleList
    if moleList[c]['text'] == 'mole':
        hitNum += 1
        hitLabel.config(text=str(hitNum)+'hits')
    else:
        missNum += 1
        missLabel.config(text=str(missNum)+'misses')



def init():
    count = 0
    for r in range(moleNum):
        for c in range(moleNum):
            button = Button(moleFrame, command=lambda c=count:mole_hit(c))
            button.config(text='no mole',image=nomoleP)
            button.grid(row=r,column=c)
            moleList.append(button)
            count+=1

def update():
    global moleList
    for i in range(moleNum*moleNum):
        button = moleList[i]
        button.config(text='no mole',image=nomoleP)

    x = randint(0,moleNum*moleNum-1)
    moleList[x].config(text='mole',image=moleP)
    window.after(1000,update)




init()
update()

window.mainloop()
