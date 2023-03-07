# 산술연산자
a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)    # 나누기
print(a % b)    # 나머지
print(a ** b)   # 제곱
print(a // b)   # 몫

# 연산자 우선순위
# **
# *, /, //, %
# +, -

# a = 10 + 2 - (3 * (2 ** 2))
# print(a)
#
# # 반지름이 5인 원의 면적을 구하시오
# a = 5 ** 2 * 3.14
# print(a)

# 입력
# a = input("입력 : ")
# print(a)

# 대입연산자
a = 5
b = 3

# a += b      # a = a + b
# a -= b      # a = a - b
# a *= b
# a /= b
# a **= b
# a %= b
# a //= b
# print(a)

# 관계연산자
a = 3

b = a > b
print(b)
b = a < b
print(b)
b = a >= b
print(b)
b = a <= b
print(b)
b = a == b     # is
print(b)
b = a != b      #
print(b)
b = 0 < a < 10
print(b)

# 변수 선언방식
a = 3
a, b = (1, 2)
a, b = 3, 5
(a, b) = 1, 2
[a, b] = [1, 2]

# 논리연산자
# and(논리곱) - 둘다 참일때만 참이고 나머지는 거짓
# 1010
# 1100
# ----
# 1000

# or(논리합) - 둘중에 하나가 참이면 참
# 1010
# 1100
# ----
# 1110

# xor(배타적논리함)^ - 다르면 참, 같으면 거짓
# 1010
# 1100
# ----
# 0110

# not(반전)
# 1010
# ----
# 0101

# from operator import xor
#
# a = 5
# b = 3
# result = a > 0 and b < 0
# result1 = a > 0 or b < 0
# result2 = not(a > 0)
# result3 = xor(a > 0, b < 0)
# print(result)
# print(result1)
# print(result2)
# print(result3)

# 비트연산자
# << 왼쪽쉬프트
# >> 오른쪽쉬프트
# & and
# | or
# ^ xor
# ~ not

# a = 2 & 1
# print(a)
# a = 2 | 1
# print(a)
# a = 2 ^ 1
# print(a)
# a = ~(2)
# print(a)
# a = 2 >> 1
# print(a)
# a = 2 << 1
# print(a)

# 음수
# 0000 0010
# 1111 1101 # 1의 보수
# 1111 1110 # 2의 보수

# 1111 1110
# 0000 0001

# a = -2 & 1
# print(a)
# a = -2 | 1
# print(a)
# a = -2 << 1
# print(a)
# a = -2 >> 1
# print(a)

# 구성원연산자
# in
# not in
# a = " hello world"
# print("hello" in a)
# print("hello" not in a)
# a = [1, 2, 3, 4]
# print(2 in a)

# 식별연산자
# is
# is not
# a = 10
# b = 10
# print(a is b)
# print(a is not b)

