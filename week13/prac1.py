from tkinter import *

pList = ['jeju1.gif','jeju2.gif','jeju3.gif','jeju4.gif','jeju5.gif']

num = 0

def cNext():
    global num
    num += 1
    if num > 4:
        num = 0
    photo = PhotoImage(file='gif/'+pList[num])
    pBox.config(image=photo)
    pBox.image = photo
    pNum.config(text=pList[num])

def cPrev():
    global num
    num -= 1
    if num < 0:
        num = 4
    photo = PhotoImage(file='gif/'+pList[num])
    pBox.config(image=photo)
    pBox.image = photo
    pNum.config(text=pList[num])


window = Tk()

window.title('editor')
window.geometry('700x500')

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File',menu=fileMenu)

fileMenu.add_command(label='quit',command=quit)

#버튼
next = Button(window,text='다음 >>',command=cNext)
prev = Button(window,text='<< 이전',command=cPrev)
pNum = Label(window,text=pList[0])

next.place(x=400,y=10)
prev.place(x=250,y=10)
pNum.place(x=330,y=10)

photo = PhotoImage(file='gif/'+pList[0])
pBox = Label(window, image=photo)
pBox.place(x=15,y=50)




window.mainloop()


