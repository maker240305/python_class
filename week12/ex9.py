#아이디, 패스워드 체크
from tkinter import *
from tkinter import messagebox

IDPW = {'python':'1111', 'java':'2222', 'C++':'3333'}

#함수 선언
def check():
    uid = id.get()
    upw = pw.get()
    if uid in IDPW:
        if upw == IDPW[uid]:
            messagebox.showinfo('로그인 성공',uid+'님, 안녕하세요~!')
        else:
            messagebox.showerror('로그인 실패','비밀번호 확인!!!')
    else:
        messagebox.showerror('로그인 실패','아이디 확인!!!')




#main code
window = Tk()

#위젯 구성
label1 = Label(window,text='ID 입력')
id = Entry(window, width=30)
label2 = Label(window,text='PASSWORD 입력')
pw = Entry(window, width=30, show='*')

btn = Button(window, text='로그인', width=20, command=check)

label1.pack()
id.pack()
label2.pack()
pw.pack()
btn.pack()

window.mainloop()
