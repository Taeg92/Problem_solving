function solution(n) {
  return (n + "").split("").reduce((acc, cur) => acc + parseInt(cur), 0);
}

const n = 987;
console.log(solution(n));
