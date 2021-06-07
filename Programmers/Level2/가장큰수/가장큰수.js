function solution(numbers) {
  const maxNum = numbers
    .map((ele) => ele + "")
    .sort((a, b) => b + a - (a + b))
    .join("");
  return maxNum[0] === "0" ? "0" : maxNum;
}

const numbers = [6, 10, 2];
console.log(solution(numbers));
