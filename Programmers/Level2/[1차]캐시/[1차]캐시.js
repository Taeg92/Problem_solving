function solution(cacheSize, cities) {
  let answer = 0;
  const buffer = [];

  if (cacheSize == 0) return cities.length * 5;

  for (let i = 0; i < cities.length; i++) {
    const city = cities[i].toLowerCase();
    if (buffer.includes(city)) {
      answer += 1;
      buffer.splice(buffer.indexOf(city), 1);
      buffer.push(city);
    } else {
      if (buffer.length < cacheSize) {
        buffer.push(city);
      } else {
        buffer.shift();
        buffer.push(city);
      }
      answer += 5;
    }
  }
  return answer;
}

const cacheSize = 3;
const cities = [
  "Jeju",
  "Pangyo",
  "Seoul",
  "NewYork",
  "LA",
  "Jeju",
  "Pangyo",
  "Seoul",
  "NewYork",
  "LA",
];

console.log(solution(cacheSize, cities));
