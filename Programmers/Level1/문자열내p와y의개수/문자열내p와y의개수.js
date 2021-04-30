function solution(s) {
  const count = [0, 0];

  for (let i = 0; i < s.length; i++) {
    if (s[i].toUpperCase() === "P") {
      count[0] += 1;
    } else if (s[i].toUpperCase() === "Y") {
      count[1] += 1;
    }
  }
  return count[0] === count[1] ? true : false;
}

const s = "pPoooyY";

console.log(solution(s));
