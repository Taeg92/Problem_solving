class Deque {
  constructor(arr) {
    this.queue = arr;
  }

  popleft = () => {
    const val = this.queue[0];
    this.queue.splice(0, 1);
    return val;
  };

  pop = () => {
    this.queue.pop();
  };

  append = (element) => {
    this.queue.push(element);
  };

  display = () => {
    console.log(this.queue);
  };

  isEmpty = () => {
    if (this.queue.length === 0) {
      return true;
    }
    return false;
  };
}

function solution(n, computers) {
  function bfs(start, computers) {
    const deque = new Deque([start]);

    while (!deque.isEmpty()) {
      const nxt = deque.popleft();

      for (let i = 0; i < computers.length; i++) {
        if (!check[i]) {
          if (computers[i][nxt]) {
            deque.append(i);
            check[i] = 1;
          }
        }
      }
    }

    return;
  }

  let answer = 0;
  const check = Array.from({ length: computers.length }, () => 0);

  for (let i = 0; i < check.length; i++) {
    if (!check[i]) {
      answer += 1;
      bfs(i, computers);
    }
  }

  return answer;
}

const n = 3;
const computers = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
];

console.log(solution(n, computers));
