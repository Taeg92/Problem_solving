function division(p) {
  const cnt = [0, 0];
  for (let i = 0; i < p.length; i++) {
    if (p[i] === "(") {
      cnt[0] += 1;
    } else {
      cnt[1] += 1;
    }
    if (cnt[0] == cnt[1]) return [p.slice(0, i + 1), p.slice(i + 1)];
  }
}

function isRight(p) {
  const stack = [];
  for (let i = 0; i < p.length; i++) {
    if (p[i] === "(") {
      stack.push(p[i]);
    } else {
      if (stack.length) {
        stack.pop();
      } else {
        return false;
      }
    }
  }
  return true;
}

function solution(p) {
  if (!p.length) return "";

  const [u, v] = division(p);

  if (isRight(u)) {
    return u + solution(v);
  } else {
    let answer = "(";
    answer += solution(v);
    answer += ")";

    for (let i = 1; i < u.length - 1; i++) {
      if (u[i] === "(") {
        answer += ")";
      } else {
        answer += "(";
      }
    }
    return answer;
  }
}

const p = "(()())()";
console.log(solution(p));
