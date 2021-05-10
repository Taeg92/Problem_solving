function solution(numbers) {
  const numSet = new Set();
  for (let i = 0; i < numbers.length - 1; i++) {
    for (let j = i + 1; j < numbers.length; j++) {
      numSet.add(numbers[i] + numbers[j]);
    }
  }
  return [...numSet].sort((a, b) => a - b);
}

const numbers = [2, 1, 3, 4, 1];

console.log(solution(numbers));
