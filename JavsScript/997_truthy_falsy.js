// python => 대부분이 class로 되어 있죠?
// javascript => class가 ES6부터 나온 문법입니다. 원래 있던 문법이 아닙니다! 그 전에는 생성자 함수로 사용했었습니다!


let myArr = new Array(1, 2, 3); // python에서 마치 클래스로 인스턴스를 만들어내듯 찍어내는 겁니다.


let myArr = new Array(1,2,3);
let myArr2 = new Array(4,5,6);

myArr2.length
myArr.length

myArr.forEach(item=>{
    console.log(item);
})

myArr2.forEach(item => {
    console.log(item);
})

function Factory(){}
function NewFactory(name){
    this.name = name;
    this.sayYourName = function(){
        console.log(`삐리비리. 제 이름은 ${this.name}입니다. 주인님.`);
    }
}

let robot1 = new Factory();
let robot2 = new NewFactory('브랜든');