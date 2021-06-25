function solution(skill, skill_trees) {
  const order = skill.split("");
  let count = 0;
  for (let i = 0; i < skill_trees.length; i++) {
    const mySkill = skill_trees[i]
      .split("")
      .filter((ele) => order.includes(ele))
      .join("");
    if (mySkill === skill.substring(0, mySkill.length)) {
      count++;
    }
  }
  return count;
}

const skill = "CBD";
const skill_trees = ["BACDE", "CBADF", "AECB", "BDA"];
console.log(solution(skill, skill_trees));
