function solution(n) {
  const rev = (n + "")
    .split("")
    .sort((a, b) => b - a)
    .join("");
  return parseInt(rev);
}

const n = 118372;

console.log(solution(n));
