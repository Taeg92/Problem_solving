function solution(priorities, location) {
  let target = location;
  let answer = 1;
  let temp = 0;

  while (priorities.length > 0) {
    temp = priorities.shift();
    if (priorities.some((val) => val > temp)) {
      priorities.push(temp);
    } else {
      if (target === 0) {
        break;
      } else answer++;
    }
    if (target === 0) target = priorities.length - 1;
    else target--;
  }
  return answer;
}

const priorities = [1, 1, 9, 1, 1, 1];
const location = 0;
console.log(solution(priorities, location));
