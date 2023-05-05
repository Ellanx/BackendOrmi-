# list, tuple, dict, set
# 1. list 순서가 있기에 수정이 가능함. 순회가능.값의 중복허락

name = []
my_home = ['광주', '서울', '경기도', '부산', '대전', '대구']

print(my_home[0:3])

my_home.append('장성')

print(my_home)
# 항상 print를 다시 쳐주어야지 메서드값이 입력이 된다!! 기억하자. 사소한건데.. colab만하다가 당연한걸 잊음..
# 그리고 항상 type과 dir을 통해 무엇인지 알아봐야함

my_home.index()  # 우리가 찾으려는 값 찾을 때
my_home.count()  # 내가 찾으려는 데이터가 몇개인지
my_home.insert(,)  # (몇번째자리, 무엇을 넣을지)
my_home.pop()  # 맨마지것을 빼고 다시 리스트
my_home.reverse()  # 역순으로 배열
my_home.sort()  # 정렬
my_home.remove()  # 제거하려는 값 제거

# tuple 순서가 있고 값의 변화에 줄 수 없음

my_home = ['광주', '서울', '경기도', '부산', '대전', '대구']

# dict 순서가 없고 무조건 key을 주고 value값을 줌 key값은 절대 중복하면 안됨.

my_things = {'computer': 1, 'mouse': [2, 3, 4, 5], 'phone': 3, 'book': 4}
my_things['computer']  # 그러면 내가 원하는 값을 줌
del my_things['computer']  # 이렇게 하면 값이 지워짐

my_things.items  # 이러면 키와 밸류값이 튜플형식으로 지정됨
my_things.values()  # 값들만 줌
my_things.keys()  # key들만 줌
my_things.copy()  # 하면 따로 복사가 된다는것을 잊말자

# set 순서가 없음. 값의 중복을 허락하지 않고 차집합, 합집합, 교집합을 알수 있음

animals = {'lion', 'tiger', 'tiger', 'tiger',
           'cat', 'dog', 'dog', 'dog', 'hawk'}
animals_a = set(animals)

print(animals_a)
