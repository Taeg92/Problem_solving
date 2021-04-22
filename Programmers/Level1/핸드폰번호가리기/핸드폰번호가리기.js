function solution(phone_number) {
  const size = phone_number.length;
  return "*".repeat(size - 4) + phone_number.slice(-4);
}

const phone_number = "01033334444";

console.log(solution(phone_number));
