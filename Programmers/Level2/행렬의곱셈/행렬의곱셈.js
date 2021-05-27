function solution(arr1, arr2) {
  return Array(arr1.length)
    .fill(0)
    .map((ele, i) =>
      Array(arr2[0].length)
        .fill(0)
        .map((e, j) =>
          arr1[i].reduce((acc, cur, k) => acc + cur * arr2[k][j], 0)
        )
    );
}

const arr1 = [
    [1, 4],
    [3, 2],
    [4, 1],
  ],
  arr2 = [
    [3, 3],
    [3, 3],
  ];

console.log(solution(arr1, arr2));
