#파일 메뉴를 이용해서 이미지 파일 띄우기
from tkinter import *
from tkinter.filedialog import *

#함수 정의
def func_open():
    filename = askopenfilename( parent=window,filetypes=(('png 파일','*.png'),('모든 파일','*.*')) )
    photo = PhotoImage(file=filename)
    pLabel.config(image=photo)
    pLabel.image = photo

window = Tk()
window.geometry('700x700')
window.title('이미지 불러오기')

#이미지가 띄워질 레이블 준비
photo = PhotoImage()
pLabel = Label(window,image=photo)
pLabel.pack()

#메뉴 만들기
#1.메뉴 객체 생성
mainMenu = Menu(window)
window.config(menu=mainMenu)

#2.상위 메뉴 만들기
fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일',menu=fileMenu)

editMenu = Menu(mainMenu)
mainMenu.add_cascade(label='편집',menu=editMenu)

#3.하위 메뉴 만들기
fileMenu.add_command(label='열기',command=func_open)
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=quit)

editMenu.add_command(label='수정')
editMenu.add_command(label='삭제')

window.mainloop()