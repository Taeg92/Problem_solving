function solution(board) {
  let x = board[0].length;
  let y = board.length;
  let answer = 0;

  if (x < 2 || y < 2) return 1;

  for (let i = 1; i < y; i++) {
    for (let j = 1; j < x; j++) {
      if (board[i][j] > 0) {
        const min = Math.min(
          board[i - 1][j - 1],
          board[i][j - 1],
          board[i - 1][j]
        );
        board[i][j] = min + 1;
      }
      if (answer < board[i][j]) {
        answer = board[i][j];
      }
    }
  }
  return answer * answer;
}

const board = [
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [1, 1, 1, 1],
  [0, 0, 1, 0],
];

console.log(solution(board));
