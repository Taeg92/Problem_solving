function isValid(arr) {
  const pair = { "}": "{", "]": "[", ")": "(" };
  const stack = [];
  for (let i = 0; i < arr.length; i++) {
    const chr = arr[i];
    if (pair[chr] === undefined) stack.push(chr);
    else {
      if (stack[stack.length - 1] !== pair[chr]) return false;
      stack.pop();
    }
  }
  if (stack.length) return false;
  return true;
}

function solution(s) {
  const arr = s.split("");
  let result = 0;
  for (let i = 0; i < s.length; i++) {
    if (isValid(arr)) result++;
    arr.push(arr.shift());
  }

  return result;
}

const s = "[](){}";
console.log(solution(s));
