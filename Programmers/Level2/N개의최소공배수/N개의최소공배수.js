function lcs(a, b) {
  if (!(a % b)) return b;
  return lcs(b, a % b);
}

function solution(arr) {
  let answer = 1;
  for (let i = 0; i < arr.length; i++) {
    answer = parseInt((answer * arr[i]) / lcs(answer, arr[i]));
  }
  return answer;
}

const arr = [2, 6, 8, 14];
console.log(solution(arr));
