# class
# 객체지향

# result = 0
# result2 = 0
#
# def add(a, b):
#     global result
#     result = a + b
#     return result
#
# def add2(a, b):
#     global result2
#     result2 = a + b
#     return result2
#
# print(add(3, 4))
# print(add2(5, 9))

# class Calculator:
#     def add(self, a, b):
#         self.result = a + b
#         return self.result
#
# a = Calculator() #객체 생성
# b = Calculator()
# c = Calculator()
#
# print(a.add(3, 4))
# print(b.add(3, 5))
#
# print(a.result)
# print(b.result)

# pass(함수 완성전 미리 만들어둠)
# class Myclass:
#     pass
#======================================================================
# class Calculator:
#     def __init__(self, a, b): #생성자 : 생성할때 실행
#         self.a = a
#         self.b = b
#     def __del__(self): #소멸자 : 끌날때 실행
#         pass
#     def setdata(self, a, b): #값 변경시 사용
#         self.a = a
#         self.b = b
#     def add(self):
#         self.result = self.a + self.b
#         return self.result
#     def mul(self):
#         self.result = self.a * self.b
#         return self.result
#     def div(self):
#         self.result = self.a / self.b
#         return self.result
#     def sub(self):
#         self.result = self.a - self.b
#         return self.result
#
# a = Calculator(4, 5)
# b = Calculator(2, 6)
# a.setdata(5, 3)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.div())
# print(a.a)
# print(a.b)
# print(a.result)
# b.setdata(1, 2)
# print(b.a)

# 생성자(__init__) : 클래스에게 값을 전달하고 싶을때
# print(a.add())
# a.setdata(7, 3)
# print(a.add())

# ++클래스의 상속
# class Player:
#     def __init__(self, hp, attack):
#         self.hp = hp
#         self.attack = attack
#     def Move(self):
#         print("이동")
#     def Attack(self):
#         print("공격")
#
# class Knight(Player):
#     def Attack(self): # 함수 오버라이딩 : 상속 받았지만 재정의
#         print("기사 공격")
#     pass
#
# class Mage(Player):
#     def Attack(self):
#         print("마법사 공격") # 함수 오버라이딩 : 상속 받았지만 재정의
#     def setMp(self, mp):
#         self.mp = mp
#
# knight1 = Knight(100, 10)
# mage1 = Mage(60, 5)
# mage1.setMp(20)
# print(mage1.mp)
# mage1.Attack()
# knight1.Attack()
#
# knight1.Move()
# print(knight1.hp)

# 클래스변수와 객체변수
class Myclass:
    id = 0 # 클래스변수
    def __init__(self, a):
        self.a = a #객체변수
    def getData(self):
        return self.a

my = Myclass(10)
my2 = Myclass(3)
print(my.id)
print(my2.id)
my.id = 10      # 객체변수 접근
Myclass.id = 2   # 클래스변수 접근
print(my.id)
print(my2.id)
print(Myclass.id)
print(my.id)

