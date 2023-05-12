# colab 사용법

* MAC을 사용하는 경우 Ctrl 대신 Command입니다. Alt 대신 Option입니다.
1. **실행 단축키**
    1. (필수) `Ctrl(Command)` + `Enter` : 해당 셀 실행
    2. `Shift` + `Enter` : 해당 셀 실행 + 커서를 다음 셀로 이동
    3. (필수) `Alt(Option)` + `Enter` : 해당 셀 실행 + 코드 불록 하단 추가
2. **셀 삽입/삭제 관련 단축키**
    1. `Ctrl(Command)` + M A : 코드 셀 위에 삽입
    2. `Ctrl(Command)` + M B : 코드 셀 아래 삽입
    3. `Ctrl(Command)` + M D : 셀 지우기
    4. `Ctrl(Command)` + M Y : 코드 셀로 변경
    5. `Ctrl(Command)` + M M : 마크다운 셀로 변경
    6. `Ctrl(Command)` + M Z : 실행 취소
3. 수정 관련된 단축키
    1. `Ctrl(Command)` + `Alt(Option)` + 화살표위아래 : 동시 수정
    2. (자주) `Ctrl(Command)` + D : 같은 단어 찾아 동시 수정
    3. `Ctrl(Command)` + `Shift` + L : 동일 단어를 전체로 찾아 동시 수정
    4. `Alt(Option)` + `Shift` + 화살표위아래 : 해당내용을 위나 아래 복사해서 붙여넣기
    5. `Alt(Option)` + 화살표위아래 : 해당 내용을 위나 아래로 보내기
    6. (자주) `Ctrl(Command)` + `Alt(Option)` + 화살표위아래 : 위아래 동시 수정
    7. (자주) Home, End : 문장의 양 끝
    8. (필수) `Ctrl` + `/` : 주석
    9. (필수) `Shift` + `Del` : 한 줄 지우기
    10. (필수) `Tab`, `Ctrl` + `]` : 들여쓰기
    11. (필수) `Shift` + `Tab`, `Ctrl` + `[` : 내어쓰기
4. 단축키 보기 및 설정
    1. `Ctrl(Command)` + M H : 단축키 모음

# 마크다운

* 필수 마크다운

    ```
    # hello
    ## hello
    ### hello

    1. hello
    2. hello
    3. hello

    * hello
    * hello
    * hello
    ```

* 선택 마크다운(필수가 아니니 부담가지지 마세요.)

    ```
    # h1
    ## h2
    ### h3
    #### h4
    ##### h5
    ###### h6

    ---

    1. hello
    2. hello
    3. hello

    * hello
    * hello
    * hello

    - hello
    - hello
    - hello

    __굵게__
    **굵게**
    _기울여 쓰기_
    *기울여 쓰기*
    ~취소선~
    ~~취소선~~

    > 인용문 작성하기
    `인라인 코드는 이렇게 작성해요.`

    [인라인 링크](https://velog.io/)

    ![이미지 설명](이미지 링크)
    
    * table은 직접 만들지 마시고 https://www.tablesgenerator.com/markdown_tables 와 같은 서비스를 이용하세요.
    
    | 1 | 2     | 3 | 4 | 5     |
    |---|-------|---|---|-------|
    | 1 | hello | 3 | 4 | world |

    * [ ] hello
    * [X] hello
    ```


# Python


```python
#행 단위 주석입니다.

"""
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
"""

'''
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
'''
```




    '\n큰 따옴표로 세번 묶거나\n작은따옴표로 세번 묶으면\n열단위 주석이 됩니다.\n'




```python
# 아래와 같이 열단위 주석으로 text를 넣을 수도 있습니다.
data = '''
큰 따옴표로 세번 묶거나
작은따옴표로 세번 묶으면
열단위 주석이 됩니다.
'''

data
```

* Code convention python
* https://google.github.io/styleguide/
* https://google.github.io/styleguide/pyguide.html


```python
def connect_to_next_port(self, minimum: int) -> int:
    """Connects to the next available port.

    Args:
      minimum: A port value greater or equal to 1024.

    Returns:
      The new minimum port.

    Raises:
      ConnectionError: If no available port is found.
    """
    if minimum < 1024:
        # Note that this raising of ValueError is not mentioned in the doc
        # string's "Raises:" section because it is not appropriate to
        # guarantee this specific behavioral reaction to API misuse.
        raise ValueError(f'Min. port must be at least 1024, not {minimum}.')
    port = self._find_next_open_port(minimum)
    if port is None:
        raise ConnectionError(
            f'Could not connect to service on port {minimum} or higher.')
    assert port >= minimum, (
        f'Unexpected port {port} when minimum was {minimum}.')
    return port
```


```python
connect_to_next_port
```


```python
# 띄어쓰기 4칸 (tab(스페이스 4칸과 다릅니다!), 6칸, 7칸 다 작동합니다.)
```


```python
# 아래와 같이 탭과 띄어쓰기 4번을 혼용하시면 error가 납니다.
for i in range(10):
    print(i)
	print('큰 따옴표로 세번 묶거나')
```


```python
a = 10     #int, 정수형
b = 10.1   #float, 실수
c = -1
d = True   #bool, 논리형(부울형, 참거짓형)
e = 'good'
f = '10'   #str, 문자열
g = 'kim'
h = 'honggildong'
i = 'example'
j = 10 + 2j #complex, 복소수
k = 0b110   #int, 2진법 
l = 0o56    #int, 8진법
m = 0xAC    #int, 16진법

##########
def hello(x):
    return x**2

class A: # 자동차 공장
    pass

n = hello # function
o = print # bulit-in function (https://docs.python.org/3/library/functions.html)
p = lambda x:x**2 # function
q = int # type
r = A # class
s = A() # instance # 자동차
##########

print(f'type(10) : {type(a)}')
print(f'type(10.1) : {type(b)}')
print(f'type(-1) : {type(c)}')
print(f'type(True) : {type(d)}')
print(f'type(\'good\') : {type(e)}')
print(f'type(\'good\'.upper) : {type(e.upper)}')
print(f'\'10\' + \'10\' : {f + f}')
print(f'\'10\' * 3 : {f * 3}')
print(f'\'hong\' + \'gildong\' : {g + h}')
print(f'type(\'gildong\') : {type(h)}')
print(f'type(\'gildong100!!\') : {type(i)}')
print(f'type(10 + 2j) : {type(j)}')
print(f'type(0b110) : {type(k)}')
print(k)
print(f'type(0o56) : {type(i)}')
print(i)
print(f'type(0xAC) : {type(m)}')
print(m)
print(f'type(def func():...생략...) : {type(n)}')
print(f'type(print) : {type(o)}')
print(f'type(lambda x:x**2) : {type(p)}')
print(f'type(int) : {type(int)}')
```

    type(10) : <class 'int'>
    type(10.1) : <class 'float'>
    type(-1) : <class 'int'>
    type(True) : <class 'bool'>
    type('good') : <class 'str'>
    type('good'.upper) : <class 'builtin_function_or_method'>
    '10' + '10' : 1010
    '10' * 3 : 101010
    'hong' + 'gildong' : kimhonggildong
    type('gildong') : <class 'str'>
    type('gildong100!!') : <class 'str'>
    type(10 + 2j) : <class 'complex'>
    type(0b110) : <class 'int'>
    6
    type(0o56) : <class 'str'>
    example
    type(0xAC) : <class 'int'>
    172
    type(def func():...생략...) : <class 'function'>
    type(print) : <class 'builtin_function_or_method'>
    type(lambda x:x**2) : <class 'function'>
    type(int) : <class 'type'>



```python
# 이스케이프 문자
# https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84_%EB%AC%B8%EC%9E%90
print('hello \n world')
print('hello \t world')
print('hello \' world')
print('hello \" world')
print('hello \\ world')
```

    hello 
     world
    hello 	 world
    hello ' world
    hello " world
    hello \ world



```python
# type -> string

hello = 10

print(r'hello \n world') # str -> raw (Django 2.x까지 url parsing을 이렇게 사용하고 있어요.)
print(f'hello \n world {hello}') # 앞으로 f-string 기법
print('hello world {}'.format(hello))
```

    hello \n world
    hello 
     world 10



```python
# type -> float
# 오일러의 수를 모른다 해서, 수학 연산이 약하다 해서 우리 수업에 문제가 되지 않습니다.
print(2.3e3) # 무리수, 오일러 수(2.718에 수렴, 파이가 3.14인 것처럼)
print(2.3E3)

2.3 * (10 ** 3)
```


```python
print(2.3e-3) # 무리수, 오일러 수(2.718에 수렴, 파이가 3.14인 것처럼)
print(2.3E-3)

2.3 * (10 ** -3)
```

    0.0023
    0.0023





    0.0023




```python
type(2.3E-3)
```




    float




```python
class A: # 자동차 공장
    pass

a = A # class
b = A() # instance # 자동차

print(type(a))
print(type(b))
```

    <class 'type'>
    <class '__main__.A'>



```python
# 변수를 처음 만나시면 type, dir을 해봅니다.
# type을 찍으면 검색 키워드를 알 수 있습니다.
# dir을 찍으면 속성을 알 수 있습니다.
type(a)
```




    int




```python
print(type(a))
```

    <class 'int'>



```python
dir(a)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']




```python
# 실무에서 자주 사용하는 구문
type(10)
type(10) == int
type(10.1) == float
```




    True




```python
# 위만큼 자주사용하진 않지만 타입 확인 코드
a = 10
isinstance(a, int)
isinstance(a, float)
```




    False



## 변수


```python
# CS 변수는 포스트잇
# 변수는 메모리 공간을 가리킵니다.

# x라는 포스트잇도 붙였지만
# y라는 포스트잇도 붙여져 있는 것입니다.
x = 10
y = 10

id(x), id(y) # id는 누굴 가리키고 있는지 그 주소값을 반환합니다.
```




    (139737727205904, 139737727205904)




```python
x is y
```




    True




```python
x = 257
y = 257

id(x), id(y)
```




    (139736413794128, 139736413797264)




```python
x is y
```




    False




```python
# Python은 자체적으로 속도를 높이기 위한 
# 여러가지 노력들을 해왔습니다.
# (아래 언급한 것 말고도 각각의 자료형에서 메모리를 효율적으로 관리하기 위한 노력들을 말씀드리겠습니다.)
# 구버전도 말씀을 드릴 것인데 이유는 여러분이 실무에가서 접할 환경이 최신 버전이 아니기 때문입니다.
# 야xx의 경우에는 Django 1.x, python 2.x를 사용하고 있어요. 
# 대부분의 기업들이 한 번 구축해놓은 시스템은 바꾸기가 쉽지 않습니다.

# 그래서 -5 ~ 256은 먼저 메모리에 적재를 합니다.
```


```python
x = -5
y = -5

id(x), id(y)
```




    (139737727205424, 139737727205424)



* 변수의 타입이란 무엇인가?
* 변수의 타입은 왜 있는 것일까?
* 어떤 고민을 통해 변수의 속성을 정했을까?


```python
'a' + 'a'
```




    'aa'




```python
# 왜 이어 붙였지?
# 컴퓨터 입장에서 a는 97(인간이 보는 숫자) -> 0x61! 결국 숫자!
```


```python
# cpython -> 이어 붙이라고 정의가 되어 있어서
# 사회 통념적인 약속 -> 코드로 구현
# type, dir
# 이러한 약속들은 메직메서드(__init__.....)를 통해 구현하게 됩니다.
```

## 변수의 속성 변경


```python
'10' + '10'
```




    '1010'




```python
int('10') + int('10')
```




    20




```python
# 지금 배우는 포인트는 class가 중요한 문법이 아니라
# 이러한 '약속'을 우리가 변경할 수 있다가 중요한 포인트입니다.
class int(int):
    def __add__(self, a):
        return 'leehojun'

int('10') + int('10')
```




    'leehojun'




```python
class int(int):
    def __add__(self, a):
        return self * a

int('10') + int('10')
```




    100




```python
dir(10)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']




```python
class int(int):
    def 제곱(self, 승수):
        return self ** 승수

value = int('10')
print(dir(value))
```

    ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dict__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__module__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes', '제곱']



```python
value.제곱(3)
```




    1000




```python
x = 10
y = x
z = y

print(id(x), id(y), id(z))
```

    139737727205904 139737727205904 139737727205904



```python
x = 10
y = x
x = 100

print(x, y)
print(id(x), id(y), id(z))
```

    100 10
    139737727208784 139737727205904 139737727205904


## 변수의 속성

* 변수는 주로 스네이크 표기법을 많이 사용합니다. 물론 회사 컨벤션에 따르셔야 합니다.
* 영문과 숫자를 사용할 수 있지만, 숫자로  시작하지는 못합니다.
* 특수문자는 사용하지 않아요.(언더바(_)는  사용합니다. 스네이크 표기법, 특수문자나  이미중 사용 가능한 것들이 있기는 합니다.  권하지 않습니다.)
* 예약어는 사용하지 않습니다.(if, elif, while, * for, etc)
* 대소문자는 구분합니다.
* 언더바로만 사용하거나 언더바로 시작할 수 있습니다.
* 대문자로 시작하는 변수를 사용할 수 있지만, 관습적으로 대문자로 시작하는 변수는 Class로 만들기 때문에 소문자로 시작하는 변수를 만들기를 권합니다. Class는 보통 파스칼 표기법을 따릅니다. 다만 회사 컨벤션마다 다릅니다.


```python
# 스네이크 표기법(Python에서 주로)
hello_world = 10
# 카멜 표기법(JavaScript에서 주로)
helloWorldHello = 10
# 파스칼 표기법(Class 같은 곳에서 많이 사용합니다.)
Hello = 10
```


```python
# 10hello = 100
hello10 = 10

π = 3.14 # 권하지 않습니다.
print(π)

_ = 100 # 언더바는 자주사용되는데 이렇게 사용되진 않습니다.
print(_)
```

    3.14
    100



```python
for _ in range(10): # 언더바를 순회 안에서 변수로 사용하지 않을때
    print('hello')
```

    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello
    hello



```python
# if = 100
# print = 100
```


```python
# print('hello')
```


```python
print(a)
```

## 입력과 출력


```python
x = input()
x
```

    10





    '10'




```python
x + x # 사용자에게 받은 입력은 str
```




    '1010'




```python
print(10, 10, 10)
```

    10 10 10



```python
print('hello', 'world', 'hello')
```

    hello world hello



```python
print(x, x)
```

    10 10



```python
print('hello world', end='!')
print('hello world', end='!')
print('hello world', end='!')
```

    hello world!hello world!hello world!


```python
print('hello', 'world', sep='!')
print('010', '5044', '2903', sep='-')
```

    hello!world
    010-5044-2903



```python
이름 = '이호준'
나이 = 10

print('1. 제 이름은 이호준입니다. 제 나이는 10입니다.')
print('2. 제 이름은 ', 이름, '입니다. 제 나이는 ', 나이, '입니다.', sep='')
print('3. 제 이름은 %s입니다. 제 나이는 %d입니다.'%(이름, 나이))
print('4. 제 이름은 {}입니다. 제 나이는 {}입니다.'.format(이름, 나이))
print(f'4. 제 이름은 {이름}입니다. 제 나이는 {나이}입니다.')
```

    1. 제 이름은 이호준입니다. 제 나이는 10입니다.
    2. 제 이름은 이호준입니다. 제 나이는 10입니다.
    3. 제 이름은 이호준입니다. 제 나이는 10입니다.
    4. 제 이름은 이호준입니다. 제 나이는 10입니다.
    4. 제 이름은 이호준입니다. 제 나이는 10입니다.


[포멧코드](https://www.notion.so/paullabworkspace/9fd33417740f4eba8715f5c4a1ed7c7b?v=e01ecdfe2f9448dcaad68b03a38057a5)

## formatting


```python
print(f'{100 * 10}')
```

    1000



```python
# 중괄호 안에서 복잡한 연산을 하시는 것을 권하지 않습니다.
result = 100 * 10
print(f'{result}')
```


```python
# 이런 문법은 필요에 의해 검색해 보시다 보면 익숙해집니다.
print(f'{"hello":<10}')
print(f'{"hello":>10}')
print(f'{"hello":^10}')
```

    hello     
         hello
      hello   



```python
txt = 'hello'
i = 10
print(f'{txt:>10}')
print(f'{txt:>{i}}')
```

         hello
         hello



```python
# 이런 문법은 필요에 의해 검색해 보시다 보면 익숙해집니다.
print(f'{"hello":!<10}')
print(f'{"hello":!>10}')
print(f'{"hello":!^10}')
```

    hello!!!!!
    !!!!!hello
    !!hello!!!



```python
# 이런 문법은 필요에 의해 검색해 보시다 보면 익숙해집니다.
print(f'{"hello":=<10}')
print(f'{"hello":=>10}')
print(f'{"hello":=^10}')
```

    hello=====
    =====hello
    ==hello===



```python
# 둘 다 잊으셔도 됩니다.
# 어디에 활용되는지 궁금하다 하신 분이 있으셔서 해드린 것입니다.
# https://tech.kakao.com/2017/09/27/kakao-blind-recruitment-round-1/
bin(9)
print(f'{bin(9)[2:]:0>5}')
```

    01001



```python
bin(9 | 30)[2:].replace('1', '#').replace('0', ' ')
```




    '#####'




```python
# 요정도 활용을 합니다.
print(f'{"start":-^20}')
```

    -------start--------



```python
print(f'{0.12345:0.2f}')
```

    0.12


* 이 아래 코드는 필수는 아닙니다. 참고삼아서만 넣어드립니다.


```python
# 이전 방식
print('나의 이름은 %s입니다'%('한사람'))
print('나의 이름은 "%s"입니다. 나이는 %d세이고 성별은 %s입니다.'%('한사람',33,'남성'))
print('나이는 %d세이고 성별은 %s입니다. 나의 이름은 %s입니다. '%(33,'남성','한사람'))
print('나이는 %03d세이고 신장은 %6.2f입니다. 나의 이름은 %s입니다. '%(33,56.789,'한사람'))
print('-' * 40)

# 파이썬(Python) 3 포맷팅 방식
print('나의 이름은 {}입니다'.format('한사람'))
print('나의 이름은 {0}입니다. 나이는 {1}세이고 성별은 {2}입니다.'.format('한사람',33,'남성'))
print('나이는 {1}세이고 성별은 {2}입니다. 나의 이름은 {0}입니다. '.format('한사람',33,'남성'))
print('나이는 {age}세이고 성별은 {gender}입니다. 나의 이름은 {name}입니다. '
         .format(name='한사람',age=33,gender='남성'))
print('만세삼창 :  {0}!!! {0}!!! {0}!!! '.format('만세'))
print('삼삼칠 박수 :  {0}!!! {0}!!! {1}!!! '.format('짝'*3,'짝'*7))
print('-' * 40)

# 파이썬(Python) 3.6 f-string 방식
something = '볼펜'
EA = 2
one_length = 5.343
scale = 'cm'

print(f'{something} {EA}개의 길이는 {one_length*EA}{scale} 입니다.')
print(f'{something} {EA}개의 길이는 {one_length*EA:.1f}{scale} 입니다.')
```

    나의 이름은 한사람입니다
    나의 이름은 "한사람"입니다. 나이는 33세이고 성별은 남성입니다.
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다. 
    나이는 033세이고 신장은  56.79입니다. 나의 이름은 한사람입니다. 
    ----------------------------------------
    나의 이름은 한사람입니다
    나의 이름은 한사람입니다. 나이는 33세이고 성별은 남성입니다.
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다. 
    나이는 33세이고 성별은 남성입니다. 나의 이름은 한사람입니다. 
    만세삼창 :  만세!!! 만세!!! 만세!!! 
    삼삼칠 박수 :  짝짝짝!!! 짝짝짝!!! 짝짝짝짝짝짝짝!!! 
    ----------------------------------------
    볼펜 2개의 길이는 10.686cm 입니다.
    볼펜 2개의 길이는 10.7cm 입니다.



```python
print('Python is [{:15}]'.format('good'))
print('Python is [{:<15}]'.format('good'))
print('Python is [{:>15}]'.format('good'))
print('Python is [{:^15}]'.format('good'))
print('당신의 나이는 [{:15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('당신의 나이는 [{:>15}]세'.format(22))
print('당신의 나이는 [{:<15}]세'.format(22))
print('-' * 40)
```

    Python is [good           ]
    Python is [good           ]
    Python is [           good]
    Python is [     good      ]
    당신의 나이는 [             22]세
    당신의 나이는 [22             ]세
    당신의 나이는 [             22]세
    당신의 나이는 [22             ]세
    ----------------------------------------



```python
char_a = '5'
int_a = 5

'''기본적으로 {} 포맷팅의 특성을 그대로 가짐'''
print(1234567890)
print(f'{char_a:>5}') # >는 오른쪽정렬
print(f'{char_a:<5}') # <는 왼쪽정렬
print(f'{char_a:^5}') # ^는 가운데정렬
print(f'{int_a:0<5}')# <는 왼쪽정렬, 빈자리를 0으로 채울수도 있음
print(f'{int_a:^10.2f}') # ^ 가운데 정렬하면서 float 타입지정
```

    1234567890
        5
    5    
      5  
    50000
       5.00   


## int (정수)

* 파이썬에서는 숫자를 정수, 실수, 복소수로 나눠 표현합니다.
* 2진수, 8진수, 16진수는 정수로 표현됩니다.


```python
a = 1234567899999999999999999999999999999999999999999999999999999
print(type(a))
# 2.x에서는 int와 long 두 가지가 있었는데 Python3에서는 int만 있습니다! 아무리 큰 수가 담겨도 int!
```

    <class 'int'>



```python
a = 10**100 # 구골(googol)
print(a)
print(type(a))
```

    10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
    <class 'int'>



```python
10 # 정수
-10 # 정수
10.1 # 실수

a = 10
type(a)
dir(a)
```




    ['__abs__',
     '__add__',
     '__and__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__index__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__invert__',
     '__le__',
     '__lshift__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__or__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     '__xor__',
     'as_integer_ratio',
     'bit_count',
     'bit_length',
     'conjugate',
     'denominator',
     'from_bytes',
     'imag',
     'numerator',
     'real',
     'to_bytes']




```python
'bit_length' # bit로 바꾸었을 때 비트의 길이
'to_bytes' # 컴퓨터에 저장하는 바이트의 형태로 숫자를 표현
```


```python
# 1Bit, 0 ~ 1 # bit - 1자리
# 1Bytes = 8bit, 00000000 ~ 11111111 # 1byte - 8bit
# 1KB (키로바이트) = 1024Bytes
# 1MB (메가바이트) = 1024KB
# 1GB (기가바이트) = 1024MB
# 1TB (테라바이트) = 1024GB
# 1PB (페타바이트) = 1024TB
```


```python
(9).bit_length() # 1001
```




    4




```python
# 컴퓨터가 숫자를 어떻게 저장하는가?
(2).to_bytes(1, byteorder='little', signed=True)
(1).to_bytes(1, byteorder='little', signed=True)
(0).to_bytes(1, byteorder='little', signed=True)
(-1).to_bytes(1, byteorder='little', signed=True)
(-2).to_bytes(1, byteorder='little', signed=True)
```




    b'\xfe'




```python
# 컴퓨터는 음수를 자체적으로 표현할 수 없기에 2의 보수를 사용합니다. 
# 1의 보수를 사용하게 되면 +0과 -0이 존재하게 됨으로 비트 하나를 낭비하게 됩니다. 
# 따라서 2의 보수를 사용합니다.
```


```python
# 0000 0001 # 1
# 1111 1110 # 1의 1의 보수
# 1111 1111 # 1의 2의 보수 => ff
```


```python
# 진법 변환 쉽게 하는 법 : 가장 가까운 승수를 찾아 더하거나 뺍니다.
# 10진법
# 0 1 2 3 4 5 6 7 8 9 -> 10
# 1324 = 1*10^3 + 3*10^2 + 2*10^1 + 4*10^0

# 2진법
# 0 1 -> 10
# 1001 = 1*2^3 + 1*2^0 = 9

# 8진법
# 0 1 2 3 4 5 6 7 -> 10

# 16진법
# 0 1 2 3 4 5 6 7 8 9 a b c d e f -> 10
```


```python
# color의 표현
# 2596be
# 000000 ~ ffffff
# ff는 10진수로 무슨 숫자를 의미
# 100 - 1 => ff가 됩니다. 그래서 256 - 1
```


```python
a = 10
type(a)
```




    int




```python
int('10') + int('10')
```




    20




```python
int('10', 2) # 2진법으로 10은?
```




    2




```python
int('10', 8) # 8진법으로 10은?
```




    8




```python
int('10', 16) # 16진법으로 10은?
```




    16




```python
print(0b110) # 바이너리 - 2진수
print(0o110) # 옥타 - 8진수
print(0x110) # 헥사 - 16진수
```




    6




```python
type(0b110)
```




    int




```python
a = 10
type(a) == int
isinstance(a, int)
```




    True



## float (실수)


```python
a = 10.1

type(a)
```




    float




```python
dir(a)
```




    ['__abs__',
     '__add__',
     '__bool__',
     '__ceil__',
     '__class__',
     '__delattr__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__eq__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getformat__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__int__',
     '__le__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__neg__',
     '__new__',
     '__pos__',
     '__pow__',
     '__radd__',
     '__rdivmod__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rfloordiv__',
     '__rmod__',
     '__rmul__',
     '__round__',
     '__rpow__',
     '__rsub__',
     '__rtruediv__',
     '__setattr__',
     '__setformat__',
     '__sizeof__',
     '__str__',
     '__sub__',
     '__subclasshook__',
     '__truediv__',
     '__trunc__',
     'as_integer_ratio',
     'conjugate',
     'fromhex',
     'hex',
     'imag',
     'is_integer',
     'real']




```python
a = 10
b = 10.1

a + b # 다른 일부 언어에서는 허용되지 않습니다. 
```




    20.1




```python
# 부동소수점 오차(2진법으로 변환했을 때 0.1이 무한대수가 발생합니다.)
0.1 + 0.2 # 대부분의 언어 공통입니다.
```




    0.30000000000000004




```python
a = 0.1
```


```python
# 20번 반복해보세요.
a = a + 0.1
a
```




    1.0999999999999999



* https://docs.python.org/ko/3/tutorial/floatingpoint.html
* https://0.30000000000000004.com/ 에서 언어별 해결책을 제시한다.
* 컴퓨터에서 부동소수점 숫자는 2진 분수로 표현되기에 무한대수가 발생한다.
* [무한수가 발생되는 원리](https://www.notion.so/paullabworkspace/5f34f21bf9a34015b170e7afd7da9593)

## !! 오늘 배운 것 정리
1. 단축키
    * (필수) Ctrl(Command) + Enter : 해당 셀 실행
    * (필수) Alt(Option) + Enter : 해당 셀 실행 + 코드 불록 하단 추가
    * (필수) Ctrl + / : 주석
    * (필수) Shift + Del : 한 줄 지우기
    * (필수) Tab, Ctrl + ] : 들여쓰기
    * (필수) Shift + Tab, Ctrl + [ : 내어쓰기

2. 마크다운
    ```
    # hello
    ## hello
    ### hello

    1. hello
    2. hello
    3. hello

    * hello
    * hello
    * hello
    ```

3. 주석

    ```python
    #행 단위 주석입니다.

    """
    큰 따옴표로 세번 묶거나
    작은따옴표로 세번 묶으면
    열단위 주석이 됩니다.
    """

    '''
    큰 따옴표로 세번 묶거나
    작은따옴표로 세번 묶으면
    열단위 주석이 됩니다.
    '''
    ```

4. PEP8 권고사항
    * 띄어쓰기는 4칸
    * 한 줄에 79자 이상을 사용하지 않는다.

5. 형의 종류(type, dir)
    * 컨벤션 자료형(list, tuple, dict, set)은 나중에 진행합니다.
    * int
    * float
    * bool
    * str
    * function
    * bulit-in function

6. 이스케이프 문자
    * https://ko.wikipedia.org/wiki/%EC%9D%B4%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%94%84_%EB%AC%B8%EC%9E%90
    ```python
    print('hello \n world')
    print('hello \t world')
    print('hello \' world')
    print('hello \" world')
    print('hello \\ world')
    ```

7. 실무에서 자주 사용하는 타입확인 구문
    ```python
    type(10)
    type(10) == int
    type(10.1) == float

    a = 10
    isinstance(a, int)
    isinstance(a, float)
    ```

8. 변수의 인사이트
    ```
    dir을 입력했을 때
    1. __hello__와 같은 형태의 메직 메서드는 속성을 표현한다
    2.  언더바가 없는 메서드는 해당 자료형의 편의 기능을 제공한다
    ```

9. 입력과 출력
    ```python
    x = input() #입력, 숫자를 입력해도 str
    print(x) #출력

    이름 = '이호준'
    나이 = 10
    print(f'제 이름은 {이름}입니다. 제 나이는 {나이}입니다.')
    print(f'{100 * 10}')
    ```


10. int 형
    * 2진수, 8진수, 16진수는 정수


11. float 형
    * 부동소수점 오차(2진법으로 변환했을 때 0.1이 무한대수가 발생합니다.)
    0.1 + 0.2 # 대부분의 언어 공통입니다.
    * https://docs.python.org/ko/3/tutorial/floatingpoint.html
    * https://0.30000000000000004.com/ 에서 언어별 해결책을 제시한다.

## str (문자열)

- 순서가 있는 **시퀀스 자료형**입니다.
- 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표('''str''', """str""")로 감싸는 것도 가능합니다. (삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
- 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
- 이스케이프 문자도 사용이 가능합니다.
- 리스트, 튜플도 시퀀스 자료형입니다.


```python
s = 'paullab CEO leehojun'
s[0] # 0은 index입니다. 이렇게 호출하는 것을 indexing이라고 합니다.
```




    'p'




```python
type(s)
```




    str




```python
dir(s)
```




    ['__add__',
     '__class__',
     '__contains__',
     '__delattr__',
     '__dir__',
     '__doc__',
     '__eq__',
     '__format__',
     '__ge__',
     '__getattribute__',
     '__getitem__',
     '__getnewargs__',
     '__gt__',
     '__hash__',
     '__init__',
     '__init_subclass__',
     '__iter__',
     '__le__',
     '__len__',
     '__lt__',
     '__mod__',
     '__mul__',
     '__ne__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__rmod__',
     '__rmul__',
     '__setattr__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     'capitalize',
     'casefold',
     'center',
     'count',
     'encode',
     'endswith',
     'expandtabs',
     'find',
     'format',
     'format_map',
     'index',
     'isalnum',
     'isalpha',
     'isascii',
     'isdecimal',
     'isdigit',
     'isidentifier',
     'islower',
     'isnumeric',
     'isprintable',
     'isspace',
     'istitle',
     'isupper',
     'join',
     'ljust',
     'lower',
     'lstrip',
     'maketrans',
     'partition',
     'removeprefix',
     'removesuffix',
     'replace',
     'rfind',
     'rindex',
     'rjust',
     'rpartition',
     'rsplit',
     'rstrip',
     'split',
     'splitlines',
     'startswith',
     'strip',
     'swapcase',
     'title',
     'translate',
     'upper',
     'zfill']




```python
# 문자열의 메서드
# 'capitalize','casefold','center','count','encode',
# 'endswith','expandtabs','find','format','format_map',
# 'index','isalnum','isalpha','isascii','isdecimal','isdigit',
# 'isidentifier','islower','isnumeric','isprintable','isspace',
# 'istitle','isupper','join','ljust','lower','lstrip',
# 'maketrans','partition','removeprefix','removesuffix',
# 'replace','rfind','rindex','rjust','rpartition','rsplit',
# 'rstrip','split','splitlines','startswith','strip','swapcase',
# 'title','translate','upper','zfill'
```


```python
s = 'paullab CEO leehojun'
s.lower(), s.upper() 
# 특히 사용자에게 입력을 받는 경우 lower도 많이 사용합니다.
```




    ('paullab ceo leehojun', 'PAULLAB CEO LEEHOJUN')




```python
s = 'paullab CEO leehojun'
s.find('C'), s.index('C')
```




    (8, 8)




```python
# 견고한 코드란?
# 시간이 지나도 그대로 사용할 수 있고
# error가 예측 가능하게 나는 코드
# 네이버에 이미지 슬라이딩 코드
# bool(s.find('Z')) => -1은 True이기 때문에 주의가 필요합니다.
s.find('Z')
```




    -1




```python
# Error가 나면 Error를 주는 것이 좋을 수 있습니다.
# Error를 안주는 언어로 JavaScript
s.index('Z')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-13-85c68513f932> in <cell line: 3>()
          1 # Error가 나면 Error를 주는 것이 좋을 수 있습니다.
          2 # Error를 안주는 언어로 JavaScript
    ----> 3 s.index('Z')
    

    ValueError: substring not found



```python
s = 'paullab CEO leehojun'
s.find('CEO')
```




    8




```python
# 별 5개
s = 'paullab CEO leehojun'
s.count('l')
```




    3




```python
str([1, 2, 3, 4, 5])
```




    '[1, 2, 3, 4, 5]'




```python
str([1, 2, 3, 4, 5]).count(' ')
```




    4




```python
str([1, 2, 3, 4, 5]).count(',')
```




    4




```python
str([1, 2, 11, 4, 111]).count('1')
```




    6




```python
str(list(range(0, 10001))).count('8')
```




    4000



* https://codingdojang.com/scode/393?answer_mode=hide


```python
str([1,2,3,4,5]).count(' ') 
# list는 콤마 다음에 공백이 없더라도 공백으로 인식해줍니다.
```




    4




```python
str([1,
     2,
     3,
     4,
     5]).count(' ')
# list는 콤마 다음에 공백이 없더라도 공백으로 인식해줍니다.
```




    4




```python
'hello'.count('')
```




    6




```python
'a'.count('')
```




    2




```python
''.count('')
```




    1




```python
'' + ''
```




    ''




```python
'   hello   !  '.strip() # 공백제거 메서드
```




    'hello   !'




```python
'   hello   !  '.rstrip()
```




    '   hello   !'




```python
'   hello   !  '.lstrip()
```




    'hello   !  '




```python
# 별 5개
'hello world hi'.replace(' ', '!')
'hello world hi'.replace('world', 'W@O@R@L@D').upper()
```




    'HELLO W@O@R@L@D HI'




```python
'hello world hi'.replace('world', 'W@O@R@L@D').upper().split('@')
# 반환값이 list이기 때문에 메서드 체이닝을 하려면 
# 이후로 list 메서드를 사용해야 합니다.
```




    ['HELLO W', 'O', 'R', 'L', 'D HI']




```python
'hello world hi'.replace(' ', '')
```




    'helloworldhi'




```python
data = '''  "+ +-+ -+-"  
  "++ -- +-+"  
  "++-+ -+ -"  
  "+ ++-+ -+"  '''

data.split('\n')[0].replace(' ', '').replace('"', '')

# Pythonic하지 않다!
data.split('\n')[0].replace(' ', 
                '').replace('"', 
                '')

# Pythonic하게 하려면
data.split('\n')[0]\
                .replace(' ', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')\
                .replace('"', '')

# 제가 사용하는 기법
processed_string = data.split('\n')[0].replace(' ', '').replace('"', '')
processed_string.replace('"', '').replace('"', '')
```




    '++-+-+-'




```python
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 79자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 39자
```


```python
data = '''  "+ +-+ -+-"  
  "++ -- +-+"  
  "++-+ -+ -"  
  "+ ++-+ -+"  '''

data.split('\n')[0].replace(' ', '').replace('"', '').replace('+', '1').replace('-', '0')
ord('A'), chr(65) # ord는 문자를 가지고 숫자로 변경 chr은 숫자를 가지고 문자로 변경합니다.

숫자 = data.split('\n')[0].replace(' ', '').replace('"', '').replace('+', '1').replace('-', '0')
int(숫자, 2)
chr(int(숫자, 2))
```




    'j'




```python
# 별 4.5개
'paullab CEO leehojun'.split(' ') #문자열을 쪼개어 줍니다.
'paullab!CEO!leehojun'.split('!')
'paullab,CEO,leehojun'.split(',')
```




    ['paullab', 'CEO', 'leehojun']




```python
# 퀴즈
'010 5044 2903' # 1번
'010-5044-2903' # 2번
'010 5044-2903' # 3번
```


```python
# 원하는 결과값
# ['010', '5044', '2903']
# [10, 5044, 2903] # 010은 error가 나기 때문에 10으로 저장
```




    [10, 5044, 2903]




```python
'010 5044 2903'.split(' ')
'010-5044-2903'.split('-')
'010 5044-2903'.replace(' ', '-').split('-')
```




    ['010', '5044', '2903']




```python
'010 5044 2903'.split() # 공백단위가 들어가기 됩니다.
```




    ['010', '5044', '2903']




```python
# '01050442903'.split('') # 빈 문자열을 넣지는 못합니다.
```


```python
list(map(int,'010 5044 2903'.split(' ')))
```


```python
int('010')
```




    10




```python
# print(010) # error
```


```python
num ='010 5044-2903'.replace('-',' ').split(' ')
[int(i) for i in num] # 리스트 컴프리헨션 사용
list(map(int, '010 5044 2903'.split(' ')))

# 2개 모두 새로운 리스트를 만드는 것입니다.
# 원본을 변경시키지 않습니다.
```




    [10, 5044, 2903]




```python
# 이 코드 보다는
s = []
for i in '010 5044-2903'.replace('-',' ').split(' '):
    s.append(int(i))
s

# 요 코드를 추천합니다.
[int(i) for i in num]
```




    [10, 5044, 2903]




```python
# 지금 진도에서 과하기 때문에 
# 지금은 잊으셔도 됩니다.
# 뒤에서 상세하게 다룹니다.
def 제곱함수(x):
    return x ** 2

def 정수함수(x):
    return int(x)

list(map(제곱함수, [1, 2, 3]))
list(map(정수함수, ['1', '2', '3']))
list(map(int, ['1', '2', '3']))

list(map(int, ['010', '5044', '2903']))
list(map(int,'010 5044 2903'.split(' ')))
```




    [10, 5044, 2903]




```python
# 별 4.5 개
'~'.join(['hello', 'world', 'hello'])
'!'.join(['hello', 'world', 'hello'])
''.join(['hello', 'world', 'hello'])
' '.join(['hello', 'world', 'hello'])
```




    'hello world hello'




```python
'hello'.isalpha()
```




    True




```python
'he llo'.isalpha()
```




    False




```python
'123'.isdigit()
```




    True




```python
'12a3'.isdigit(), '12 3'.isdigit()
```




    False




```python
'12a3'.isalnum(), '12 3'.isalnum()
```




    (True, False)




```python
'안녕하세요!'.isalpha(), '안녕하세요!'.isalnum()
```




    (False, False)




```python
# 퀴즈
# 숫자를 모두 더하라!
result = 0
for i in '123abc913sldlf':
    # print(i.isdigit())
    if i.isdigit():
        result += int(i) # result = result + int(i)
result
```




    19




```python
result = 0
for i in '123abc913sldlf':
    if i.isdigit():
        result += int(i)
result
```


```python
'paullab CEO leehojun'.isascii()
```




    True




```python
'paullab CEO leehojun'.rjust(30) #오른쪽 정렬
'paullab CEO leehojun'.ljust(30) #왼쪽 정렬
'paullab CEO leehojun'.center(30)#가운데 정렬
```




    '     paullab CEO leehojun     '




```python
'hello'.zfill(20) # 데이터의 빈 공간을 0으로 채워줍니다.
```




    '000000000000000hello'




```python
'1001'.zfill(5)
'hello'.zfill(10).replace('0', '-')
```




    '-----hello'




```python
규칙테이블 = str.maketrans({'\n':'', '\t':''})
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)
```




    'paullab  CEO  leehojun'




```python
'paullab \n\n\n CEO \t\t\t leehojun'.replace('\n', '').replace('\t', '')
```




    'paullab  CEO  leehojun'




```python
규칙테이블 = str.maketrans('\n\t', '  ') # 똑같은 길이를 가지고 있어야 함
'paullab \n\n\n CEO \t\t\t leehojun'.translate(규칙테이블)
```




    'paullab     CEO     leehojun'




```python
규칙테이블 = str.maketrans('le','12')
'paullab CEO leehojun'.translate(규칙테이블) #어떤 규칙을 정하는것
```




    'pau11ab CEO 122hojun'



## pep


```python
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa => 80자
# 아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아아 => 40자면 한글 넘어갑니다.
# line에 딱 맞춰 들어간 것을 볼 수 있습니다. 
# 강제사항은 아닙니다.
# 띄어쓰기 4번도 강제사항은 아닙니다.
# pep8, pep20에 기술되어 있습니다. => pep(Python Enhancement Proposal)란 무엇인가요? 8이란 무엇인가요?
# pep8 : Style Guide for Python Code (https://peps.python.org/pep-0008/)
# pep20 : The Zen of Python(https://peps.python.org/pep-0020/) #이스터애그로 숨겨져 있습니다.
# https://peps.python.org/
```

## cpython

* 공식홈페이지에서 다운로드 받는 것이 cpython입니다.
* https://github.com/python/cpython
* list를 구현한 코드 : https://github.com/python/cpython/blob/main/Objects/listobject.c

## 인덱싱과 슬라이싱


```python
name = 'Guido van Rossum'
print(name[0])
print(name[1])
print(name[2])
```

    G
    u
    i



```python
# s[start:stop:step]
s = 'paullab CEO leehojun'
s[5:]
s[:5]
s[3:10]
s[:]
s[0:20:2]
```




    'pulbCOleou'




```python
# 자주 사용되는 코드
s = 'paullab CEO leehojun!'
s[:] # string에서는 많이 사용하지 않지만 list에서 많이 사용합니다.
s[:-1] # 마지막 요소만 제외하고 다 슬라이싱 합니다.
```




    'paullab CEO leehojun'




```python
test = [1, 2, 3, 4]
test2 = test
test2[0] = 1000
test, test2
```




    ([1000, 2, 3, 4], [1000, 2, 3, 4])




```python
test = [1, 2, 3, 4]
test2 = test[:] # 새로운 리스트를 만들어서 test2에게 줍니다.
test2[0] = 1000
test, test2
```




    ([1, 2, 3, 4], [1000, 2, 3, 4])



## 문자열의 연산


```python
s = 'hello world'
dir(s)
s + s
s * 3
```




    'hello worldhello worldhello world'



## 형변환

* 형변환 : type을 변경하는 것입니다.


```python
x = int(input())
x + x # but 알파벳 입력하면 error!
```


```python
x = input()
if x.isdigit():
    x = int(x) # but 알파벳 입력하면 error!
x + x
```

    10





    20




```python
# int('abc') # error
int(10.1) # 버림
int('10') # 형변환 가능
# int('10.1') # 형변환 불가능
```


```python
float('10') # 형변환 가능
float('10.1') # 형변환 가능
```




    10.1




```python
int('10a') # 되는 언어가 있어서 보여드린 것입니다.
# Python에서는 허용하지 않습니다.
```


```python
def hello():
    pass

str(type)
str(hello)

str('123')
str(True)
str(None)
str([1, 2, 3])
str({1, 2, 3})
str({'one':1, 'two':2})
```




    "{'one': 1, 'two': 2}"




```python
# 별 5개
# bool 형으로 형변환 하는 것
if True:
    print('hi')

if 'hello':
    print('hi')

# 정말 많이 사용하는 코드
l = [1, 2, 3]
while l:
    print(l.pop())

bool('') # 빈 문자열을 제외하고 모두 True
bool('a')
bool('False') # 문자열 False이기 때문에 True
bool(0) # 0을 제외하고 모두 True
bool(-1)
bool(100)
bool(None) # None은 비어있음을 명시해주는 키워드, False
bool([]) # 컨벤션 자료형은 비어있으면 False입니다.
bool({})
```

    hi
    hi





    False




```python
# list로 형변환
s = '10'
l = list(s)
l
```




    ['1', '0']




```python
s = 'leehojun'
l = list(s)
l
```




    ['l', 'e', 'e', 'h', 'o', 'j', 'u', 'n']




```python
# tuple로 형변환
s = 'leehojun'
l = tuple(s)
l
```




    ('l', 'e', 'e', 'h', 'o', 'j', 'u', 'n')




```python
# dict
# name = 'leehojun' # error
# dict(name)

s = [('name','leehojun'), ('age',10)]
d = dict(s)
d
```




    {'name': 'leehojun', 'age': 10}




```python
# set(집합)으로 형변환
name = 'leehojun'
set(name)
```




    {'e', 'h', 'j', 'l', 'n', 'o', 'u'}




```python
len('hello world') # __len__
len([1, 2, 3, 4])
```




    4



## !! 문제풀이


```python
# 1번의 오답(아래처럼 변수를 선언하지 않도록 주의해주세요.)

#1번
# print = 100

#2번
# 10 = a

#4번
# 100k = 10000
```


```python
# 2번
user_input = input('문자를 입력해주세요!')
print(user_input * 2)
```

    문자를 입력해주세요!hello
    hellohello



```python
print(input('문자를 입력해주세요!') * 2)
```

    문자를 입력해주세요!hello
    hellohello



```python
# 3번
num = 1234567890
list(str(num))
list(str(num))[3]
```




    '4'



## 산술연산


```python
a = 10
b = 3

print(f'10 + 3 == {a + b}')
print(f'10 - 3 == {a - b}')
print(f'10 / 3 == {a / b}')
print(f'10 // 3 == {a // b}') # 몫만 나옵니다.(정수만요!)
print(f'10 * 3 == {a * b}')
print(f'10 ** 3 == {a ** b}')
print(f'10 % 3 == {a % b}') # 나머지
```

    10 + 3 == 13
    10 - 3 == 7
    10 / 3 == 3.3333333333333335
    10 // 3 == 3
    10 * 3 == 30
    10 ** 3 == 1000
    10 % 3 == 1



```python
# 연산자 우선순위는 and, or, 4칙연산, 제곱 정도만 아셔도 
# 코딩하는데 큰 무리가 없습니다.
# (모르시면 읽는데 어려움이 생기기도 합니다.)

print(3 ** 2 * 3)
print(3 * 3 ** 2) # 왜 81이 아니지?
# 곱하기 보다 제곱이 우선순위가 더 높습니다.
print(3 + 3 * 2) # 3 + 3부터 먼저 하지 않습니다.
```

    27
    27
    9



```python
a = 10
b = 3

print(f'10 > 3 == {a > b}')
print(f'10 >= 3 == {a >= b}')
print(f'10 < 3 == {a < b}')
print(f'10 <= 3 == {a <= b}')
print(f'10 == 3 == {a == b}')
print(f'10 != 3 == {a != b}')
```

    10 > 3 == True
    10 >= 3 == True
    10 < 3 == False
    10 <= 3 == False
    10 == 3 == False
    10 != 3 == True


## 논리연산


```python
# and 는 곱
# or 는 합
# not은 반대
# True 1
# False 0
# 중요한 포인트는 저렇게 했을 때 언제 True가 되는지 정리하는 것

print(True and False)
print(True or False)
print(True or True)

if True and False:
    print('hello')

if 10 > 3 and 8 % 3 == 0:
    print('hello')

# and는 언제 True가 되나요?
# 모두 True일 때만 True
# or는 언제 True가 되나요?
# 둘 중에 하나라도 참이라면 True
```


```python
# https://codingdojang.com/scode/350?answer_mode=hide
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
```

    0
    15
    30
    45
    60
    75
    90



```python
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
```

    0
    3
    5
    6
    9
    10
    12
    15
    18
    20
    21
    24
    25
    27
    30
    33
    35
    36
    39
    40
    42
    45
    48
    50
    51
    54
    55
    57
    60
    63
    65
    66
    69
    70
    72
    75
    78
    80
    81
    84
    85
    87
    90
    93
    95
    96
    99
    100



```python
result = 0
for i in range(101):
    if i % 3 == 0:
        result += i # result = result + i
    if i % 5 == 0:
        result += i
    if i % 15 == 0:
        result -= i
print(result)
```

    2418



```python
result = 0
for i in range(101):
    if i % 3 == 0 or i % 5 == 0:
        result += i
result
```




    2418




```python
not True
```




    False




```python
not False
```




    True




```python
# python 입장에서 보는 코드
# False and ????? => 물음표에 무엇이 나오든 False
# 그래서 Python도 저 물음표를 보지 않습니다.
def solution():
    1/0

if False and solution():
    print('hello')
```


```python
# True or ?????  => 물음표에 무엇이 나오든 True
# 그래서 Python도 저 물음표를 보지 않습니다.
def solution():
    1/0

if True or solution():
    print('hello')
```

    hello



```python
# 단락 평가(컴퓨터가 어디까지 보는지 판단해서 활용)
username = '' # 사용자가 아무것도 입력하지 않았을 경우
username = username or 'licat'
username
```




    'licat'




```python
username = 'leehojun' # 사용자가 이름을 입력했을 경우
username = username or 'licat'
username
```




    'leehojun'




```python
# and와 or의 우선순위(and가 더 높습니다.)
for i in range(21):
    if i % 3 == 0 and i % 5 == 0 or i % 2 == 0:
        print(i)

for i in range(21):
    if (i % 3 == 0 and i % 5 == 0) or i % 2 == 0:
        print(i)
```

    0
    2
    4
    6
    8
    10
    12
    14
    15
    16
    18
    20
    0
    2
    4
    6
    8
    10
    12
    14
    15
    16
    18
    20



```python
# 아래는 출력되는 값이 다릅니다! 우선순위가 낮은 or가 먼저 나왔기 때문입니다.
# 결론 : 헷갈리시면 괄호를 사용해주세요!
for i in range(21):
    if (i % 3 == 0 or i % 5 == 0) and i % 2 == 0:
        print(i)

for i in range(21):
    if i % 3 == 0 or i % 5 == 0 and i % 2 == 0:
        print(i)
```

    0
    6
    10
    12
    18
    20
    0
    3
    6
    9
    10
    12
    15
    18
    20


## 비트연산 (중요도 하)


```python
# and(곱하기)
# 1001 == 9
# 0010 == 2
# ----
# 0000
```


```python
9 & 2
```




    0




```python
# and(곱하기)
# 1001 == 9
# 1000 == 8
# ----
# 1000
```


```python
9 & 8
```




    8




```python
# or(더하기, 대신 자리올림이 되진 않습니다.)
# 1001 == 9
# 0011 == 3
# ----
# 1011

9 | 3
```




    11




```python
# xor(같을 경우 0, 다를경우 1)
# 1001 == 9
# 0011 == 3
# ----
# 1010
9 ^ 3
```




    10




```python
~9 # 2보수를 취하는 것입니다.(9에게 +1한 다음에 -를 취하시면 됩니다.)
~-7 # 2보수를 취하는 것입니다.(7에게 +1한 다음에 -를 취하시면 됩니다.)
```




    6




```python
3 << 2 
# 3을 2진수로 표현하면 11인데 2칸을 왼쪽으로 미는 것입니다.
# 1100
```




    12




```python
7 >> 2
```




    1



## 디스코드 단축키

* `:ok`

## 할당연산


```python
# a = 10
# a = a + 10
a = + 10 # 이렇게 a를 지우면 양수를 표현하는 10만 남아요.
a
```




    10




```python
a = 10
a += 10 # a = a + 10
a
```




    20




```python
a = 10
a //= 10 # 산술연산 모두 됩니다.
a
```


```python
# Python에서 특이하게 ++a, ++b, a++, b++가 없습니다.
```

## 식별연산자


```python
# 앞으로 아래 2개를 활용해서 Python에 
# 컨벤션 자료형이 어떻게 구성이되는지 확인해볼겁니다.
# id()
# is
```


```python
a = 256
b = 256
a is b
```




    True




```python
a = 999
b = 999
a is b
```




    False




```python
a = [1, 2, 3]
b = [1, 2, 3]
a is b
```




    False




```python
a[0] = 100
a, b
```




    ([100, 2, 3], [1, 2, 3])




```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b # Python에 등호는 type과 value를 봅니다.
```




    True




```python
# is는 주소값을 비교합니다.
id(a) == id(b) # 이게 False면 is도 False입니다.
```




    False




```python
a = [1, 2, 3]
b = [1, 2, 3]

id(a) #5152
```




    139943949385152




```python
id(b) #9280
```




    139943949529280




```python
a == b # 값이 같은 것과 메모리에 같은 공간에 저장되어 있다는 얘기는 다른 얘기입니다!
```




    True



## not의 위치


```python
a = 10
b = 100
a is not b
# a not is b # error
```


```python
a = 10
b = [10, 20, 30]
a not in b
```




    False



## 멤버연산


```python
'a' in 'helalo world'
'a' in 'hello world'
'a' in ['a', 'b']
'a' in {'a':10, 'b':20}
# 10 in {'a':10, 'b':20} # dict안에있는 value값이 있는지 확인하고 싶으면
10 in {'a':10, 'b':20}.values()
10 in {10, 20, 30}
```




    True




```python
'a' not in ['aa', 'bb']
```




    True




```python
10 in [10, 20, 30]
[10] in [10, 20, 30]
[10] in [[10], 20, 30]
[10, 20] in [10, 20, 30]
[10, 20] in [[10, 20], 30]
set([10, 20]).issubset(set([10, 20, 30]))
{10, 20}.issubset({10, 20, 30, 40})
```




    True



## !! 연습문제


```python
#1번
a = 100
print((a > 100) and (a < 200))
print((a > 100) or (a < 200))
print((a >= 100) and (a <= 200))
print((a >= 100) or (a <= 200))
```

    False
    True
    True
    True



```python
#2번
b = 25
(b % 2 == 0) and (b % 5 == 0)
```


```python
#3번
c = 1000
c / 100
c // 100
```




    10




```python
#4번
# 그리디 알고리즘(욕심쟁이 알고리즘)
남은금액 = int(input())

오천원 = 남은금액 // 5000
# 남은금액 = 남은금액 % 5000
남은금액 = 남은금액 - (5000 * 오천원)

천원 = 남은금액 // 1000
남은금액 = 남은금액 % 1000

오백원 = 남은금액 // 500
남은금액 = 남은금액 % 500

백원 = 남은금액 // 100
남은금액 = 남은금액 % 100

print(오천원, 천원, 오백원, 백원)
```

    8800
    1 3 1 3


## !! 오늘 배운 것 정리

1. str
    - 순서가 있는 **시퀀스 자료형**입니다.
    - 작은 따옴표(' ')나 큰 따옴표(" "), 삼중따옴표('''str''', """str""")로 감싸는 것도 가능합니다. (삼중따옴표를 사용할 경우에는 줄단위의 문자열을 나타낼 수 있습니다.)
    - 작은 따옴표 안에 큰 따옴표, 큰 따옴표 안에 작은 따옴표 사용이 가능합니다.
    - 이스케이프 문자도 사용이 가능합니다.
    - 리스트, 튜플도 시퀀스 자료형입니다.
    - 메서드
        - lower
        - index, find
        - count
        - strip
        - replace
        - split, join
        - isdigit
2. 슬라이싱
    - 시퀀스형 자료형을 자를 수 있습니다.
    - 형태
    ```
    # s[start:stop:step]
    s = 'paullab CEO leehojun'
    s[5:]
    s[:5]
    s[3:10]
    s[:]
    s[0:20:2]
    # 자주 사용되는 코드
    s = 'paullab CEO leehojun!'
    s[:] # string에서는 많이 사용하지 않지만 list에서 많이 사용합니다.
    s[:-1] # 마지막 요소만 제외하고 다 슬라이싱 합니다.
    ```

3. 형변환
    - 형변환 : type을 변경하는 것입니다.
    - int, float, str 등 자료형에 이름으로 형태를 변경할 수 있습니다.
    - 그 중에서도 bool이 매우 중요합니다.
    ```
    # 별 5개
    # bool 형으로 형변환 하는 것
    if True:
        print('hi')

    if 'hello':
        print('hi')

    # 정말 많이 사용하는 코드
    l = [1, 2, 3]
    while l:
        print(l.pop())

    bool('') # 빈 문자열을 제외하고 모두 True
    bool('a')
    bool('False') # 문자열 False이기 때문에 True
    bool(0) # 0을 제외하고 모두 True
    bool(-1)
    bool(100)
    bool(None) # None은 비어있음을 명시해주는 키워드, False
    bool([]) # 컨벤션 자료형은 비어있으면 False입니다.
    bool({})
    ```

4. 산술연산
    ```
    a = 10
    b = 3

    print(f'10 + 3 == {a + b}')
    print(f'10 - 3 == {a - b}')
    print(f'10 / 3 == {a / b}')
    print(f'10 // 3 == {a // b}') # 몫만 나옵니다.(정수만요!)
    print(f'10 * 3 == {a * b}')
    print(f'10 ** 3 == {a ** b}')
    print(f'10 % 3 == {a % b}') # 나머지
    ```

5. 논리연산
    ```
    # and 는 곱
    # or 는 합
    # not은 반대
    # True 1
    # False 0
    # 중요한 포인트는 저렇게 했을 때 언제 True가 되는지 정리하는 것

    print(True and False)
    print(True or False)
    print(True or True)

    # https://codingdojang.com/scode/350?answer_mode=hide
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print(i)
    ```

6. 할당연산
    ```
    a = 10
    a += 10 # a = a + 10
    a //= 2
    a
    ```

7. is, in
    1. is
        ```
        a = [1, 2, 3]
        b = [1, 2, 3]

        id(a), id(b)
        a == b # 값이 같은 것과 메모리에 같은 공간에 저장되어 있다는 얘기는 다른 얘기입니다!
        ```
    2. in
        ```
        'a' in 'helalo world'
        'a' in 'hello world'
        'a' in ['a', 'b']
        'a' in {'a':10, 'b':20}
        # 10 in {'a':10, 'b':20} # dict안에있는 value값이 있는지 확인하고 싶으면
        10 in {'a':10, 'b':20}.values()
        10 in {10, 20, 30}
        ```

## 함수

1. 코드 덩어리(정말 쉽게 설명하자면..)
2. 코드를 재사용 할 수 있으며, 실수를 줄일 수 있습니다.
3. 코드의 구조를 한 눈에 파악할 수 있습니다.


```python
def 부지매입():
    pass

def 설계도면작성():
    pass

def 인력모집():
    pass

def 벽돌쌓기():
    pass

def 지붕올리기():
    pass

# 건축 또는 집짓기?
# 신입사원이 왔을 때
# 3년에 한 번 이직
# 7년에 한 번 이직
# 오래 있으신 분들
부지매입()
설계도면작성()
인력모집()
벽돌쌓기() # 10만줄
벽돌쌓기() # 10만줄
벽돌쌓기() # 10만줄
지붕올리기()
```


```python
# 파선아실(파라미터는 선언할 때, 아규먼트는 실제)
def function(x, y):
    z = x + y
    return z
print(f'function(5, 7) = {function(5, 7)}')
```


```python
# 같은 코드 1
def function(x, y):
    z = x + y
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None



```python
# 같은 코드 2
def function(x, y):
    z = x + y
    return None
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None



```python
# 같은 코드 3
def function(x, y):
    z = x + y
    return
print(f'function(5, 7) = {function(5, 7)}')
```

    function(5, 7) = None



```python
def hello():
    print('1')
    print('2')
    print('3')

print(hello())
```


```python
# 함수 연습문제 1
def one():
    print('one1')
    print('one2')
    print('one3')
    return 100

def two():
    print('two1')
    print('two2')
    one()
    return

print(two())
```

    two1
    two2
    one1
    one2
    one3
    None



```python
# 함수 연습문제 2
def one():
    print('one1')
    print('one2')
    print('one3')
    return 100

def two():
    print('two1')
    print('two2')
    x = one()
    return x + x

print(two())
```

    two1
    two2
    one1
    one2
    one3
    200



```python
# 함수 연습문제 3
def one(a, b):
    print('one1')
    print('one2')
    print('one3')
    return a + b

def two(x):
    y = 100
    print('two1')
    print('two2')
    x = one(x, y)
    return x + x

print(two(10))
```

    two1
    two2
    one1
    one2
    one3
    220



```python
# 함수 연습문제 3
def one(a, b):
    print('one1')
    print('one2')
    print('one3')
    return a + b

def two(x):
    y = 100
    print('two1')
    print('two2')
    x = one(x, y)
    return x + x

print(two(10))
```


```python
# 함수 연습문제 4
def one():
    print('one')
    return 10

def two():
    print('two')
    return 10

def three():
    print('three')
    return 10

a = one()
b = two()
c = three()
print(a + b)
print(a + b + c)
```


```python
# 함수 연습문제 4
def one():
    print('one')
    print('one')
    print('one')
    return 10

def two():
    print('two')
    print('two')
    print('two')
    return 10

def three():
    print('three')
    print('three')
    print('three')
    return 10

a = one()
b = two()
c = three()
print(a + b)
print(a + b + c)
```

    one
    one
    one
    two
    two
    two
    three
    three
    three
    20
    30



```python
# 함수 연습문제 4
# 좋지 않은 예 입니다!
def one():
    print('one')
    print('one')
    print('one')
    return 10

def two():
    print('two')
    print('two')
    print('two')
    return 10

def three():
    print('three')
    print('three')
    print('three')
    return 10

print(one() + two())
print(one() + two() + three())
```

    one
    one
    one
    two
    two
    two
    20
    one
    one
    one
    two
    two
    two
    three
    three
    three
    30



```python
# 함수란 무엇일까요?
# 함수의 이름은 메모리 상에 코드 블럭을 가리키는 변수입니다. 
leehojun = print
leehojun('hello') # 소괄호는 그 함수 블록을 실행시키는 명령어가 됩니다.
```

    hello



```python
id(leehojun), id(print)
```




    (140462240912688, 140462240912688)




```python
l = [leehojun, print, leehojun, print]
leehojun('hello world')
l[0]('hello world')
```

    hello world
    hello world



```python
def hello(a):
    a('hello')
    a('hello')
    a('hello')

print(hello(print))
```

    hello
    hello
    hello
    None



```python
def hello():
    def custom_sum(a, b):
        return a + b
    return custom_sum

c = hello()
c(10, 100)
```




    110




```python
def hello(a):
    return a

c = hello(print)
c(10, 100)
```

    10 100


## 함수의 기본 기능


```python
# 파선아실(파라미터는 선언할 때, 아규먼트는 실제)
def function(x, y):
    z = x + y
    return z
print(f'function(5, 7) = {function(5, 7)}')
```


```python
# return을 만나게 되면 함수는 종료가 됩니다.
def function(x, y):
    z = x + y
    return z
    print('hello')
    print('hello')
print(function(5, 7))
```

    12



```python
# return을 빨리 만나게 해주세요.
# early return
# 조건이 부합하지 않으면 바로 return을 하도록 하는 코딩 패턴
# 이렇게 작성함으로써, 가독성이 좋은 코드
def custom_sum(x, y):
    if type(x) != int or type(y) != int:
        return '연산할 수 없습니다.'
    z = x + y # 100줄이라 가정
    return z
print(custom_sum(5, '가나다'))
```

    연산할 수 없습니다.



```python
# 한글코딩에 장점
# 1. 고유명사(한라산, 새싹멤버) -> 기획자와 소통하기도 좋습니다.
# 2. 알고리즘 가독성은 괜찮습니다. 프로젝트는 조금 힘들 수 있어요. 일부 모듈에서는 사용할 수 있습니다.

# 한글코딩에 단점
# 1. 싫어하시는 분도 많습니다.
# 2. 한영키 바꾸는 것
```


```python
# 함수 안에 함수
def one():
    def two():
        print('hello1')
    def three():
        print('hello2')
    return 100

print(one())
```

    100



```python
# 함수 안에 함수
def one():
    def two():
        print('hello1')
    def three():
        print('hello2')
    two()
    three()
    return 100

print(one())
```

    hello1
    hello2
    100



```python
# 함수 안에 함수와 함수 안에 변수는 밖에서 호출이 안됩니다.
# 아래것이 만약 실행되었다면 위 어딘가에서 two와 x가 정의되어 있는 것입니다.
def one():
    def two():
        print('hello1')
    def three():
        print('hello2')
    two()
    three()
    x = 1000
    return 100

one()
print(x)
two()
```


```python
# 함수 안에 함수와 함수 안에 변수를 해봤으니
# 이번에는 함수 밖에 함수와 함수 밖에 변수를 해보도록 하겠습니다.

def test():
    print('test')

def one():
    test()

def two():
    test()

one()
two()
test()
```

    test
    test
    test



```python
# 위 원리와 마찬가지로 밖에 있는 변수를 '가져오는 것만' 가능합니다.
# 수정은 안됩니다.
test = 10

def one():
    print(test)

def two():
    print(test)

one()
two()
```

    10
    10



```python
# 이렇게 하시면 error가 납니다! 밖에 있는 변수는 수정이 안됩니다.
test = 10

def one():
    test = test + 10

one()
```

## 지역 변수와 전역 변수


```python
# 전역변수 접근은 가능하지만 수정이 되진 않습니다.
a = 100
def f():
    a = a + 1
f()
```


```python
# 전역변수를 함수 내부에서 수정이 되게 하는 코드입니다.
# 권하지 않습니다.
a = 100
def f():
    global a # 실무에서 사용 안합니다.
    a = a + 1
f()
print(a)
```

    101



```python
# 정해진 루트 외에 다른 루트로 해당 값을 수정하려고 하지 마세요.
a = 100
def f(x):
    x = x + 1
    return x
a = f(a)
print(a)
```

    101



```python
# 순수 함수
def f(x):
    return x + x + 100
f(10)
f(20) 
# 아규먼트 값에 따라 다르지만 
# 아규먼트에 2배해서 100이 더해진 다는 사실은 변하지 않죠?
```




    140




```python
test = 100
def f(x):
    return x + x + 100 + test
f(10)
# 아규먼트 값에 따라 다르지만 
# 아규먼트에 2배해서 200이 더해진 다는 사실은 변하지 않죠?
# 그렇지 않습니다. test값이 다른 곳에서 조작이 되면
# 더해지는 값이 200이 안될 수도 있죠.
# 예측이 불가하게 되는 것!
```




    220




```python
# 지역변수와 전역변수 이어서
# 전역변수 : 전역에서 접근할 수 있는 변수
# 지역변수 : 함수 내에서만 접근할 수 있는 변수
```


```python
a = 100
def one():
    a = 10
    print(a)

one()
print(a)
```

    10
    100



```python
# 어려우신 분들은 pass!
# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.
# 자신의 공간에 변수가 선언되어 있지 않으면
# 전역까지 찾아 올라갑니다. 전역에도 없으면 error

a = 100
def one():
    a = 10
    def two():
        def three():
            a = 1000
            print(a)
        three()
        print(a)
    two()
    print(a)

one()
print(a)
```

    1000
    10
    10
    100



```python
# 왜 a에서 애러가 나는가?
# enclosing scope에서 변수가 어디에 선언되어 있던 선언된 것은 기억합니다.
# 자유변수가 이를 참고하려 할 때 자신의 선언 뒤에 있다면 애러를 발생하게 됩니다.
a = 100
def one():
    def two():
        def three():
            print(a)
        three()
        print(a)
        a = 10
    two()
    print(a)

one()
print(a)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-27-4b3b8ab846cf> in <cell line: 12>()
         10     print(a)
         11 
    ---> 12 one()
         13 print(a)


    <ipython-input-27-4b3b8ab846cf> in one()
          7         print(a)
          8         a = 10
    ----> 9     two()
         10     print(a)
         11 


    <ipython-input-27-4b3b8ab846cf> in two()
          4         def three():
          5             print(a)
    ----> 6         three()
          7         print(a)
          8         a = 10


    <ipython-input-27-4b3b8ab846cf> in three()
          3     def two():
          4         def three():
    ----> 5             print(a)
          6         three()
          7         print(a)


    NameError: free variable 'a' referenced before assignment in enclosing scope



```python
def one():
    x = 1
    def two():
        print(x)
        print(locals())
    print(locals())
    two()
one()
```

    {'two': <function one.<locals>.two at 0x7f5c90303370>, 'x': 1}
    1
    {'x': 1}



```python
a = 100
print(locals())
def one():
    print(locals())
    def two():
        print(locals())
        def three():
            print(locals())
            print(a)
        three()
        print(a)
        a = 10
    two()
    print(a)

one()
print(a)
```

    {'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', 'print(reversed(l))', 'print(list(reversed(l)))', 'print(list(reversed(l)))\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', 'reversed(l)', 'print(type(range(10)))', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)'], '_oh': {2: <built-in method reverse of list object at 0x7f5c904bddc0>, 4: [1, 9, 8, 3, 4, 6, 5], 8: [1, 9, 8, 3, 4, 6, 5], 13: <list_reverseiterator object at 0x7f5c90498880>, 16: 14348907, 17: 81, 18: 243, 19: 729, 20: 3, 21: 9, 22: 9, 23: 729, 24: 27}, '_dh': ['/content'], 'In': ['', 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', 'print(reversed(l))', 'print(list(reversed(l)))', 'print(list(reversed(l)))\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', 'reversed(l)', 'print(type(range(10)))', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)'], 'Out': {2: <built-in method reverse of list object at 0x7f5c904bddc0>, 4: [1, 9, 8, 3, 4, 6, 5], 8: [1, 9, 8, 3, 4, 6, 5], 13: <list_reverseiterator object at 0x7f5c90498880>, 16: 14348907, 17: 81, 18: 243, 19: 729, 20: 3, 21: 9, 22: 9, 23: 729, 24: 27}, 'get_ipython': <bound method InteractiveShell.get_ipython of <google.colab._shell.Shell object at 0x7f5cb36aa620>>, 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x7f5cb36aabc0>, 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x7f5cb36aabc0>, '_': 27, '__': 729, '___': 9, '_i': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', '_ii': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', '_iii': 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', '_i1': 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l': [5, 6, 4, 3, 8, 9, 1], '_i2': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', '_2': <built-in method reverse of list object at 0x7f5c904bddc0>, '_i3': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', '_i4': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', '_4': [1, 9, 8, 3, 4, 6, 5], '_i5': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', '_i6': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', '_i7': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', '_i8': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', '_8': [1, 9, 8, 3, 4, 6, 5], '_i9': 'print(reversed(l))', '_i10': 'print(list(reversed(l)))', '_i11': 'print(list(reversed(l)))\nprint(l)', '_i12': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', '_i13': 'reversed(l)', '_13': <list_reverseiterator object at 0x7f5c90498880>, '_i14': 'print(type(range(10)))', '_i15': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'power': <function power at 0x7f5c9033e440>, '_i16': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', '_16': 14348907, '_i17': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', '_17': 81, '_i18': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', '_18': 243, '_i19': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', '_19': 729, '_i20': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', '_20': 3, '_i21': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', '_21': 9, '_i22': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', '_22': 9, '_i23': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', '_23': 729, '_i24': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '_24': 27, '_i25': '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a': 100, 'one': <function one at 0x7f5c90302e60>, '_i26': 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_i27': 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_i28': 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'bar': <function bar at 0x7f5c9033f9a0>, '_i29': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', '_i30': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', '_i31': 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)'}
    {}
    {}
    {}



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-062b42d4fe0d> in <cell line: 16>()
         14     print(a)
         15 
    ---> 16 one()
         17 print(a)


    <ipython-input-31-062b42d4fe0d> in one()
         11         print(a)
         12         a = 10
    ---> 13     two()
         14     print(a)
         15 


    <ipython-input-31-062b42d4fe0d> in two()
          8             print(locals())
          9             print(a)
    ---> 10         three()
         11         print(a)
         12         a = 10


    <ipython-input-31-062b42d4fe0d> in three()
          7         def three():
          8             print(locals())
    ----> 9             print(a)
         10         three()
         11         print(a)


    NameError: free variable 'a' referenced before assignment in enclosing scope



```python
# 함수내에서 사용되는 로컬 변수들의 변수 이름 및 현재 값 등을 알고 싶을 때 
# locals 빌트인 함수를 사용할 수 있습니다.
a = 100
print(locals())
def one():
    a = 10
    print(locals())
    def two():
        print(locals())
        def three():
            print(locals())
            print(a)
        three()
        print(a)
    two()
    print(a)

one()
print(a)
```

    {'__name__': '__main__', '__doc__': 'Automatically created module for IPython interactive environment', '__package__': None, '__loader__': None, '__spec__': None, '__builtin__': <module 'builtins' (built-in)>, '__builtins__': <module 'builtins' (built-in)>, '_ih': ['', 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', 'print(reversed(l))', 'print(list(reversed(l)))', 'print(list(reversed(l)))\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', 'reversed(l)', 'print(type(range(10)))', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\nprint(locals())\ndef one():\n    a = 10\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)'], '_oh': {2: <built-in method reverse of list object at 0x7f5c904bddc0>, 4: [1, 9, 8, 3, 4, 6, 5], 8: [1, 9, 8, 3, 4, 6, 5], 13: <list_reverseiterator object at 0x7f5c90498880>, 16: 14348907, 17: 81, 18: 243, 19: 729, 20: 3, 21: 9, 22: 9, 23: 729, 24: 27}, '_dh': ['/content'], 'In': ['', 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', 'print(reversed(l))', 'print(list(reversed(l)))', 'print(list(reversed(l)))\nprint(l)', 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', 'reversed(l)', 'print(type(range(10)))', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', 'a = 100\nprint(locals())\ndef one():\n    a = 10\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)'], 'Out': {2: <built-in method reverse of list object at 0x7f5c904bddc0>, 4: [1, 9, 8, 3, 4, 6, 5], 8: [1, 9, 8, 3, 4, 6, 5], 13: <list_reverseiterator object at 0x7f5c90498880>, 16: 14348907, 17: 81, 18: 243, 19: 729, 20: 3, 21: 9, 22: 9, 23: 729, 24: 27}, 'get_ipython': <bound method InteractiveShell.get_ipython of <google.colab._shell.Shell object at 0x7f5cb36aa620>>, 'exit': <IPython.core.autocall.ZMQExitAutocall object at 0x7f5cb36aabc0>, 'quit': <IPython.core.autocall.ZMQExitAutocall object at 0x7f5cb36aabc0>, '_': 27, '__': 729, '___': 9, '_i': 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_ii': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', '_iii': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', '_i1': 'l = [5, 6, 4, 3, 8, 9, 1]\nreverse(l)', 'l': [5, 6, 4, 3, 8, 9, 1], '_i2': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse', '_2': <built-in method reverse of list object at 0x7f5c904bddc0>, '_i3': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()', '_i4': 'l = [5, 6, 4, 3, 8, 9, 1]\nl.reverse()\nl', '_4': [1, 9, 8, 3, 4, 6, 5], '_i5': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(reversed(l)) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', '_i6': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.\nprint(l)', '_i7': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())', '_i8': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(l.reverse())\nl', '_8': [1, 9, 8, 3, 4, 6, 5], '_i9': 'print(reversed(l))', '_i10': 'print(list(reversed(l)))', '_i11': 'print(list(reversed(l)))\nprint(l)', '_i12': 'l = [5, 6, 4, 3, 8, 9, 1]\nprint(list(reversed(l)))\nprint(l)', '_i13': 'reversed(l)', '_13': <list_reverseiterator object at 0x7f5c90498880>, '_i14': 'print(type(range(10)))', '_i15': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)', 'power': <function power at 0x7f5c9033e440>, '_i16': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y * y\n\npower(3, 4)', '_16': 14348907, '_i17': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)', '_17': 81, '_i18': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)', '_18': 243, '_i19': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', '_19': 729, '_i20': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 1)', '_20': 3, '_i21': 'def power(x, n):\n    if n == 0:\n        return 1\n    else:\n        y = power(x, n-1)\n        return x * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', '_21': 9, '_i22': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 2)', '_22': 9, '_i23': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 6)', '_23': 729, '_i24': 'def power(x, n):\n    if n == 0:\n        return 1\n    elif n % 2 == 0:\n        y = power(x, n/2)\n        return y * y\n    else:\n        y = power(x, (n-1)/2)\n        return x * y * y\n\npower(3, 4)\npower(3, 5)\npower(3, 3)', '_24': 27, '_i25': '# 어려우신 분들은 pass!\n# 조금 있다가 요약정리에서도 써드리지 않을 예정입니다.\n# 자신의 공간에 변수가 선언되어 있지 않으면\n# 전역까지 찾아 올라갑니다. 전역에도 없으면 error\n\na = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)', 'a': 100, 'one': <function one at 0x7f5c9033c040>, '_i26': 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_i27': 'a = 100\ndef one():\n    def two():\n        def three():\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_i28': 'def bar():\n    x = 1\n    def foo():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', 'bar': <function bar at 0x7f5c9033f9a0>, '_i29': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    foo()\n\nbar()', '_i30': 'def one():\n    x = 1\n    def two():\n        print(x)\n        print(locals())\n    print(locals())\n    two()\n\none()', '_i31': 'a = 100\nprint(locals())\ndef one():\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n        a = 10\n    two()\n    print(a)\n\none()\nprint(a)', '_i32': 'a = 100\nprint(locals())\ndef one():\n    a = 10\n    print(locals())\n    def two():\n        print(locals())\n        def three():\n            print(locals())\n            print(a)\n        three()\n        print(a)\n    two()\n    print(a)\n\none()\nprint(a)'}
    {'a': 10}
    {'a': 10}
    {'a': 10}
    10
    10
    10
    100



```python
# error가 나는 코드
x = 100
def outer():
    x = 1
    def inner():
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```


```python
# inner가 outer에 변수를 건드리고 싶은데
# inner 안에서는 x에 수정권한이 전혀 없습니다.
x = 100
def outer():
    x = 1
    def inner():
        nonlocal x
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```

    2
    2
    100



```python
x = 100
def outer():
    x = 1
    def inner():
        global x
        x += 1
        print(x)
    inner()
    print(x)

outer()
print(x)
```

    101
    1
    101


## 재귀함수

* 내가 나를 호출하는 것입니다.
* 재귀 <-> for문은 대부분 호환이 가능합니다.
* 반복문 사용하시기를 권합니다!
* 어렵고 효율도 안좋아요! (얼마나 효율이 안좋은지도 확인해보겠습니다.)
* 필수적으로 사용하는 곳이 있습니다.


```python
# sys.setrecursionlimit -> 제한을 늘릴 수 있음
# 실행시키지 마세요.
def 숫자출력():
    print(1)
    return 숫자출력()
숫자출력()
```


```python
# for로 펙토리얼
# 5! = 5 * 4 * 3 * 2 * 1

result = 1

# 1 * 2 * 3 * 4 * 5
for i in range(1, 6):
    result *= i
    
result
```




    120




```python
# 재귀로 펙토리얼

def f(n):
    if n <= 1:
        return 1
    else:
        return n * f(n-1)

f(5)

'''
f(5)    5 * f(4) == 5 * 24 => 120
f(4)    4 * f(3) == 4 * 6
f(3)    3 * f(2) == 3 * 2
f(2)    2 * f(1) == 2 * 1
f(1)    1
'''
```




    120




```python
# for로 문자열 거꾸로 출력하기
s = 'hello'
result = ''

for i in s:
    result = i + result

result
'''
result = 'h' + ''
result = 'e' + 'h'
result = 'l' + 'eh'
result = 'l' + 'leh'
result = 'o' + 'lleh'
'''
# 실무에서는 이렇게 거꾸로 만들지 않습니다.
# 슬라이싱이 일반 for문보다 8배 빠릅니다.
# s[::-1] 이렇게 쓰시면 됩니다.
```




    'olleh'




```python
def reverse(s):
    if len(s) == 1:
        return s
    else:
        return reverse(s[1:]) + s[0]

reverse('hello')

'''
reverse('hello')    reverse('ello') + 'h'   == 'olle' + 'h'
reverse('ello')     reverse('llo') + 'e'    == 'oll' + 'e'
reverse('llo')      reverse('lo') + 'l'     == 'ol' + 'l'
reverse('lo')       reverse('o') + 'l'      == 'o' + 'l'
reverse('o')        'o'
'''
```




    'olleh'




```python
# 피보나치 for
# 재귀가 얼마나 비효율적인지 보여드리기 위해서 진행
# 1 1 2 3 5 8 13 21

curr = 1
next = 1
for i in range(1, 6):
    curr, next = next, curr + next

next
```




    13




```python
# 피보나치 재귀

def f(n):
    if n == 1 or n == 2:
        return 1
    return f(n-1) + f(n-2)

1, 1, f(3), f(4), f(5), f(6)
```




    (1, 1, 2, 3, 5, 8)




```python
f(35) #8초
```




    24157817




```python
# 재귀에 비효율을 이렇게 해결할 수는 있다를 보여드리기 위함
# but 가능 하면 for를 이용해주세요.
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)

fib(40)
```

## !! 연습문제


```python
# 1번
a = 'pithon'

def 함수1():
    def 함수2():
        print('love')
        
    print('I')
    함수2()
    return "python"
	

a = 함수1()
print(a)
```

    I
    love
    python



```python
# 2번
def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')
```

    plus : 15
    minus : 5
    multiply : 50
    divide : 2.0



```python
plus = lambda num1, num2 : num1 + num2
minus = lambda num1, num2 : num1 - num2
multiply = lambda num1, num2 : num1 / num2
divide = lambda num1, num2 : num1 * num2

print(f'plus : {plus(10, 5)}')
print(f'minus : {minus(10, 5)}')
print(f'multiply : {multiply(10, 5)}')
print(f'divide : {divide(10, 5)}')
```

    plus : 15
    minus : 5
    multiply : 2.0
    divide : 50



```python
# 실력이 있으신 분은 견고한 코드가 될 수 있도록 해주셔야 합니다.
def plus(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    return '정수가 아니기에 연산할 수 없습니다.'

# 테스트 주도 개발
print(f"plus : {plus(10, 5)}")
print(f"plus : {plus(10, '5')}")
print(f"plus : {plus('10', 5)}")
print(f"plus : {plus('10', '5')}")
print(f"plus : {plus(10, 'a')}")
print(f"plus : {plus(10, True)}")
print(f"plus : {plus(False, 5)}")
print(f"plus : {plus(10, 10.1)}")
```

    plus : 15
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.
    plus : 정수가 아니기에 연산할 수 없습니다.



```python
# 실력이 있으신 분은 견고한 코드가 될 수 있도록 해주셔야 합니다.
def plus(num1, num2):
    if type(num1) == int and type(num2) == int:
        return num1 + num2
    return float('inf')

# 테스트 주도 개발
print(f"plus : {plus(10, 5)}")
print(f"plus : {plus(10, '5')}")
print(f"plus : {plus('10', 5)}")
print(f"plus : {plus('10', '5')}")
print(f"plus : {plus(10, 'a')}")
print(f"plus : {plus(10, True)}")
print(f"plus : {plus(False, 5)}")
print(f"plus : {plus(10, 10.1)}")
```


```python
# 실력이 있으신 분은 견고한 코드가 될 수 있도록 해주셔야 합니다.
def plus(num1, num2):
    try:
        return num1 + num2
    except:
        return float('inf')

# 테스트 주도 개발
print(f"plus : {plus(10, 5)}")
print(f"plus : {plus(10, '5')}")
print(f"plus : {plus('10', 5)}")
print(f"plus : {plus('10', '5')}")
print(f"plus : {plus(10, 'a')}")
print(f"plus : {plus(10, True)}")
print(f"plus : {plus(False, 5)}")
print(f"plus : {plus(10, 10.1)}")
```

    plus : 15
    plus : inf
    plus : inf
    plus : 105
    plus : inf
    plus : 11
    plus : 5
    plus : 20.1



```python
float('inf') > 1000000000000000000000000
```




    True




```python
x = 3
def 제곱(n):
    if n == 0:
        return 1
    return x * 제곱(n-1)

제곱(3)
제곱(4)
```




    81




```python
def 제곱(x, n):
    if n == 0:
        return 1
    return x * 제곱(x, n-1)

제곱(3, 3)
제곱(3, 4)
```




    81




```python
# 재귀를 Log(N, 2)
def my_pow(num1, num2):
    if num2 == 0:
        return 1
    if num2 == 1:
        return num1
    if num2 % 2 == 0:
        half = my_pow(num1, num2 // 2)
        return half * half
    else:
        half = my_pow(num1, num2 // 2)
        return half * half * num1

my_pow(2, 3)
```




    8



* my_pow(2, 3)의 경우 2번 호출
    1. 1번째 호출 : my_pow(2, 3), num1에는 2, num2에는 3
        * else 구문에 걸림
        * half = my_pow(2, 1)을 호출하여 자기 자신을 호출하게 됨
    2. 2번째 호출 : my_pow(2, 1), num1에는 2, num2에는 1
        * 2번째 if문에 걸림
        * num1을 반환

* my_pow(2, 8)의 경우 0번 호출
    1. 1번째 호출 : my_pow(2, 8), num1에는 2, num2에는 8
        * 3번째 if문에 걸림
        * half = my_pow(2, 4)을 호출하여 자기 자신을 호출하게 됨
    2. 2번째 호출 : my_pow(2, 4), num1에는 2, num2에는 4
        * 3번째 if문에 걸림
        * half = my_pow(2, 2)을 호출하여 자기 자신을 호출하게 됨
    3. 3번째 호출 : my_pow(2, 2), num1에는 2, num2에는 2
        * 3번째 if문에 걸림
        * half = my_pow(2, 0)을 호출하여 자기 자신을 호출하게 됨
    4. 4번째 호출 : my_pow(2, 0), num1에는 2, num2에는 0
        * 1번째 if문에 걸림
        * return 0를 반환


* 결론 : 기존의 코드는 n승이면 n승 그대로를 출력하는데 반하여 이 코드는 log(N, 2)으로 걸리는 것을 확인할 수 있다. 밑이 2인 log N번 호출하면 정답이 나오게 된다.


```python
# 재귀함수를 사용해서 푼 것은 아니고
# 팩토리 함수라고도 하고, 클로져라고도 합니다.
def 제곱(x):
    def 승수(y):
        return x ** y
    return 승수

제곱3 = 제곱(3)
제곱3(4)
```




    81



## list (리스트)

* 순서를 가진 데이터들의 집합(Sequence)
* 리스트는 값의 변경
* 리스트 안에 리스트로 다차원의 리스트를 만드는 것도 가능
* 리스트 안에 다른 딕셔너리, 셋, 튜플 등을 넣는 것도 가능합니다


```python
l = [1000, 2000, 3000, 1000, 2000, 3000]
id(l[0]), id(l[3])
```




    (140027035575536, 140027035575536)




```python
# 컨벤션 자료형(딕셔너리, 튜플, 셋, 리스트)에서는
# 메모리 효율을 위해
# 같은 값이 있을 경우 같은 곳을 가리키게 설계되어 있습니다.
```


```python
l = [10, 20, 30, 40]
l[0] = 1000
l
```




    [1000, 20, 30, 40]




```python
s = 'hello world'
s[0] = 'k' # error
s
```


```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

data
```




    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




```python
data[0]
```




    [1, 2, 3]




```python
data[0][0]
[1, 2, 3][0]
```




    1




```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

data[0][0] *= 2
data[0][1] *= 2
data[0][2] *= 2
data[1][0] *= 2
data[1][1] *= 2
data[1][2] *= 2
data[2][0] *= 2
data[2][1] *= 2
data[2][2] *= 2
data
```




    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]




```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for i in range(3):
    data[i][0] *= 2
    data[i][1] *= 2
    data[i][2] *= 2

data
```


```python
data = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

for i in range(3):
    for j in range(3):
        data[i][j] *= 2
        
data
```




    [[2, 4, 6], [8, 10, 12], [14, 16, 18]]




```python
'''
3                       == 스칼라
[3, 4]                  == 벡터
[[1, 2, 3],             == 메트릭스(행렬)
 [4, 5, 6],
 [7, 8, 9]]
[[[1], [2], [3]],       == 텐서(다차원, 3차원 이상)
 [[4], [5], [6]],
 [[7], [8], [9]]]

텐서플로우 : 인공지능 중 유명한 라이브러리
'''
```


```python
# 리스트에서 주의해야 하는 연산!
x = [10] * 3
x
```




    [10, 10, 10]




```python
x[0] = 100
x
```




    [100, 10, 10]




```python
x = [[10] * 2] * 3
x
```




    [[10, 10], [10, 10], [10, 10]]




```python
x[0][0] = 100
x
```




    [[100, 10], [100, 10], [100, 10]]




```python
x = [[[10] * 3] * 3] * 4
x[0][0][0] = 1000
x
```




    [[[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]],
     [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]],
     [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]],
     [[1000, 10, 10], [1000, 10, 10], [1000, 10, 10]]]




```python
[1, 2, 3] + [1, 2, 3] # 많이 사용합니다!
```




    [1, 2, 3, 1, 2, 3]




```python
[1, 2, 3] + 1 # error
```


```python
id(x[0][0]), id(x[0][1])
```




    (140027034041600, 140027034041600)




```python
id(x[0][0]) == id(x[0][1])
```




    True




```python
l = [10, 20, 30]
type(l), dir(l), help(l)
```

    Help on list object:
    
    class list(object)
     |  list(iterable=(), /)
     |  
     |  Built-in mutable sequence.
     |  
     |  If no argument is given, the constructor creates a new empty list.
     |  The argument must be an iterable if specified.
     |  
     |  Methods defined here:
     |  
     |  __add__(self, value, /)
     |      Return self+value.
     |  
     |  __contains__(self, key, /)
     |      Return key in self.
     |  
     |  __delitem__(self, key, /)
     |      Delete self[key].
     |  
     |  __eq__(self, value, /)
     |      Return self==value.
     |  
     |  __ge__(self, value, /)
     |      Return self>=value.
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __gt__(self, value, /)
     |      Return self>value.
     |  
     |  __iadd__(self, value, /)
     |      Implement self+=value.
     |  
     |  __imul__(self, value, /)
     |      Implement self*=value.
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  __iter__(self, /)
     |      Implement iter(self).
     |  
     |  __le__(self, value, /)
     |      Return self<=value.
     |  
     |  __len__(self, /)
     |      Return len(self).
     |  
     |  __lt__(self, value, /)
     |      Return self<value.
     |  
     |  __mul__(self, value, /)
     |      Return self*value.
     |  
     |  __ne__(self, value, /)
     |      Return self!=value.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __reversed__(self, /)
     |      Return a reverse iterator over the list.
     |  
     |  __rmul__(self, value, /)
     |      Return value*self.
     |  
     |  __setitem__(self, key, value, /)
     |      Set self[key] to value.
     |  
     |  __sizeof__(self, /)
     |      Return the size of the list in memory, in bytes.
     |  
     |  append(self, object, /)
     |      Append object to the end of the list.
     |  
     |  clear(self, /)
     |      Remove all items from list.
     |  
     |  copy(self, /)
     |      Return a shallow copy of the list.
     |  
     |  count(self, value, /)
     |      Return number of occurrences of value.
     |  
     |  extend(self, iterable, /)
     |      Extend list by appending elements from the iterable.
     |  
     |  index(self, value, start=0, stop=9223372036854775807, /)
     |      Return first index of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  insert(self, index, object, /)
     |      Insert object before index.
     |  
     |  pop(self, index=-1, /)
     |      Remove and return item at index (default last).
     |      
     |      Raises IndexError if list is empty or index is out of range.
     |  
     |  remove(self, value, /)
     |      Remove first occurrence of value.
     |      
     |      Raises ValueError if the value is not present.
     |  
     |  reverse(self, /)
     |      Reverse *IN PLACE*.
     |  
     |  sort(self, /, *, key=None, reverse=False)
     |      Sort the list in ascending order and return None.
     |      
     |      The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
     |      order of two equal elements is maintained).
     |      
     |      If a key function is given, apply it once to each list item and sort them,
     |      ascending or descending, according to their function values.
     |      
     |      The reverse flag can be set to sort in descending order.
     |  
     |  ----------------------------------------------------------------------
     |  Class methods defined here:
     |  
     |  __class_getitem__(...) from builtins.type
     |      See PEP 585
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes defined here:
     |  
     |  __hash__ = None
    





    (list,
     ['__add__',
      '__class__',
      '__class_getitem__',
      '__contains__',
      '__delattr__',
      '__delitem__',
      '__dir__',
      '__doc__',
      '__eq__',
      '__format__',
      '__ge__',
      '__getattribute__',
      '__getitem__',
      '__gt__',
      '__hash__',
      '__iadd__',
      '__imul__',
      '__init__',
      '__init_subclass__',
      '__iter__',
      '__le__',
      '__len__',
      '__lt__',
      '__mul__',
      '__ne__',
      '__new__',
      '__reduce__',
      '__reduce_ex__',
      '__repr__',
      '__reversed__',
      '__rmul__',
      '__setattr__',
      '__setitem__',
      '__sizeof__',
      '__str__',
      '__subclasshook__',
      'append',
      'clear',
      'copy',
      'count',
      'extend',
      'index',
      'insert',
      'pop',
      'remove',
      'reverse',
      'sort'],
     None)



## 리스트의 메서드


```python
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 
# 'insert', 'pop', 'remove', 'reverse', 'sort'
```


```python
l = [1, 2, 3]
l.append(4)
l
```




    [1, 2, 3, 4]




```python
l = [1, 2, 3]
l.append([1, 2, 3])
l
```




    [1, 2, 3, [1, 2, 3]]




```python
l = [1, 2, 3]
l.extend(4) #error
l
```


```python
l = [1, 2, 3]
l.extend('hello')
l
```




    [1, 2, 3, 'h', 'e', 'l', 'l', 'o']




```python
l = [1, 2, 3]
l.extend({'one':10, 'two':20})
l
```




    [1, 2, 3, 'one', 'two']




```python
l = [1, 2, 3]
l.extend({10, 20, 30})
l
```




    [1, 2, 3, 10, 20, 30]




```python
l = [1, 2, 3]
l.extend([1, 2, 3])
l
```




    [1, 2, 3, 1, 2, 3]




```python
l = [10, 20, 30]
l.clear()
l
```




    []




```python
l = [10, 20, 30]
l = []
l
```




    []




```python
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```




    ([['바나나', 2000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 2000], ['수박', 2000], ['딸기', 3000]])




```python
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게.copy() # 얕은 복사
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```




    ([['바나나', 2000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 1000], ['수박', 2000], ['딸기', 3000]])




```python
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
서울과일가게 = 제주과일가게[:] # 얕은 복사
서울과일가게[0] = ['바나나', 2000]
서울과일가게, 제주과일가게
```




    ([['바나나', 2000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 1000], ['수박', 2000], ['딸기', 3000]])




```python
s = 'hello world'
s[:5]
```




    'hello'




```python
l = [10, 20, 30, 40, 50]
l[:3]
ll = l[:]
ll
```




    [10, 20, 30, 40, 50]




```python
id(l), id(ll)
```




    (140027035736448, 140027034219968)




```python
# 이 이상의 내용은 뒤에 얕은 복사와 깊은 복사에서 알아봅니다.
제주과일가게 = [['바나나', 1000], ['수박', 2000], ['딸기', 3000]]
# 서울과일가게 = 제주과일가게[:] # 얕은 복사
서울과일가게 = 제주과일가게.copy() # 얕은 복사
id(서울과일가게[0]), id(제주과일가게[0])
id(서울과일가게[0][0]), id(제주과일가게[0][0])
서울과일가게[0][1] = 3000
서울과일가게, 제주과일가게
```




    ([['바나나', 3000], ['수박', 2000], ['딸기', 3000]],
     [['바나나', 3000], ['수박', 2000], ['딸기', 3000]])




```python
l = [1, 2, 3]
ll = l[:]
l[0] = 1000
l, ll
```




    ([1000, 2, 3], [1, 2, 3])




```python
l = [1, 2, 3]
ll = l.copy()
l[0] = 1000
l, ll
```


```python
l = [1, 2, 3, 1, 1, 1, 2, 3, 2, 3, 1, 1]
l.count(1)
```




    6




```python
a = [10, 1, 1, 11, 2, 23, 12, 11]
a.index(11)
a[:a.index(11)]
```




    [10, 1, 1]




```python
a = [10, 20, 30]
a.insert(2, 1000) # insert는 값을 지우지는 않습니다.
a
```




    [10, 20, 1000, 30]




```python
l = [10, 20, 30, 40, 50]
l.pop()
```




    50




```python
l
```




    [10, 20, 30, 40]




```python
l = [10, 20, 30, 40, 50]
l.pop(0) # 많이 사용합니다.
l
```




    [20, 30, 40, 50]




```python
# append : 맨 뒤에 추가
# pop : 맨 뒤에서 값을 뽑아내고, index가 들어갈 경우 index에서 뽑습니다.
# insert : index에 값을 삽입하고 원래 있던 값을 뒤로 밀어버립니다.
```


```python
l = [10, 20, 30, 40, 50]
l.remove(20) # 예를 들어 for를 돌면서 remove를 하지 않기 바랍니다.
l
```




    [10, 30, 40, 50]




```python
l = [20, 20, 20, 20]
for i in range(len(l)):
    print(len(l)) # len가 계속 변하기 때문에 의도치 않은 에러가 날 수 있어요.
    l.remove(20)
```

    4
    3
    2
    1



```python
# 무한 반복입니다.
l = [20, 20, 20, 20]
for i in l:
    print(len(l))
    l.append(20)
```


```python
l = [10, 20, 30, 40, 50, 20, 20, 20]
for i in range(l.count(20)):
    l.remove(20)
l
```




    [10, 30, 40, 50]




```python
# 실무에서 
# 어떤 값을 전부 없애거나
# 어떤 값을 전부 찾는 것
# 조건에 부합하는 것
def f(x):
    return x != 20

# True인 것만 반환해줍니다.
list(filter(f, [10, 20, 30, 40, 50, 20, 20, 20]))
```




    [10, 30, 40, 50]




```python
filter(f, [10, 20, 30, 40, 50, 20, 20, 20])
```




    <filter at 0x7eff013af550>




```python
range(100)
```




    range(0, 100)




```python
for i in filter(f, [10, 20, 30, 40, 50, 20, 20, 20]):
    print(i)
```

    10
    30
    40
    50



```python
list(filter(lambda x: x!=20, [10, 20, 30, 40, 50, 20, 20, 20]))
```




    [10, 30, 40, 50]




```python
l = [5, 6, 4, 3, 8, 9, 1]
l.reverse() # 역 정렬이 아니고 역순이며 원본을 만집니다.
l
```




    [1, 9, 8, 3, 4, 6, 5]




```python
l = [5, 6, 4, 3, 8, 9, 1]
print(list(reversed(l))) # 역 정렬이 아니고 역순이며 원본을 만지지 않습니다.
print(l)
```

    [1, 9, 8, 3, 4, 6, 5]
    [5, 6, 4, 3, 8, 9, 1]



```python
# l.reverse() : 리스트에 메서드 이며, return None입니다! 원본이 역순, 원본을 만집니다.
# reversed() : 빌트인펑션이며, return 역순 입니다! 원본을 만지지 않습니다.
```


```python
l = [5, 6, 4, 3, 8, 9, 1]
print(l.reverse())
l
```

    None





    [1, 9, 8, 3, 4, 6, 5]




```python
l = [5, 6, 4, 3, 8, 9, 1]
print(list(reversed(l)))
print(l)
```

    [1, 9, 8, 3, 4, 6, 5]
    [5, 6, 4, 3, 8, 9, 1]



```python
reversed(l)
```




    <list_reverseiterator at 0x7f5c90498880>




```python
print(type(range(10)))
```

    <class 'range'>


## sort


```python
l = [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]
l.sort() # 원본을 만지고, 반환값은 None
l
```




    [1, 2, 2, 3, 4, 5, 5, 8, 9, 10]




```python
l = [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]
print(sorted([1, 5, 4, 2, 8, 5, 10, 9, 2, 3]))
# 원본을 만지지 않고, 반환값은 정렬된 값
print(l)
```

    [1, 2, 2, 3, 4, 5, 5, 8, 9, 10]
    [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]



```python
# 이렇게 실무에서 진행하진 않습니다.
l = [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]
l.sort()
l.reverse()
l
```




    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]




```python
# 이렇게 많이 사용합니다.
l = [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]
l.sort(reverse=True) # 내림차순
l
```




    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]




```python
l = [1, 5, 4, 2, 8, 5, 10, 9, 2, 3]
sorted(l, reverse=True) # 내림차순
```




    [10, 9, 8, 5, 5, 4, 3, 2, 2, 1]




```python
l = [[1, 10, 'leehojun'], 
     [20, 30, 'hojun'], 
     [10, 20, 'weniv!'], 
     [1, 2, 'hello world'], 
     [55, 11, 'sun']]

# 1. 글자 수 대로 정렬해주세요.
def f(x):
    return len(x[2])

print(sorted(l, key=f, reverse=False))
print(sorted(l, key=lambda x:len(x[2]), reverse=False))

# 2. 맨 앞에 위치한 숫자대로 정렬해주세요.
def f2(x):
    return x[0]

print(sorted(l))
print(sorted(l, key=f2))
print(sorted(l, key=lambda x:x[0]))

# 3. 중앙에 위치한 값대로 정렬해주세요.

def f3(x):
    return x[1]

print(sorted(l))
print(sorted(l, key=f3))
print(sorted(l, key=lambda x:x[1]))

l = [[1, 10, 32], 
     [20, 30, 11], 
     [10, 20, 22], 
     [1, 2, 13], 
     [55, 11, 44]]


# 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

def f4(x):
    return x[0] + x[1] + x[2]

def f5(x):
    return sum(x)

print(sorted(l, key=f4))
print(sorted(l, key=f5))
print(sorted(l, key=lambda x: sum(x)))
print(sorted(l, key=sum))
```

    [[55, 11, 'sun'], [20, 30, 'hojun'], [10, 20, 'weniv!'], [1, 10, 'leehojun'], [1, 2, 'hello world']]
    [[55, 11, 'sun'], [20, 30, 'hojun'], [10, 20, 'weniv!'], [1, 10, 'leehojun'], [1, 2, 'hello world']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 10, 'leehojun'], [1, 2, 'hello world'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 10, 'leehojun'], [1, 2, 'hello world'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [10, 20, 'weniv!'], [20, 30, 'hojun'], [55, 11, 'sun']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [55, 11, 'sun'], [10, 20, 'weniv!'], [20, 30, 'hojun']]
    [[1, 2, 'hello world'], [1, 10, 'leehojun'], [55, 11, 'sun'], [10, 20, 'weniv!'], [20, 30, 'hojun']]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]
    [[1, 2, 13], [1, 10, 32], [10, 20, 22], [20, 30, 11], [55, 11, 44]]



```python
# https://codingdojang.com/scode/408?answer_mode=hide
# 좌표 평면 문제가 나오면 차원 축소나 차원 확대가 가능한 문제인지 확인

point = [1, 3, 4, 8, 13, 17, 20]
point[1:]

[1, 3, 4, 8, 13, 17, 20]
[3, 4, 8, 13, 17, 20]
```




    [3, 4, 8, 13, 17, 20]




```python
list(zip('hello', 'world'))
```




    [('h', 'w'), ('e', 'o'), ('l', 'r'), ('l', 'l'), ('o', 'd')]




```python
list(zip(point, point[1:]))
```




    [(1, 3), (3, 4), (4, 8), (8, 13), (13, 17), (17, 20)]




```python
# 다음 문제를 풀어보세요.
def f(x):
    return x[1] - x[0]

sorted(zip(point, point[1:]), key=f)
```




    [(3, 4), (1, 3), (17, 20), (4, 8), (13, 17), (8, 13)]




```python
def f(x):
    return x[1] - x[0]

sorted(zip(point, point[1:]), key=f)[0]
```




    (3, 4)




```python
sorted(zip(point, point[1:]), key=lambda x:x[1]-x[0])[0]
```




    (3, 4)




```python
# https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 응급도
# [3, 76, 24]
# 우선순위
# [3, 1, 2]

l = [3, 76, 24]
정렬된값 = sorted(l, reverse=True)
정렬된값 # [76, 24, 3]
# 우리가 원하는 값 [2, 0, 1]

결과값 = [
            정렬된값.index(l[0]), 
            정렬된값.index(l[1]), 
            정렬된값.index(l[2])
        ]
결과값
```




    [2, 0, 1]



## !! 오늘 배운 것 정리

1. 함수
    1. 코드 덩어리(정말 쉽게 설명하면)
    2. 코드를 재사용 할 수 있으며, 실수를 줄일 수 있습니다.
    3. 코드의 구조를 한 눈에 파악할 수 있습니다.
    4. 형태
        ```python
        # 파선아실(파라미터는 선언할 때, 아규먼트는 실제)
        def function(x, y):
            z = x + y
            return z
        print(f'function(5, 7) = {function(5, 7)}')
        ```
    5. 함수 안에 함수와 함수 안에 변수는 밖에서 접근이 불가합니다.
    6. 지역 변수와 전역 변수
        * 전역변수 : 전역에서 접근할 수 있는 변수
        * 지역변수 : 함수 내에서만 접근할 수 있는 변수
        ```python
        # 전역변수는 각 함수에서 접근은 가능하지만 수정이 되진 않습니다.
        # only read
        # global이라는 키워드로 밖에 있는 변수를 수정할 수도 있지만 권하지 않습니다.
        # 권하지 않기에 요약자료에도 없습니다.
        a = 100
        def f():
            a = a + 1
        f()
        ```
    7. 재귀함수
        * 내가 나를 호출하는 것입니다.
        * 재귀 <-> for문은 대부분 호환이 가능합니다.
        * 반복문 사용하시기를 권합니다!
        * 어렵고 효율도 안좋아요! (얼마나 효율이 안좋은지도 확인해보겠습니다.)
        * 필수적으로 사용하는 곳이 있습니다.
        ```python
        def f(n):
            if n <= 1:
                return 1
            else:
                return n * f(n-1)

        f(5)
        ```
2. list (리스트)
    * 순서를 가진 데이터들의 집합(Sequence)
    * 리스트는 값의 변경
    * 리스트 안에 리스트로 다차원의 리스트를 만드는 것도 가능
    * 리스트 안에 다른 딕셔너리, 셋, 튜플 등을 넣는 것도 가능합니다
    ```python
    l = [10, 20, 30, 40]
    print(l[0]) # 순서로 값 호출
    l[0] = 1000 # 값의 변경 가능
    print(l)

    data = [[1, 2, 3], # 다차원 배열
        [4, 5, 6],
        [7, 8, 9]]

    print(data)
    ```
    * 리스트 메서드
        * append : 맨 뒤에 값 추가
        * clear : 모든 값 지우기
        * copy : 얕은 복사
        * count : 갯수 세기
        * extend : 확장하기(뒤에 순회 가능한 객체가 들어오면 순차적으로 추가)
        * index : 위치 찾기
        * insert : 삽입하기
        * pop: 맨 뒤에서 값 꺼내기(index가 들어오면 index에서 값 꺼냄)
        * remove : 값 지우기
        * reverse : 역순
        * sort : 정렬

## 깊은 복사와 얕은 복사

* 깊은 복사는 안에 있는 요소까지 새로 생성
* 얕은 복사는 가장 바깥에 있는 요소의 주소만 새로 생성(a is b는 False, a == b는 True)


```python
# 아무런 복사도 이뤄지지 않은 상태
l = [[1, 2, 3], [4, 5, 6]]
ll = l
ll[0][0] = 10
l, ll
```




    ([[10, 2, 3], [4, 5, 6]], [[10, 2, 3], [4, 5, 6]])




```python
# 얕은 복사
l = [1000, 2000, 3000, 4000, 5000, 6000]
ll = l.copy()
ll[0] = 10
l, ll
```




    ([1, 2, 3, 4, 5, 6], [10, 2, 3, 4, 5, 6])




```python
l = [1000, 2000, 3000, 1000, 1000, 1000]
id(l[0]), id(l[3]), id(l[4]), id(l[5])
```




    (139632941249648, 139632941249648, 139632941249648, 139632941249648)




```python
# 얕은 복사
l = [1000, 2000, 3000, 4000, 5000, 6000]
ll = l.copy()
id(l[0]), id(ll[0]) # 같은 값이 나오니까 같은 객체를 가리키고 있다?
```




    (139632941250224, 139632941250224)




```python
# 얕은 복사
l = [1000, 2000, 3000, 4000, 5000, 6000]
ll = l.copy()
id(l), id(ll)
```




    (139633419252864, 139632939250304)




```python
# 얕은 복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l.copy()
ll[0][0] = 10
l, ll
```




    ([[10, 2, 3], [4, 5, 6]], [[10, 2, 3], [4, 5, 6]])




```python
id(l[0]), id(ll[0])
```




    (139633419254976, 139633419254976)




```python
# 얕은 복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l.copy()
ll[0] = 100
l, ll
```




    ([[1, 2, 3], [4, 5, 6]], [100, [4, 5, 6]])




```python
# 깊은 복사
import copy

l = [[1, 2, 3], [4, 5, 6]]
ll = copy.deepcopy(l)
ll[0][0] = 10
l, ll
```




    ([[1, 2, 3], [4, 5, 6]], [[10, 2, 3], [4, 5, 6]])




```python
# 깊은 복사
import copy

l = [[1, 2, 3], [4, 5, 6]]
ll = copy.deepcopy(l)
ll[0][0] = 10
id(l), id(ll)
id(l[0]), id(ll[0])
id(l[0][0]), id(ll[0][0])
```




    (139634188714224, 139634188714512)




```python
# 깊은 복사
import copy

l = [[1, 2, [1, [999, 998]]], [4, 5, [2, [333, 332]]]]
ll = copy.deepcopy(l)
ll[0][2][1][0] = 10
l, ll
id(l), id(ll)
id(l[0]), id(ll[0])
id(l[0][0]), id(ll[0][0])
```




    ([[1, 2, [1, [999, 998]]], [4, 5, [2, [333, 332]]]],
     [[1, 2, [1, [10, 998]]], [4, 5, [2, [333, 332]]]])



* 얕은 복사는 1 계층만 복사합니다.
* 깊은 복사는 n 계층까지 모두 복사합니다. 

* 나를 이해시키는 단 하나의 코드는 반드시 존재합니다.


```python
# 얕은 복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l[:]
l[0] = 100
l, ll
```




    ([100, [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])




```python
# 얕은 복사
l = [[1, 2, 3], [4, 5, 6]]
ll = l[:] # l.copy를 써도 마찬가지입니다.
l[0][0] = 100
l, ll
```




    ([[100, 2, 3], [4, 5, 6]], [[100, 2, 3], [4, 5, 6]])




```python
# sorted도 얕은 복사!
l = [[1, 2], [3, 4], [5, 6]]
ll = sorted(l)
l[0][0] = 100
l, ll
```




    ([[100, 2], [3, 4], [5, 6]], [[100, 2], [3, 4], [5, 6]])




```python
# 얕은 복사
# 리스트 컴프리헨션은 안배운 내용이니 keep해두시고
# for문 배운다음 다시 오셔서 복습하시기를 권해드립니다.
l = [[1, 2, 3], [4, 5, 6]]
ll = [i for i in l]
l[0][0] = 100
l, ll
```




    ([[100, 2, 3], [4, 5, 6]], [[100, 2, 3], [4, 5, 6]])




```python
# 1단계 깊은 복사
# 리스트 컴프리헨션은 안배운 내용이니 keep해두시고
# for문 배운다음 다시 오셔서 복습하시기를 권해드립니다.
l = [[1, 2, 3], [4, 5, 6]]
ll = [i[:] for i in l]
l[0][0] = 100
l, ll
```




    ([[100, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])



## 다차원 리스트


```python
a = [[1, 2, 3],
     [11, 22, 33],
     ['leehojun', 20, 30]]

# 문제 : jun만 뽑아주세요!
print(a[2][0][-3:])
print(a[2][0][5:])
print(a[2][0][5], a[2][0][6], a[2][0][7], sep='')
```

    jun
    jun
    jun


## 리스트에서 built-in function을 활용

* 알아야 하는 built-in function
    ```
    A
    abs()
    all()
    any()

    B
    bin()
    bool()

    C
    chr()

    D
    dict()
    dir()

    E
    enumerate()
    eval()

    F
    filter()
    float()

    G
    globals()

    H
    help()
    hex()

    I
    id()
    input()
    int()
    isinstance()
    issubclass()
    iter()

    L
    len()
    list()
    locals()

    M
    map()
    max()
    min()

    N
    next()

    O
    object()
    oct()
    open()
    ord()

    P
    pow()
    print()
    property()

    R
    range()
    repr()
    reversed()
    round()

    S
    set()
    setattr()
    slice()
    sorted()
    staticmethod()
    str()
    sum()
    super()

    T
    tuple()
    type()

    V
    vars()

    Z
    zip()
    ```


```python
a = [1, 2, 3, 4, 5, 6, 7, 8]
print(max(a)) #최댓값
print(min(a)) #최솟값
print(sum(a)) #전체값의 합
```

    8
    1
    36



```python
#2차원
a = [[1, 2, 3, 'a'],
     [11, 22, 33, 'aaa'],
     [10, 2000, 30, 'aa']]

max(a, key=lambda x:x[1])
max(a, key=lambda x:len(x[3]))
```




    [11, 22, 33, 'aaa']




```python
# 이름, 별점, 객실수, 가격
호텔 = [
    ['이스트소프트 호텔', 5, 100, 155000],
    ['삼스트소프트 호텔', 4, 80, 145000],
    ['사스트소프트 호텔', 3, 70, 135000], 
    # 마지막에 콤마를 허락하는 언어는 제한적(특히 JSON에서는 엄격해서 허락하지 않습니다.)
]

max(호텔, key=lambda x:x[3]) # 가장 가격이 높은 것을 뽑아낼 수 있음
min(호텔, key=lambda x:x[3])
```




    ['사스트소프트 호텔', 3, 70, 135000]




```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [10, 2000, 30]]
     
max(a, key=lambda x:x[1])
min(a, key=lambda x:x[1])
# sum(a) error
sum(a, [])
```

## 리스트의 순회


```python
#1차원
a = [1, 2, 3, 4, 5, 6, 7, 8]

# for 변수 in 순회가능한객체
for i in a:
     print(i)
```

    1
    2
    3
    4
    5
    6
    7
    8



```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [13, 20000, 300000]]

for i in a:
    print(i)
    print('---')
print('end')
```

    [1, 2, 3]
    ---
    [11, 22, 33]
    ---
    [13, 20000, 300000]
    ---
    end



```python
#2차원
a = [[1, 2, 3],
     [11, 22, 33],
     [13, 20000, 300000]]

for i in a:
    for j in i:
        print(j)
        print('---')
print('end')
```

    1
    ---
    2
    ---
    3
    ---
    11
    ---
    22
    ---
    33
    ---
    13
    ---
    20000
    ---
    300000
    ---
    end


## range


```python
# range(start, stop, step) 
# 슬라이싱과 같은 규칙
# 슬라이싱은 ':'(콜론)으로 연결되어 있고
# range는 ','(콤마)로 연결되어 있습니다.

print(list(range(100))) 
# python 2.x에서 python 3.x에 range를 사용하고 싶다면 xrange(10)
print(list(range(5, 10)))

print(list(range(0, 101, 2))) #짝수
print(list(range(1, 101, 2))) #홀수
print(list(range(100, 1, -2)))
print(sum(list(range(0, 101))))
print(sum(range(0, 101))) # 이렇게 형 변환을 하지 않고 sum하시는 것을 권합니다.
```

    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    [5, 6, 7, 8, 9]
    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
    [100, 98, 96, 94, 92, 90, 88, 86, 84, 82, 80, 78, 76, 74, 72, 70, 68, 66, 64, 62, 60, 58, 56, 54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10, 8, 6, 4, 2]
    5050
    5050


## list comprehension


```python
# l = [1, 2, 3, 4, ...]
# list(range(1, 101))
l = []
for i in range(1, 101):
    l.append(i)
l
```


```python
# l = []
# for i in range(1, 11):
#     l.append(i**i)
# l

l = [i**i for i in range(1, 11)]
l

l = [i for i in range(1, 11)]
l
```




    [1, 4, 27, 256, 3125, 46656, 823543, 16777216, 387420489, 10000000000]




```python
l = []
for i in range(1, 100):
    if i %3 == 0 or i %5 == 0:
        l.append(i)

[i for i in range(1, 100) if i %3 == 0 or i %5 == 0]
```

## tuple (튜플)

- 튜플은 순서가 있는 시퀀스형 자료형입니다.
- 참조값은 변경이 불가능(immutable) 합니다.
- 다른 자료형을 입력할 수 있으며, 튜플 안에 튜플로 다차원의 튜플을 만드는 것도 가능합니다.
- 값의 중복을 허락합니다.


```python
t = (10, 20, 30)
t[1] = 1000
```


```python
l = [1, 2, 3]
t = (l, 20, 30) # 불변인 것은 t가 l을 참조하고 있다는 것이 불변!
l[0] = 1000
t
```




    ([1000, 2, 3], 20, 30)




```python
t = (10, 20, 30, 40, 50)
t[:3]
```




    (10, 20, 30)




```python
type(t), dir(t)
```




    (tuple,
     ['__add__',
      '__class__',
      '__class_getitem__',
      '__contains__',
      '__delattr__',
      '__dir__',
      '__doc__',
      '__eq__',
      '__format__',
      '__ge__',
      '__getattribute__',
      '__getitem__',
      '__getnewargs__',
      '__gt__',
      '__hash__',
      '__init__',
      '__init_subclass__',
      '__iter__',
      '__le__',
      '__len__',
      '__lt__',
      '__mul__',
      '__ne__',
      '__new__',
      '__reduce__',
      '__reduce_ex__',
      '__repr__',
      '__rmul__',
      '__setattr__',
      '__sizeof__',
      '__str__',
      '__subclasshook__',
      'count',
      'index'])




```python
t = (10, 20, 30, 40, 50, 20)
t.index(20), t.count(20)
```




    (1, 2)




```python
t = tuple('leehojun')
t
t = tuple()
t
t = tuple(range(10))
t
t = (1) 
t
t = (1,) #원소를 하나씩 넣고 싶을 때는 콤마(,)를 사용해줍니다.
t
```




    1



## dict (딕셔너리, 사전형)

- 딕셔너리는 순서가 없는 자료형입니다.
- 사전형은 Key와 Value 가 하나의 묶음으로 이루어진 자료 체계입니다.
- 값의 변경이 가능합니다.
- 다른 자료형을 입력할 수 있습니다.
- 키의 중복은 허락하지 않고, 값의 중복을 허락합니다.


```python
{
    '게시물 번호' : 1,
    '게시자': '이호준',
    '게시물 내용' : '......'
}
```




    {'게시물 번호': 1, '게시자': '이호준', '게시물 내용': '......'}




```python
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d['one']
```




    '하나'




```python
d['two'] = '투'
d
```




    {'one': '하나', 'two': '투', 'three': '셋'}




```python
d = {} #dict
type(d)

d = {10} #set
type(d)

d = dict()
type(d)

d = {'one' : 1}
type(d)
```


```python
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d.items()
```




    dict_items([('one', '하나'), ('two', '둘'), ('three', '셋')])




```python
dict([('one', '하나'), ('two', '둘'), ('three', '셋')])
```




    {'one': '하나', 'two': '둘', 'three': '셋'}




```python
dict([['one', '하나'], ['two', '둘'], ['three', '셋']])
```




    {'one': '하나', 'two': '둘', 'three': '셋'}




```python
dict(name='leehojun', age=10)
```




    {'name': 'leehojun', 'age': 10}




```python
list(zip('ABC', '123', 'abc'))

dict(zip('ABC', '123')) #형변환
```




    {'A': '1', 'B': '2', 'C': '3'}




```python
# 연습문제
# dict와 zip를 사용해서 아래와 같은 형태로 데이터를 만들어주세요.
# 잘 모르시겠으면 어떻게든 저 형태를 만들어주세요.
dict(zip('ABC', [[10,20], [20,30], [30,40]]))
dict(zip('ABC', [list(elem) for elem in zip([10, 20, 30], [20, 30, 40])]))
l = [10, 20, 30, 40]
dict(zip('ABC', zip(l, l[1:])))
dict(zip(['A','B','C'],[[10, 20],[20, 30],[30, 40]]))
# 원하는 형태 {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}
```




    {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}




```python
'B' in {'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}
```




    True




```python
len({'A': [10, 20], 'B': [20, 30], 'C': [30, 40]})
```




    3




```python
# 공부해두시면 좋습니다!
def switch(day):
    return {
        1 : '월요일',
        2 : '화요일',
        3 : '수요일',
        4 : '목요일',
        5 : '금요일',
        6 : '토요일',
        7 : '일요일',
    }[day]

switch(7)
# switch(8) # error
```




    '일요일'




```python
# 공부해두시면 좋습니다!
def switch(day):
    return {
        1 : '월요일',
        2 : '화요일',
        3 : '수요일',
        4 : '목요일',
        5 : '금요일',
        6 : '토요일',
        7 : '일요일',
    }.get(day)

switch(7)
switch(8) # get을 사용하면 None을 줍니다.
```


```python
def switch(day):
    return {
        1 : '월요일',
        2 : '화요일',
        3 : '수요일',
        4 : '목요일',
        5 : '금요일',
        6 : '토요일',
        7 : '일요일',
    }.get(day, '요일을 찾지 못했습니다.')

switch(8) 
# get을 사용하면 못찾는 값을 넣었을 때 '요일을 찾지 못했습니다.' 값을 줍니다.
```




    '요일을 찾지 못했습니다.'




```python
!python --version
```

    Python 3.10.11



```python
# 3.10버전 최신 문법에서는 match문법을 허용합니다!
def number_to_string(agrument):
    match agrument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "nothing"

number_to_string(1)
```




    'one'




```python
%%timeit

s = 0
for i in range(10000):
    s += i
```

    1.04 ms ± 37.7 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)



```python
%%timeit

sum([i for i in range(10000)])
```

    907 µs ± 161 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)



```python
%%timeit

sum(range(10000))
```

    536 µs ± 237 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)



```python
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.keys()
```




    dict_keys(['A', 'B', 'C'])




```python
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.values()
```




    dict_values([[10, 20], [20, 30], [30, 40]])




```python
{'A': [10, 20], 'B': [20, 30], 'C': [30, 40]}.items()
```




    dict_items([('A', [10, 20]), ('B', [20, 30]), ('C', [30, 40])])




```python
dict.fromkeys('leehojun')
```




    {'l': None, 'e': None, 'h': None, 'o': None, 'j': None, 'u': None, 'n': None}




```python
dict.fromkeys('leehojun', 100)
```




    {'l': 100, 'e': 100, 'h': 100, 'o': 100, 'j': 100, 'u': 100, 'n': 100}




```python
keys = ('name', 'age', 'grade')
values = ('leehojun', '10', '수')

dict.fromkeys(keys, values)
```




    {'name': ('leehojun', '10', '수'),
     'age': ('leehojun', '10', '수'),
     'grade': ('leehojun', '10', '수')}




```python
d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
d.update({'one' : 1, 'two' : 2})
d
```




    {'one': 1, 'two': 2, 'three': '셋'}



## 딕셔너리의 순회


```python
# key만 순회합니다.
d = {'two' : 2, 'three' : '셋'}
for i in d:
    print(i)
```

    two
    three



```python
d = {'two' : 2, 'three' : '셋'}
for i in d:
    print(d[i])
```

    2
    셋


## 언패킹


```python
# 패킹 :   1, 2, 3   => [1, 2, 3]
# 언패킹 : [1, 2, 3] => 1, 2, 3
```


```python
a, b, c = 10, 20, 30
a
```




    10




```python
a, b, c = (10, 20, 30) # 소괄호든 대괄호든 상관 없습니다.
a
```




    10




```python
i, j = [10, 20]
i
```




    10




```python
for i, j in [[10, 20], [30, 40], [50, 60]]:
    print(i, j)
```

    10 20
    30 40
    50 60



```python
for i, j, k in [[10, 20, [1, 2]], [30, 40, [3, 4]], [50, 60, [5, 6]]]:
    print(i, j, k)
```

    10 20 [1, 2]
    30 40 [3, 4]
    50 60 [5, 6]



```python
for i, j, k in [[10, 20, [1, 2]], [30, 40, [3, 4]], [50, 60, []]]:
    print(i, j, k)
```

    10 20 [1, 2]
    30 40 [3, 4]
    50 60 []



```python
# swap
a = 10
b = 15
a, b = b, a
a, b
```




    (15, 10)




```python
# swap in c
a = 10
b = 15
temp = a
a = b
b = temp
a, b
```




    (15, 10)




```python
for i, j in d.items():
     print(i, j)
```

    two 2
    three 셋


## max를 이용한 dict 최대 value의 key값 가져오기




```python
d = {
    'test1': 10,
    'test2': 20,
    'test3': 31,
    'test4': 11,
}

# max(d.values()) # 이걸로는 뭔가 찾아내기 힘듭니다.
max(d, key=lambda x: d[x])
max(d, key=d.get) #많이 사용하는 코드입니다.
```




    'test3'



## set (셋, 집합)

* 집합 자료형은 중복을 허용하지 않으며
* 순서가 없는 자료형


```python
n = set([1, 1, 2, 2, 3, 3, 4])
print(n)
```

    {1, 2, 3, 4}



```python
s = set('hello world')
print(s)
```

    {'d', 'h', 'r', 'e', 'w', ' ', 'l', 'o'}



```python
type(s), dir(s)
```




    (set,
     ['__and__',
      '__class__',
      '__class_getitem__',
      '__contains__',
      '__delattr__',
      '__dir__',
      '__doc__',
      '__eq__',
      '__format__',
      '__ge__',
      '__getattribute__',
      '__gt__',
      '__hash__',
      '__iand__',
      '__init__',
      '__init_subclass__',
      '__ior__',
      '__isub__',
      '__iter__',
      '__ixor__',
      '__le__',
      '__len__',
      '__lt__',
      '__ne__',
      '__new__',
      '__or__',
      '__rand__',
      '__reduce__',
      '__reduce_ex__',
      '__repr__',
      '__ror__',
      '__rsub__',
      '__rxor__',
      '__setattr__',
      '__sizeof__',
      '__str__',
      '__sub__',
      '__subclasshook__',
      '__xor__',
      'add',
      'clear',
      'copy',
      'difference',
      'difference_update',
      'discard',
      'intersection',
      'intersection_update',
      'isdisjoint',
      'issubset',
      'issuperset',
      'pop',
      'remove',
      'symmetric_difference',
      'symmetric_difference_update',
      'union',
      'update'])




```python
n = set([1, 1, 2, 2, 3, 3, 4])
n.add(1000)
print(n)
```

    {1, 2, 3, 4, 1000}



```python
n = set([1, 1, 2, 2, 3, 3, 4])
n.update({10, 20})
print(n)
```

    {1, 2, 3, 4, 20, 10}



```python
n = set([1, 1, 2, 2, 3, 3, 4])
n.remove(1)
print(n)
```

    {2, 3, 4}


* pop은 실무에서 잘 사용하지 않습니다. 값을 랜덤하게 뽑아내기 때문입니다. 높은 확률로 앞에서부터 뽑아내긴 하지만 확률에 기대는 코딩을 하지 않기를 바랍니다. 공식문서에서는 랜덤하게 뽑아낸다고 되어 있습니다.
* https://docs.python.org/3.11/library/stdtypes.html#frozenset.pop


```python
# 교집합 별 3개
a = {1, 2, 3}
b = {3, 4, 5}
a & b
a.intersection(b)
```




    {3}




```python
# 합집합
a = {1, 2, 3}
b = {3, 4, 5}
a | b
a.union(b)
# a + b # error
```




    {1, 2, 3, 4, 5}




```python
# 차집합
a = {1, 2, 3}
b = {3, 4, 5}
a - b
a.difference(b)
# a + b # error
```




    {1, 2}




```python
s = {1, 2, 3, 4}
ss = {3, 4, 5, 6}
s.issubset({1, 2})
s.issubset({1, 2, 3, 4, 5, 6, 7, 8})
```




    True




```python
# https://school.programmers.co.kr/learn/courses/30/lessons/120903?language=python3
def solution(s1, s2):
    return len(set(s1) & set(s2))
```


```python
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# my_string	    result
# "people"	    "peol"
```


```python
# my_string	    result
# "people"	    "peol"

result = ''
for i in 'people':
    if i not in result:
        result += i
result
```




    'peol'




```python
def solution(my_string):
    return set(my_string)

solution('people')
```




    {'e', 'l', 'o', 'p'}




```python
def solution(my_string):
    return ''.join(set(my_string))

solution('people')
```




    'leop'




```python
def solution(my_string):
    집합 = set(my_string)
    result = ''
    for i in my_string:
        if i in 집합:
            result += i
            집합.remove(i)
    return result

solution('people')
```




    'peol'



## !! 연습문제


```python
student_score = {
		'홍의': 97,
		'원희': 60,
		'동해': 77,
		'변수': 79,
		'창현': 89,
}
```


```python
sum(student_score.values())
```




    402




```python
sum(student_score.values())/len(student_score)
```




    80.4




```python
이름 = max(student_score, key=student_score.get)
가장큰값 = student_score[이름]
print(이름, 가장큰값)
```

    홍의 97



```python
가장큰값 = max(student_score.values())
for i in student_score:
    if student_score[i] == 가장큰값:
        print(i, 가장큰값)
```

    홍의 97



```python
이름 = min(student_score, key=student_score.get)
가장작은값 = student_score[이름]
print(이름, 가장작은값)
```

    원희 60



```python
like = ['볶음밥', '라면', '국수', '파스타', '치킨', '짜장면', '국밥']
dislike = ['국밥', '짬뽕', '찜닭', '파스타', '국수', '카레', '덮밥']
set(like) - set(dislike)
# 아래와 같이 코드를 작성할 수도 있습니다.
final_menu = [menu for menu in like if menu not in dislike]
```




    {'라면', '볶음밥', '짜장면', '치킨'}



## !! 오늘 배운 것 정리

1. sort
    * sorted는 원본을 만지지 않는 'built-in function', 정렬입니다.
    * sort는 원본을 만지는 '리스트 메서드', 정렬입니다.
    * sort의 다양한 예
        ```python
        l = [[1, 10, 'leehojun'], 
            [20, 30, 'hojun'], 
            [10, 20, 'weniv!'], 
            [1, 2, 'hello world'], 
            [55, 11, 'sun']]

        # 1. 글자 수 대로 정렬해주세요.
        def f(x):
            return len(x[2])

        print(sorted(l, key=f, reverse=False))
        print(sorted(l, key=lambda x:len(x[2]), reverse=False))

        # 2. 맨 앞에 위치한 숫자대로 정렬해주세요.
        def f2(x):
            return x[0]

        print(sorted(l))
        print(sorted(l, key=f2))
        print(sorted(l, key=lambda x:x[0]))

        # 3. 중앙에 위치한 값대로 정렬해주세요.

        def f3(x):
            return x[1]

        print(sorted(l))
        print(sorted(l, key=f3))
        print(sorted(l, key=lambda x:x[1]))

        l = [[1, 10, 32], 
            [20, 30, 11], 
            [10, 20, 22], 
            [1, 2, 13], 
            [55, 11, 44]]
            
        # 4. 3개의 전체 합이 작은 순서대로 출력해주세요.

        def f4(x):
            return x[0] + x[1] + x[2]

        def f5(x):
            return sum(x)

        print(sorted(l, key=f4))
        print(sorted(l, key=f5))
        print(sorted(l, key=lambda x: sum(x)))
        print(sorted(l, key=sum))
        ```

2. 깊은 복사와 얕은 복사
    1. 깊은 복사 : 완전히 다른 객체를 만듭니다.(깊은 복사는 n 계층까지 모두 복사)
        ```python
        # 깊은 복사
        import copy

        l = [[1, 2, 3], [4, 5, 6]]
        ll = copy.deepcopy(l)
        ll[0][0] = 10
        l, ll
        ```
    2. 얕은 복사 : 내용물은 같은 다른 객체를 만듭니다.(얕은 복사는 1 계층만 복사)
        ```python
        # 얕은 복사
        l = [[1, 2, 3], [4, 5, 6]]
        ll = l[:] # l.copy, sorted를 써도 마찬가지입니다.
        l[0][0] = 100
        l, ll
        ```

3. range
    ```python
    # range(start, stop, step) 
    # 슬라이싱은 ':'(콜론)으로 연결되어 있고
    # range는 ','(콤마)로 연결되어 있습니다.

    print(list(range(100))) 
    # python 2.x에서 python 3.x에 range를 사용하고 싶다면 xrange(10)
    print(list(range(5, 10)))

    print(list(range(0, 101, 2))) #짝수
    print(list(range(1, 101, 2))) #홀수
    print(list(range(100, 1, -2)))
    print(sum(list(range(0, 101))))
    print(sum(range(0, 101))) # 이렇게 형 변환을 하지 않고 sum하시는 것을 권합니다.
    ```

4. list comprehension
    ```python
    # l = []
    # for i in range(1, 11):
    #     l.append(i**i)
    # l

    l = [i**i for i in range(1, 11)]
    l
    ```

5. tuple
    - 튜플은 순서가 있는 시퀀스형 자료형입니다.
    - 참조값은 변경이 불가능(immutable) 합니다.
        ```python
        t = (10, 20, 30)
        t[1] = 1000 # error
        ```
    - 다른 자료형을 입력할 수 있으며, 튜플 안에 튜플로 다차원의 튜플을 만드는 것도 가능합니다.
    - 값의 중복을 허락합니다.
    - 메서드는 index와 count밖에 없습니다.

6. dict (딕셔너리, 사전형)
    - 딕셔너리는 순서가 없는 자료형입니다.
    - 사전형은 Key와 Value 가 하나의 묶음으로 이루어진 자료 체계입니다.
    - 값의 변경이 가능합니다.
        ```python
        d = {'one' : '하나', 'two' : '둘', 'three' : '셋'}
        print(d['one']) # 호출
        d['two'] = '투' # 변경
        d
        ```
    - 다른 자료형을 입력할 수 있습니다.
    - 키의 중복은 허락하지 않고, 값의 중복을 허락합니다.
    - dict를 활용한 switch 만들기
        ```python
        def switch(day):
            return {
                1 : '월요일',
                2 : '화요일',
                3 : '수요일',
                4 : '목요일',
                5 : '금요일',
                6 : '토요일',
                7 : '일요일',
            }.get(day, '요일을 찾지 못했습니다.')

        switch(8) 
        ```
    - max를 이용한 dict 최대 value의 key값 가져오기
        ```python
        d = {
            'test1': 10,
            'test2': 20,
            'test3': 31,
            'test4': 11,
        }

        # max(d.values()) # 이걸로는 뭔가 찾아내기 힘듭니다.
        max(d, key=lambda x: d[x])
        max(d, key=d.get) #많이 사용하는 코드입니다.
        ```

7. 언패킹
    * 언패킹 예
        ```python
        for i, j, k in [[10, 20, [1, 2]], [30, 40, [3, 4]], [50, 60, [5, 6]]]:
            print(i, j, k)
        ```
    * swap 예
        ```python
        # swap
        a = 10
        b = 15
        a, b = b, a
        a, b
        ```

8. set (셋, 집합)
    * 집합 자료형은 중복을 허용하지 않으며
    * 순서가 없는 자료형
        ```python
        n = set([1, 1, 2, 2, 3, 3, 4])
        print(n)
        ```
    * 메서드
        - add : 값 추가
        - update : 값 여러개 추가
        - remove : 제거
        - copy : 값 복사
        - union : 합집합
        - intersection : 교집합
        - difference : 차집합
        - issubset : 부분집합


```python
# 질의응답:
# 1. 자습시간 활용
# 혼자 자습하시더라도 일단 보이스채널로 모두 모여주세요.
# 1.1 혼자라는 느낌이 들면 기댈 때가 없습니다.ㅜㅜ
# 1.2 정보 공유차원에서라도 채팅방이 활성화 되길 바랍니다.

# 2. max 값을 제대로 출력하지 않습니다.
print(max(student_score.items()))
print(min(student_score.items()))
# max, min, sorted 모두 가장 앞에 값 기준으로 판단합니다.
# 가장 앞에 값에 key 값이 있기 때문에 key 값만 본것입니다.

# 3. 좋은 코드란? set을 이용한 코드보다 이 코드가 별로일까요?
final_menu = [menu for menu in like if menu not in dislike]
print(final_menu)

# 4. args, kargs
# 뒤에서 진행하게 됩니다. => 함수의 아규먼트 수

# 5. 차원을 알고 싶은 경우? numpy의 ndim을 사용하지 않고?
# str으로 변환 후 맨 앞에 [의 갯수를 count하면 됩니다.

# 6. 질문 : max(student_score, key=student_score.get) 어떻게 동작하는가?
# 답변 : max가 key=안에 있는 함수로 key를 전달합니다! 그래서 student_score.get이 함수가 된거에요. 
# 파라미터 값은 student_score에 key이고요! 이건 제가 다음주 월요일에 한 번 더 해드릴게요. 


# https://school.programmers.co.kr/learn/courses/30/lessons/181943#
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

# 이렇게 제출했는데 테스트 케이스에서 하나만 실패 => 예외 케이스는 케이스를 캐치하기가 정말 힘듭니다.
# 일단 각 값이 0이나 1인 것을 찾아보고
# 예외처리 했는데도 풀이가 안되면 다른 풀이를 해보세요.
```

    ('홍의', 97)
    ('동해', 77)
    ['볶음밥', '라면', '치킨', '짜장면']



```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

solution("He11oWor1d", 'a', 0)
```




    'ae11oWor1d'




```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

solution("H", 'a', 0)
```




    'a'




```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

solution("He", 'ji', 1)
```




    'Hji'




```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string.replace(my_string[s:os_len], overwrite_string)

solution("He", 'ji', 0)
```




    'ji'




```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    원본길이 = len(my_string)
    결괏값 = my_string.replace(my_string[s:os_len], overwrite_string) # replace가 문제 있습니다.
    return 결괏값[:원본길이]

solution("He", 'ji', 1)
```




    'Hj'




```python
def solution(my_string, overwrite_string, s):
    os_len = len(overwrite_string) + s
    return my_string[:s] + overwrite_string + my_string[os_len:]

solution("He11oWor1d", "lloWorl", 2)
solution("Program29b8UYP", "merS123", 7) # "ProgrammerS123"
```




    'ProgrammerS123'




```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']

z = zip(li, st)

print(z)
print(type(z))

print(list(z)[0])      # 이후에 z는 있지만 모든 원소가 사라져 비어있게됨
print(z)        # 같은 객체 z 있기는 하지만....
tmp= list(z)
print(tmp) 
```

    <zip object at 0x7efed3cf1d40>
    <class 'zip'>
    (1, 'VScode')
    <zip object at 0x7efed3cf1d40>
    []



```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']
z = zip(li, st)

for i in z:
    print(i)

for i in z:
    print(i)
```

    (1, 'VScode')
    (2, 'Pycharm')
    (3, 'Jupyter notebook')



```python
li = [1,2,3]
st = ['VScode', 'Pycharm', 'Jupyter notebook']
i = iter(zip(li, st))
next(i)
```




    (1, 'VScode')




```python
next(i)
```




    (2, 'Pycharm')




```python
next(i)
```




    (3, 'Jupyter notebook')




```python
next(i)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-248-a883b34d6d8a> in <cell line: 1>()
    ----> 1 next(i)
    

    StopIteration: 



```python
li = [1,2,3]
i = iter(li)
next(i), next(i), next(i)
```




    (1, 2, 3)




```python
next(i)
```


    ---------------------------------------------------------------------------

    StopIteration                             Traceback (most recent call last)

    <ipython-input-252-a883b34d6d8a> in <cell line: 1>()
    ----> 1 next(i)
    

    StopIteration: 



```python
li
```




    [1, 2, 3]




```python
z
# zip 함수가 한 번 호출되면 모든 요소를 반환하고 iterator가 소멸됩니다. 
# 따라서, zip 객체를 다시 사용하려면 다시 호출하여 새로운 iterator를 생성해야 합니다.
# https://junstar92.tistory.com/358
```




    <zip at 0x7efed3c74d40>




```python
li = [1, 2, 3]
z = map(lambda x:x**2, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    4
    9



```python
li = [1, 2, 3]
z = sorted(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    2
    3
    1
    2
    3



```python
li = [1, 2, 3]
z = reversed(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    3
    2
    1



```python
li = [1, 2, 3]
z = filter(lambda x:x>1, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    2
    3


## (질의응답) max(student_score, key=student_score.get)


```python
def 함수(x):
    print(x, ll[x])
    return ll[x]

l = [2, 4, 5, 3, 6, 0, 7, 1]
ll = [10, 20, 30, 40, 50, 60, 70, 80]

max(l, key=함수)
```

    2 30
    4 50
    5 60
    3 40
    6 70
    0 10
    7 80
    1 20





    7




```python
def 함수(x):
    print(x, len(ll[x]))
    return len(ll[x])

l = [2, 4, 5, 3, 6, 0, 7, 1]
ll = ['hello', 'a', 'bb', 'ccc', 'a', 'bbbb', 'hello world', 'cc']

max(l, key=함수)
```

    2 2
    4 1
    5 4
    3 3
    6 11
    0 5
    7 2
    1 1





    6




```python
# return에 초점을 맞춰주세요.
def 함수(x):
    return d.get(x)

d = {
    'test1': 10,
    'test2': 20,
    'test3': 31,
    'test4': 11,
}

max(d, key=함수)
max(d, key=d.get)
# max(d, key=lambda x: d[x])
```




    'test3'




```python
# return에 초점을 맞춰주세요.
def 함수(x):
    return len(x)
l = ['a', 'bb', 'ccc', 'dd']

max(l, key=함수)
max(l, key=len)
```




    'ccc'




```python
def 함수(x):
    return d.get(x)

수학 = {
    '학생1': 10,
    '학생2': 20,
    '학생3': 31,
    '학생4': 11,
}

과학 = {
    '학생1': 11,
    '학생2': 17,
    '학생3': 13,
    '학생4': 11,
    '학생5': 25,
    '학생6': 100,
}

수학점수가가장큰사람 = max(수학, key=수학.get)
과학점수가가장큰사람 = max(과학, key=과학.get)
max(수학, key=과학.get)
```




    '학생2'



## (질의응답) 함수의 아규먼트 순서


```python
def f(a, b, c):
    print(a, b, c)

# f() # error
# f(100, 10) # error
f(a=100, b=200, c=300)
f(c=300, a=100, b=200) #실무에서 이렇게 순서를 바꿔서 넣지 않고 보통 순서를 지켜줍니다.

# 실무에서 언제 사용이 될까요?
# 파라미터, 아규먼츠가 매우 많을 때
# 이런 함수가 나오면 이 함수가 무엇을 뜻하는 것일까요?
# addNewControl("Title", 20, 50, 100, 50, 200, 300, 150)
# addNewControl(title="Title", height=20, width=50, textlen = 100, ...)
# 어? 컨트롤 박스를 만드는 구나...
```

    100 200 300
    100 200 300



```python
def f(a=10, b=20, c=30):
    print(a, b, c)

f()
f(100, 10)
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)
```


```python
def f(a=10, b=20, c): # c만 default value를 안주게 되면 error, 순서대로 안주어야 합니다.
    print(a, b, c)

# f() # error
# f(100, 10) # error
# f(a=100, b=200, c=300) # error
# f(c=300, a=100, b=200) # error
# f(c=300) # error
```


```python
def f(a, b=20, c=10): # 순서대로 안주어야 하기 때문에 a에 값을 넣지 않았습니다.
    print(a, b, c)

# f() # error
f(100, 10)
f(a=100, b=200, c=300)
f(c=300, a=100, b=200)
```

    100 10 10
    100 200 300
    100 200 300


## (질의응답) zip, map 등 한 번 순회가 되면 순회가 안되는 이유


```python
a = [1, 2, 3]
b = ['a', 'b', 'c']

z = zip(a, b)
print(list(z)) # [(1, 'a'), (2, 'b'), (3, 'c')]

# zip 객체는 한 번 사용되었으므로 빈 리스트가 반환됩니다.
print(list(z)) # []
```

    [(1, 'a'), (2, 'b'), (3, 'c')]
    []



```python
li = [1, 2, 3]
st = ['a', 'b', 'c']
z = zip(li, st)

for i in z:
    print(i)

for i in z:
    print(i)
```

    (1, 'a')
    (2, 'b')
    (3, 'c')



```python
li = [1, 2, 3]
st = ['a', 'b', 'c']
i = iter(zip(li, st))
next(i)
```




    (1, 'a')




```python
next(i)
```




    (2, 'b')




```python
next(i)
```




    (3, 'c')




```python
next(i) # StopIteration
```


```python
li = [1, 2, 3]
z = map(lambda x:x**2, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    4
    9



```python
li = [1, 2, 3]
z = reversed(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    3
    2
    1



```python
li = [1, 2, 3]
z = filter(lambda x:x>1, li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    2
    3



```python
# 계속 순회가 가능하게 설계가 되어 있습니다.
# 이런 설계를 뒤에서 우리가 직접 해보게 될 것입니다.
li = [1, 2, 3]
z = sorted(li)

for i in z:
    print(i)

for i in z:
    print(i)
```

    1
    2
    3
    1
    2
    3


## 조건문

* if, elif, else, continue, break


```python
x = 2
if x > 1 and x < 10:
    print('Hello')
```

    True



```python
if True:
    print('hello')
```

    hello



```python
if 12309:
    print('hello')
```

    hello



```python
def f():
    return False # True와 False로 바꿔보세요.

if f():
    print('hello')
    print('one')
print('two')
```

    hello



```python
if '': # [], {}, '' 는 모두 False 취급 합니다.
    print('hello')
    print('one')
print('two')
```


```python
if ' ': # 공백이 있는 것입니다.
    print('hello')
    print('one')
print('two')
```

    hello
    one
    two



```python
if [                    ]:
    print('hello')
    print('one')
print('two')
```

    two



```python
if [,]: # SyntaxError
    print('hello')
    print('one')
print('two')
```


```python
if [10,
    20,
    30, # 마지막 콤마는 허락합니다! 소괄호, 중괄호, 대괄호에 공백은 병합니다.
    ]:
    print('hello')
    print('one')
print('two')
```

    hello
    one
    two



```python
if None:
    print('false')
```


```python
class int(int):
    def __eq__(self, next):
        return True
        
if int('11') == int('10'):
    print('hello')
```

    hello



```python
if 10 > 11:
    print('one')
    print('two')
print('three')
else: # error
    print('four')
```


```python
if 10 > 11:
    print('one')
    print('two')
else:
    print('three')
```

    three



```python
# else가 없어도 되는 경우
def f():
    if 10 > 11:
        return 'one'
    return 'two'

print(f())
```


```python
# 여러개의 if문을 단축할 수 있는 방법 => 
# 가독성이 좋아지는 것을 선택하세요! 정답은 없습니다.
# and구문으로 if를 합칠 수 있습니다.
x = 10
if x > 5:
    if type(x) == int:
        print('one')

if x > 5 and type(x) == int:
    print('one')
```


```python
# 여러개의 if문을 단축할 수 있는 방법 => 
# 가독성이 좋아지는 것을 선택하세요! 정답은 없습니다.
# and구문으로 if를 합칠 수 있습니다.
x = 10
if x > 5:
    if type(x) == int:
        if x % 2 == 0:
            print('one')

if x > 5 and type(x) == int and x % 2 == 0:
    print('one')
```


```python
if True:
    print('hello')
else:
    print('hello')
else: # error
    print('hello')
else:
    print('hello')
```


```python
if True:
    print('hello')
if True:
    print('hello')
if True:
    print('hello')
else:
    print('hello')
```

    hello
    hello
    hello



```python
if True:
    print('hello')
elif True:
    print('hello')
elif True:
    print('hello')
else:
    print('hello')
```

    hello



```python
elif True: # error 위에 구문이 있어야 합니다.
    print('hello')
elif True:
    print('hello')
else:
    print('hello')
```


```python
score = 81
money = 0

if score >= 90: # 만약에 조건이 참이라면
    print('mom : i\'m so happy!')
    money += 1000000
elif score >= 80: # 그렇지 않고 만약에 조건이 참이라면
    print('mom : i\'m happy!')
    money += 100000
elif score >= 70: # '그렇지 않고 만약에'에서 '그렇지 않고'가 만족이 안되기 때문에 실행하지 못합니다.
    print('mom : i\'m so...!')
    money += 10000
elif score >= 60:
    print('mom : i\'m so...!')
    money += 1000
else:
    print('mom : i\'m...!')
print(money)
# if, elif, else 구문은 함께 썼다면 한 덩어리가 되어
# 하나만 실행이 되고 나머지는 실행이 되지 않습니다.
```


```python
# Ctrl + M, m 누르시면 코드블록이 마크다운 블록이 됩니다.
# Ctrl + M, y 누르시면 마크다운이 코드 블록이 됩니다.
```

## if 심화


```python
# 저는 개인적으로 해당 문법이 가독성을 떨어트린다라고 생각해
# 권장하진 않습니다.
if 10 > 5: print('hello') # 1줄에 사용하는 것이 가능합니다.
```

    hello



```python
if 1 > 5: print('hello')
elif 5 > 1: print('world') 
```

    world



```python
if 1 > 5: print('hello')
elif 1 > 5: print('world')
else: print('hello world')
```

    hello world



```python
# 3항 연산자는 가독성을 해치지 않는 선에서 많이 사용합니다.
print('one') if 5 > 1 else print('two')
```

    one



```python
(print('one') if 5 > 1 else print('two'))
```

    one



```python
# error 이렇게 사용하지 않습니다!
if 5 > 1 print('one') else print('two')
```


```python
if 5 > 1:
    print('one') 
else:
    print('two')
```


```python
# 할당이나 return에서 많이 사용합니다.
# 할당이나 return을 할 때 어떤 조건을 달고 싶을 때
# 그런데 일반 if문과 else문 거창하다고 생각이 되었을 때
y = 100
x = 'one' if y > 80 else None
```


```python
x
```




    'one'




```python
def f(y):
    if y > 80:
        x = 'one'
    else:
        x = None
    return x

print(f(100))
print(f(30))
```

    one
    None



```python
def f(y):
    if y > 80:
        return 'one'
    return None

print(f(100))
print(f(30))
```

    one
    None



```python
def f(y):
    return 'one' if y > 80 else None

print(f(100))
print(f(30))
```

    one
    None



```python
def custom_sum(x):
    return sum(x)

custom_sum([1, 2, 3, 4, 5, 6]) # 21
custom_sum([1, 2, 3, 4, '5', 6]) # float('inf')
```


```python
# 이해를 위해 만든 예제이지 효율적이진 않습니다.
def custom_sum(li):
    return sum(li) if len(list(filter(lambda x:type(x)==int, li))) == len(li) else float('inf')

custom_sum([1, 2, 3, 4, 5, 6]) # 21
custom_sum([1, 2, 3, 4, '5', 6]) # float('inf')
```




    21




```python
l = [1, 2, 3, '4', '5']
list(filter(lambda x : type(x) == int, l))
len(list(filter(lambda x : type(x) == int, l)))
len(l)
```




    5




```python
# 문제 : 다음 if문을 3항 연산자로 표현해주세요. (이것만 캐치하시면 OK 입니다!)
if x % 2 == 0:
    홀짝여부 = '짝수'
else:
    홀짝여부 = '홀수'

# 답
x = 10
홀짝여부 = '짝수' if x % 2 == 0 else '홀수'
```


```python
# 지금하는 것은 위 보다 빈도도 거의 없습니다.
# 3항 연산자의 중첩
# '조건1이 True일 때' if '조건1' else '조건1일 False이고 조건2가 True일 때' if '조건2' else '조건1, 조건2가 False일 때'
```


```python
# '조건1이 True일 때' 
# if '조건1' 
# else '조건1일 False이고 조건2가 True일 때' 
#     if '조건2' 
#     else '조건1, 조건2가 False일 때'
```


```python
x = 15
if x % 2 == 0:
    배수 = '2X' # 2의 배수
elif x % 3 == 0:
    배수 = '3X' # 3의 배수
else:
    배수 = '?' # 2의 배수도 아니고 3의 배수도 아니다!
배수
```




    '3X'




```python
x = 15
배수 = '2X' if x % 2 == 0 else '3X' if x % 3 == 0 else '?'
배수
```




    '3X'



## 반복문


```python
# for 변수 in 순회가능한객체:
#     code
```


```python
# 순회가능한객체 != 시퀀스형자료형 # 순서가 없어도 순회가 가능하기 때문에
```


```python
for i in 'hello world':
    print(i)
```


```python
for i in 10: # error
    print(i)
```


```python
for i in 10.1: # error
    print(i)
```


```python
for i in [1, 2, 3]:
    print(i)
```


```python
for i in (1, 2, 3):
    print(i)
```


```python
for i in {1, 2, 3}:
    print(i)
```


```python
for i in {'one':1, 'two':2, 'three':3}:
    print(i)
```


```python
# 변수에는 range, enumerate, zip, map, sorted, reversed...
for i in range(10):
    print(i)
```


```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i in 언어순위:
    print(i)
```

    Python
    JavaScript
    JAVA
    Ruby



```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i in enumerate(언어순위):
    print(i)
```

    (0, 'Python')
    (1, 'JavaScript')
    (2, 'JAVA')
    (3, 'Ruby')



```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i in enumerate(언어순위, 1):
    print(i)
```

    (1, 'Python')
    (2, 'JavaScript')
    (3, 'JAVA')
    (4, 'Ruby')



```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i in enumerate(언어순위, 101):
    print(i)
```

    (101, 'Python')
    (102, 'JavaScript')
    (103, 'JAVA')
    (104, 'Ruby')



```python
언어순위 = ['Python', 'JavaScript', 'JAVA', 'Ruby']
for i, j in enumerate(언어순위, 101):
    print(i, j)
```

    101 Python
    102 JavaScript
    103 JAVA
    104 Ruby


## !! 오늘 배운 것 정리
* 조건문
    * 조건에 따라 코드를 분기할 수 있는 구문
    * if, elif, else
    * elif와 else는 단독으로 사용이 되지 않습니다.
    * 예시(score에 값을 변경해보면서 money 값을 확인해주세요.)
    ```python
    score = 81
    money = 0

    if score >= 90: # 만약에 조건이 참이라면
        print('mom : i\'m so happy!')
        money += 1000000
    elif score >= 80: # 그렇지 않고 만약에 조건이 참이라면
        print('mom : i\'m happy!')
        money += 100000
    elif score >= 70: # '그렇지 않고 만약에'에서 '그렇지 않고'가 만족이 안되기 때문에 실행하지 못합니다.
        print('mom : i\'m so...!')
        money += 10000
    elif score >= 60:
        print('mom : i\'m so...!')
        money += 1000
    else:
        print('mom : i\'m...!')
    print(money)
    ```
    * 3항 연산자
    ```python
    def f(y):
    return 'one' if y > 80 else None
    ```
* 정해진 순서를(next) 반복하는 것
    * 형태
    ```python
    # for 변수 in 순회가능한객체:
    #     code
    ```
    * 순회 가능한 객체(이터러블 객체) : 문자열, 리스트, 튜플, 딕셔너리, 셋, range, enumerate, map, set, sorted, reverse 등
    * 순회 불가능한 객체 : int, float 등 
    * code 안에서 변수를 사용하지 않을 경우 언더바를 관습적으로 사용합니다.
    ```python
    # for _ in 순회가능한객체:
    #     code
    ```


```python
for _ in range(3):
    print('hello world')
```

    hello world
    hello world
    hello world



```python
for _, i in [[1, 2], [3, 4], [5, 6]]:
    print('hello world')
    print(i)
```

    hello world
    2
    hello world
    4
    hello world
    6



```python
s = 0
for i in range(0, 101, 2):
    s += i
s
```




    2550




```python
listx= [100,200,300,400]
strx= 'abcd'
dictx = {'one':1, 'two':2}

listxlter = iter(listx)
strxlter= iter(strx)
dictxlter= iter(dictx)

# 시퀀스형 자료형에만 next가 되는 것이 아니고 
# next 다음 순회 값을 지정할 뿐입니다.
print(next(listxlter), next(listxlter), next(listxlter), next(listxlter))
print(next(strxlter), next(strxlter), next(strxlter), next(strxlter))
print(next(dictxlter), next(dictxlter))
```

    100 200 300 400
    a b c d
    one two



```python
# for True: # 이렇게 사용하지는 못합니다.
#    print('hello')
```

## break과 continue


```python
for i in range(10):
    print(i)
    if i == 5:
        break
```

    0
    1
    2
    3
    4
    5



```python
# 모든 for가 중단이 되는 것은 아닙니다!
# 자신을 감싸고 있는 단일 반복문만 탈출합니다.
for i in range(10):
    print('----------------')
    print(i)
    for j in range(10):
        print(i, j)
        if i == 5:
            break
```

    ----------------
    0
    0 0
    0 1
    0 2
    0 3
    0 4
    0 5
    0 6
    0 7
    0 8
    0 9
    ----------------
    1
    1 0
    1 1
    1 2
    1 3
    1 4
    1 5
    1 6
    1 7
    1 8
    1 9
    ----------------
    2
    2 0
    2 1
    2 2
    2 3
    2 4
    2 5
    2 6
    2 7
    2 8
    2 9
    ----------------
    3
    3 0
    3 1
    3 2
    3 3
    3 4
    3 5
    3 6
    3 7
    3 8
    3 9
    ----------------
    4
    4 0
    4 1
    4 2
    4 3
    4 4
    4 5
    4 6
    4 7
    4 8
    4 9
    ----------------
    5
    5 0
    ----------------
    6
    6 0
    6 1
    6 2
    6 3
    6 4
    6 5
    6 6
    6 7
    6 8
    6 9
    ----------------
    7
    7 0
    7 1
    7 2
    7 3
    7 4
    7 5
    7 6
    7 7
    7 8
    7 9
    ----------------
    8
    8 0
    8 1
    8 2
    8 3
    8 4
    8 5
    8 6
    8 7
    8 8
    8 9
    ----------------
    9
    9 0
    9 1
    9 2
    9 3
    9 4
    9 5
    9 6
    9 7
    9 8
    9 9



```python
# continue는 다음 루프로 갑니다.
# 아래 코드에서 continue는 의미가 없습니다.
for i in range(10):
    print(i)
    if i == 5:
        continue
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
# continue는 다음 루프로 갑니다.
# 아래 코드에서 continue는 아래 print를 실행시키지 않고
# 다음 루프로 가게됩니다.
for i in range(10):
    if i == 5:
        continue
    print(i)
```

    0
    1
    2
    3
    4
    6
    7
    8
    9



```python
for i in range(10):
    if i == 5:
        pass # 공백을 채워주는 역활만 합니다.
    print(i)
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
for i in range(10):
    print(i)
    i += 2 # 작동이 되지 않습니다.
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
for i in range(0, 10, 2):
    print(i)
```

    0
    2
    4
    6
    8



```python
# 실행과 동시에 정지를 눌러주세요.
# 무한반복입니다.
# 아래 코드는 효율적이지 못하니
# 뒤에서 배울 generator로 무한반복을 구현해주세요.
l = [1]
for i in l:
    l.append(i+1)
    print(i)
```

## for와 else 구문


```python
# 다른 언어에서는 이 구문이 작동되지 않습니다.
for i in range(10):
    if i == 5:
        break
else:
    print('정상종료!')
```


```python
# 반복문 + else구문은
# 반복문이 break을 쓰지 않고 정상 종료되었을 때
# else 구문이 실행됩니다.

for i in range(10):
    if i == 5:
        pass
else:
    print('정상종료!')
```

    정상종료!


## 리스트 표현식(list comprehension)


```python
# 별 3.5개
# 리스트 안에 반복문이나 조건문을 넣어 한 번에 리스트를 생성하는 기법
# 리스트 표현식은 for보다 빠릅니다! (가독성 + 속도우위)
l = []
for i in range(10):
    l.append(i)
l
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
[i for i in range(10)]
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
# 이정도만 하실 수 있으면 우리 수업에서는 문제 없습니다.
l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i)
l
```




    [0, 2, 4, 6, 8]




```python
[i for i in range(10) if i % 2 == 0]
```




    [0, 2, 4, 6, 8]




```python
list(range(0, 10, 2)) # 이것도 가능하고, 직관적이죠.
```




    [0, 2, 4, 6, 8]




```python
l = ['aa', 'abc', 'bbb', 'ccc', 'aba']
[i for i in l if 'a' in i]
```




    ['aa', 'abc', 'aba']




```python
# 아래 코드는 어떻게 할까요?
l = []
for i in range(10):
    if i % 2 == 0:
        l.append(i)
    elif i % 3 == 0:
        l.append(i)
l
```




    [0, 2, 3, 4, 6, 8, 9]




```python
l = []
for i in range(10):
    if i % 2 == 0 or i % 3 == 0:
        l.append(i)
l
```




    [0, 2, 3, 4, 6, 8, 9]




```python
[i for i in range(10) if i % 2 == 0 or i % 3 == 0]
```




    [0, 2, 3, 4, 6, 8, 9]




```python
# [i for i in range(10) if i % 2 == 0 elif i % 3 == 0] # error
```


```python
# 구구단
# 손으로 꼭 순회 1번씩 돌아보셔야 합니다.
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, j, i*j)

'''
# step 0
# 이렇게 손이나 문자열로 늘여트려놓고
# 내가 무엇을 줄일 수 있을까?를 고민하세요.
2 1 2
2 2 4
2 3 6
2 4 8
2 5 10
2 6 12
2 7 14
2 8 16
2 9 18
3 1 3
3 2 6
3 3 9
3 4 12
3 5 15
3 6 18
3 7 21
3 8 24
3 9 27
'''

# step 1 ~ 100 이렇게 하나씩 줄여가면 됩니다.
# for i in range(1, 10):
#     print(2, i, 99)

# step 1 ~ 100 이렇게 하나씩 줄여가면 됩니다.
# for i in range(1, 10):
#     print(2, i, 2*i)

for 단 in range(2, 10):
    for i in range(1, 10):
        print(단, i, 단*i)
```


```python
# 별찍기
# 트리 만드는 문제도 있고, 원 만드는 문제도 있고...
'''
*
**
***
****
*****
'''
```


```python
user_input = int(input('찍을 별의 층수?'))
for i in range(1, user_input+1):
    print('*' * i)
```

    찍을 별의 층수?5
    *
    **
    ***
    ****
    *****



```python
l = []
for i in range(2, 10):
    for j in range(1, 10):
        l.append([i, j, i*j])
l
```


```python
[[i, j, i*j] for i in range(2, 10) for j in range(1, 10)]
```

## 다중 리스트 순회


```python
skill = [
        ('고기잡이', 100),
        ('고기팔기', 120),
        ('낚시', 5),
        ('통발', 5),
        ('큰그물', 5)
]

for i, j in skill:
    print(i,j)
```


```python
skill_name = ['고기잡이', '고기팔기', '낚시']
skill_point = [100, 120, 5]

for i, j in zip(skill_name, skill_point):
    print(i,j)
```


```python
# 이정도 코드만 아셔도 실무하는 것에는 무리가 없습니다.
skill = [
        ('고기잡이', [1, 100]),
        ('고기팔기', [1, 100]),
        ('낚시', [2, 100]),
        ('통발', [2, 100]),
        ('큰그물', [2, 100])
]

for i, j in skill:
    print(i, j)
```


```python
skill = [
        ('고기잡이', [1, 100]),
        ('고기팔기', [1, 100]),
        ('낚시', [2, 100]),
        ('통발', [2, 100]),
        ('큰그물', [2, 100])
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 1 100
    고기팔기 1 100
    낚시 2 100
    통발 2 100
    큰그물 2 100



```python
skill = [
        ('고기잡이', (1, 100)),
        ('고기팔기', (1, 100)),
        ('낚시', (2, 100)),
        ('통발', (2, 100)),
        ('큰그물', (2, 100))
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 1 100
    고기팔기 1 100
    낚시 2 100
    통발 2 100
    큰그물 2 100



```python
skill = [
        ('고기잡이', 'ab'), # ('고기잡이', 'abcd') 이런 형태는 error
        ('고기팔기', 'cd'),
        ('낚시', 'aa'),
        ('통발', 'cc'),
        ('큰그물', 'dd')
]

for i, [x, y] in skill:
    print(i, x, y)
```

    고기잡이 a b
    고기팔기 c d
    낚시 a a
    통발 c c
    큰그물 d d



```python
# 문제
# data는 다음과 같은 데이터가 있습니다.
# 각각 skill 이름, skill 제한 레벨, skill 포인트, skill 등급입니다.
# 아래와 같이 출력해주세요.
data = [
        ('고기잡이', (1, 100, 'S')),
        ('고기팔기', (1, 100, 'A')),
        ('낚시', (2, 100, 'A')),
        ('통발', (2, 100, 'B')),
        ('큰그물', (2, 100, 'S'))
]

# 출력값
# 아래와 같은 형식으로 총 5개 출력해야 합니다.
# '축하합니다. S등급에 skill 고기잡이를 습득하셨습니다! 
#  해당 스킬은 레벨 제한 1에 스필 포인트 100입니다.'
```


```python
for name,(level_limit, point, rank) in data:
    print(f'축하합니다. {rank}등급의 skill {name}을(를) 습득하셨습니다!')
    print(f'해당 스킬은 레벨 제한 {level_limit}에 스킬 포인트 {point}입니다.')
```

    축하합니다. S등급의 skill 고기잡이을(를) 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100입니다.
    축하합니다. A등급의 skill 고기팔기을(를) 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100입니다.
    축하합니다. A등급의 skill 낚시을(를) 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100입니다.
    축하합니다. B등급의 skill 통발을(를) 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100입니다.
    축하합니다. S등급의 skill 큰그물을(를) 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100입니다.



```python
for idx, (name, (level, point, rank)) in enumerate(data):
    print(f'축하합니다. {rank}등급의 skill {name}를 습득하셨습니다!\n해당 스킬은 레벨 제한 {level}에 스킬 포인트 {point} 입니다.')
```

    축하합니다. S등급의 skill 고기잡이를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.
    축하합니다. A등급의 skill 고기팔기를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.
    축하합니다. A등급의 skill 낚시를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. B등급의 skill 통발를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. S등급의 skill 큰그물를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.



```python
# 이 풀이가 좋습니다.
for name, (level, point, rank) in data:
    print(f'축하합니다. {rank}등급의 skill {name}를 습득하셨습니다!\n해당 스킬은 레벨 제한 {level}에 스킬 포인트 {point} 입니다.')
```

    축하합니다. S등급의 skill 고기잡이를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.
    축하합니다. A등급의 skill 고기팔기를 습득하셨습니다!
    해당 스킬은 레벨 제한 1에 스킬 포인트 100 입니다.
    축하합니다. A등급의 skill 낚시를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. B등급의 skill 통발를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.
    축하합니다. S등급의 skill 큰그물를 습득하셨습니다!
    해당 스킬은 레벨 제한 2에 스킬 포인트 100 입니다.


## while


```python
# 반복문 : for, while
a = 1
while a < 10: # True인 동안에
    print(a)
    a += 1
```

    1
    2
    3
    4
    5
    6
    7
    8
    9



```python
# while 특정요소:
#     특정요소 값 꺼내는 문법
#     특정요소가 모두 없어질 때까지

l = [1, 2, 3]
while l: # []
    print(l.pop())
```

    3
    2
    1



```python
l = {1, 2, 3}
while l: 
    print(l.pop())
```

    1
    2
    3



```python
# 중복되는 문자열 중 가장 첫번째 나온
# 문자의 index를 반환하라!
s = 'abkkkbnbbbccdennnnneefefg'
ss = set(s)
while ss:
    string = ss.pop()
    print(string, s.index(string))
```

    c 10
    d 12
    f 21
    b 1
    a 0
    k 2
    e 13
    n 6
    g 24



```python
# 이러한 무한반복은 메모리를 모두 소진합니다.
# 서버가 뻗을 수도 있습니다.
while True:
    user_input = input('$')
    split_data = user_input.split(' ')
    if split_data[0] == 'mkdir':
        print(f'{split_data[1]} 폴더가 생성되었습니다!')
    elif split_data[0] == 'rmdir':
        print(f'{split_data[1]} 폴더가 삭제되었습니다!')
    elif split_data[0] == 'exit':
        print('프로그램을 종료합니다.')
        break
```

    $exit
    프로그램을 종료합니다.



```python
import random

random.randint(1, 100)
```




    14




```python
import random
# up down game

result = random.randint(1, 100)

while True:
    user_input = int(input())
    if user_input > result:
        print('down')
    elif user_input < result:
        print('up')
    else:
        print('맞췄습니다!')
        print('프로그램을 종료합니다.')
        break
```

    50
    down
    25
    down
    12
    down
    9
    맞췄습니다!
    프로그램을 종료합니다.



```python
# 구구단이 출력되지 않는 코드
# 한땀한땀 따라가면서 왜 출력이 되지 않는지 체크해보세요.
x = 2
y = 1
while x < 10:
    while y < 10:
        print(x, y, x * y)
        y += 1
    x += 1
```

    2 1 2
    2 2 4
    2 3 6
    2 4 8
    2 5 10
    2 6 12
    2 7 14
    2 8 16
    2 9 18



```python
# 구구단이 출력되지 않는 코드
# 한땀한땀 따라가면서 왜 출력이 되지 않는지 체크해보세요.
x = 2
y = 1
while x < 10:
    while y < 10:
        print(x, y, x * y)
        y += 1
    y = 1 # 초기화를 해주어야 다음 while에서 y < 10에 들어갈 수 있습니다.
    x += 1
```


```python
count = 0
while True:
    print(count)
    if count == 5:
        break
    count += 1
print('end')
```

    0
    1
    2
    3
    4
    5
    end



```python
# 무한루프
count = 0.0
while True:
    print(count)
    if count == 0.3: #부동소수점 문제가 발생할 수 있습니다.
        break
    count += 0.1
print('end')
```


```python
# 0.30000000000000004
count = 0.0
while True:
    print(count)
    if count >= 0.3:
        break
    count += 0.1
print('end')
```

    0.0
    0.1
    0.2
    0.30000000000000004
    end



```python
# 다른 언어에서는 이 구문이 작동되지 않습니다.
i = 0
while i < 10:
    if i == 5:
        break
    i += 1
else:
    print('정상종료!')
```


```python
i = 0
while i < 10:
    i += 1
else:
    print('정상종료!')
```

    정상종료!


* https://school.programmers.co.kr/learn/courses/30/lessons/120871


```python
# step1
count10 = 0
n = 15
while count10 < n + 1:
    print(count10)
    count10 += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15



```python
# step2 조건만 간단히 구현
count10 = 0
count3 = 0 # 3x 마을에서 쓰는 숫자
n = 5
while count10 < n + 1:
    count10 += 1
    count3 += 1
    if count3 % 3 == 0 or '3' in str(count3):
        count3 += 1
    # 저주의 숫자를 지나가도 다시 저주의 숫자일수 있습니다
    # 체크를 계속해야하는데 한 번만 합니다
    print(count10, count3)

count3
```

    1 1
    2 2
    3 4
    4 5
    5 7
    6 8





    8




```python
# step3 조건만 간단히 구현 => 조건이 계속 반복되도록
count10 = 0
count3 = 0 # 3x 마을에서 쓰는 숫자
n = 10
while count10 < n:
    count10 += 1
    count3 += 1
    while count3 % 3 == 0 or '3' in str(count3):
        count3 += 1
    # 저주의 숫자를 지나가도 다시 저주의 숫자일수 있습니다
    # 체크를 계속해야하는데 한 번만 합니다
    print(count10, count3)
```

    1 1
    2 2
    3 4
    4 5
    5 7
    6 8
    7 10
    8 11
    9 14
    10 16



```python
# step3 조건만 간단히 구현 => 조건이 계속 반복되도록
count10 = 0
count3 = 0 # 3x 마을에서 쓰는 숫자
n = 10
while count10 < n:
    count10 += 1
    count3 += 1
    while count3 % 3 == 0 or '3' in str(count3):
        count3 += 1
    print(count10, count3)
```


```python
def solution(n):
    count10 = 0
    count3 = 0
    while count10 < n:
        count10 += 1
        count3 += 1
        while count3 % 3 == 0 or '3' in str(count3):
            count3 += 1
    return count3
```


```python
[i for i in range(1, 31) if i % 3 != 0 and not('3' in str(i))][n-1]
```




    [1, 2, 4, 5, 7, 8, 10, 11, 14, 16, 17, 19, 20, 22, 25, 26, 28, 29]




```python
def solution(n):
    return [i for i in range(1, 1001) if i % 3 != 0 and not('3' in str(i))][n-1]
```

## 예외처리(try, except, else)


```python
# try:
# 	실행문
# except:
# 	예외 발생 시 처리문
# else:
# 	예외 발생하지 않을 경우 실행문
```


```python
try:
    i = 1
    j = 0
    x = i/j
except:
    print("error")
else:
    print(x)
```

    1.0


## 실제 데이터를 가지고 연습 (json gen)


```python
data = [
  {
    "_id": "6459c9f4ebc9d86c2a656d5e",
    "index": 0,
    "age": 27,
    "name": "Burgess Hammond",
    "gender": "male"
  },
  {
    "_id": "6459c9f4d99872fea5ad0459",
    "index": 1,
    "age": 38,
    "name": "Leon Luna",
    "gender": "male"
  },
  {
    "_id": "6459c9f4234b6e3701033326",
    "index": 2,
    "age": 35,
    "name": "Huber Nieves",
    "gender": "male"
  }
]

# 반복문을 사용해도 좋지만,
# 반복문을 사용하실 수 없다면 index로만 계산하셔도 좋습니다.
data[0]
data[0]['age']
data[0]['gender']
```




    100




```python
#Lv0
(data[0]['age'] + data[1]['age'] + data[2]['age']) / 3

성별 = []
성별.append(data[0]['gender'])
성별.append(data[1]['gender'])
성별.append(data[2]['gender'])
print(성별)
print(성별.count('male') / len(data) * 100)
print(성별.count('female') / len(data) * 100)
```




    0.0




```python
#Lv1
age_sum = 0
for i in range(3): # 좋은 코드는 아닙니다.
    age_sum += data[i]['age']
age_sum / 3

성별 = []
for i in range(3):
    성별.append(data[i]['gender'])
print(성별.count('male') / len(data) * 100)
print(성별.count('female') / len(data) * 100)
```

    100.0
    0.0



```python
#Lv1
age_sum = 0
for i in range(len(data)):
    age_sum += data[i]['age']
age_sum / 3

성별 = []
for i in range(len(data)):
    성별.append(data[i]['gender'])
print(성별.count('male') / len(data) * 100)
print(성별.count('female') / len(data) * 100)
```


```python
#Lv2

# 평균 (1줄)
# list(map(lambda x:x['age'], data))
sum(map(lambda x:x['age'], data)) / len(data)

# 성별 (1줄)
len(list(filter(lambda x:x['gender'] == 'male', data))) / len(data) * 100
len(list(filter(lambda x:x['gender'] == 'female', data))) / len(data) * 100
```




    0.0




```python
# Q1
# sol1
sum([elem['age'] for elem in data]) / len(data)

# sol2
sum(map(lambda x:x['age'], data)) / len(data)

# Q2
gender = [elem['gender'] for elem in data]
male = gender.count('male')
female = gender.count('female')
print(f'{male/len(gender)*100:.2f} : {female/len(gender)*100:.2f}')
```




    100




```python
# Q1
# sol1
sum([elem['age'] for elem in data]) / len(data)

# sol2
sum(map(lambda x:x['age'], data)) / len(data)

# Q2
gender = [elem['gender'] for elem in data]
male = gender.count('male')
female = gender.count('female')
malepercentage = male/len(gender)*100
femalepercentage = female/len(gender)*100
print(f'{malepercentage:.2f} : {femalepercentage:.2f}')
```


```python
# solve1
average_age = sum(map(lambda x: x['age'], data))/len(data)
male = len(list(filter(lambda x: x['gender'] == 'male', data)))
female = len(list(filter(lambda x: x['gender'] == 'female', data)))

print(f'평균나이는 {average_age} 입니다.\n성비는 남성 {male} : 여성 {female} 입니다.')

# solve2
average_age = sum(map(lambda x: x['age'], data))/len(data)
gender = list(map(lambda x : x['gender'], data))
gender_count = [gender.count('male'), gender.count('female')]
print(f'평균나이는 {average_age} 입니다.\n성비는 남성 {gender_count[0]} : 여성 {gender_count[1]} 입니다.')
```

## 알아야 하는 built-in function

### 수학적 통계에 활용되는 함수

- abs( ) : 괄호 안에 있는 값을 절대값으로 출력해줍니다.
- all( ) : 괄호 안에 있는 값들이 모두 True(False)일 때 True(False)를 출력합니다.
- any( ) : 괄호안에 있는 값이 하나라고 True이면 True로 출력합니다.
- pow( ) : 제곱을 출력합니다.
- max( ) : 값의 최댓값을 출력합니다.
- min( ) : 값의 최솟값을 출력합니다.
- sum( ) : 값의 합계를 출력합니다.
- len( ) : 문자열의 길이를 출력합니다.
- sorted( ) : 데이터를 정렬해줍니다.
- reversed( ) : 정렬되지 않은 상태에서 값을 역순으로 출력합니다.


```python
abs(-1)
all([True, True, True])
all([True, True, False])
all(['a', 'b', 'ccc'])
all(['a', '', 'ccc'])
if all([3 > 5, 12 % 2 == 0, 15 % 5 == 0]):
    print('hello')

if all([3 > 5, 
        12 % 2 == 0, 
        15 % 5 == 0]):
    print('hello')


if 3 > 5 and 12 % 2 == 0 and 15 % 5 == 0:
    print('hello')

# if all([one(), two(), three()]):
#     print('hello')

# all(True, True, True) # all() takes exactly one argument (3 given)

pow(2, 3) # 2 ** 3
```




    8




```python
sum([[1, 2], [3, 4], [5, 6]], [])
sum([1, 2, 3, 4, 5], 100)
# sum([1, 2, 3, 4, 5], {1, 2, 3}) # error
```


```python
# __len__가 없는 것들 : map, zip, filter...
class str(str):
    def __len__(self):
        return 1000

len(str('hello world'))
```




    1000




```python
# len(zip([1, 2, 3], 'abc')) # error
```

### 형변환 함수

- set( )
- dict( )
- hex( ) : 16진법
- bin( ) : 2진법
- oct( ) : 8진법
- bool( )
- str( )
- ord( ) : 각각의 문자에 대한 숫자값을 출력해줍니다.(유니코드표를 참고하세요.)
- float( )
- tuple( )
- chr( ) : 숫자값을 통해서 문자를 출력합니다.
- list( )
- range( )
- complex( )


```python
l = [1, 2, 3]
type(l)
```




    list




```python
# 아래 3개는 int형
# bin( ) : 2진법
# oct( ) : 8진법
# hex( ) : 16진법
bin(7)
type(bin(7))
0b111
type(0b111)
int('111', 2)
int('0b111', 2)
# int(0b111, 2) #error
```


```python
chr(65)
ord('A')
```




    65




```python
# list(range(start, stop, step))
list(range(0, 10, 2))
list(range(0, 10))
list(range(10))
list(range(-10, 10, 2))
list(range(0, -10, -2))
```




    [0, -2, -4, -6, -8]



### 도움말


```python
def hojun():
    '''
    이호준이 작성한 함수
    '''
    pass

help(hojun)
```

    Help on function hojun in module __main__:
    
    hojun()
        이호준이 작성한 함수
    


### object 관련 함수

- dir( )
- id( )
- type( )


```python
# dir() # directory에 약자로 대상이 가진 attribute를 모두 출력합니다.
# attribute가 무엇인가? class에서 배울 멤버 + 메서드 입니다.
```


```python
def f():
    return 100

f.name = 'leehojun'
dir(f)
print(f.name)
```

    leehojun



```python
# 배우는 재미
# 단시간에 될 수 없습니다. => 경쟁력
```


```python
l = 10
# 복사가 제대로 이뤄졌나?
id(l) # 깊은복사, 얕은복사
```




    140662941172240




```python
type('abc') # str
print(type('abc')) # <class 'str'>
# print(type(f)) # class가 전체 Python을 관통하고 있습니다.
```

    <class 'str'>
    <class 'function'>


### 유용한 순회 가능 객체

- enumerate( ) : 값에 순위를 매기고 싶을 때 사용합니다.
- range( )
- sorted( )
- reversed( )
- filter( )
- zip( )
- map( )


```python
print(type(range(3)))
```

    <class 'range'>



```python
list(enumerate([10, 20, 30]))
```




    [(0, 10), (1, 20), (2, 30)]




```python
list(enumerate([10, 20, 30], 100))
# list(enumerate([10, 20, 30], 'abc')) # error 뒤에 숫자를 입력해야 합니다.
```


```python
def 함수(x):
    return x > 15

list(filter(함수, [10, 20, 30, 40]))
list(filter(None, [True, True, False, False]))
# filter에 None 주는 것이 어디에 유용할까요?
# 여러가지 자료형이 섞여 있을 때 값이 들어있는 것만 찾을 경우
list(filter(None, [[], 'abc', '', ''])) 
```




    ['abc']




```python
list(zip('abc', 'defaaaa', 'ght', [1, 2, 3], [4, 5, 6, 7]))
```




    [('a', 'd', 'g', 1, 4), ('b', 'e', 'h', 2, 5), ('c', 'f', 't', 3, 6)]




```python
x = [5, 4, 6, 8, 2]
list(zip('abcdefg', sorted(x)))
```




    [('a', 2), ('b', 4), ('c', 5), ('d', 6), ('e', 8)]




```python
x = [5, 4, 6, 8, 2]
y = [7, 6, 45, 4, 2, 3, 3]
list(zip('abcdefg', zip(x, y)))
```




    [('a', (5, 7)), ('b', (4, 6)), ('c', (6, 45)), ('d', (8, 4)), ('e', (2, 2))]



## args, kargs

* 가변 아규먼트, 가변 키워드 아규먼트


```python
def print_args(a, *args): # 꼭 args가 될 필요는 없습니다.
    print(args)

print_args(100, True, 'leehojun')
```

    (100, True, 'leehojun')



```python
def print_kwargs(a, **kwargs): # 꼭 kargs가 될 필요는 없습니다.
    print(a)
    print(kwargs)

print_kwargs(100, name='leehojun', age='10')
```

    100
    {'name': 'leehojun', 'age': '10'}



```python
def print_args(*args, b): # error입니다.
    print(args)

print_args(100, True, 'leehojun')
```


```python
def print_args(b, *args): # error입니다.
    print(args)

print_args(100, True, 'leehojun')
```

    (True, 'leehojun')



```python
def print_args(b, *args): # error입니다. args 앞에 순서대로 넣을 변수가 있어야 합니다.
    print(args)

print_args(100, True, b='leehojun')
```


```python
one, two, *three = 1, 2, 3, 4, 5 # *가 하는 역활은? 남은 데이터의 패킹
print(one, two, three)
```

    1 2 [3, 4, 5]


## lambda

* lambda 는 익명함수라고 하며, 이름이 없는 함수


```python
leehojun = lambda x : x**2

# def leehojun(x):
#     return x ** 2
```


```python
print(type(leehojun))
```

    <class 'function'>



```python
print(type(lambda x : x**2))
```

    <class 'function'>



```python
print(dir(lambda x : x**2))
```

    ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



```python
def 함수(x):
    return x ** 2

print(dir(함수))
```

    ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']



```python
def add(x, y):
    return x + y
def sub():
    pass
def div():
    pass
def mul():
    pass

caculator = [add, sub, div, mul]
print(caculator[0](10, 20))#0번째 값은 add 입니다.

caculator2 = [lambda x,y:x+y, 
              lambda x,y:x-y, 
              lambda x,y:x/y, 
              lambda x,y:x*y]

print(caculator2[0](10, 20)) #0번째 값은 add 입니다.
print(caculator2[0](10, 20))
```

    30
    30
    30



```python
def f():
    return lambda x,y:x+y

f()(10, 20)
```




    30




```python
def f():
    return lambda x:lambda i:i**2

f()(1)(10)
```




    100




```python
def f():
    return lambda x:lambda i:x*i**2

f()(2)(10)
```




    200



### lambda 실무 응용

* lambda가 응용되는 곳 : map, filter, max, min, sorted


```python
# 실무에서도 많이 사용됩니다.
def 제곱(x):
    return x ** 2

# 재사용 하는 경우에는 함수로 선언하는 경우도 있습니다.
list(map(제곱, [1, 2, 3, 4]))
list(map(제곱, [1, 2, 3, 4]))

list(map(lambda x : x ** 2, [1, 2, 3, 4]))
```


```python
# 질문 : 람다함수를 재귀로 사용할 수 있나요?
# 답 : Yes
fact = lambda x: 1 if x == 0 else x * fact(x-1)
fact(5)
```




    120




```python
# 질문 : i와 j가 뜻하는 바
# 답 : 
skill = [
        ('고기잡이', 100, 'SS'),
        ('고기팔기', 120, 'SSS'),
        ('낚시', 5, 'C'),
        ('통발', 5, 'C'),
        ('큰그물', 5, 'C')
]

for i, j in enumerate(skill, 100):
    print(i, j)

for idx, item in enumerate(skill, 100):
    print(idx, item)
```

    100 ('고기잡이', 100, 'SS')
    101 ('고기팔기', 120, 'SSS')
    102 ('낚시', 5, 'C')
    103 ('통발', 5, 'C')
    104 ('큰그물', 5, 'C')



```python
data = [i for i in range(len(숫자))]
data
```




    [0, 1, 2, 3, 4]




```python
[i for i in data]
[i[0] ** i[1] for i in data]
```




    [1, 4, 9, 64, 125]




```python
숫자 = [1, 2, 3, 4, 5]
승수 = [2, 2, 2, 3, 3]

#문제
#1. 숫자의 승수를 zip으로 맵핑해서 진행하세요.
#2. 숫자를 승수만큼 제곱하여 결과값을 표현해주세요.
#3. 승수한 값이 100이상인 값을 출력하세요.
#4. 승수한 값을 모두 더하세요.

# Q1
# Q1.1
data = list(zip(숫자, 승수))

# Q1.2 (list comprehension)
data = [i for i in range(len(숫자))]
###
data = [(숫자[i], 승수[i]) for i in range(len(숫자))]
data


# Q2
# Q2.1
l = []
for i in data:
    l.append(i[0] ** i[1])
print(l)

# Q2.2
def f(x):
    return x[0] ** x[1]

print(list(map(f, data)))

# Q2.3
print(list(map(lambda x:x[0] ** x[1], data)))

# Q2.4
print(list(map(lambda x:pow(x[0], x[1]), data)))

# Q2.5 (list comprehension)
[i for i in data]
[i[0] ** i[1] for i in data] # 공간을 바로 할당해버립니다.

# Q3
# Q3.1
l = []
for i in map(lambda x:x[0] ** x[1], data):
    if i >= 100:
        l.append(i)
print(l)

# Q3.2
def f(x):
    return x > 100
data2 = map(lambda x:x[0] ** x[1], data)
print(list(filter(f, data2)))

# Q3.3
data2 = map(lambda x:x[0] ** x[1], data)
print(list(filter(lambda x:x>=100, data2)))

# Q3.4
# list(filter(lambda x:x>=100, [1, 4, 9, 64, 125]))
print(list(filter(lambda x:x>=100, map(lambda x:x[0] ** x[1], data))))

# Q3.5
print([i[0] ** i[1] for i in data if i[0] ** i[1] >= 100])

# Q4
sum(map(lambda x:x[0] ** x[1], data))
```

    [1, 4, 9, 64, 125]
    [1, 4, 9, 64, 125]
    [1, 4, 9, 64, 125]
    [1, 4, 9, 64, 125]
    [125]
    [125]
    [125]
    [125]
    [125]





    203



## !! 오늘 배운 것 정리
* 반복문
    * 정해진 순서를(next) 반복하는 것
    * 형태
    ```python
    # for 변수 in 순회가능한객체: # stopItoration까지 반복
    #     code

    # while 조건: # true까지 반복
    #     code 
    ```
    * 순회 가능한 객체(이터러블 객체) : 문자열, 리스트, 튜플, 딕셔너리, 셋, range, enumerate, map, set, sorted, reverse 등
    * 순회 불가능한 객체 : int, float 등 
    * code 안에서 변수를 사용하지 않을 경우 언더바를 관습적으로 사용합니다.
    ```python
    # for _ in 순회가능한객체:
    #     code
    ```
    * 반복문 다음 else 구문 : break 없이 정상 종료 되면 실행
    * 반복문 안에 break 구문 : 자신을 감싸고 있는 반복문 1개 탈출
    * 반복문 안에 continue 구문 : 다음 루프로 넘어감
    * 반복문 안에 pass : 공백만 채워줄 뿐 아무 기능 없음

* bulit-in function
    * 수학적 통계에 활용되는 함수
        - abs( ) : 괄호 안에 있는 값을 절대값으로 출력해줍니다.
        - all( ) : 괄호 안에 있는 값들이 모두 True(False)일 때 True(False)를 출력합니다.
        - any( ) : 괄호안에 있는 값이 하나라고 True이면 True로 출력합니다.
        - pow( ) : 제곱을 출력합니다.
        - max( ) : 값의 최댓값을 출력합니다.
        - min( ) : 값의 최솟값을 출력합니다.
        - sum( ) : 값의 합계를 출력합니다.
        - len( ) : 문자열의 길이를 출력합니다.
        - sorted( ) : 데이터를 정렬해줍니다.
        - reversed( ) : 정렬되지 않은 상태에서 값을 역순으로 출력합니다.

    * 형변환 함수
        - set( )
        - dict( )
        - hex( ) : 16진법
        - bin( ) : 2진법
        - oct( ) : 8진법
        - bool( )
        - str( )
        - ord( ) : 각각의 문자에 대한 숫자값을 출력해줍니다.(유니코드표를 참고하세요.)
        - float( )
        - tuple( )
        - chr( ) : 숫자값을 통해서 문자를 출력합니다.
        - list( )
        - range( )
        - complex( )

    * 도움말
        - help( )

    * object 관련 함수
        - dir( )
        - id( )
        - type( )

    * 순회 가능한 객체
        - enumerate( ) : 값에 순위를 매기고 싶을 때 사용합니다.
        - range( )
        - sorted( )
        - reversed( )
        - filter( )
        - zip( )
        - map( )

* args, kargs
    * 가변 아규먼트, 가변 키워드 아규먼트
    ```python
    def print_args(*args): # 꼭 args가 될 필요는 없습니다.
        print(args)

    print_args(100, True, 'leehojun')

    ####

    def print_kwargs(**kwargs): # 꼭 kargs가 될 필요는 없습니다.
    print(kwargs)

    print_kwargs(name='leehojun', age='10')
    ```

* lambda
    * lambda 는 익명함수라고 하며, 이름이 없는 함수
    * 보통은 다시 사용되지 않을 함수를 선언할 때 사용
    ```python
    leehojun = lambda x : x**2

    # def leehojun(x):
    #     return x ** 2

    list(map(lambda x : x ** 2, [1, 2, 3, 4]))
    ```

## 클래스

* 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할
* 우리가 배우고 있는 Python을 객체 지향 프로그래밍 언어
    ```
    현실                                코드
    차 ---------------------------> class Car()
    정수 -------------------------> class int()
    실수 -------------------------> class float()

    인간이 만들어 
    놓은 현실 세계에서의 
    정의 또는 약속 --------------> class
    
    1 + 1 = 2가 컴퓨터 입장에서는 10일 수도 있고
    'A' + 'A' = 'AA'가 아니라 컴퓨터 입장에서는 130일 수 있습니다.
    ```


```python
class CarFactory(object): # 첫 문자는 대문자로 합니다.
    max_speed = 300
    max_people = 5
    # 아래 self는 스스로를 가리키기에
    # self는 인스턴스를 가리킵니다.
    def move(self):
        print('차가 움직이고 있습니다.')
    def stop(self):
        print('차가 멈췄습니다.')

# 클래스로 바로 접근해서 무엇을 하는 것을 권고하지 않습니다.
# (제대로 알지 못하는 상태에서(인스턴스 변수, 클래스 변수))
print(CarFactory.max_speed)
k5 = CarFactory() # 붕어빵(인스턴스) = 붕어빵틀(클래스)
k3 = CarFactory() # 차(인스턴스) = 자동차공장(클래스)
```

    300



```python
class CarFactory(object):
    max_speed = 300
    max_people = 5
    def move(self):
        print('차가 움직이고 있습니다.')
    def stop(self):
        print('차가 멈췄습니다.')

k5 = CarFactory()
k3 = CarFactory()
k5.move()
k3.move()
k5.stop()
k3.stop()
print(k5.max_speed)
```

    300
    차가 움직이고 있습니다.
    차가 움직이고 있습니다.
    차가 멈췄습니다.
    차가 멈췄습니다.
    300



```python
d = {'one':10, 'two':20}
# d.three = 30
d['three'] = 30
print(d['three'])
```

    30



```python
def f():
    pass
f.one = 10
f.two = 20
f.three = 30
print(f.one)
```

    10



```python
# 메서드 : 클래스 내에 함수
# 멤버 : 클래스 내에 변수
class CarFactory(object):
    max_speed = 300
    max_people = 5
    def __init__(self, userInputName): # 인스턴스가 만들어질 때 실행되는 메서드
        self.name = userInputName
    def move(self):
        print(self.name, '차가 움직이고 있습니다.')
    def stop(self):
        print(self.name, '차가 멈췄습니다.')

k5 = CarFactory('케이파이브')
k3 = CarFactory('케이쓰리')
k5.move()
k3.move()
k5.stop()
k3.stop()
print(k5.max_speed)
```

    케이파이브 차가 움직이고 있습니다.
    케이쓰리 차가 움직이고 있습니다.
    케이파이브 차가 멈췄습니다.
    케이쓰리 차가 멈췄습니다.
    300



```python
k3.name
k3.max_speed
```




    300




```python
print(type(k3))
print(dir(k3))
# 'max_people', 멤버
# 'max_speed', 멤버
# 'move', 메소드
# 'name', 멤버
# 'stop' 메소드
```

    <class '__main__.CarFactory'>
    ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'max_people', 'max_speed', 'move', 'name', 'stop']



```python
l = [10, 20, 30]
print(type(l))
print(dir(l))
# 메소드
# 'append', 'clear', 'copy', 'count', 'extend', 
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
```

    <class 'list'>
    ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']



```python
class list(object):
    def __add__(self):
        pass
    def __class__(self):
        pass
    def __class_getitem__(self):
        pass
    def __eq__(self):
        pass
    def __ge__(self):
        pass 
    # ... 생략 ...
    def append(self):
        pass
    def clear(self):
        pass
    def copy(self):
        pass
    def count(self):
        pass
    def extend(self):
        pass
    def index(self):
        pass
    # ... 생략 ...
```


```python
# 클래스 변수
# 클래스 바로 하위에 자리하고 있으며
# 모든 인스턴스가 공유합니다.
class Car(object):
    # kinds가 인스턴스에 없기에 class변수로 접근
    # speed는 값을 = 로 할당했기에 인스턴스변수 생성
    kinds = []
    speed = 300
    def add_kinds(self, name):
        self.kinds.append(name)
    def change_speed(self, speed):
        self.speed = speed

k5 = Car()
k3 = Car()
k5.add_kinds('k5')
k3.add_kinds('k3')
k5.change_speed(500)
k3.change_speed(250)

print('k5.kinds:', k5.kinds)
print('k3.kinds:', k3.kinds)
print('k5.speed:', k5.speed)
print('k3.speed:', k3.speed)
```

    k5.kinds: ['k5', 'k3']
    k3.kinds: ['k5', 'k3']
    k5.speed: 500
    k3.speed: 250



```python
# 클래스 변수
# 클래스 바로 하위에 자리하고 있으며
# 모든 인스턴스가 공유합니다.
# 인스턴스 변수
# 인스턴스 영역 안에서만 사용하는 변수
class Car(object):
    # kinds가 인스턴스에 없기에 class변수로 접근
    # speed는 값을 = 로 할당했기에 인스턴스변수 생성
    kinds = []
    speed = 300
    def add_kinds(self, name):
        self.kinds.append(name) # self.kinds = [name]로 사용하면 인스턴스 변수가 됩니다.
    def change_speed(self, speed):
        self.speed = speed

k5 = Car()
k3 = Car()
k5.speed = 500
k3.speed # 클래스 변수는 값을 공유한다고 했는데?
```




    300




```python
id()
```


```python
주인공 = ['licat', 10000]

class MobFactory(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.dropRate = 아이템확률

    def attack(self):
        주인공[1] -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'주인공의 체력이 {주인공[1]}가 되었습니다.')

슬라임 = MobFactory('슬라임', 1, 10, 10, 2, 2, 100, 1, 1)
오크 = MobFactory('오크', 10, 10, 10, 2, 2, 80, 1, 1)
고블린 = MobFactory('고블린', 100, 10, 10, 2, 2, 60, 1, 1)
드래곤 = MobFactory('드래곤', 1000, 10, 10, 2, 2, 40, 1, 1)
해골 = MobFactory('해골', 10000, 10, 10, 2, 2, 1, 1, 1)

슬라임.attack()
```

    슬라임이 1데미지로 공격했습니다.
    주인공의 체력이 9999가 되었습니다.



```python
주인공 = ['licat', 10000]

class MobFactory(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.dropRate = 아이템확률

    def attack(self):
        주인공[1] -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'주인공의 체력이 {주인공[1]}가 되었습니다.')


오크 = MobFactory('오크', 10, 10, 10, 2, 2, 80, 1, 1)
고블린 = MobFactory('고블린', 100, 10, 10, 2, 2, 60, 1, 1)
드래곤 = MobFactory('드래곤', 1000, 100000, 10, 2, 2, 40, 1, 1)
해골 = MobFactory('해골', 10000, 10, 10, 2, 2, 1, 1, 1)

슬라임.attack()
```

    슬라임이 1데미지로 공격했습니다.
    주인공의 체력이 9999가 되었습니다.



```python
주인공 = ['licat', 10000]

class MobFactory(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.dropRate = 아이템확률

    def __add__(self, next):
        if self.name == '슬라임':
            return MobFactory(f'왕{self.name + next.name}', 
                              self.power + next.power, 
                              10, 10, 2, 2, 100, 1, 1)
        return None

    def attack(self):
        주인공[1] -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'주인공의 체력이 {주인공[1]}가 되었습니다.')
    

슬라임 = 슬라임 = MobFactory('슬라임', 1, 10, 10, 2, 2, 100, 1, 1)
왕슬라임 = 슬라임 + 슬라임

왕슬라임.power
왕슬라임.name
```




    '왕슬라임슬라임'




```python
# 성철님 코드
class User(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.dropRate = 아이템확률

    def 슬라임_attack(self):
        슬라임.hp -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'몬스터의 체력이 {슬라임.hp}가 되었습니다.')

licat = User('licat', 5, 10000, 1000, 2, 2, 0, 2, 2)
licat.슬라임_attack()
mura = User('mura', 5, 10000, 1000, 2, 2, 0, 2, 2)
mura.슬라임_attack()
```

    licat이 5데미지로 공격했습니다.
    몬스터의 체력이 5가 되었습니다.
    mura이 5데미지로 공격했습니다.
    몬스터의 체력이 0가 되었습니다.



```python
# 개선 코드
class User(object):
    def __init__(self, 이름, 공격력, 체력, 마력, 크기_넓이, 크기_높이, 아이템확률, x, y):
        self.name = 이름
        self.power = 공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.dropRate = 아이템확률

    def attack(self, target):
        target.hp -= self.power
        print(f'{self.name}이 {self.power}데미지로 공격했습니다.')
        print(f'{target.name}의 체력이 {target.hp}가 되었습니다.')

licat = User('licat', 5, 10000, 1000, 2, 2, 0, 2, 2)
licat.attack(슬라임)
licat.attack(드래곤)
```

    licat이 5데미지로 공격했습니다.
    슬라임의 체력이 -5가 되었습니다.
    licat이 5데미지로 공격했습니다.
    드래곤의 체력이 99995가 되었습니다.



```python
# 준균님 코드
class Hero(object):
    def __init__(self, hero_info):
        self.info = hero_info
    def get_info(self):
        print(f"{self.info['name']}/위치 : {self.info['pos']}/체력 {self.info['hp']}/{self.info['max_hp']} / 레벨{self.info['level']}")

licat = Hero({
    'name' : 'licat',
    'pos' : [1,2],
    'max_hp' : 100,
    'hp' : 100,
    'level' : 1,
})

mura = Hero({
    'name' : 'mura',
    'pos' : [5,5],
    'max_hp' : 200,
    'hp' : 200,
    'level' : 5,
})

licat.get_info()
mura.get_info()
```


```python
# 질문? JAVA의 this와 self가 같은 개념인지?
# 답? JavaScript나 JAVA의 self와 개념이 비슷한데, 역시나 이렇게 대조를 해가면서 공부를 하면
# 오해의 여지가 생깁니다. 데이터 구조부터 다르긴 합니다.
```


```python
# 동섭님 코드
고블린 = ['Monster', 5000]
class PlayerSet(object):
    def __init__(self, 이름, 물리공격력, 마법공격력, 체력, 마력, 크기_넓이, 크기_높이, 위치_x축, 위치_y축):
        self.name = 이름
        self.hit_power = 물리공격력
        self.magic_power = 마법공격력
        self.hp = 체력
        self.mp = 마력
        self.width = 크기_넓이
        self.height = 크기_높이
        self.coordinate_x = 위치_x축
        self.coordinate_y = 위치_y축
    def attack(self):
        고블린[1] -= self.hit_power
        print(f'{self.name}이 {self.hit_power}데미지로 공격했습니다.')
        print(f'고블린의 체력이 {주인공[1]}이 되었습니다.')
    def magic(self):
        고블린[1] -= self.magic_power
        self.mp -= 5
        print(f'{self.name}이 {self.magic_power}데미지로 공격했습니다.')
        print(f'고블린의 체력이 {고블린[1]}이 되었습니다.')
        print(f'{self.name}의 마력이 {self.mp}이 되었습니다.')


라이캣 = PlayerSet('liecat', 100, 10, 2000, 500, 5, 5, 25, 10)
뮤라 = PlayerSet('mura', 5, 100, 2000,  1000, 3, 3, 30, 17)

라이캣.attack(), 뮤라.magic()
라이캣.magic(), 뮤라.attack()
```


```python
# 종수님 코드
class Character(object):
    def __init__(self, 이름, 직업, 외형):
        self.name = 이름
        self.characterClass = 직업
        self.characterModel = 외형
        self.x = 0
        self.y = 0
    
    def change_model(self, newCharacterModel):
        self.characterModel = newCharacterModel
        print(f'외형 변경 {self.characterModel} -> {newCharacterModel}')
    
    def move_left(self):
        self.x += 1
        print(f'현재 좌표 ({self.x}, {self.y})')
    
    def move_right(self):
        self.x -= 1
        print(f'현재 좌표 ({self.x}, {self.y})')

    def move_up(self):
        self.y += 1
        print(f'현재 좌표 ({self.x}, {self.y})')
    
    def move_down(self):
        self.y -= 1
        print(f'현재 좌표 ({self.x}, {self.y})')

licat = Character('licat', 직업=1, 외형=1)
mura = Character('mura', 2, 2)
```


```python
# 쉽고 중요한 예제!

class BlogFactory(object):
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

게시글3 = BlogFactory(
        '오늘 강원의 날씨',
        '오늘 강원의 날씨는 참 좋네요! 블라블라',
        '10000',
        '범남궁',
        '2023/05/10',
    )
    
게시글1.title
```




    '오늘 제주의 날씨'




```python
# 쉽고 중요한 예제!

class BlogFactory(object):
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

게시글3 = BlogFactory(
        '오늘 강원의 날씨',
        '오늘 강원의 날씨는 참 좋네요! 블라블라',
        '10000',
        '범남궁',
        '2023/05/10',
    )

data = [게시글1, 게시글2, 게시글3]
for i in data:
    print(i.title)
```

    오늘 제주의 날씨
    오늘 부산의 날씨
    오늘 강원의 날씨



```python
# 쉽고 중요한 예제!
# 이 코드는 가능하면 손으로 2 ~ 3번 써보시길 권해드립니다.

class BlogFactory(object):
    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

게시글3 = BlogFactory(
        '오늘 강원의 날씨',
        '오늘 강원의 날씨는 참 좋네요! 블라블라',
        '10000',
        '범남궁',
        '2023/05/10',
    )

data = [게시글1, 게시글2, 게시글3]
for i in data:
    if i.writer == '이호준':
        print(i.title)
        print(i.content)
        print(i.count)
        print(i.create_date)
```

    오늘 제주의 날씨
    오늘 제주의 날씨는 참 좋네요! 블라블라
    0
    2023/05/10



```python
data = [게시글1, 게시글2, 게시글3]
for i in data:
    print(i.title)
    print(i.content)
    print(i.writer)
    print(i.count)
    print(i.create_date)
```


```python
data = [게시글1, 게시글2, 게시글3]
for i in data:
    print(f'<h2>{i.title}</h2>')
    print(f'<p>{i.content}</p>')
    print(f'<p>{i.writer}</p>')
    print(f'<p>{i.count}</p>')
    print(f'<p>{i.create_date}</p>')
```


```python
# 클래스 변수로 글쓴이 찾기
```


```python
# 조금 난이도가 있는 예제이기 때문에
# 기억하지 않으셔도 됩니다.

class BlogFactory(object):
    dataset = []

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

게시글3 = BlogFactory(
        '오늘 강원의 날씨',
        '오늘 강원의 날씨는 참 좋네요! 블라블라',
        '10000',
        '범남궁',
        '2023/05/10',
    )

for i in 게시글1.dataset:
    print(i.title)
```

    오늘 제주의 날씨
    오늘 부산의 날씨
    오늘 강원의 날씨



```python
# x = 10
# y = 10
# x.__add__ = lambda self, next : str(self) + str(next) # error
```


```python
# python read only method create 가능한가?
```


```python
class BlogFactory(object):
    dataset = []

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):
        return 'hello'

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

print(게시글1, 게시글2)
```

    hello hello



```python
# 중요한 예제입니다.
class BlogFactory(object):
    dataset = []

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):
        return self.title

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

print(게시글1)
print(게시글2)
```

    오늘 제주의 날씨
    오늘 부산의 날씨



```python
# 중요한 예제입니다.
class BlogFactory(object):
    dataset = []

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):
        return f'제목 : {self.title}, 내용 : {self.content[:5]}, 글쓴이 : {self.writer}'

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

print(게시글1)
print(게시글2)
```

    제목 : 오늘 제주의 날씨, 내용 : 오늘 제주, 글쓴이 : 이호준
    제목 : 오늘 부산의 날씨, 내용 : 오늘 부산, 글쓴이 : 김재현



```python
# 중요한 예제입니다.
class BlogFactory(object):
    dataset = []

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜
        self.dataset.append(self)

    def __str__(self):
        return f'{len(self.dataset)}. 제목 : {self.title}, 내용 : {self.content[:5]}, 글쓴이 : {self.writer}'

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )
print(게시글1)

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )
print(게시글2)
```

    1. 제목 : 오늘 제주의 날씨, 내용 : 오늘 제주, 글쓴이 : 이호준
    2. 제목 : 오늘 부산의 날씨, 내용 : 오늘 부산, 글쓴이 : 김재현


### !! 클래스 연습문제


```python
# 각각 class를 만들어주시고, instance를 2개 이상 넣어서
# 활용(출력, 수정 등) 해보세요.
# 15분씩 총 30분, 6분에 문제를 냈기 때문에 36분까지 실습해보겠습니다.
# 각 코드는 만들어서 쓰레드에 올려주세요.
# 중요한 코드이니 꼭 한 번 만들어보세요! :)
class UserInfo(object):
    pass

class BookInfo(object):
    pass
```


```python
# (advanced) 그리고 물건을 사면 물건의 값이 UserInfo를 건드려야 하겠죠. 
# 물건도 class로 구현해주시면 너무 좋은 예제가 될 것 같네요. 🙂

# (advanced) 실제 github의 유저 정보를 등을 이용해서도 만들어보세요.
# https://api.github.com/repos/paullabkorea/jupyternotebookblog/languages
# https://docs.github.com/ko/rest/repos/repos?apiVersion=2022-11-28#get-a-repository

```


```python
import hashlib

비밀번호 = hashlib.sha256()
비밀번호.update('helloworld!'.encode('utf-8'))
비밀번호.hexdigest() # 영화를 집어넣든, 음악을 집어넣든, 소설을 집어넣든, 암호를 집어넣든 모두 64자로 만듭니다.
```




    '98d234db7e91f5ba026a25d0d6f17bc5ee0a347ea2216b0c9de06d43536d49f4'




```python
# 1번째 스탭
# 공개되는 정보, 공개되지 않는 정보
# 멤버(정적 수치, 문자열)와 메서드(기능)
class Product(object):
    def __init__(self, 품명, 가격):
        self.product_name = 품명
        self.price = 가격
        
자전거 = Product(
    '자전거',
    100000,
)

class UserInfo(object):
    def __init__(self, 
                 이름, 
                 이메일,
                 비밀번호, 
                 주요접속기기, 
                 주요접속국가, 
                 주요접속지역, 
                 마지막접속일자, 
                 회원가입날짜, 
                 별명, 
                 적립금, 
                 생일, 
                 휴대폰번호, 
                 휴대폰인증여부, 
                 고객등급, 
                 휴면계정여부):
        self.이름 = 이름
        self.고객등급 = 고객등급
        self.적립금 = 적립금
    
    def 물품구매(self, product):
        self.적립금 -= product.price

    def 회원탈퇴(self):
        pass

    def 장바구니등록(self):
        pass

이호준 = UserInfo(
    이름 = '이호준',
    이메일 = 'hojun@gmail.com',
    비밀번호 = '98d234db7e91f5ba026a25d0d6f17bc5ee0a347ea2216b0c9de06d43536d49f4',
    주요접속기기 = 'Android',
    주요접속국가 = 'Korea',
    주요접속지역 = 'Jeju',
    마지막접속일자 = '23/05/10',
    회원가입날짜 = '23/05/10',
    별명 = '준',
    적립금 = 1000000000,
    생일 = '13/13',
    휴대폰번호 = '010-0000-0000',
    휴대폰인증여부 = True,
    고객등급 = 'VIP',
    휴면계정여부 = False,
)

이호준.물품구매(자전거)
이호준.적립금
```




    999900000




```python
# 광호님 코드
class BookInfo(object):
    def __init__(self, title, price, writer, publisher, count, soldout, buyer):
        self.title = title
        self.price = price
        self.writer = writer
        self.publisher = publisher
        self.count = count
        self.soldout = soldout
        self.buyer = buyer

    def __str__(self):
        return self.title

    def sell(self, buyer):
        if self.get_soldout():
            print('재고가 없습니다')
            return None
        
        self.count -= 1
        self.add_buyer(buyer)
        
        if self.count <= 0:
           self.set_soldout(True)

    def add_buyer(self, buyer):
        self.buyer.append(buyer)
    
    def set_soldout(self, value):
        self.soldout = value

    def get_soldout(self):
        return self.soldout
```


```python
# 진찬님 코드
class BookInfo(object):
    dataset = []

    def __init__(self, title, writer, publisher, publish_date, price):
        self.title = title
        self.writer = writer
        self.publisher = publisher
        self.publish_date = publish_date
        self.price = price
        self.dataset.append(self)

    def __str__(self):
        return f'제목: {self.title}, 저자: {self.writer}, 출판사: {self.publisher}, 출판일: {self.publish_date}, 가격: {self.price}'
    
book1 = BookInfo(
    title = '마블',
    writer = '아이언맨',
    publisher = '어벤져스',
    publish_date = '2023/05/10',
    price = 10000
)
print(book1)
```

    제목: 마블, 저자: 아이언맨, 출판사: 어벤져스, 출판일: 2023/05/10, 가격: 10000



```python
class Car(object):
    MaxSpeed = 300
    MaxPeoeple = 5
    def __init__(self):
        pass
    def move(self, x):
        pass
    def stop(self):
        print('멈췄습니다.')
    @staticmethod #decorator
    def 스피드배속(현재스피드, 배속할스피드):
        print(f'현재 {현재스피드 * 배속할스피드}의 스피드로 달리고 있습니다.')

Car.스피드배속(100, 2) # 붕어빵 찍는 틀이 얼마나 붕어빵을 만들어 냈는가?
```

    현재 200의 스피드로 달리고 있습니다.



```python
#예를 들어
class Hotel:
    pass

Hotel.빈방있는호텔() # 전체 호텔에 빈방이 있는 호텔
호텔1.빈방() #호텔1에 빈방이 있는지 여부
```

### 상속


```python
# 이 예제는 기억하고 있으셔야 합니다.
class Car:
    maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')
    def stop(self):
        print('멈췄습니다.')

class HybridCar(Car):
    battery = 1000
    batteryKM = 300

class ElectricCar(HybridCar):
    battery = 2000
    batteryKM = 600
```


```python
dir(k3)

```


```python
K3 = Car()
HyK3 = HybridCar()
ElHyK3 = ElectricCar()
# id(K3.maxSpeed), id(HyK3.maxSpeed)
# id(K3.move), id(HyK3.move)

ElHyK3.move(10)
```

    10 의 스피드로 달리고 있습니다.


### !! 오늘 배운 것 정리
* 클래스
    * 클래스는 데이터(멤버)와 기능(메서드)을 가지고 있는 인스턴트 객체를 생성하기 위한 역할
    * 우리가 배우고 있는 Python을 객체 지향 프로그래밍 언어
        ```
        현실                                코드
        차 ---------------------------> class Car()
        정수 -------------------------> class int()
        실수 -------------------------> class float()

        인간이 만들어 
        놓은 현실 세계에서의 
        정의 또는 약속 --------------> class
        
        1 + 1 = 2가 컴퓨터 입장에서는 10일 수도 있고
        'A' + 'A' = 'AA'가 아니라 컴퓨터 입장에서는 130일 수 있습니다.
        현실세계에서 '인간끼리' 약속을 코드에 세계로 옮긴거에요.
        ```
    * 예제 1
        ```python
        # 메서드 : 클래스 내에 함수
        # 멤버 : 클래스 내에 변수
        # 애트리뷰트 : 멤버 + 메서드
        class CarFactory(object):
            max_speed = 300
            max_people = 5
            def move(self):
                print('차가 움직이고 있습니다.')
            def stop(self):
                print('차가 멈췄습니다.')

        k5 = CarFactory()
        k3 = CarFactory()
        k5.move()
        k3.move()
        k5.stop()
        k3.stop()
        print(k5.max_speed)
        ```
    * 예제2
        ```python
        # 클래스 변수
        # 클래스 바로 하위에 자리하고 있으며
        # 모든 인스턴스가 공유합니다.
        # 인스턴스 변수
        # 인스턴스 영역 안에서만 사용하는 변수
        class Car(object):
            # kinds가 인스턴스에 없기에 class변수로 접근
            # speed는 값을 = 로 할당했기에 인스턴스변수 생성
            kinds = []
            speed = 300
            def add_kinds(self, name):
                self.kinds.append(name) # self.kinds = [name]로 사용하면 인스턴스 변수가 됩니다.
            def change_speed(self, speed):
                self.speed = speed

        k5 = Car()
        k3 = Car()
        k5.speed = 500
        k3.speed # 클래스 변수는 값을 공유한다고 했는데?
        ```
    * 예제3
        ```python
        # 쉽고 중요한 예제!
        # 이 코드는 가능하면 손으로 2 ~ 3번 써보시길 권해드립니다.

        class BlogFactory(object):
            def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
                self.title = 제목
                self.content = 내용
                self.count = 조회수
                self.writer = 글쓴이
                self.create_date = 생성날짜

        게시글1 = BlogFactory(
                '오늘 제주의 날씨',
                '오늘 제주의 날씨는 참 좋네요! 블라블라',
                '0',
                '이호준',
                '2023/05/10',
            )

        게시글2 = BlogFactory(
                '오늘 부산의 날씨',
                '오늘 부산의 날씨는 참 좋네요! 블라블라',
                '1000000',
                '김재현',
                '2023/05/10',
            )

        게시글3 = BlogFactory(
                '오늘 강원의 날씨',
                '오늘 강원의 날씨는 참 좋네요! 블라블라',
                '10000',
                '범남궁',
                '2023/05/10',
            )

        data = [게시글1, 게시글2, 게시글3]
        for i in data:
            if i.writer == '이호준':
                print(i.title)
                print(i.content)
                print(i.count)
                print(i.create_date)
        ```
* 클래스 상속
    * 클래스에서 상속은 상속해주는 클래스(Parent Class, Super class)의 내용(속성과 메소드)을 상속받는 클래스(Child class, sub class)가 가지게 되는 것
    * 코드 예
        ```python
        # 이 예제는 기억하고 있으셔야 합니다.
        class Car:
            maxSpeed = 300
            maxPeople = 5
            def move(self, x):
                print(x, '의 스피드로 달리고 있습니다.')
            def stop(self):
                print('멈췄습니다.')

        class HybridCar(Car):
            battery = 1000
            batteryKM = 300

        class ElectricCar(HybridCar):
            battery = 2000
            batteryKM = 600

        K3 = Car()
        HyK3 = HybridCar()
        ElHyK3 = ElectricCar()
        # id(K3.maxSpeed), id(HyK3.maxSpeed)
        # id(K3.move), id(HyK3.move)

        ElHyK3.move(10)
        ```


```python
# 질문 : id를 객체가 아니라 count라는 정수값을 지정해줘서 증가시키고 싶습니다.
# 답 : 아래코드처럼 사용하시면 됩니다.
class BlogFactory(object):

    count = 0

    def __init__(self, 제목, 내용, 조회수, 글쓴이, 생성날짜):
        BlogFactory.count += 1
        self.id = BlogFactory.count
        self.title = 제목
        self.content = 내용
        self.count = 조회수
        self.writer = 글쓴이
        self.create_date = 생성날짜

    def __str__(self):
        return f'{self.id}. 제목 : {self.title}, 내용 : {self.content[:5]}'

게시글1 = BlogFactory(
        '오늘 제주의 날씨',
        '오늘 제주의 날씨는 참 좋네요! 블라블라',
        '0',
        '이호준',
        '2023/05/10',
    )

게시글2 = BlogFactory(
        '오늘 부산의 날씨',
        '오늘 부산의 날씨는 참 좋네요! 블라블라',
        '1000000',
        '김재현',
        '2023/05/10',
    )

print(게시글1)
print(게시글2)
```

    1. 제목 : 오늘 제주의 날씨, 내용 : 오늘 제주
    2. 제목 : 오늘 부산의 날씨, 내용 : 오늘 부산



```python
# 자율학습시간에 대한 피드백 => 문제를 내드리기로 하였습니다.
# 매일 3시 40분 즈음에 advanced 문제를 드리고 각 조별 단톡방에 해당 내용을 공유하고 얘기하는 시간을 가지기로 하였습니다.
```


```python
# 어제 새벽에 주신 코드ㅎㅎ
# 반갑습니다. :) 이거 제가 오전에 설명해드려도 될까요? :) 
# 우선 설계에서 UserInfo와 Product를 상속 관계로 만드는 것은 적절치 않습니다. 
# 적절한지 여부는 부모 클래스의 정보를 자식 클래스가 가질 필요가 있는지로 판단해주시면 됩니다.
class Product(object):
    def __init__(self, 품명, 개수, 가격):
        self.product_name = 품명
        self.product_count = 개수
        self.product_price = 가격
    
    def __str__(self):
        return f'품명:{self.product_name}, 개수:{self.product_count}, 가격:{self.product_price}'

시리얼 = Product('시리얼', 20, 8900)
초코칩쿠키 = Product('초코칩쿠키', 30, 4300)
칸쵸 = Product('칸쵸', 12, 1400)

class UserInfo(Product):
    dataset = []

    def __init__(self, 이름, 닉네임, 휴대폰번호, 생년월일, 주소, 예치금, 고객등급):      
        self.user_name = 이름
        self.nickname = 닉네임
        self.user_phone = 휴대폰번호
        self.user_birth = 생년월일
        self.user_addr = 주소
        self.user_deposit = 예치금
        self.user_rank = 고객등급

    def 물품구매(self, product, count):
        self.user_deposit -= product.product_price
        시리얼.product_count -= count


홍길동 = UserInfo(
                    '홍길동', 
                    '길동이', 
                    '010-0000-0000', 
                    '1993/10/10', 
                    '경기도 광주시', 
                    1000000, 
                    'VIP')

장판수 = UserInfo(
                    '장판수', 
                    '판자', 
                    '010-1111-1111', 
                    '1992/02/10', 
                    '경기도 광명시', 
                    20000000, 
                    'Silver')

홍길동.물품구매(시리얼, 2)
print(홍길동.user_deposit)
print(시리얼.product_count)

장판수.물품구매(시리얼, 10)
print(시리얼.product_count)

print(시리얼)
```

    991100
    18
    8
    품명:시리얼, 개수:8, 가격:8900



```python
class Product:
    def __init__(self, 품명, 개수, 가격):
        self.product_name = 품명
        self.product_count = 개수
        self.product_price = 가격
    
    def __str__(self):
        return f'품명:{self.product_name}, 개수:{self.product_count}, 가격:{self.product_price}'

시리얼 = Product('시리얼', 20, 8900)
초코칩쿠키 = Product('초코칩쿠키', 30, 4300)
칸쵸 = Product('칸쵸', 12, 1400)

class UserInfo:
    dataset = []

    def __init__(self, 이름, 닉네임, 휴대폰번호, 생년월일, 주소, 예치금, 고객등급):      
        self.user_name = 이름
        self.nickname = 닉네임
        self.user_phone = 휴대폰번호
        self.user_birth = 생년월일
        self.user_addr = 주소
        self.user_deposit = 예치금
        self.user_rank = 고객등급

    def 물품구매(self, product, count):
        self.user_deposit -= product.product_price
        product.product_count -= count


홍길동 = UserInfo(
                    '홍길동', 
                    '길동이', 
                    '010-0000-0000', 
                    '1993/10/10', 
                    '경기도 광주시', 
                    1000000, 
                    'VIP')

장판수 = UserInfo(
                    '장판수', 
                    '판자', 
                    '010-1111-1111', 
                    '1992/02/10', 
                    '경기도 광명시', 
                    20000000, 
                    'Silver')

홍길동.물품구매(시리얼, 2)
print(홍길동.user_deposit)
print(시리얼.product_count)

장판수.물품구매(시리얼, 10)
print(시리얼.product_count)

print(시리얼)
```


```python
print(chr(ord("生") & ord("死")))
```

    愛



```python
# 우리가 앞으로 알고리즘에서 할 코드입니다.
# 예방주사 차원에서 진행하도록 하겠습니다.
```


```python
# 아주 간단한 코드입니다.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

노드1 = Node(10)
노드2 = Node(20)
노드3 = Node(30)

# 노드1.data

노드1.next = 노드2
노드2.next = 노드3

노드1.next.data # 노드2.data
노드1.next.next.data # 노드2.next.data # 노드3.data
```




    30




```python
# 바름님 코드
class Node:
    dataset = []

    def __init__(self, data1, data2):
        self.data = [data1, data2]
        self.next = None
        self.dataset.append(self)

node1 = Node(10,20)
node2 = Node(20,30)
node3 = Node(30,40)

for i in range(len(node1.dataset)-1):
    node1.dataset[i].next = node1.dataset[i+1]

print(node1.data, node1.next.data, node1.next.next.data)
```


```python
class Node:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.next = None

노드1 = Node(101,201)
노드2 = Node(301,401)
노드3 = Node(501,601)

노드1.next = 노드2
노드2.next = 노드3

노드1.data1
노드1.next.data1
```




    301



### 메서드 오버라이딩

* 부모 클래스에서 상속받은 함수를 자식 클래서에서 같은 이름으로 선언하여 사용하는 것


```python
class Car(object):
    maxSpeed = 300
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')

class HybridCar(Car):
    battery = 1000

class ElectricCar(HybridCar):
    battery = 2000

    def move(self, x):
        print(x, '스피드로 달리고 있습니다.')

car1 = ElectricCar()
car1.move()
```

### 다중상속


```python
class Car(object):
    maxSpeed = 300
    def move(self, x):
        print(x, '의 스피드로 달리고 있습니다.')

class HybridCar(Car):
    battery = 1000

class ElectricCar(HybridCar):
    battery = 2000

    def move(self, x):
        print(x, '스피드로 달리고 있습니다.')

class Test(ElectricCar):
    pass

Test.mro() # MRO(Method Resolution Order)
# print(Test.battery)
```




    [__main__.Test, __main__.ElectricCar, __main__.HybridCar, __main__.Car, object]




```python
class A(object):
    maxSpeed = 300

class B(A):
    battery = 1000

class C(A):
    battery = 2000

class D(C):
    pass

D.mro()
# D.battery
```




    [__main__.D, __main__.C, __main__.A, object]




```python
class A(object):
    maxSpeed = 300

class B(A):
    battery = 1000

class C(A):
    battery = 2000

class D(B, C):
    pass

D.mro()
# D.battery
```




    [__main__.D, __main__.B, __main__.C, __main__.A, object]




```python
# __는 문법 적으로 접근이 안됩니다. : 변수를 보호할 수 있어요.
# 변수를 변경하는 것을 보다 엄격하게 관리할 수 있습니다.

# _는 공식 X
# _는 문법 적으로 접근이 됩니다.(회사 컨벤션마다 다릅니다.)

class Car(object):
    __maxSpeed = 300
    maxPeople = 5
    def move(self, x):
        print(x, '의 스피드로 움직이고 있습니다.')
        print(self.__maxSpeed, '가 최고 속도입니다.')
    def stop(self):
        print('멈췄습니다.')

k5 = Car()
k5.move(10)
# k5.__maxSpeed #error
# k5.maxPeople
```

    10 의 스피드로 움직이고 있습니다.
    300 가 최고 속도입니다.


## 이터레이터


```python
class MyIter:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        self.currentValue += 1
        return self.currentValue

li = MyIter(5)
for i in li:
    print(i)
```

    1
    2
    3
    4
    5



```python
raise StopIteration
```


```python
class MyIter:
    def __init__(self, stop):
        self.currentValue = 0
        self.stop = stop
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        result = self.currentValue
        self.currentValue += 1
        return result

li = MyIter(5)
for i in li:
    print(i)

for i in li:
    print(i)
```

    0
    1
    2
    3
    4



```python
class MyIter:
    def __init__(self, stop):
        self.stop = stop
    
    def __iter__(self):
        self.currentValue = 0
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        result = self.currentValue
        self.currentValue += 1
        return result

li = MyIter(5)
# for는 iter먼저 실행하고, next로 StopIteration
for i in li:
    print(i)

for i in li:
    print(i)
```

    0
    1
    2
    3
    4
    0
    1
    2
    3
    4



```python
class MyIter:
    def __init__(self, stop):
        self.stop = stop
    
    def __iter__(self):
        self.currentValue = 0
        return self

    def __next__(self):
        if self.currentValue >= self.stop:
            raise StopIteration
        result = self.currentValue
        self.currentValue += 1
        return result

li = MyIter(5)
# for는 iter먼저 실행하고, next로 StopIteration
i = iter(li)
next(i)
```




    0




```python
next(i)
```


```python
a, b, c, d = MyIter(4)
print(a, b, c, d)
```

    0 1 2 3



```python
a, b, c, d = range(4)
print(a, b, c, d)
```

    0 1 2 3


## 제너레이터

* 제너레이터란, 이터레이터를 생성해주는 함수


```python
def gen():
    count = 0
    while True:
        yield count
        count += 1


for i in gen():
    print(i)
    if i == 10:
        break
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10



```python
def gen():
    count = 0
    while True:
        yield count
        count += 2

l = [10, 20, 30, 40, 50]
list(zip(l, gen()))
```




    [(10, 0), (20, 2), (30, 4), (40, 6), (50, 8)]




```python
def gen():
    count = 0
    while True:
        yield f'{count}주차'
        count += 2
과목 = ['HTML', 'CSS', 'JavaScript', 'Python']

list(zip(과목, gen()))
```




    [('HTML', '0주차'), ('CSS', '2주차'), ('JavaScript', '4주차'), ('Python', '6주차')]




```python
def gen():
    count = 1
    while True:
        yield count
        count += 1
        if count == 6:
            count = 1
과목 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

list(zip(과목, gen()))
```




    [('A', 1),
     ('B', 2),
     ('C', 3),
     ('D', 4),
     ('E', 5),
     ('F', 1),
     ('G', 2),
     ('H', 3),
     ('I', 4),
     ('J', 5),
     ('K', 1)]



## 데코레이터 (데커레이터)


```python
# 아래와 같이 실무에서 활용됩니다.

@login
def 비밀게시판():
    return render()

@check_vip
def vip용쿠폰():
    return render()

# 데이터 전처리 : 
# 데이터에 이상치(이상한 값), 결측치(비어있는 값) 등을 처리
# ['10', 1, 2, 3, '20'] -> [10, 1, 2, 3, 20]
@데이터전처리
sum(data)

@데이터전처리후페센테이지
sum(data)

# [10, 20, 30] -> 60%
```


```python
def one():
    return lambda x, y: x + y

더하기 = one()
더하기(10, 10)
```




    20




```python
def one():
    def two(x, y):
        return x + y
    return two

더하기 = one()
더하기(10, 10)
```




    20




```python
# 중요한 코드입니다.
# 손으로 2 ~ 3번 써보시길 권해드립니다.
def print_hello(func):
    def wrap_func():
        print('hello start')
        func()
        print('hello end')
    return wrap_func

@print_hello
def func1():
    print('func1 입니다.')

func1()
```

    hello
    func1 입니다.



```python
def 인사말(func):
    def wrap_func():
        print('안녕하세요.')
        func()
    return wrap_func

@인사말
def 자기소개1():
    print('이호준입니다.')

@인사말
def 자기소개2():
    print('홍길동입니다.')

def 작별인사():
    print('안녕히계세요.')

자기소개1()
자기소개2()
작별인사()
```

    안녕하세요.
    이호준입니다.
    안녕하세요.
    홍길동입니다.
    안녕히계세요.



```python
def 인사말(func):
    def wrap_func():
        print('안녕하세요.')
        func()
    return wrap_func

def 자기소개1():
    print('이호준입니다.')

def 자기소개2():
    print('홍길동입니다.')

def 작별인사():
    print('안녕히계세요.')

인사말(자기소개1)()
인사말(자기소개2)()
작별인사()
```

    안녕하세요.
    이호준입니다.
    안녕하세요.
    홍길동입니다.
    안녕히계세요.



```python
def 인사말(func):
    def wrap_func(이름):
        print('안녕하세요.')
        func(이름)
    return wrap_func

@인사말
def 자기소개1(name):
    print(f'{name}입니다.')

@인사말
def 자기소개2(name):
    print(f'{name}입니다.')

def 작별인사():
    print('안녕히계세요.')

자기소개1('이호준')
자기소개2('홍길동')
작별인사()
```


```python
def 인사말(func):
    def wrap_func(이름):
        print('안녕하세요.')
        func(이름)
    return wrap_func

def 자기소개1(name):
    print(f'{name}입니다.')

def 자기소개2(name):
    print(f'{name}입니다.')

def 작별인사():
    print('안녕히계세요.')

인사말(자기소개1)('이호준')
인사말(자기소개2)('홍길동')
작별인사()
```

    안녕하세요.
    이호준입니다.
    안녕하세요.
    홍길동입니다.
    안녕히계세요.



```python
def 전처리(func):
    def wrap_func(iterable):
        iterable = list(map(int, iterable))
        print(func(iterable))
    return wrap_func

@전처리
def 평균(l):
    return sum(l) / len(l)

평균(['1', 2, 3, '4'])
```

    2.5



```python
def 전처리(func):
    def wrap_func(iterable):
        return func(list(map(int, iterable)))
    return wrap_func

@전처리
def 평균(l):
    return sum(l) / len(l)

평균(['1', 2, 3, '4'])
```




    2.5




```python
def 전처리(func):
    def wrap_func(iterable):
        i = list(map(int, iterable))
        calculate = func(i)
        result = str(calculate) + '%'
        return result
    return wrap_func

@전처리
def 평균(l):
    return sum(l) / len(l)

평균(['1', 2, 3, '4'])
```




    '2.5%'




```python
# 데코레이터 실습 문제
# 다음 값이 들어갔을 때, 숫자만 모두 더하는 코드를 완성하세요.
li = ['10', True, False, '21', 0, 10, 20]

@전처리
def custom_sum(l):
    sum(l)

custom_sum(li)
```


```python
# 코드리뷰는 여러분들과 분리하셔야 합니다.

# 승현님 코드
ls = ['10', True, False, '21', 0, 10, 20]

def 전처리(func):
    def wrap_func():
        return sum(filter(lambda x: isinstance(x, int), ls))
    return wrap_func

@전처리
def custom_sum():
    pass
    
custom_sum()
```




    31




```python
# 준균님 코드
def 전처리(func):
    def wrap_func(iterable):
        print(func([int(i) for i in iterable if str(i).isdigit() == True]))
    return wrap_func

@전처리
def custom_sum(l):
    return sum(l)
    
custom_sum(['10', True, False, '21', 0, 10, 20])
```

    61



```python
# 바름님 코드
l = ['10', True, False, '21', 0, 10, 20]

def 전처리(func):
    def warp_func(iterable):
        iterable = map(int, filter(lambda x: type(x) == int or type(x) == str, iterable))
        return func(iterable)
    return warp_func
    
@전처리
def custom_sum(data):
    return sum(data)

print(custom_sum(l))
```

    61



```python
# 데코레이터에 argument를 넣는 방법
def deco1(name):
    def deco2(func):
        def wrapper():
            print('decorator1')
            func()
        return wrapper
    return deco2
 
# 데코레이터를 여러 개 지정
@deco1('hojun')
def hello():
    print('hello')
 
hello()
```

    decorator1
    hello



```python
# 2중 decorator
def decorator1(func):
    def wrapper():
        print(f'deco1 > wrapper > func : {id(func)}')
        func()
    print(f'deco1 > wrapper : {id(wrapper)}')
    return wrapper
 
def decorator2(func):
    def wrapper():
        print(f'deco2 > wrapper > func : {id(func)}')
        func()
    print(f'deco2 > wrapper : {id(wrapper)}')
    return wrapper
 
# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
 
hello()
```

    deco2 > wrapper : 140658962986416
    deco1 > wrapper : 140658962701552
    deco1 > wrapper > func : 140658962986416
    deco2 > wrapper > func : 140658962973744
    hello



```python
id(decorator1), id(decorator2), id(hello)
```




    (139922952125840, 139922952126272, 139922950549520)



## 모듈과 패키지


```python
# 연습1 (파일 1개 생성)
# 현재 폴더에 test1.py 파일을 생성했고
# name = 'leehojun'
# age = 10

# def hello():
#     pass

# class Human():
#     pass
```


```python
import test1

print(test1.name)
print(test1.hello())
```

    leehojun
    None



```python
# 연습 2 (파일 2개 생성)
# 주의!! 같은 이름이 있었을 경우
# 마지막에 추가된 추가된 변수명으로 할당
# import * 는 더더욱 포함시키는 변수, 메서드, 클래스 명을 알 수 없기에
# 주의해서 사용해야 합니다.
from test2 import name
from test1 import name

print(name)
```

    leehojun1



```python
# 연습 3 (폴더 > 파일 생성)
# one이라는 것이 여기서는 폴더입니다!
# two가 file 이름이에요.
from one import two

print(two.name)
```

    hello world



```python
# 연습 4 (폴더 > 폴더 > 파일 생성)
# 런타임 재시작 하세요!
from one.two import three

print(three.name)
```

    hello world



```python
# 연습 5
import test1 as t

t.hello()
```

    hello world



```python
# Python에 모듈
import pandas as pd
import numpy as np
```


```python
!mkdir leehojun
```


```python
!pip install 패키지이름
```


```python
!pip list # 실행 결과를 남겨드리고 싶으나 너무 길어 삭제
```


```python
import random as rd #랜덤한 숫자 반환

rd.randint(0, 10)
```




    4



## 파일 입출력


```python
f = open('python.txt', 'w') # 파일모드 : r(read), w(write, 덮어씁니다.ㅜㅜ), a(append)
f.close()
```


```python
f = open('python.txt', 'w')
s = 'hello\nworld'
f.write(s)
f.close()
```


```python
# 문제 : 다음 입력을 통해 아래와 같은 출력 결과를 만드세요.
# (모듈 써수 푸셔도 좋지만 가능하면 모듈을 안쓰고 풀어보시길 권해드립니다.)
# 입력
data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]
# 출력
'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''
#코드
f = open('data.json', 'w')
s = str(dict(zip(data1,data2)))
f.write(s)
f.close()
```


```python
import json
# 입력
data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]
# 출력
'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''
#코드
f = open('data.json', 'w')
s = json.dumps(dict(zip(data1,data2)), indent=4)
f.write(s)
f.close()
```


```python
# 정답에 근접하였으나 콤마가 없고
# 띄어쓰기 4번이 안되어 있습니다.
data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]

'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''
f = open('data.json', 'w')
# 이 코드를 보면 다 덮어쓸 것 같지만 write할 때마다 append됩니다. w모드로 열어서도요.
f.write('{\n')
for elem in [f'"{d1}\" : {d2}' for d1, d2 in zip(data1, data2)]:
    f.write(elem)
    f.write('\n')
f.write('}')
f.close()
```


```python
# 바름님 코드 (정답!)
import json

data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]
'''
{
    "one" : 10,
    "two" : 20,
    "three" : 30
}
'''
f = open('data.json', 'w')
json.dump(dict(zip(data1,data2)),f,indent = '\t')
f.close()
```


```python
data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]

### https://stackoverflow.com/a/3229493
def pretty(d):
    ret = "{\n"
    for key, value in d.items():
        ret += '\t' + str(key).replace("'", "\"") + ": "
        ret += '\t' + str(value) + "\n"
    ret += "}"
    return ret

res = dict(zip(data1, data2))
stringed = str(res).replace("'", "\"")

# print(pretty(res))

f = open('data.json', 'w')
f.write(pretty(res))
f.close()
```


```python
import json
text = f'/////////////// 업데이트 방법 //////////////\n\
// 1. 아래 데이터는 민감데이터로 크롤링에 의존하지 않는 데이터입니다.\n\
//    긴급할 경우 아래 데이터만 수정하여 push 해주세요.\n\
// 2. 크롤러_통합.py를 실행시키시고, 모두 push해주시면 됩니다.\n\
//    크롤러_세계확진자.js, koreaRegionalData.js가 뽑힙니다.\n\
// 3. 크롤러가 동작하지 않을 경우 수동업데이트해야 합니다.\n\
////////////////////////////////////////////\n\
// 존스홉킨스 : https://gisanddata.maps.arcgis.com/a\n\
// https://www.worldometers.info/coronavirus/\n\
// 질본 : http://ncov.mohw.go.kr/bdBoardLis\n\
// 선차트용 데이터 - 제주도청 제공\n\
var 입도객현황 = '

data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]


f = open('data.js', 'w')
s = json.dumps(dict(zip(data1,data2)), indent=4)
s = text + s
f.write(s)
f.close()
```


```python
import json

text = f'안내문구\nvar 입도객현황 = '

data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]

f = open('data.js', 'w')
s = json.dumps(dict(zip(data1,data2)), indent=4)
s = text + s
f.write(s)
f.close()
```


```python
text = f'//안내문구\nvar 입도객현황 = '

data1 = ['one', 'two', 'three']
data2 = [10, 20, 30]

f = open('data.js', 'w')
s = str(dict(zip(data1,data2)))
s = text + s
f.write(s)
f.close()
```


```python
text = f'//안내문구\nvar 입도객현황 = '

data1 = ['one', 'two', 'three',]
data2 = [10, 20, 30,]

f = open('data.js', 'w')
s = str(data1)
s = text + s
f.write(s)
f.close()
```


```python
str(['one', 'two', 'three',])
```




    "['one', 'two', 'three']"



## 파일 읽기

* readline( ) : 라인 별로 읽습니다.


```python
f = open('python.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()
```

    hello
    
    world


* readlines( ) : 전체 텍스트를 한꺼번에 읽어옵니다.


```python
f = open('python.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()
```

* read( ) : 파일 전체 내용을 읽어옵니다.


```python
f = open('python.txt', 'r')
data = f.read()
print(data)
f.close()
```

    hello
    world



```python
# 개행이 2번 되었던 이유는 print 함수가 이미 개행 옵션을 가지고 있기 때문
f = open('python.txt', 'r')
lines = f.readlines()
for line in lines:
    print(line, end='')
f.close()
```

    hello
    world

## 파일 내용 추가


```python
f = open('python.txt', 'w')
s = ''
for i in range(5):
    s += f'{i}명 참여 중입니다. \n'
f.write(s)
f.close()
```


```python
f = open('python.txt', 'a') # 다시 write 모드로 하면 처음부터 덮어 씁니다.
s = ''
for i in range(5, 11):
    s += f'{i}명 참여 중입니다. \n'
f.write(s)
f.close()
```

* 파일이 계속 열려있는 상태가 유지
* 메모리 효율

## 파일 열기와 닫기를 동시에


```python
with open('test.txt', 'w') as f:
	f.write('Life is too short, you need python')
```

## 파일 입출력 심화 과정

* github(https://github.com/paullabkorea/xlsxwriter) 에서 모든 소스코드를 다운로드 받으실 수 있습니다.
* 무료책인 인공지능을 활용한 업무자동화 책(2021 Version Notion)을 활용하면 좀 더 활용성이 극대화된 코딩이 가능합니다.(크롤링, 워드파일 크롤링, PDF크롤링, 문자 보내기 등)
* 업무자동화 Notion 링크 : https://paullabworkspace.notion.site/2021-6192ed4219fc4e7a96e10b22cfa27c80


```python
!pip3 install xlsxwriter
```

    Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
    Collecting xlsxwriter
      Downloading XlsxWriter-3.1.0-py3-none-any.whl (152 kB)
    [2K     [90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━[0m [32m152.7/152.7 kB[0m [31m3.7 MB/s[0m eta [36m0:00:00[0m
    [?25hInstalling collected packages: xlsxwriter
    Successfully installed xlsxwriter-3.1.0



```python
# openpyxl, xlrd, xlwt...
# 다른 사용자가 만든 모듈
```


```python
import xlsxwriter

# 엑셀 파일 생성하기
workbook = xlsxwriter.Workbook('test.xlsx')

# 파일 안에 워크 시트 생성하기
worksheet = workbook.add_worksheet('test')

data = ['AA', 'BB', 'CC', 'DD']
worksheet.write('A1', data[0])
worksheet.write('B1', data[1])
worksheet.write('C1', data[2])
worksheet.write('D1', data[3])

worksheet.write('A2', 1)
worksheet.write('B2', 2)
worksheet.write('C2', 3)
worksheet.write('D2', 4)
            #(행, 열, 데이터)
worksheet.write(2, 0, 10)
worksheet.write(2, 1, 20)
worksheet.write(2, 2, 30)
worksheet.write(2, 3, 40)

workbook.close()
```


```python
홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]
```


```python
홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('test')

l = ['이름', '국어', '영어', '수학', '평균']
for i in range(5):
    worksheet.write(0, i, l[i])

worksheet.write(1, 0, '홍길동')
for i in range(3):
    worksheet.write(1, i+1, 홍길동[i])
worksheet.write(1, 4, sum(홍길동) / len(홍길동))

worksheet.write(2, 0, '이호준')
for i in range(3):
    worksheet.write(2, i+1, 이호준[i])
worksheet.write(2, 4, sum(이호준) / len(이호준))

worksheet.write(3, 0, '김철수')
for i in range(3):
    worksheet.write(3, i+1, 김철수[i])
worksheet.write(3, 4, sum(김철수) / len(김철수))

workbook.close()
```


```python
홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]
all_data = [홍길동, 이호준, 김철수]

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('Grades')

row_header = ['', '국어', '영어', '수학', '평균']
col_header = ['', '홍길동', '이호준', '김철수']

for idx, subject in enumerate(row_header):
    worksheet.write(0, idx, subject)

for idx, subject in enumerate(col_header):
    worksheet.write(idx, 0, subject)

for row_idx, line in enumerate(all_data):
    for col_idx, value in enumerate(line):
        worksheet.write(row_idx +1, col_idx + 1, value)
    # average
    avg = sum(line) / len(line)
    worksheet.write(row_idx + 1, len(line) + 1, avg)

workbook.close()
```


```python
import xlsxwriter

홍길동 = [33, 88, 24]
이호준 = [34, 66, 77]
김철수 = [78, 82, 36]

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('test')

worksheet.write(0, 0, '이름')
worksheet.write(0, 1, '국어')
worksheet.write(0, 2, '영어')
worksheet.write(0, 3, '수학')

worksheet.write(1, 0, '홍길동')
worksheet.write(2, 0, '이호준')
worksheet.write(3, 0, '김철수')

for i in range(len(홍길동)):
    worksheet.write(1, i+1, 홍길동[i])
    worksheet.write(2, i+1, 이호준[i])
    worksheet.write(3, i+1, 김철수[i])

workbook.close()
```


```python
# 배보다 배꼽이 더 큰지 꼭 확인 하세요.
# 개발 시간 + 유지 보수
```

## OS 모듈


```python
import os

os.getcwd() # os.getcwd() 함수는 현재 작업 디렉토리를 출력
```




    '/content'




```python
os.listdir() # 경로에 존재하는 파일과 디렉토리를 리스트로 반환할 때 사용
```




    ['.config',
     'leehojun',
     'test.xlsx',
     'python.txt',
     'test1.py',
     '__pycache__',
     'test2.py',
     'data.js',
     'data.json',
     '.ipynb_checkpoints',
     'one',
     'sample_data']




```python
for i in os.listdir():
    if len(i.split('.')) >= 2:
        if i.split('.')[1] == 'py' or i.split('.')[1] == 'txt':
            print(i)
```

    python.txt
    test1.py
    test2.py



```python
os.mkdir('hello') # 폴더를 생성할 일이 없습니다. # log 누적할 때
```


```python
import glob

glob.glob("*.py")
```




    ['test1.py', 'test2.py']



## advanced 문제

```python
@writefile
def add(a, b):
    return a + b

# writefile의 데코레이터 기능은 아래와 같은 형식으로 result.txt에 항상 저장되게 하는 것입니다.
# {
#     "a": 10,
#     "b": 20,
#     "a+b": 30
# }
```


```python
# 동건님 코드 : 문제는 없으나 add를 실행시키긴 해야합니다!
# 데코레이터 => 아래 코드는 데코할 대상이 없는거에요.

'''
추가로 부연 설명을 합니다. :)
스토리로 굳이 표현하자면 아래와 같습니다.

1. add라는 함수를 내가 1년 전에 만들었다. 문제 없이 잘 작동하는 함수이다.
2. 이 add를 데코레이터를 써서 파일 입출력이 되게 하고 싶다.
3. 데코레이터를 만든다.
4. 기존의 코드도 정상적으로 작동이 되어야 한다.
'''

import json

def writerfile(func):
    def wrapper(a, b):
        data1 = ['a', 'b', 'a+b']
        data2 = [a, b, a+b]
        f = open('writerfile.json', 'w')
        json.dump(dict(zip(data1,data2)), f, indent = 4)
        f.close()
    return wrapper

@writerfile
def add(a,b):
    return a + b

add(10, 20)
```


```python
# 기존 코드
def add(a,b):
    return a + b

result = add(10, 20) + add(10, 20)
print(result)
```

    60



```python
import json

def writerfile(func):
    def wrapper(a, b):
        data1 = ['a', 'b', 'a+b']
        data2 = [a, b, a+b]
        f = open('writerfile.json', 'w')
        json.dump(dict(zip(data1,data2)), f, indent = 4)
        f.close()
        return func(a, b)
    return wrapper

@writerfile
def add(a,b):
    return a + b

result = add(10, 20) + add(10, 20)
print(result)
```

    60


## !! 오늘 배운 것 정리
* 제너레이터
    * 제너레이터란, 이터레이터(순회 가능한 객체)를 생성해주는 함수
    * 예제 1
        ```python
        def gen():
            count = 0
            while True:
                yield count
                count += 1
        for i in gen():
            print(i)
            if i == 10:
                break
        ```
* 데코레이터
    * 함수 앞 뒤로 다른 역활을 해주는 기능을 붙이고 싶을 때 사용
    * 코드 예
        ```python
        def print_hello(func):
            def wrap_func():
                print('hello start')
                func()
                print('hello end')
            return wrap_func

        @print_hello
        def func1():
            print('func1 입니다.')

        func1()
        ```

* 파이썬 모듈
    * 모듈 : 함수나 변수 또는 클래스를 모아 놓은 파이썬 파일
    * 패키지 : 파이썬 모듈들을 계층적으로 관리
    * 모듈 사용 예1
    ```python
    # 같은 폴더 내 test1.py
    name = 'leehojun'
    age = 10

    def hello():
        pass

    class Human():
        pass

    # 같은 폴더 내 실행 파일
    import test1

    print(test1.name)
    print(test1.hello())
    ```
    * 예2
    ```python
    # 연습 3 (폴더 > 파일 생성)
    # one이라는 것이 여기서는 폴더입니다!
    # two가 file 이름이에요.
    from one import two

    print(two.name)
    ```
    * 예3
    ```python
    # 연습 4 (폴더 > 폴더 > 파일 생성)
    # 런타임 재시작 하세요!
    from one.two import three

    print(three.name)
    ```

* 파일 입출력
    * 파일을 읽고 쓰는 것
        * 파일 쓰기
        ```python
        f = open('python.txt', 'w') 
        # 파일모드 : r(read), w(write, 처음부터 덮어씁니다.), a(append)
        s = 'hello\nworld'
        f.write(s)
        f.close()
        ```
        * 파일 읽기
        ```python
        f = open('python.txt', 'r')
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
        f.close()
        ```
        ```python
        f = open('python.txt', 'r')
        data = f.read()
        print(data)
        f.close()
        ```

## Python Error

* Python에서는 애러를 만나면 코드가(서비스가) 멈춥니다.
* 여러분들이 짠 코드가 서비스에 영향이 끼쳐지지 않도록 시니어 분들이 견고한 코드를 작성해놨을 겁니다.
* TDD, 테스트 주도 개발 등 Test를 할 수 있는 환경 등이 갖춰져 있습니다.
* 작성한 코드는 실서비스로 바로 배포되지 않습니다. 작성한 코드는 테스트 서버로 일단 배포되서 잘 작동하는지 테스트 해봅니다.


```python
1 / 0
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-5-bc757c3fda29> in <cell line: 1>()
    ----> 1 1 / 0
    

    ZeroDivisionError: division by zero



```python
for i in range(10)
    print(i)
```


      File "<ipython-input-6-7a8a49ad5eea>", line 1
        for i in range(10)
                          ^
    SyntaxError: expected ':'




```python
# Name Error
print(x)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-7-e9e3baa318b0> in <cell line: 2>()
          1 # Name Error
    ----> 2 print(x)
    

    NameError: name 'x' is not defined



```python
# Type Error
x = 10
y = '20'
print(x + y)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-62c7d5a446c2> in <cell line: 4>()
          2 x = 10
          3 y = '20'
    ----> 4 print(x + y)
    

    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
# Index Error
my_list = [1, 2, 3]
print(my_list[3])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    <ipython-input-9-f79f21f7e49e> in <cell line: 3>()
          1 # Index Error
          2 my_list = [1, 2, 3]
    ----> 3 print(my_list[3])
    

    IndexError: list index out of range



```python
# Key Error
my_dict = {'a': 1, 'b': 2}
print(my_dict['c'])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-10-8f9ea626777a> in <cell line: 3>()
          1 # Key Error
          2 my_dict = {'a': 1, 'b': 2}
    ----> 3 print(my_dict['c'])
    

    KeyError: 'c'



```python
# Value Error
int('a')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-11-b8f9f0574b88> in <cell line: 2>()
          1 # Value Error
    ----> 2 int('a')
    

    ValueError: invalid literal for int() with base 10: 'a'



```python
# Attribute Error
my_list = [1, 2, 3]
print(my_list.appeend(4))
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-14-dceecff01ea8> in <cell line: 3>()
          1 # Attribute Error
          2 my_list = [1, 2, 3]
    ----> 3 print(my_list.appeend(4))
    

    AttributeError: 'list' object has no attribute 'appeend'



```python
# Type Error
def add(x, y):
    return x + y

add(1, 2, 3)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-15-cbb8c8b9d43a> in <cell line: 5>()
          3     return x + y
          4 
    ----> 5 add(1, 2, 3)
    

    TypeError: add() takes 2 positional arguments but 3 were given


## 예외 처리


```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
```


```python
def div(a, b):
    return a / b

try:
    div(1, 0)
except:
    print('예외 발생')
```

    예외 발생



```python
div(1, 0)
```


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-17-4267cdef819f> in <cell line: 1>()
    ----> 1 div(1, 0)
    

    <ipython-input-16-6d8b9416aa45> in div(a, b)
          1 def div(a, b):
    ----> 2     return a / b
          3 
          4 try:
          5     div(1, 0)


    ZeroDivisionError: division by zero



```python
def div(a, b):
    return a / b

def f():
    try:
        return div(1, 0)
    except:
        print('예외 발생')

result = f() + f() #result에는 float이 오길 기대하죠.
print(result)
```

    예외 발생
    예외 발생



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-19-b48a77103e02> in <cell line: 10>()
          8         print('예외 발생')
          9 
    ---> 10 result = f() + f() #result에는 float이 오길 기대하죠.
         11 print(result)


    TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'



```python
def div(a, b):
    return a / b

def f():
    try:
        return div(1, 0)
    except:
        return float('inf')

result = f() + f() #result에는 float이 오길 기대하죠.
print(result)
```

    inf



```python
def div(a, b):
    return a / b

def f():
    try:
        return div(1, 0)
    except:
        return None

result = f() + f() #result에는 float이 오길 기대하죠.
print(result)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-21-6c7844611608> in <cell line: 10>()
          8         return None
          9 
    ---> 10 result = f() + f() #result에는 float이 오길 기대하죠.
         11 print(result)


    TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'



```python
def div(a, b):
    return a / b

def f():
    try:
        return div(1, 0)
    except:
        return 0

result = f() + f() #result에는 float이 오길 기대하죠.
print(result)
```

    0



```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
else:
    # 예외가 발생하지 않을 때 실행되는 코드
```


```python
try:
    1/0
except:
    print('예외 발생!')
else:
    print('정상 종료!')
```

    예외 발생!



```python
# while, for, try-except 구문에서 else는 언제 실행?
# 정상 정료 되었을 때
```


```python
try:
    10/2
except:
    print('예외 발생!')
else:
    print('정상 종료!')
```

    정상 종료!



```python
# error가 나면 코드가 멈추기 때문에 보통 except와 함께 사용합니다.
try:
    # 예외가 발생할 가능성이 있는 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```


```python
try:
    1/0
finally:
    print('finally')

print('hello world')
```

    finally



    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-26-3c89f1d3cb5e> in <cell line: 1>()
          1 try:
    ----> 2     1/0
          3 finally:
          4     print('finally')
          5 


    ZeroDivisionError: division by zero



```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```


```python
try:
    1/0
except:
    print('hello')
finally:
    print('world')
```

    hello
    world



```python
try:
    # 예외가 발생할 가능성이 있는 코드
except:
    # 예외 처리 코드
else:
    # 예외가 발생하지 않을 때 실행되는 코드
finally:
    # 예외 발생 여부와 상관없이 항상 실행되는 코드
```


```python
try:
    1/0
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
```


```python
try:
    10/2
except:
    print('except')
else:
    print('else')
finally:
    print('finally')
```

    else
    finally



```python
raise
```


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-29-9c9a2cba73bf> in <cell line: 1>()
    ----> 1 raise
    

    RuntimeError: No active exception to reraise



```python
# raise 애러이름
raise ValueError
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-30-ea8ffc0226cd> in <cell line: 2>()
          1 # raise 애러이름
    ----> 2 raise ValueError
    

    ValueError: 



```python
raise LeeHoJun
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-31-ab25c57c1073> in <cell line: 1>()
    ----> 1 raise LeeHoJun
    

    NameError: name 'LeeHoJun' is not defined



```python
raise ValueError('코드를 잘~~ 만들어주세요.')
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-32-805fbfed3b7d> in <cell line: 1>()
    ----> 1 raise ValueError('코드를 잘~~ 만들어주세요.')
    

    ValueError: 코드를 잘~~ 만들어주세요.



```python
try:
    1/0
except ValueError:
    print('ValueError')
except ZeroDivisionError:
    print('ZeroDivisionError')

print(ZeroDivisionError)
print(type(ZeroDivisionError))
print(dir(ZeroDivisionError))
```

    ZeroDivisionError
    <class 'ZeroDivisionError'>
    <class 'type'>
    ['__cause__', '__class__', '__context__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__', '__suppress_context__', '__traceback__', 'args', 'with_traceback']



```python
class Leehojun(Exception): #Exception을 상속받으면 됩니다.
    def __init__(self):
        super().__init__('입력된 값이 leehojun이 아닙니다.')

if 'leehojun' != input():
    raise Leehojun
else:
    print('leehojun이 맞습니다!')
```

    adsf



    ---------------------------------------------------------------------------

    Leehojun                                  Traceback (most recent call last)

    <ipython-input-37-4297290162e2> in <cell line: 5>()
          4 
          5 if 'leehojun' != input():
    ----> 6     raise Leehojun
          7 else:
          8     print('leehojun이 맞습니다!')


    Leehojun: 입력된 값이 leehojun이 아닙니다.



```python
!pip list
```


```python
import sys

sys.path
```




    ['/content',
     '/env/python',
     '/usr/lib/python310.zip',
     '/usr/lib/python3.10',
     '/usr/lib/python3.10/lib-dynload',
     '',
     '/usr/local/lib/python3.10/dist-packages',
     '/usr/lib/python3/dist-packages',
     '/usr/local/lib/python3.10/dist-packages/IPython/extensions',
     '/root/.ipython']




```python
l = []
for i in [[10, 5], [20, 3], [30, 4], [40, 1]]:
    l.append(i[0] - i[1])
l
```




    [5, 17, 26, 39]




```python
l = []
for i, j in [[10, 5], [20, 3], [30, 4], [40, 1]]:
    l.append(i - j)
l
```




    [5, 17, 26, 39]




```python
l = [i - j for i, j in [[10, 5], [20, 3], [30, 4], [40, 1]]]
l
```




    [5, 17, 26, 39]




```python
l = [[10, 5], [20, 3], [30, 4], [40, 1]]
map(lambda x: x[0]-x[1], l)
```


```python
s = 0
for i in '11123':
    s += int(i)
s
```




    8




```python
[int(i) for i in '11123']
```




    [1, 1, 1, 2, 3]




```python
sum([int(i) for i in '11123'])
```




    8




```python
list(map(int, '11123'))
```




    [1, 1, 1, 2, 3]




```python
sum(map(int, '11123'))
```




    8




```python
list('11123')
```




    ['1', '1', '1', '2', '3']




```python
'!hello!wor     ld!     '.replace('!', '')
```




    'hellowor     ld     '




```python
'!hello!wor     ld!     '.replace('!', '').strip()
```




    'hellowor     ld'




```python
'!hello!wor     ld!     '.replace('!', '').replace(' ', '')
```




    'helloworld'



## 클로저, 팩토리 함수


```python
def one():
    def two():
        return
    return two

hello = one() # hello == two
```


```python
def one(x):
    def two():
        return x + x
    return two

hello = one(10) # hello == two
hello() # hello() == two()
```




    20




```python
def one(x):
    def two(a, b):
        return a + b + x
    return two

hello = one(10) # hello == two
hello(2, 3) # hello() == two()
```


```python
def user(username, usermoney):
    def userbuy(productname, productprice):
        leftmoney = usermoney - productprice
        return f'{productname}를 {username}님이 구매하셔서 계좌에 {leftmoney}가 남아있습니다.'
    return userbuy

이호준구매 = user('leehojun', 1000000)
이호준구매('자전거', 100000)

홍길동구매 = user('hongildong', 1000000)
홍길동구매('킥보드', 50000)

# 이호준구매와 홍길동구매 함수를 가지고 계좌를 조작할 수 있나요?
# 계좌 변수에 접근할 수 있나요?
```




    '킥보드를 hongildong님이 구매하셔서 계좌에 950000가 남아있습니다.'




```python
# S은행에 입사를 했습니다. 여러분들의 권한은 이호준구매 등에 구매함수만 조작할 수 있습니다
# 이렇게 되면 계좌 정보를 접근할 수가 없겠죠?
# 접근 통제, 제한, 변수 보호 등으로 사용합니다.
```
