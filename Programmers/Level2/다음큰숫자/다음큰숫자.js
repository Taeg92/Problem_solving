function solution(n) {
  let answer = n + 1;
  const bin = n.toString(2);
  const cnt = bin.split("").filter((ele) => ele === "1").length;
  while (true) {
    if (
      cnt ===
      answer
        .toString(2)
        .split("")
        .filter((e) => e === "1").length
    ) {
      return answer;
    }
    answer += 1;
    if (answer > 1000000) return -1;
  }
}

const n = 78;
console.log(solution(n));
