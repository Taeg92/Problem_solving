function getScore(answers, pattern) {
  const score = [0, 0, 0];
  let maxScore = 0;
  for (let i = 0; i < answers.length; i++) {
    for (let j = 0; j < 3; j++) {
      if (pattern[j][i % pattern[j].length] === answers[i]) {
        score[j] += 1;
        if (score[j] > maxScore) {
          maxScore = score[j];
        }
      }
    }
  }
  return {
    score,
    maxScore,
  };
}

function solution(answers) {
  const answer = [];
  const pattern = {
    0: [1, 2, 3, 4, 5],
    1: [2, 1, 2, 3, 2, 4, 2, 5],
    2: [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  };

  const { score, maxScore } = getScore(answers, pattern);

  for (let i = 0; i < score.length; i++) {
    if (score[i] === maxScore) {
      answer.push(i + 1);
    }
  }

  return answer;
}

const answers = [1, 3, 2, 4, 2];
console.log(solution(answers));
