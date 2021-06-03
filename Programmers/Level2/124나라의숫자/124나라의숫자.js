function solution(n) {
  if (n <= 3) {
    return "124"[n - 1];
  }
  const q = parseInt((n - 1) / 3);
  const r = (n - 1) % 3;
  return solution(q) + "124"[r];
}

const n = 4;
console.log(solution(n));
