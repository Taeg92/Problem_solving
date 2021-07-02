function solution(people, limit) {
  let answer = 0;
  people = people.sort((a, b) => b - a);

  for (let i = 0, j = people.length - 1; i <= j; i++, answer++)
    if (people[i] + people[j] <= limit) j--;

  return answer;
}

const people = [70, 50, 80, 50];
const limit = 100;
console.log(solution(people, limit));
