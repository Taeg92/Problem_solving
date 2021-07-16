function solution(number, k) {
  let answer = "";
  const stack = [];

  for (let i = 0; i < number.length; i++) {
    const n = number[i];
    while (k > 0 && stack[stack.length - 1] < n) {
      stack.pop();
      k--;
    }
    stack.push(n);
  }
  stack.splice(stack.length - k, k);
  answer = stack.join("");
  return answer;
}

const number = "1924";
const k = 2;

console.log(solution(number, k));
