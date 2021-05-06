function solution(n, m) {
  let gcd = 0;
  let lcm = 0;
  for (let i = 1; i <= n; i++) {
    if (!(n % i) && !(m % i)) {
      gcd = i;
    }
  }

  if (gcd === 1) {
    lcm = n * m;
  } else {
    lcm = gcd * parseInt(n / gcd) * parseInt(m / gcd);
  }
  return [gcd, lcm];
}

const [n, m] = [2, 5];

console.log(solution(n, m));
