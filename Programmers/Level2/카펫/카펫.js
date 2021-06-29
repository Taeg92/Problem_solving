function solution(brown, red) {
  const total = brown + red;

  for (let i = Math.floor(total / 2); i > 0; i--) {
    if (total % i !== 0) continue;

    const width = i;
    const height = total / i;

    if ((width - 2) * (height - 2) === red) {
      return [width, height];
    }
  }
}

const brown = 24;
const yellow = 24;

console.log(solution(brown, yellow));
