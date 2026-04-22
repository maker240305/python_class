#특정 단어 검색하기 => in
# ss = 'C C++ C# Java Python Basic'
# print('C++' in ss)
# print('delphi' in ss)

#간단한 챗봇 만들기
print('챗봇:안녕하세요! 무엇이든 물어보세요.(종료하려면 q)')
while True:
    user = input('사용자:')
    if user == 'q':   #종료조건
        break
    if '안녕' in user or '반가워' in user:
        print('챗봇:안녕하세요!')
    elif '이름' in user:
        print('챗봇:내 이름은 챗도우미야.')
    elif '날씨' in user:
        print('챗봇:오늘의 날씨는 흐리고 바람이 많습니다.')
    elif '시간' in user:
        import datetime
        now = datetime.datetime.now()
        print('챗봇:현재시간은',now.strftime('%H:%M:%S'))
    else:
        print('챗봇:잘 모르겠습니다.')