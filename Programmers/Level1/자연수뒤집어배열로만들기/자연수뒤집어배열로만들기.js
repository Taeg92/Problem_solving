function solution(n) {
  return (n + "")
    .split("")
    .reverse()
    .map((e) => parseInt(e));
}

const n = 12345;

console.log(solution(n));
