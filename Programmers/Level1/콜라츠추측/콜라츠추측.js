function solution(num) {
  let cnt = 0;

  while (true) {
    if (cnt >= 500) {
      return -1;
    } else if (num === 1) {
      return cnt;
    } else if (num % 2) {
      num = num * 3 + 1;
    } else {
      num = parseInt(num / 2);
    }
    cnt += 1;
  }
}

const num = 6;

console.log(solution(num));
