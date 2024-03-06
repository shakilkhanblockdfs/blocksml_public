const fs = require('fs')

//Async File read
// fs.readFile('/Users/joe/test.txt', 'utf8' , function(err, data) => {
//   if (err) {
//     console.error(err)
//     return
//   }
//   console.log(data)

let data = "";

try {
  data = fs.readFileSync('words.txt', 'utf8')
} catch (err) {
  console.error(err)
}

console.log(typeof(data));
// data = "A";
data = data.toLowerCase();
// console.log(data);


data = data.split("\n");
let dataMap = new Map();
let value = 0;

for(let i=0; i<data.length; ++i){
  // console.log(data[i]);
  dataMap.set(data[i], value);
  value++;
}

// npm install prompt-sync
const prompt = require('prompt-sync')();
userInput = prompt("Please enter the sentence: ");
userInput = userInput.split(" ");

let sentence = "";
for(let i=0; i<userInput.length; ++i){
  // console.log(data[i]);
  sentence = sentence + '-' + dataMap.get(userInput[i]);
  value++;
}

console.log(sentence);


