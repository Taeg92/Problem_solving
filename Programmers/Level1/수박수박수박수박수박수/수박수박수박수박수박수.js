function solution(n) {
  const [q, r] = [parseInt(n / 2), n % 2];

  return "수박".repeat(q) + "수".repeat(r);
}

const n = 3;

console.log(solution(n));
