function solution(a, b) {
  const size = a.length;
  let answer = 0;
  for (let i = 0; i < size; i++) {
    console.log(a[i], b[i]);
    answer += a[i] * b[i];
  }
  return answer;
}

const a = [1, 2, 3, 4];
const b = [-3, -1, 0, 2];

console.log(solution(a, b));
