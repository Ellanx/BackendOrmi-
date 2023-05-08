# break에 관하여

for i in range(5):
    print(f'{i}마리 건짐.')
    if i == 20:
        print('끝!')
        break
else:
    print('없다 이제!')
print('the end')

# list comprehension

l = []

for i in range(1, 201):
    l.append(i)

print(l)
# 바로 위랑 또같이 만들수 있음
ll == [i for i in rang(1, 201)]
print(ll)

# 중첩 구문에 대해서

for i in range(2, 10):
    for j in range(1, 10):
        print(f'{i} X {j} = {i*j}')

# 똑같은 말로 이렇게 표현될 수도 있음. 기억하자!
l = [f'{i} X {j} = {i*j}' for i in range(2, 10) for j in range(1, 10)]
print(l)

# 여기서 짝수 구구단만 나오게 할려면
l = [f'{i} X {j} = {i*j}' for i in range(2, 10)
     for j in range(1, 10) if i % 2 == 0]
print(l)

# 다중 리스트 for 문
my_skill = [('베기', 10, 'c'), ('찌르기', 15, 'c+'), ('파이어볼', 30, 'b')]

for i, j in my_skill:
    print(i, j)
# 이렇게 i,j만 프린트에 넣으면 0,1번째만 나옴 for i,j,k 까지하면 0,1,2번째까지 나온다는 것 잊지말기 !

# 이렇게 바꿀수 있음 또!! 가독성 좋게

for skillName, skillPower, skillGrade in my_skill:
    print(skillName, skillPower, skillGrade)  # 이렇게 하면 더 가독성이 좋아짐

for i, (skillName, skillPower, skillGrade) in enumerate(my_skill):
    print(i, skillName, skillPower, skillGrade)

# 참고


def solution(str1, str2):
    return 1 if str2 in str1 else 2


def solution(str1, str2):
    return 2 if str1.find(str2) == -1 else 1


def solution(str1, str2):
    return 1 if str2 in str1 else 2


def solution(n):
    return 1 if int(n ** 0.5) ** 2 == n else 2


def solution(n):
    return 1 if n ** 0.5 == int else 2


def solution(n):
    return 1 if (n ** 0.5).is_integer() else 2


def solution(sides):
    sides.sort(reverse=True)
    return 1 if sides[0] < sides[1] + sides[2] else 2
