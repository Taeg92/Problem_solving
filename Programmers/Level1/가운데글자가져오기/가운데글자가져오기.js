function solution(s) {
  return s.length % 2
    ? s.substr(s.length / 2, 1)
    : s.substr(s.length / 2 - 1, 2);
}

const s = "qwer";

console.log(solution(s));
