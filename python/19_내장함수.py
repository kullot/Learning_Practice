# 내장함수

# abs 절대값
# print(abs(2))
# print(abs(-2))

# all
# 반복가능한 자료형안에 있는 요소들이 모두 참이면 참
# 거짓이 하나라도 있으면 거짓

# a = [1, 2, 3, 4, 5]
# a = [1, True, 3, "aaaa", []]
# print(all(a))

# any
# 반복가능한 자료형안에 있는 요소들이 하나라도 참이면 참
# 아니면 거짓
# a = [1, True, 3, "aaaa", []]
# print(any(a))

# chr
# 유니코드값을 입력받아 그 코드에 해당하는 문자를 출력
# print(chr(97))
# print(chr(0xAC01))

# ord
# 문자를 입력받아 유니코드로 출력
# print(ord("가"))

# dir
# 객체가 가지고 있는 변수는 함수를 보여준다
# print(dir((1, 2, 3)))

# divmod
# 2개의 숫자를 입력받아 몫과 나머지를 튜플로 출력
# print(divmod(6, 4))

# enumerate
# mutable 자료형의 인덱스와 값을 반화
# 순서있는 문자열을 입력받아 index값 출력
# for i, v in enumerate(["a", "b", "c"]):
#     print(i,v)

# eval
# 실행 가능한 문자열을 입력받아서 실행
# print(eval('1 + 2'))
# print(eval("divmod(4,3)"))

# hex
# 16진수 변환
# print(hex(234))

# oct
# 8진수 변화
# print(oct(234))

# id
# 객체의 고유 주소값(레퍼런스)를 반환
# print(id(3))

# isinstance
# 클래스의 객체인지 판별하는 함수
# class Myclass:
#     pass
# a = Myclass()
# b = 3
# print(isinstance(a, Myclass))
# print(isinstance(b, Myclass))

# len
# 요소의 전체 개수
# print(len("asdfasdfsadfasd"))
# print(len([1, 2, 3, 4, 5, 6, 7]))

# # max(최대값)
# a = [1, 4, 67, 38, 79, 5]
# print(max(a))
#
# # min(최소값)
# print(min(a))

# sum(합계)
print(sum([1, 3, 4]))

# (평균)
a = [2, 3, 4, 5, 6]
print(sum(a) / len(a))
import numpy as np
print(np.mean(a))

# round
# 반올림
print(round(123.12345, 4))

# sorted(정렬)
a = [2, 4, 6, 3]
print(sorted(a))
print(a.sort())
print(a)

# zip
# 동일한 개수로 이루어진 자료형을 묶어주는 역할(큐플로)
print(list(zip([1, 2, 3], [5, 6, 7], ['a', 'b', 'c'])))
print(list(zip("abc", "qwe")))
