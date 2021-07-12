function solution(record) {
  let answer = [];
  const table = {};
  for (let i = 0; i < record.length; i++) {
    const [state, uid, name] = record[i].split(" ");
    if (state == "Leave") {
      answer.push([uid, "님이 나갔습니다."]);
      continue;
    }
    if (state == "Enter") {
      answer.push([uid, "님이 들어왔습니다."]);
    }
    table[uid] = name;
  }
  return answer.map((ele) => table[ele[0]] + ele[1]);
}

const record = [
  "Enter uid1234 Muzi",
  "Enter uid4567 Prodo",
  "Leave uid1234",
  "Enter uid1234 Prodo",
  "Change uid4567 Ryan",
];

console.log(solution(record));
