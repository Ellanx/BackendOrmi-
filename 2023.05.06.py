# 2023.05.06 study
# 산술연산자
today_get = 0
today_sell = 0
net = 0
today_rest = today_get - today_sell
real_net = today_sell

print(f'나는 오늘 {today_get} 마리 사냥했고 {today_sell} 마리를 팔았다')
print(f'오늘 재고는{today_rest}마리다. ')

print(f'오늘 {real_net}원을 벌었으니 내일은 꼭 {real_net*2}원을 벌겠다.')

# 또다른 예시

price_clss = {'A등급': 10000, 'B등급': 5000, 'C등급 ': 1000}

price_sum: (price_clss['A등급'] * 3) + {price_clss['B등급'] * 5}

give_money = 50000

# 산술연산자 정리
# + / * ** %(나머지) %%(몫만) ## ++ -- 는 Python에 존재하지 않음
# today_get += 10 을 처리하면 today_get = today_get + 10 이랑 똑같은 값을 가진다는 것을 기억하자 . 쓸데없느 반복을 줄일수가 있음

# 비교연산자 정리

# != (다르다!)   ===(JS에서 등장하는 것임)

# 논리연산자 정리
# and(곱) or(합) not a(아니다)

비트연산자  # 비트연산자는 크게 의미는 없음 그래도 지나가면서 배우기

a = bin(5)
b = bin(10)

print(a), print(b)
101
1010

# a&b 를 하면 비트값이 둘다 1인경우 1을 반환, 다르면 0을 반환한다는 것을 기억하기 즉 2값이 됨
# & and// | or // a << 2 => 0010 이 1000가 되어 8이됨
# a ^ b는 다른값은 1 같은값은 0 으로 값이 나옴
# ~a 는 +1 을 시키고 맨앞에 -(음수)를 취해줌
# 그래도 지금 당장은 이정도로 알고 지나가기

# 연산자 우선순위
# 리스트, 튜플, 딕셔너리, 셋
# 인덱싱, 슬라이싱
# **
# * @ / // %
# + -
# 비트연산 단위
# in, not in, is , is not
# 논리연산 (not, and, or)
# if, else
# lambda

# 기억할 것
a = 11111111
b = 11111111

a == b  # 는 True
a is b  # 는 Flase로 나옴  # 숫자가 커지면 false나 숫자가 작으면 true로 나옴! 메모리때문에

# in 구문
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]

2 in b, [2] in b, [1, 2, 3] in b  # true, false, false라는것을 잊지마시길

a = (1, 2, 3)  # 튜플
# 1 in a // (1) in a // (1,2) in a => true, false, false
b = {1, 2, 3}  # 셋
#  1 in a // {1} in a // {1,3} in a => true, false, false
c = {'key': 'value1', 'key2': 'value2'}
#  'key' in a // 'value1' in a // {'key2' : 'value2'} in a // ('key','key2') in a => true, false, error , false

#  함수
result = []  # 따로 값을 입력하고 싶으면


def today_get(x, y):  # (x,y)  =  파라미터
    z = x + y
    return z


print('sell : ', today_get(1, 3))  # today_get이라는 함수를 호출하는걸 아규먼트
print(today_get(4, 1), '개 팔았다.')  # 이렇게도 입력이 가능하다.

# 여러가지 입력할 시 이렇게도 가능


def sell_out(a, b, c):
    price = {'A등급': 100, 'B등급': 50, 'C등급': 10}
    sell_sum = a*price['A등급']+b*price['B등급']+c*price['C등급']
    return sell_sum


print(sell_out(3, 4, 5), '원이다')

# 전역변수 이미 밖에서 선언이 된것.
# 지역변수 안에서 선언된것. 전역변수가 선언된것이 다시 지역변수에서 다시 선언을 하면 오류가 발생함.

# global은 자주 사용되지는 않음

food = {'A등급': 0, 'B등급': 0, 'C등급': 0}


def buy_mine():
    food['A등급'] += 3
    return


buy_mine()
print(food)

# if else 문제

구매가격 = input('가격을 입력하세요 :')
회원명 = input('회원명을 입력하세요 :')

회원 = ['동', '임', '썽', '렁', '홍']

# if 회원명 in 회원:
#     print('회원입니다.')
#     print(f'{구매가격}원 중에서 {int(구매가격)*0.1}원이 적립되었습니다')
# else:
#     print('회원이 아닙니다. 회원가입을 해주세요.')

# input인경우 프롬르프에 등장하기에 거기에 값을 입력해주면된다. 콜랩이랑 약간 다르니 파이썬할 때마다 차이를 잘 구분해야한다. ㄴ
