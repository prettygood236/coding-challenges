const spiralTraversal = function (matrix) {
  // TODO: 여기에 코드를 작성합니다.
  let result = [];
  let charNum = matrix.length * matrix[0].length
  function solve(matrix, result){
    console.log("call solve")
    let m = matrix.length
    let n = matrix[0].length || 1
    for (let j=0; j<n; j++){
      result.push(matrix[0][j])
      if (result.length === charNum){
        return result.join('')
      }
      // console.log(`j=${j}`)
      console.log("1")
      console.log(result)
    }
    for (let i=1; i<m; i++){
      result.push(matrix[i][n-1])
      if (result.length === charNum){
        return result.join('')
      }
      console.log("2")
      console.log(result)
    }
    for (let j=n-2; j>=0; j--){
      result.push(matrix[m-1][j])
      if (result.length === charNum){
        return result.join('')
      }
      console.log("3")
      console.log(result)
    }
    for (let i=m-2; i>0; i--){
      result.push(matrix[i][0])
      if (result.length === charNum){
        return result.join('')
      }
      console.log("4")
      console.log(result)
    }
  let newMatrix = [];
  for (let i = 1; i<matrix.length-1; i++){
    newMatrix.push(matrix[i].slice(1,matrix[0].length-1));
  }
  console.log("newMatrix")
  console.log(newMatrix);
  return solve(newMatrix, result)
  }
  return solve(matrix, result)
};

const matrix = [
  ['I', "'", 'm', ' ', 'a', ' ', 's', 'l'],
  ['t', ' ', 'I', ' ', 'n', 'e', 'v', 'o'],
  ['u', ' ', 'b', 'a', 'c', 'k', 'e', 'w'],
  ['b', 'k', 'l', 'a', 'w', ' ', 'r', ' '],
  [' ', ',', 'r', 'e', 'k', 'l', 'a', 'w'],
];
let output = spiralTraversal(matrix);
console.log(output); // --> "I'm a slow walker, but I never walk back"
