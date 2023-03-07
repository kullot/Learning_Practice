# if문
# a = 5
#
# if a > 0 and a < 10:
#     print("hello world")
#     print("hello world")
#     print("hello world")
# else:
#     print("python")
#
# print("끝")

# 가위바위보 게임
# 1 - 가위, 2 - 바위, 3 - 보
# 컴퓨터가 랜덤으로 가위바위보
# 사용자의 입력을 받아 가위바위보

# 춮력예시
# 당신은 가위
# 컴퓨터는 바위
# 승리, 패배, 무승부

# import random
# com = random.randint(1, 3)
# print(com)
# player = int(input("입력 : "))

# if player == 1:
#     print("당신은 가위")
# elif player == 2:
#     print("당신은 바위")
# elif player == 3:
#     print("당신은 보")
# else:
#     print("이상한 값입니다")
#
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

# if player == 1 and com == 2:
#     print("패배")
# elif player == 2 and com == 3:
#     print("패배")
# elif player == 3 and com == 1:
#     print("패배")
# elif player == 2 and com == 1:
#     print("승리")
# elif player == 3 and com == 2:
#     print("승리")
# elif player == 1 and com == 3:
#     print("승리")
# elif com == player:
#     print("무승부")


# a = int(input("입력 : "))
# if a == 1:
#     print("가위")
# elif a == 2:
#     print("바위 입니다")
# elif a == 3:
#     print("보 입니다.")
# else:
#     print("이상한 값입니다")

# if 축약형
a = 10

result = 100 if a < 0 else 200
print(result)

