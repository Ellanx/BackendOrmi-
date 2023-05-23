// 파이썬과의 차이점
// key값에 따옴표가 없을 경우 자동으로 문자열로 변환해줍니다. 
// true, false 값은 앞에 대소문자가 다릅닏나. 

let obj = {
    id : 'licat',
    pw: '1234',
    name : 'leelele',
    email : 'aaaa@gmail.co.kr',
    active:false                                                                                
}

obj['id']
obj.id
// obj.'id' 이건 error

// value의 값으로 문자열 외에 다른 값을 넣었을 경우
let test = {
    one: sum,
    two: console.log,
    three: window.innerWidth,
    four: [10, 20, 30],
    five: "10",
    six: 100,
}
console.log(test)
test.two("호준!!")


let user = {
    id: 'licat',
    pw: '1234',
    name: 'leehojun',
    email: 'hojun@gmail.co.kr',
    active: false
}
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));