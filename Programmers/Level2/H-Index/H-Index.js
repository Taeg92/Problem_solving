function solution(citations) {
  const maxVal = Math.max.apply(null, citations);

  for (let i = maxVal; i >= 0; i--) {
    let cnt = 0;
    for (let j = 0; j < citations.length; j++) {
      if (citations[j] >= i) {
        cnt += 1;
      }
      if (cnt === i) return i;
    }
  }
  return 0;
}

const citations = [3, 0, 6, 1, 5];
console.log(solution(citations));
