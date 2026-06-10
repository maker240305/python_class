#글자대신 이미지를 레이블에 넣기
from tkinter import *

window = Tk()

photo = PhotoImage(file='onepiece.png')
label1 = Label(window, image=photo)
label1.pack()

#버튼 위젯 추가
btn = Button(window, text='윈도창 종료', fg='blue', command=quit) #버튼이 눌러졌을 때 실행되는 함수 이름

btn.pack()


window.mainloop()