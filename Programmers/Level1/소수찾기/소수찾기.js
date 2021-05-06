function solution(n) {
  let answer = Array(n + 1).fill(1);

  for (let i = 2; i * i < n; i++) {
    if (answer[i]) {
      for (let j = 2; j * i <= n; j++) {
        answer[i * j] = 0;
      }
    }
  }
  answer.shift();

  let total = answer.reduce((acc, cur) => acc + cur);

  return total - 1;
}

const n = 10;
console.log(solution(n));
