function solution(arr) {
  const sum = arr.reduce((acc, cur) => acc + cur);
  const size = arr.length;
  return sum / size;
}

const arr = [1, 2, 3, 4];

console.log(solution(arr));
