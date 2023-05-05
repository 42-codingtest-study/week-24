//문제: 4779
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const arr = ["-", "- -"];
  for (let j = 1; j <= 12; j++) {
    let str = arr[j];
    for (let i = 0; i < arr[j].length; i++) {
      str += " ";
    }
    str += arr[j];
    arr.push(str);
  }
  console.log(arr);

  // input.forEach((e) => {
  //   console.log(arr[+e].length);
  // });
}
