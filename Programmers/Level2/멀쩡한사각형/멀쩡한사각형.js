function gcd(w, h) {
  const rest = w % h;
  if (rest === 0) {
    return h;
  }
  return gcd(h, rest);
}

function solution(w, h) {
  return w * h - (w + h - gcd(w, h));
}

const w = 8,
  h = 12;
console.log(solution(w, h));
