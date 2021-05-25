function solution(s) {
  const numList = s
    .replace("{{", "")
    .replace("}}", "")
    .split("},{")
    .sort((a, b) => {
      return b.length - a.length;
    });
  return numList.reduce((acc, cur) => {
    cur = cur.split(",").map((ele) => Number(ele));
    return [...new Set([...cur, ...acc])];
  }, []);
}

const s = "{{4,2,3},{3},{2,3,4,1},{2,3}}";

console.log(solution(s));
