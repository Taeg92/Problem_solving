function solution(s) {
  const wordList = s.split(" ").map((word) => {
    return word
      .split("")
      .map((chr, idx) => {
        return idx % 2 ? chr.toLowerCase() : chr.toUpperCase();
      })
      .join("");
  });

  return wordList.join(" ");
}

const s = "try hello world";

console.log(solution(s));
