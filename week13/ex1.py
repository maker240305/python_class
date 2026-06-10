#사진 앨범 만들기
from tkinter import *
from tkinter import messagebox

#필요한 정보 저장
fnameList = ['jeju1.gif','jeju2.gif','jeju3.gif','jeju4.gif','jeju5.gif']
#현재 사진의 번호 저장
num = 0

#함수 선언
def clickNext():
    global num
    num += 1
    #사진 이미지의 끝을 체크
    if num > len(fnameList)-1:
        num = 0

    photo = PhotoImage(file='gif/'+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fLabel.config(text=fnameList[num]) #파일명 바꿔주기

def clickPrev():
    global num
    num -= 1
    #첫번째 사진을 체크
    if num < 0:
        num = len(fnameList)-1

    photo = PhotoImage(file='gif/'+fnameList[num])
    pLabel.configure(image=photo)
    pLabel.image = photo
    fLabel.config(text=fnameList[num])

def clickLeft(event):
    messagebox.showinfo('마우스','마우스 왼쪽 버튼이 클릭됨')

def clickImage(event):
    messagebox.showinfo('마우스','이미지가 클릭됨')



window = Tk()
window.geometry('700x500')
window.title('사진 앨범')

#윈도우 객체에 마우스 이벤트 등록하기
#window.bind('<Button-1>', clickLeft)

#메뉴 만들기
#1.메뉴 객체 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

#2.상위 메뉴 객체 생성
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='File', menu=fileMenu)

#3.하위 메뉴 만들기
fileMenu.add_command(label='종료', command=quit)

#필요한 위젯 만들기
btnPrev = Button(window, text='<< 이전',command=clickPrev)
btnNext = Button(window, text='다음 >>',command=clickNext)
photo = PhotoImage(file='gif/'+fnameList[0])
pLabel = Label(window, image=photo)
fLabel = Label(window, text=fnameList[0])

pLabel.bind('<Button>', clickImage)

#특정 위치에 좌표값을 이요해서 위젯 배치하기
btnPrev.place(x=250,y=10)
btnNext.place(x=400,y=10)
pLabel.place(x=15,y=50)
fLabel.place(x=330,y=10)

window.mainloop()

