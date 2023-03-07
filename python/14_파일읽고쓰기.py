# 파일객체 = open(파일명, 모드, 인코딩)

# 파일객체 멤버함수
# write
# read
# readline
# readlines
# seek
# tell
# close #open과 짝
# # 파일열기모드
# r - 읽기모드
# w - 쓰기모드
# a - 추가모드

# 파일 쓰기
# fp = open("test.txt", "w")
# for i in range(1, 11):
#     fp.write(f"{i} 입니다\n")
# fp.close()

# 파일 읽기
# fp = open("test.txt", "r")
# rd = fp.read()
# fp.close()
# print(rd)

# 파일읽기(readlines) # list로 출력하여 보여줌
fp = open("test.txt","r")
rd = fp.readlines()
for i in rd:
    i = i.strip()
    print(i)
fp.close()

# 추가모드
# fp = open("test.txt", 'a')
# for i in range(11, 21):
#     fp.write(f"{i} 입니다\n")
# fp.close()

# def fileWrite(filename, args, mode="w"): #함수이용 미리 폼을 만들어서 활용
#     fp = open(f"{filename}.txt", mode)
#     for i in args:
#         fp.write(i)
#     fp.close()
# fileWrite("test", "dsafasdfsdafsadfsda", "a")


# 예제 (원하는 줄수 출력) 만들 것
# def fileReadline(filename, args, mode = "r"):
#     fp = open(f"{filename}.txt", mode)
#     a = 0
#     for i in fp:
#         a += 1
#         print(i,end='')
#         if a == args:
#             break
#     fp.close()
# fileReadline("test", 3)
