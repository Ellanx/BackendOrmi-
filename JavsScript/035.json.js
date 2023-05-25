const json = '{"result":true, "count":42}';
const obj = JSON.parse(json);
console.log(obj);

const json = { "result": true, "count": 42 }
const s = JSON.stringify(json)
s