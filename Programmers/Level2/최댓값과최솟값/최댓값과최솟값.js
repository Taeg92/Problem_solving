function solution(s) {
  const numList = s.split(" ").map((ele) => Number(ele));
  const maxVal = Math.max.apply(null, numList);
  const minVal = Math.min.apply(null, numList);
  return `${minVal} ${maxVal}`;
}

const s = "-1 -2 -3 -4";
console.log(solution(s));
