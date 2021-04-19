function solution(x, n) {
  return Array.from({ length: n }, (v, i) => (i + 1) * x);
}

const x = 2;
const n = 5;

console.log(solution(x, n));
