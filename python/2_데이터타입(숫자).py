# 숫자형(Nuber) - 숫자 형태로 이루어진 자료형
# 정수, 실수, 2진수, 8진수, 16진수

# 정수 int
a = 10
b = -10
c = 0
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 실수 float
d = 3.14
print(d, type(d))

# 2진수(숫자 앞에 0b)
e = 0b01100011
print(e, type(e))

# 8진수(잘 사용하지 않음 0o)
f = 0o177
print(f, type(f))

# 16진수(0x)
g = 0x8ff
print(g, type(g))

# 연산자
a = 9
b = 4
print(a+b)
print(a-b)
print(a*b)
print(a/b, type(a/b)) # type이 정수가 아님
print(a//b, type(a//b)) # 몫
print(a%b) # 나머지
print(a**b) # a의 b제곱

# 복소수(complex)
a = 3 + 4j
print(a)
print(type(a))
print(a.imag) # 허수부
print(a.real) # 실수부
print(a.conjugate())    #켤레복소수

b = complex(3,-4)
print(b)
