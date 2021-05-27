function solution(n) {
  return n
    .toString(2)
    .split("")
    .filter((ele) => ele === "1").length;
}

const n = 5000;
console.log(solution(n));
