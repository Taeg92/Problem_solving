function solution(n) {
  const numList = [0, 1];
  for (let i = 2; i <= n; i++) {
    numList.push((numList[i - 1] + numList[i - 2]) % 1234567);
  }
  return numList[n];
}

n = 5;
console.log(solution(n));
