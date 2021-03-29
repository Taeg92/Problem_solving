function dfs(start, val, numbers, target) {
  let cnt = 0;

  if (start === numbers.length) {
    if (val === target) {
      return 1;
    }
  } else {
    cnt += dfs(start + 1, val + numbers[start], numbers, target);
    cnt += dfs(start + 1, val - numbers[start], numbers, target);
  }

  return cnt;
}

function solution(numbers, target) {
  const answer = dfs(0, 0, numbers, target);
  return answer;
}

const numbers = [1, 1, 1, 1, 1];
const target = 3;

console.log(solution(numbers, target));
