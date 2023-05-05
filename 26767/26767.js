//문제: 26767
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  for (let i = 0; i < +input[0]; i++) {
    if (i % 77 === 0) console.log("Cheers!");
    else if (i % 7 === 0) console.log("Hurra!");
    else if (i % 11 === 0) console.log("Super!");
    else console.log(i);
  }
}
