# 순서없는 데이터타입(인덱싱, 슬라이싱 불가)
# - 딕셔너리, 세트

# 변경가능(mutable) 데이터타입
# - 리스트, 딕셔너리, 세트


# 딕셔너리
# 키(key)와 값(Value)으로 저장

dic = {1:'a', 2:'b', 3:'c'}
print(dic, type(dic))

dic = {'name':'홍길동', 'phone':'01012345678', 'birth':123456}
print(dic, type(dic))

a = {1:[1, 2, 3]}
print(a)
# a = {[1, 2, 3]:3}   # 오류
# print(a)

# 딕셔너리 요소 추가하기
a = {1:'aa'}
a[2] = 'bb'
a['a'] = 'ccc'
a[3] = [1, 2, 3]
print(a)

# 딕셔너리 요소 삭제하기
del a[3]
print(a)

# key 사용해서 value 얻기
# 딕셔너리에서 a[2]의 의미는 리스트나 튜플과는 다르다
print(a[2])

# 딕셔너리 만들때 key가 중복될 경우
a = {1:'a', 1:'b'}      # 뒤에 들어오는 값을 덮어씌운다
print(a)

# key에 리스트는 쓸수없다. 그러나 튜플은 쓸수있다.
a = {(1,2):'a'}
print(a)

# 딕셔너리 관련 함수들

# key, value 리스트 만들기
dic = {'name':'홍길동', 'phone':'01012345678', 'birth':123456}
print(dic.keys())
print(dic.values())
print(dic.items())
a, b, c = dic.items()
print(a)
print(b)
print(c)
for k, v in dic.items():
    print(k, v)

# 요소 모두 지우기(clear)
dic = {'name':'홍길동', 'phone':'01012345678', 'birth':123456}
dic.clear()
print(dic)

# key로 value 얻기(get)
dic = {'name':'홍길동', 'phone':'01012345678', 'birth':123456}
print(dic.get('phone'))
print(dic['phone'])
# 위 두개는 결과값이 같다. 하지만 없는 key 값을 입력시 결과값이 다름.
# Key값이 없을경우 None 리턴. '거짓' null

# key가 없을경우 디폴트값 리턴
print(dic.get('phone1', 'key가 없다'))

# 해당 key가 딕셔너리 안에 있는지 조사(in)
print('phone' in dic)


