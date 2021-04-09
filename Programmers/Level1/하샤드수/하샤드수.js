function solution(x) {
  const total = (x + "").split("").reduce((acc, cur) => parseInt(cur) + acc, 0);
  return x % total ? false : true;
}

const x = 10;

console.log(solution(x));
