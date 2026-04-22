sec = 3675
print("< 실행 결과 >")
print("초(second) 정보 : " + str(sec))
s = sec % 60
m = (sec // 60) % 60
h = (sec // 60) // 60

print("결과 : " + str(h) + "시간 " + str(m) + "분 " + str(s) + "초")