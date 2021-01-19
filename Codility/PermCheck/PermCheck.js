function solution(A) {
  // write your code in JavaScript (Node.js 8.9.4)
  const maxVal = Math.max.apply(null, A);
  const set = new Set(A);
  if (maxVal !== A.length || set.size !== A.length) {
    return 0;
  }
  return 1;
}

const A = [4, 1, 3];
const B = [4, 1, 3, 2];

console.log(solution(A), solution(B));
