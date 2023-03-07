# 모듈
# 함수나 변수 또는 클래스를 모아놓은 파일

# print(dir(__builtins__)) #내장함수

# import mod1
# print(mod1.add(3, 4))
# print(mod1.sub(5, 1))

# from mod1 import add, sub #함수 전체 사용 "*"
# print(add(3, 4))
# print(sub(5, 3))

# import mod1
# print(mod1.__name__) #__name__변수 : 파이썬에서만 사용하는 특별한 함수

# 클래스나 변수를 포함한 모듈

import mod1

print(mod1.pi)

a = mod1.Math()
print(a.solv(5))

# Path
# 모듈을 찾기위한 경로
import sys
print(sys.path)

# 새로운 경로 등록
sys.path.append("C:\\mod")
print(sys.path)
