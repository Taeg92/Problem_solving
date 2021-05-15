function solution(n, lost, reserve) {
  var lostArr = lost.filter((e) => !reserve.includes(e));
  var reserveArr = reserve.filter((e) => !lost.includes(e));

  return (
    n -
    lostArr.filter((e) => {
      const student = reserveArr.find((ele) => Math.abs(ele - e) <= 1);
      if (!student) return true;
      reserveArr = reserveArr.filter((e) => e !== student);
    }).length
  );
}

const n = 5;
const lost = [2, 4];
const reserve = [1, 3, 5];

console.log(solution(n, lost, reserve));
