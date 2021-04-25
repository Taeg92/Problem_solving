function solution(s) {
  const size = s.length;
  return (size === 4 || size === 6) && s.split("").every((ele) => !isNaN(ele))
    ? true
    : false;
}

const s = "1234";

console.log(solution(s));
