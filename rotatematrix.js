const rotateMatrix = function (matrix, k = 1) {
  // TODO: 여기에 코드를 작성합니다.
  k %= 4;
  if (matrix.length === 0 || k === 0) {
    return matrix;
  }
  let m = matrix.length;
  let n = matrix[0].length;
  const rmatrix = [];
  for (let row = 0; row < n; row++) {
    rmatrix.push(Array(m).fill(0));
  }
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      rmatrix[j][m - 1 - i] = matrix[i][j];
    }
  }
  return rotateMatrix(rmatrix, k - 1);
};