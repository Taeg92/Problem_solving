function convert(s, depth, del) {
  const length = s.length;
  const size = s.split("").filter((e) => e === "1").length;
  const delCnt = length - size;
  const bin = size.toString(2).split("");
  if (bin.length !== 1) {
    return convert(bin.join(""), depth + 1, del + delCnt);
  }
  return [depth + 1, del + delCnt];
}

function solution(s) {
  return convert(s, 0, 0);
}

const s = "110010101001";
console.log(solution(s));
