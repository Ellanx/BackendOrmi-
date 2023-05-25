// https://www.freecodecamp.org/news/elegant-patterns-in-modern-javascript-roro-be01e7669cbd/

// 참고삼아서만 알고 있으시면 됩니다.
// RORO(Receive an object, return an object)
function mob(
    x,
    y,
    hp,
    mp,
    attack,
    depence,
    name,
    speed
) {
    console.log(x, y, hp, mp, attack, depence, name, speed)
}

mob(10, 20, 100, 200, 100, 10, 'hojun', 100)
mob(x=10, y=20, 100, 200, 100, 10, 'hojun', 100)
mob(y=10, x=20, 100, 200, 100, 10, 'hojun', 100)

// 내가 원하는 곳에 값을 주는 것이 불가합니다.
// 그렇기에 RORO기법이라는 기법이 생깁니다.

function mob({
    x: 100,
    y: 200,
    hp: 300,
    mp: 300
}) {
    console.log(x, y, hp, mp)
}

mob({x:200, y:200, hp:300, mp:400})


///////////


function mob({
    x = 100,
    y = 200,
    hp = 300,
    mp = 300
}) {
    console.log(x, y, hp, mp)
}

mob({x:200, y:200, hp:300, mp:400})


/////////////////

let one
let two
let three

{one, two, three}

let test = {one, two, three}
test


// one은 변수 => one에다가 100이라는 값을 할당한 것입니다. 
// object에 key와 value에 쌍으로 이뤄진 관계가 아닙니다. 
let {one= 100, two, three} = { two:20, three:30}