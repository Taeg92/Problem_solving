function solution(n) {
  const reversed3Base = n.toString(3).split("").reverse().join("");
  return parseInt(reversed3Base, 3);
}

const n = 45;

console.log(solution(n));
