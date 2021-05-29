function solution(s) {
  s = s.split(" ");
  return s
    .map((str) => (str === "" ? "" : str.toLowerCase()))
    .map((str) => (str === "" ? "" : str.replace(str[0], str[0].toUpperCase())))
    .join(" ");
}

const s = "3people unFollowed me";
console.log(solution(s));
