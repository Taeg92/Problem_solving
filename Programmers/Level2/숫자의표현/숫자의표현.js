function solution(n) {
  let answer = 0;
  for (let i = 1; i <= num; i++) {
    if (n % i == 0 && i % 2 == 1) answer++;
  }
  return answer;
}

const n = 15;
console.log(solution(n));
