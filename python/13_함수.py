# # 함수
# # def 함수이름(매개변수):
# #     함수내용
# #     함수내용
# #     return 리턴값
#
# # 입력값이 없는 함수
# def hello():
#     return "world"
#
# a = hello()
# print(hello())
#
# # 출력값이 없는 함수
# result = 0
# def add(a, b):
#     print(f"{a} + {b} = {a + b}")
#
# add(3, 5)
#
# # 입력값, 출력값도 없는 함수
# def world():
#     print("hello world")
#     print("hello world")
#     print("hello world")
#
#
# def mul(a, b):
#     return a * b
# print(mul(4, 3))
#
# # 매개변수를 지정해서 호출
# def div(a, b):
#     return a / b
#
# result = div(a = 5, b = 3)
# print(result)
# result = div(b = 3, a = 10)
# print(result)
#
# # 입력값이 여러개일때(가변매개변수)
# def add_many(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
# print(add_many(1, 4, 5, 6, 7, 10, 30))
#
# def Cal(select, *args):
#     if select == "add":
#         result = 0
#         for i in args:
#             result += i
#     elif select == "mul":
#         result = 1
#         for i in args:
#             result *= i
#     return result
#
# print(Cal("mul", 1, 2, 3, 4, 5, 4, 5))
#
# # 키워드 파라미터(kwargs)
# def kwfunc(**kwargs):
#     return kwargs
#
# a = kwfunc(name="홍길동", age=26, phone="12434325")
# print(a)
#
# # 함수는 출력값이 하나이다.
# def Calcula(a, b): #첫반째 함수만 출력
#     return a + b
#     return a * b
# print(Calcula(3, 4))
#
# def Calcula2(a, b): #출력값이 큐플
#     return a + b, a * b
# print(Calcula(3, 4))
#
# # return 의 다른 쓰임새
# def func1(a):
#     if a < 0:
#         return #그냥 단일로도 사용
#     print(a)
#
# func1(-1)
#
# # 매개변수 디폴트 값
# def fucn2(a, b = 0):
#     return a + b
#
# print(fucn2(3))
# print(fucn2())
#
# #잘못된예 : 중간이나 끝에 디폴트값이 비어있으면 안됨.
# # def fucn3(a = 0, b):
# #     return a + b
# #
# # fucn3(3)

# 변수의 범위

# a = 10 #전역변수 global
# def func():
#     a = 100 #지역변수
#
# func()
# print(a)

# 함수안에서 함수밖의 변수를 변경하는법

# 1)return을 이용하는 방법
# a = 10 #전역변수 global
# def func():
#     a = 100 #지역변수
#     return a
#
# a = func()
# print(a)

# 2)global 키워드 이용하는 방법
# a = 10 #전역변수 global
# def func():
#     global a
#     a = 100 #지역변수
#
# func()
# print(a)

# 함수의 참조
# def func():
#     print("hello world")
#
# a = func
# a()
# func()

# 함수의 매개변수에 함수이름으로 인자를 넘김(함수이름도 변수에 쓰일수있다)

# def fn():
#     print("hello world")
#
# fn()
#
# def my(a):
#     a()
#
# my(fn)

# def fn():
#     print("hello world")
#
# def my():
#     return fn
#
# a = my()
# a()

# 람다 lambda

add = lambda a, b: a + b

# def add(a, b):   #위의 람다 수식과 동일함
#     return a + b

result = add(3, 4)
print(result)
