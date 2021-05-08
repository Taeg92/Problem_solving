function solution(strings, n) {
  const answer = strings.sort((a, b) => {
    if (a[n] < b[n]) {
      return -1;
    } else if (a[n] > b[n]) {
      return 1;
    } else {
      if (a < b) {
        return -1;
      } else if (a > b) {
        return 1;
      }
      return 0;
    }
  });
  return answer;
}

const strings = ["sun", "bed", "car"];
const n = 1;

console.log(solution(strings, n));
