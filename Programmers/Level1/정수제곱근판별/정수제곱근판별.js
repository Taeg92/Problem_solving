function solution(n) {
  const sqrtVal = Math.sqrt(n);
  if (sqrtVal % 1) {
    return -1;
  }
  return Math.pow(sqrtVal + 1, 2);
}

const n = 121;

console.log(solution(n));
