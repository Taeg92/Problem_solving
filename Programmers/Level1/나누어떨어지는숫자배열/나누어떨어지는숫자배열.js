function solution(arr, divisor) {
  const sortedArr = arr.sort((a, b) => a - b);
  var answer = [];

  for (let i = 0; i < sortedArr.length; i++) {
    if (sortedArr[i] % divisor === 0) {
      answer.push(sortedArr[i]);
    }
  }

  return answer.length ? answer : [-1];
}

const arr = [5, 9, 7, 10];
const divisor = 5;

console.log(solution(arr, divisor));
