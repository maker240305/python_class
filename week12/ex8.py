#이미지를 버튼으로 만들어서 클릭하면 메시지 창 띄우기
from tkinter import *
from tkinter import messagebox

#함수 선언
def myFunc():
    messagebox.showinfo('원피스버튼','하이조쿠오니 고래와 나루')

def func1():
    if chk.get() == 0:
        messagebox.showinfo('','체크버튼이 꺼졋네요')
    else:
        messagebox.showinfo('','체크버튼이 켜졌네요')

def func2():
    if var.get() == 1:
        label1.configure(text='파이썬')
    elif var.get() == 2:
        label1.configure(text='C++')
    elif var.get() == 3:
        label1.configure(text='Java')



#메인 코드
window = Tk()

#체크박스 추가
chk = IntVar()
cb = Checkbutton(window, text='클릭하세요', variable=chk, command=func1)
cb.pack()

#라디오버튼 추가
var = IntVar()
rb1 = Radiobutton(window, text='파이썬',variable=var, value=1,command=func2)
rb2 = Radiobutton(window, text='C++',variable=var, value=2,command=func2)
rb3 = Radiobutton(window, text='Java',variable=var, value=3,command=func2)

label1 = Label(window,text='선택된 언어 : ', fg='red')

rb1.pack()
rb2.pack()
rb3.pack()
label1.pack()

photo = PhotoImage(file='onepiece.png')
btn = Button(window, image=photo, command=myFunc)

btn.pack()

window.mainloop()