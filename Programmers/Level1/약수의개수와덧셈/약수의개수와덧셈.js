function getDivisorCnt(num) {
  const ret = [];
  for (let i = 1; i < Math.sqrt(num); i++) {
    if (!(num % i)) {
      ret.push(i);
      ret.push(num / i);
    }
  }
  if (!(num % Math.sqrt(num))) {
    ret.push(Math.sqrt(num));
  }

  return ret.length;
}

function solution(left, right) {
  let total = 0;
  for (let i = left; i <= right; i++) {
    const cnt = getDivisorCnt(i);
    cnt % 2 ? (total -= i) : (total += i);
  }
  return total;
}

const left = 13;
const right = 17;

console.log(solution(left, right));
