# 시퀀스 데이터타입

# 리스트, 튜플, 딕셔너리, 세트

# 순서있는 데이터타입
# - 리스트, 튜플

# 순서없는 데이터타입(인덱싱, 슬라이싱 불가)
# - 딕셔너리, 세트

# 변경가능(mutable) 데이터타입
# - 리스트, 딕셔너리, 세트

# 변경불가능(immutable) 데이터타입
# - 튜플

a = list()
b = []
c = [1, 2, 3]
d = ["a", "b", "c", "d"]
e = ['a', 10, 3.14]
f = [10, ['a', 'b']]

# print(a, type(a))
# print(b, type(b))
# print(c, type(c))
# print(d, type(d))
# print(e, type(e))
# print(f, type(f))

# 인덱싱
a = [1, 2, 3]
print(a[0], type(a[0]))
print(a[-1])
print(a[1] + a[2])

a = [1, 2, 3, ['a', 'b', 'c', [10, 20, 30]]]
print(a[-1][3][1])

# 슬라이싱
a = [1, 2, 3, 4, 5]
print(a[2:])

a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(a[3][:2])

# 리스트 연산
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)
print(a*3)

# 리스트 길이 구하기
a = ['pyhotn', 'hello', 'world']
print(len(a))

# 리스트 수정
a = [1, 2, 3, 4, 5]
a[2] = 10
print(a)

# 리스트 삭제
del(a[3])
del a[3]
print(a)
del(a[0:2])
print(a)

# 리스트 추가
a.append(4)
print(a)
a.append([10, 20])
print(a)

# 리스트 정렬
a = [3, 4, 1, 2, 5]
a.sort()     #오름차순
print(a)
b = ['c', 'a', 'd', 'b']
b.sort()
print(b)
a.sort(reverse=True)    #내림차순
print(a)

# 리스트 뒤집기
b = ['c', 'a', 'd', 'b']
b.reverse()
print(b)

# 위치 반환(index)
a = [1, 2, 3, 4, 5]
print(a.index(3))

# 리스트에 요소 삽입(insert)
a = [1, 2, 3, 4, 5]
a.insert(0, 10)
print(a)

# 리스트 요소 제거(remove)
a = [1, 2, 3, 4, 5, 3]
a.remove(3)     # 중복된 값이 있으면 첫번째 값만 제거한다.
print(a)

# 리스트 요소 꺼내기(pop)
# 리스트의 맨 마지막 요소를 돌려주고 삭제
a = [1, 2, 3, 4, 5, 3, 2]
b = a.pop()
print(b)
print(a)
b = a.pop(3)        # index 값을 입력하여 꺼냄
print(b)
print(a)

# 리스트에 포함된 요소 개수 세기(count)
a = [1, 2, 3, 4, 5, 3, 2]
print(a.count(3))

# 리스트 확장(extend)
# 리스트 추가의 개념
# extend(x) x에는 리스트만 올수있다
a = [1, 2, 3]
a.extend([4, 5])
print(a)
b = [10, 20]
a.extend(b)
print(a)
