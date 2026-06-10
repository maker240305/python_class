#윈도우 프로그래밍
from tkinter import *

#윈도 객체 생성
window = Tk()
window.title('윈도창 연습')
window.geometry('500x400')
window.resizable(width=False, height=False)

#이 부분에서 화면을 구성하고 처리
label1 = Label(window, text='Python Programming')
label2 = Label(window, text='윈도우 프로그래밍', font=('말은 고딕',30), fg='blue')
label3 = Label(window,
               text='공부 중입니다.', background='orange', width=120, height=10, anchor=CENTER)

label1.pack()
label2.pack()
label3.pack()

#사용자의 이벤트 처리를 위한 대기
window.mainloop()