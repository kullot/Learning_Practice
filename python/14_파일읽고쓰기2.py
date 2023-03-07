# 파일객체 = open(파일명, 모드, 인코딩)

# 파일객체 멤버함수
# write
# read
# readline
# readlines
# seek
# tell
# close

# 파일열기모드
# r - 읽기모드
# w - 쓰기모드
# a - 추가모드

# 파일쓰기
# fp = open("test.txt", "w")
#
# for i in range(1, 11):
#     fp.write(f"{i} 입니다.\n")
#
# fp.close()
#
# # 파일읽기
# fp = open("test.txt", "r")
# rd = fp.read()
# fp.close()
# print(rd)

# 원하는 글자수만 읽어 온다. (seek 와 비슷한 역할)
# fp = open("test.txt", "r")
# rd = fp.read(10)
# fp.close()
# print(rd)

# 파일포인터위치(tell)
# fp = open("test2.txt", "w")
# print(fp.tell()) #글자 포인트의 위치 현재 0
# fp.write("sgsgsgdgsddfsdfsdfsf") #글자 포인트의 다음 위치 20
# print(fp.tell())
# fp.write("helloworld")
# fp.close()

# 파일포인터변경(seek)
# fp = open("test2.txt", "w")
# print(fp.tell()) #글자 포인트의 위치 현재 0
# fp.write("sgsgsgdg")
# fp.seek(3) #글자 포인터 3의 위치로 변경
# print(fp.tell())
# fp.write("helloworld")
# fp.close()

# 파일읽기(readline)
# fp = open("test.txt", "r")
# line = fp.readline()
# print(line)
# line = fp.readline()
# print(line)
# fp.close()

# fp = open("test.txt","r")
# for i in fp:
#     print(i)
# fp.close() # 유사한 방식

# 파일읽기(readlines) # list로 출력하여 보여줌
# fp = open("test.txt","r")
# rd = fp.readlines()
# for i in rd:
#     i = i.strip()
#     print(i)
# fp.close()

# 추가모드
# fp = open("test.txt", 'a')
# for i in range(11, 21):
#     fp.write(f"{i} 입니다\n")
# fp.close()

def fileWrite(filename, args, mode="w"): #함수이용 미리 폼을 만들어서 활용
    fp = open(f"{filename}.txt", mode)
    for i in args:
        fp.write(i)
    fp.close()
fileWrite("test", "dsafasdfsdafsadfsda", "a")

# 예제 (원하는 줄수 출력) 만들 것
def fileReadline(filename, line):

fileReadline("test", 3)