function solution(d, budget) {
    const sortedArr = d.sort((a, b) => a - b);
    let answer = 0;
    for (let i = 0; i < sortedArr.length; i++) {
        budget -= sortedArr[i];
        if (budget < 0) {
            return answer;
        }
        answer += 1;
    }
    return answer;
}

const d = [1, 3, 2, 5, 4];
const budget = 9;

console.log(solution(d, budget));
