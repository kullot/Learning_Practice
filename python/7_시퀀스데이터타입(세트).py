# 순서없는 데이터타입(인덱싱, 슬라이싱 불가)
# - 딕셔너리, 세트

# 변경가능(mutable) 데이터타입
# - 리스트, 딕셔너리, 세트

# 세트(set)
# 집합자료형
# 중복없는 데이터를 저장

a = set()
b = {1, 2, 3, 4}
c = set([1, 2, 3])
d = set("hello")        # 중복데이터는 하나만 저장
print(a)
print(b, type(b))
print(c)
print(d)

# 리스트 튜플로 변환
s = {1, 2, 3, 4}
mylist = list(s)
print(mylist)
myT = tuple(s)
print(myT)

a = set([1, 2, 3, 4, 5, 6])
b = set([4, 5, 6, 7, 8, 9])

# 교집합
print(a & b)
print(a.intersection(b))

# 합집합
print(a | b)
print(a.union(b))

# 차집합
print(a - b)
print(a.difference(b))

# 관련 함수들
# 값 1개 추가하기(add)
a = set([1, 2, 3, 4, 5, 6])
a.add(10)
print(a)

# 값 여러개 추가하기(update)
a.update([20, 30, 40])
print(a)

# 특정 값 제거하기(remove)
a.remove(4)
print(a)

# 리스트를 세트로 변경
a = [1, 2, 3, 4, 5, 4, 5, 6, 7]
b = set(a)
print(b)

