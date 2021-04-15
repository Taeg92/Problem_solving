function solution(arr) {
  const minVal = Math.min.apply(null, arr);
  const minIdx = arr.indexOf(minVal);
  arr.splice(minIdx, 1);
  return arr.length === 0 ? [-1] : arr;
}

const arr = [10];

console.log(solution(arr));
