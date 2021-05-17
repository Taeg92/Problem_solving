function solution(a, b) {
  const day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];
  const date = new Date(`2016,${a},${b}`);
  return day[date.getDay()];
}

const a = 5;
const b = 24;
console.log(solution(a, b));
