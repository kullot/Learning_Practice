# 변수
# 파이썬에서는 모든것들이 객체로 구현
# 변수에는 값이 아닌 객체의 주소를 저장

# a = 123
# print(a, type(a))
# a = str(a)
# print(a, type(a))
# str = 123
# print(str)
# b = str(str) # 에러


# a = 10
# b = 10
#
# print(a, id(a))
# print(b, id(b))
#
# b = 11
# print(a, id(a))
# print(b, id(b))
#
# a = [1, 2, 3]
# b = a
# print(a, id(a))
# print(b, id(b))
#
# print(a is b)   # a와 b가 가리키는 객체는 같은가? is는 ==과 같다.
#
# a[1] = 10
# print(a, id(a))
# print(b, id(b))

#===========================================

# mutable - list, dict, set(같아도 각각 id(메모리) 생성)
# immutable - tuple, str, int, float, bool

# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(a, id(a))
# print(b, id(b))

# 얕은복사(메모리가 달라지지만 눈속임으로 내부적으로는 같음)
# import copy
#
# a = [1, 2, 3, [10, 20]]
# b = a[:]
# a[3][0] = 100
# print(a, id(a[3]))
# print(b, id(b[3]))
#
# c = [1, 2, 3, 4]
# d = copy.copy(c)
# print(c, id(a))
# print(d, id(b))

# 깊은복사
import copy

a = [1, 2, 3, [10, 20]]
b = copy.deepcopy(a)
a[3][1] = 10000
print(a, id(a[3]))
print(b, id(b[3]))

a = 3
b = 5

temp = a
a = b
b = temp
print(a, b)

a = 3
b = 5
a, b = b, a
print(a, b)

