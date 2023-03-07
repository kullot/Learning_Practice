# 문자열(String) - 문자, 단어 등으로 구성된 문자들의 집합

a = "hello world"
b = 'hello world'
c = """hello world"""
d = '''hello world'''
print(a)
print(b)
print(c)
print(d)

e = "python's"
print(e)
f = 'hello "python"'
print(f)

# 이스케이프 코드 (Escape Code) 사용
g = 'python\'s'     # ' 작은 따옴표를 문자열로 바꾼다
print(g)
h = "hello \"python\""      # "" 큰 따옴표를 문자열로 바꾼다
print(h)

a = "hello \nworld"     # 아래로 줄바꿈. 맨 앞으로 간다. Line Feed
print(a)

# 여러줄 문자열
c = """
hello 
world
python
"""        # 여러줄 사용할때 사용
print(c)
print(type(a))

# 문자열 연산
a = "hello"
b = "world"
c = a + b       # 문자열을 붙여준다
print(c)
c = a * 3
print(c)
d = a + str(3)       # 숫자를 문자열로 타입변경
print(d)

# a + 3은 에러
a = "10"
d = int(a) + 3
print(d)

# 문자열 길이
print(len(b))

# 인덱싱(가르친다)
a = "동해물과 백두산이 마르고 닳도록"
print(a[3])     # 0부터 시작
print(a[10])
print(a[-1])
print(a[-3])
print(a[5]+a[6]+a[7])

# 슬라이싱(잘라낸다) [시작:끝 -1:증가치]
print(a[0:6])       # 0부터 5까지
print(a[5:8])       # 5부터 7까지
print(a[:6])        # 시작을 비우면 처음부터
print(a[5:])        # 끝을 비우면 끝까지
print(a[:])         # 처음과 끝을 비우면 전체
print(a[10:-3])
print(a[::2])       # 0부터 2씩 증가하며 출력


# 슬라이싱 문자열 나누기
b = "20220515rain"
date = b[:8]
weather = b[8:]
print(date)
print(weather)

# 문자열 바꾸기
# immutable(자료형)은 값 변경 불가, 바꾸기 불가
# a = "동해물과 백두산이 마르고 닳도록"
# a[0] = "서"    # 에러

# 문자열 포매팅
# 첫번째 %를 이용
# %d 정수
# %s 문자열
# %f 실수
number = 18
a = "현재 %-10s는 %s도 입니다" % ("온도",  number)
print(a)
# b = "승률 %d%% 입니다" % 30
# print(b)

a = "%10.3f" % 3.1415
print(a)

# 두번째
a = "현재 {0}는 {1}도 입니다".format("온도", 20)
print(a)
a = "현재 {0}는 {number}도 입니다".format("온도", number = 20)
print(a)

# 세번째(최신)
number = 20
a = f"현재 온도는 {number +2}도 입니다"
print(a)

# 문자열 관련 함수들
a = "hello"
print(a.count("l"))

# 문자 위치 알려주기1 (find) : 없으면 -1
a = "pythonh"
print(a.find("a"))

# 문자 위치 알려주기2 (index) : 없으면 에러
a = "python"
#print(a.index("a"))

# 문자열 삽입(join) : 문자열 사이에 내가 원하는 문자 삽입
a = "hello"
a = " ".join(a)
print(a)

# 소문자를 대문자로
a = "hello"
print(a.upper())

# 대문자를 소문자로
b = "WORLD"
print(b.lower())

# 공백 지우기
a = "    python    "
print(len(a))
#a = a.lstrip()# 왼쪽 공백 지우기
#a = a.rstrip()# 오른쪽 공백 지우기
a = a.strip()# 양쪽 공백 지우기
print(a)

# 문자열 바꾸기(replace)
a = "python"
print(a.replace("py", "f"))

# 문자열 나누기(split)
a = "just,do,it"
b = a.split(",")    # 안적으면 공백 기준으로 나눔
print(b, type(b)) # list type




