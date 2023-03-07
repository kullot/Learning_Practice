# while 문(반복분)
# 초기값, 조건식, 증감

# a = 0
# while a < 10:
#     print("hello")
#     a += 1
# break

# while a < 10:
#     if a == 3:
#         break
#     print(a)
#     a += 1
# else

# while a < 10:
#     if a == 3:
#         break
#     print(a)
#     a += 1
# else:
#     print("else")

# 합계
# n = 1
# sum = 0
#
# while n <= 10:
#     print(n)
#     sum += n
#     n += 1
# print("합계 : ", sum)


# import random
# com = random.randint(1, 3)
# print(com)
# player = 0
# while True:
#     player = input("입력 : ")
#     player = int(player)
#     if player > 0 and player <= 3:
#         break
# if player == 1:
#     print("당신은 가위")
# elif player == 2:
#     print("당신은 바위")
# elif player == 3:
#     print("당신은 보")
# if com == 1:
#     print("컴퓨터는 가위")
# elif com == 2:
#     print("컴퓨터는 바위")
# elif com == 3:
#     print("컴퓨터는 보")
# # 판정체크
# if (player == 1 and com == 2) or (player == 2 and com == 3) or (player == 3 and com == 1):
#     print("패배")
# elif (player == 2 and com == 1) or (player == 3 and com == 2) or (player == 1 and com == 3):
#     print("승리")
# elif com == player:
#     print("무승부")

# for 문
# for 변수 in 반복가능데이터:
#   수행문장
#   수행문장

# a = [1, 2, 3, 4, 5]
# for i in a:
#     print(i)

# a = [(1,2), (3,4), (5,6)]
# for i, j in a:
#     print(i, j)
#
# a = (1, 2, 3, 4, 5)
# for i in a:
#     print(i)
#
# a = {1, 2, 3, 4, 5}
# for i in a:
#     print(i)

# a = {1:'a', 2:'b', 3:'c', 4:"d", 5:'e'}
# for i, j in a.items():
#     print(i, j)

# score = {'홍길동':80, '황길동':30, '김길동':25, '고길동':48, '이길동':65, '최길동':100, '박길동':37, '조길동':55}

# 60점이면 합격, 아니면 불합격
# 합격인 사람의 명단 출력, 합격자 수 출력, 전체 평균
# 홍길동은 80점으로 합격입니다.
# 홍길동은 80점으로 불합격입니다.
# 합격자수 : 0명, 전체평균 : 0
# a=0
# b=0
# for i, j in score.items():
#     b += j
#     if j >= 60:
#         a = a + 1
#         c = "%s은 %d점으로 합격입니다" % (i, j)
#         print(c)
#     else:
#         d = "%s은 %d점으로 불합격입니다" % (i, j)
#         print(d)
# e = b/len(score)
# f = "합격자수 : %d명, 전체평균 : %d" % (a, e)
# print(f)

# count = 0
# sum = 0
# for name, jumsu in score.items():
#     sum += jumsu
#     if jumsu >= 60:
#         print(f"{name}은 {jumsu}점으로 합격입니다")
#         count += 1
#     else:
#         print(f"{name}은 {jumsu}점으로 불합격입니다")
# else:
#     print(f"합격자수 : {count}명, 전체평균 : {sum/len(score)}")

# range 함수
# a = range(10)
# print(a, type(a))
#
# for i in range(10):
#     print(i)

# for i in range(1, 11):
#     print(i)

# score = [30, 70, 50, 90, 25]
# for i in range(len(score)):
#     if score[i] >= 60:
#         print(f"{score[i]}점은 합격입니다")

# for i in range(10):
#     for j in range(10):
#         print(i, j)

# 구구단 프로그램
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f"{i}곱하기 {j}는 {i * j}")

# break
# continue
for i in range(1, 10):
    if i % 2 == 1:
        continue
    print(i)

# 축약 내장리스트
# a = [i * 3 for i in range(1, 10)]
# print(a)

a = [i for i in range(1, 10) if i % 2 == 0]
print(a)