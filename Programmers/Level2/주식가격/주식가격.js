function solution(prices) {
  const answer = new Array(prices.length).fill(0);

  for (let i = 0, len = prices.length - 1; i < len; i++) {
    answer[i] = 1;
    if (prices[i] <= prices[i + 1]) {
      for (let j = i + 1; j < len; j++) {
        if (prices[i] > prices[j]) break;
        else answer[i] += 1;
      }
    }
  }
  return answer;
}

const prices = [1, 2, 3, 2, 3];
console.log(solution(prices));
