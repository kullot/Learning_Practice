# 예외처리

# ZeroDivisionError
# print(4 / 0)

# FileNotFoundError
# fp = open("test3.txt", "r")

# IndexError
# a = [1, 2, 3]
# print(a[4])

# try except 문
# try:
#     4 / 0
#     fp = open("test3.txt", "r")
#     a = [1, 2, 3]
#     print(a[4])
#     print("hello world")
#
# except ZeroDivisionError as e:
#     print(e)
# except FileNotFoundError as f:
#     print(f)
# except IndexError as i:
#     print(i)
# except: # 기본 except는 맨밑으로
#     print("에러")

# finally
try:
    fp = open("test3.txt", "r")
    fp.close()
except:
    print("에러")
finally:
    # fp.close()
    print("close")

