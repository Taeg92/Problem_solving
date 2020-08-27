function solution(array, commands) {
    const answer = [];
    for (let k=0; k<commands.length; k++) {
        const [l1, l2, l3] = commands[k];
        let myArr = array.slice(l1-1, l2);
        for (let i=0; i< myArr.length; i++) {
            for (let j=i; j<myArr.length; j++) {
                if (myArr[i] > myArr[j]) {
                    var num = myArr[i];
                    myArr[i] = myArr[j];
                    myArr[j] = num;
                }
            }
        }
        answer.push(myArr[l3-1]);
    }
    return answer
}

const array = [1, 5, 2, 6, 3, 7, 4];
const commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]];

console.log(solution(array, commands));