from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('700x500')
window.title('자기소개')

#프레임 만들기
headfr = Frame(window, bg="#1d3557", padx=24, pady=28)
bodyfr = Frame(window, bg="#f4f7fb", padx=28, pady=24)


#headfr.grid(row=0, column=0)
headfr.pack(fill="x")
bodyfr.pack(fill="both")


#함수 선언
def clickImage(event):
    messagebox.showinfo('마우스','이미지가 클릭됨')
def info1():
    messagebox.showinfo('이름','이름: 윤인식')
def info2():
    messagebox.showinfo('나이','나이: 22세')
def jr():
    messagebox.showinfo('종료','앱이 종료됩니다.')
    quit()


#윈도우 객체에 마우스 이벤트 등록하기
#window.bind('<Button-1>', clickLeft)

#메뉴 만들기
#1.메뉴 객체 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

#2.상위 메뉴 객체 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='메뉴', menu=fileMenu)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label='도움말',menu=editMenu)

#3.하위 메뉴 만들기
fileMenu.add_command(label='이름',command=info1)
fileMenu.add_command(label='나이',command=info2)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=quit)

editMenu.add_command(label='만든이')
editMenu.add_command(label='도움말')


#필요한 위젯 만들기
fsLabel = Label(headfr, text="안녕하세요, 윤인식입니다",
            bg="#1d3557",
            fg="white",
            font=("Malgun Gothic", 22, "bold"),)
fsLabel.pack()
scLabel = Label(headfr, text="자기소개 하기",
            bg="#1d3557",
            fg="#d8e8ff",
            font=("Malgun Gothic", 11))
scLabel.pack()



bdayH = Label(
            bodyfr,
            text='생일',
            bg="white",
            fg="#1d3557",
            font=("Malgun Gothic", 13, "bold"),
        )
bdayH.pack()

bdayB = Label(
            bodyfr,
            text='2004년 3월 5일',
            bg="white",
            fg="#2b2d42",
            font=("Malgun Gothic", 10),
        )
bdayB.pack()

foodH = Label(
            bodyfr,
            text='좋아하는 음식',
            bg="white",
            fg="#1d3557",
            font=("Malgun Gothic", 13, "bold"),
        )
foodH.pack()

foodB = Label(
            bodyfr,
            text='갈비',
            bg="white",
            fg="#2b2d42",
            font=("Malgun Gothic", 10),
        )
foodB.pack()

btnQuit = Button(bodyfr, text='종료',bg="red",
            fg="white",
            command=jr
            )
btnQuit.pack()

window.mainloop()