# 2023.05.04 복습
import copy
l = [[1, 2, 3], [4, 5, 6]]
ll = l
ll[0][0] = 10
print(l)  # [[10, 2, 3], [4, 5, 6]]
print(ll)  # [[10, 2, 3], [4, 5, 6]]


# 얕은 복사
# aa만 첫번째 요소만 변한다. a는 그대로 있음
a = [1000, 2000, 3000, 4000, 5000, 6000]
aa = a.copy()
aa[0] = 10
print(a)  # [1000, 2000, 3000, 4000, 5000, 6000]
print(aa)  # [10, 2000, 3000, 4000, 5000, 6000]

b = [[1, 2, 3], [4, 5, 6]]
bb = b.copy()
b[0] = 100
print(b)  # [100, [4, 5, 6]
print(bb)  # [[1, 2, 3], [4, 5, 6]]

# 깊은 복사

c = [[1, 2, 3], [4, 5, 6]]
cc = copy.deepcopy(l)
cc[0][0] = 10
print(c)  # [[1, 2, 3], [4, 5, 6]]
print(cc)  # [[10, 2, 3], [4, 5, 6]]

# # 알아야 하는 bulit-in-function 알아야 하는 built-in function

# A
# abs()
# all()
# any()

# B
# bin()
# bool()

# C
# chr()

# D
# dict()
# dir()

# E
# enumerate()
# eval()

# F
# filter()
# float()

# G
# globals()

# H
# help()
# hex()

# I
# id()
# input()
# int()
# isinstance()
# issubclass()
# iter()

# L
# len()
# list()
# locals()

# M
# map()
# max()
# min()

# N
# next()

# O
# object()
# oct()
# open()
# ord()

# P
# pow()
# print()
# property()

# R
# range()
# repr()
# reversed()
# round()

# S
# set()
# setattr()
# slice()
# sorted()
# staticmethod()
# str()
# sum()
# super()

# T
# tuple()
# type()

# V
# vars()

# Z
# zip()

# 최댓값, 최솟값, 전체값의합
d = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(d)), print(min(d)), print(sum(d))

# 이름, 별점, 객실수, 가격
호텔 = [
    ['1호텔', 5, 100, 155000],
    ['2호텔', 4, 80, 145000],
    ['3호텔', 3, 70, 135000],
    # 마지막에 콤마를 허락하는 언어는 제한적(특히 JSON에서는 엄격해서 허락하지 않습니다.)
]

max(호텔, key=lambda x: x[3])  # 가장 가격이 높은 것을 뽑아낼 수 있음
min(호텔, key=lambda x: x[3])

# 2차원 순회
a = [[1, 2, 3],
     [11, 22, 33],
     [13, 20000, 300000]]

for i in a:
    print(i)
    print('---')
print('end')

# range(start, stop, step)
# 슬라이싱과 같은 규칙
# 슬라이싱은 ':'(콜론)으로 연결되어 있고
# range는 ','(콤마)로 연결되어 있습니다.

print(list(range(100)))
# python 2.x에서 python 3.x에 range를 사용하고 싶다면 xrange(10)
print(list(range(5, 10)))

print(list(range(0, 101, 2)))  # 짝수
print(list(range(1, 101, 2)))  # 홀수
print(list(range(100, 1, -2)))
print(sum(list(range(0, 101))))
print(sum(range(0, 101)))  # 이렇게 형 변환을 하지 않고 sum하시는 것을 권합니다.

# 공부해두기!


def switch(day):
    return {
        1: '월요일',
        2: '화요일',
        3: '수요일',
        4: '목요일',
        5: '금요일',
        6: '토요일',
        7: '일요일',
    }[day]


switch(7)

# dict에 관련된 문법
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.keys()
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.values()
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.items()
dict.fromkeys('imdongseong')
dict.fromkeys('imdongseong', 100)

keys = ('name', 'age', 'grade')
values = ('imdongseong', '5', '수')

dict.fromkeys(keys, values)

e = {'one': '하나', 'two': '둘', 'three': '셋'}
e.update({'one': 1, 'two': 2})
print(e)

# 딕셔너리 순회
# key만 순회합니다
f = {'two': 2, 'three': '셋'}
for i in f:
    print(i)
    # two three


f = {'two': 2, 'three': '셋'}
for i in f:
    print(f(i))
    # 2 셋

# 딕셔너리에서 max를 이용해서 value의 key값 가져오기
d = {
    'test1': 10,
    'test2': 20,
    'test3': 31,
    'test4': 11,
}

# max(d.values()) # 이걸로는 뭔가 찾아내기 힘듭니다.
max(d, key=lambda x: d[x])
max(d, key=d.get)  # 많이 사용하는 코드입니다.

# set에서 사용하는 함수들

# 교집합 별 3개
a = {1, 2, 3}
b = {3, 4, 5}
a & b
a.intersection(b)

# 합집합
a = {1, 2, 3}
b = {3, 4, 5}
a | b
a.union(b)
# a + b # error

s = {1, 2, 3, 4}
ss = {3, 4, 5, 6}
s.issubset({1, 2})
s.issubset({1, 2, 3, 4, 5, 6, 7, 8})
