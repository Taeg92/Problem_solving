function solution(s) {
  if (s.length === 1) return 1;
  let arr = [];

  for (let i = 1; i <= parseInt(s.length / 2); i++) {
    let cnt = 1;
    let str = "";
    for (let j = 0; j < s.length; j += i) {
      const cur = s.substr(j, i);
      const nxt = s.substr(j + i, i);
      if (cur === nxt) {
        cnt++;
      } else {
        str = cnt > 1 ? str + cnt + cur : str + cur;
        cnt = 1;
      }
    }
    arr.push(str.length);
  }
  return Math.min(...arr);
}

const s = "aabbaccc";
console.log(solution(s));
