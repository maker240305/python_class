#두더지 게임 만들기
from tkinter import *
from random import *

window = Tk()
window.title('두더지 게임')

#위젯을 넣을 프레임 생성
#왼쪽 프레임 - 두더지 이미지 버튼
#오른쪽 프레임 - 결과 창
moleFrame = Frame(window)
statusFrame = Frame(window)

moleFrame.grid(row=0, column=0)
statusFrame.grid(row=0, column=1)

#위젯 만들기
hitsLabel = Label(statusFrame,text='0 Hits')
hitsLabel.pack()
missedLabel = Label(statusFrame,text='0 Misses')
missedLabel.pack()

#필요한 정보 저장
NUM_MOLES = 5
mole_image = PhotoImage(file='gif/mole.png') #두더지 이미지
no_mole_image = PhotoImage(file='gif/no_mole.png') #빈 이미지
numHits = 0
numMisses = 0

#사용자가 두더지를 잡았는지 체크하는 함수
def mole_hit(c):
    global molesList, numHits, numMisses
    if molesList[c]['text'] == 'mole':
        numHits += 1
        hitsLabel.config(text=str(numHits)+' Hits')
    else:
        numMisses += 1
        missedLabel.config(text=str(numMisses)+' Misses')

#두더지 버튼들이 저장되는 리스트 선언
molesList = []

#초기화면 함수
def init():
    count = 0
    for r in range(NUM_MOLES):
        for c in range(NUM_MOLES):
            button = Button(moleFrame, command=lambda c=count:mole_hit(c))
            #만든 버튼의 속성 중 문자열과 이미지 적용하기
            button.config(text='no mole',image=no_mole_image)
            button.grid(row=r, column=c)
            molesList.append(button)
            count += 1

#랜덤하게 두더지 버튼이 배치되도록 함수로 처리
def update():
    global molesList

    #화면 초기화
    for i in range(NUM_MOLES*NUM_MOLES):
        btn = molesList[i]
        btn.config(text='no mole',image=no_mole_image)

    x = randint(0,NUM_MOLES*NUM_MOLES-1) #난수 발생
    #난수에 해당하는 위치의 버튼에 두더지 이미지와 텍스트 적용하기
    molesList[x].config(text='mole',image=mole_image)
    #일정 간격으로 두더지 이미지가 나타나도록
    window.after(500, update)



#main code
init()     #초기화면 호출
update()
window.mainloop()