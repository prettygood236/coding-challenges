function solve(board) {
  // TODO: 여기에 코드를 작성합니다.
  console.log('call solve');
  // 다 해결됐다면 현재 보드를 리턴
  if (solved(board)) {
    console.log('solved - finish');
    console.log('board');
    console.log(board);
    return board;
  } else {
    // 빈 자리 한 곳에 숫자 1..9를 각각 채운 9개의 보드를 담는다.
    const possibilities = nextBoards(board);
    // 그 중 가로,세로,박스 중복 검사로 유효한 보드만 남긴다.
    const validBoards = keepOnlyValid(possibilities);
    //
    return searchForSolution(validBoards);
  }
}
// 해결이 안되었다면 백트래킹
function searchForSolution(boards) {
  console.log('call searchForSolution');
  console.log('boards');
  console.log(boards);
  // 빈 자리에 1..9를 모두 채워봤음에도 유효한 보드가 없다면 해결이 불가능한 보드임으로 false를 반환한다.
  if (boards.length < 1) {
    console.log('this board is not valid');
    return false;
  } else {
    let first = boards.shift();
    console.log('first');
    console.log(first);
    // 각 빈자리마다 1..9를 채우고 유효한 보드만 남긴다.
    const tryPath = solve(first);
    //    console.log("tryPath")
    //    console.log(tryPath)
    if (tryPath != false) {
      console.log('tryPath');
      console.log(tryPath);
      return tryPath;
      // 빈 자리를 채워가다 유효하지 않게 되면 (백트래킹 해야 할 시점) solve(first)는 false를 반환하고,
      // 더 이상 유효하지 않은 보드를 제외한 나머지(shift된 board)로 다시 탐색을 시작한다.
    } else {
      return searchForSolution(boards);
    }
  }
}
// 해결된(모든 칸이 채워진) 스도쿠인지 검사
function solved(board) {
  console.log('call solved');
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] == 0) {
        return false;
      }
    }
  }
  return true;
}
// 첫 번째 빈 자리를 찾고 해당 자리를 숫자 1...9로 채우는 9개의 다른 보드를 생성
function nextBoards(board) {
  console.log('call nextBoards');
  let res = [];
  const firstEmpty = findEmptySquare(board);
  //    console.log("firstEmpty")
  //    console.log(firstEmpty)
  if (firstEmpty != undefined) {
    const y = firstEmpty[0];
    const x = firstEmpty[1];
    for (let i = 1; i <= 9; i++) {
      let newBoard = [...board];
      let row = [...newBoard[y]]; // 찾은 빈 자리가 있는 행
      //    console.log("row")
      //    console.log(row)
      row[x] = i; // 빈 자리(row[x])에 1..9를 넣어보기
      //    console.log("row[x]")
      //    console.log(row[x])
      newBoard[y] = row; // 빈 자리에 1..9를 넣은 행을 다시 보드에 넣기
      //    console.log("newBoard[y]")
      //    console.log(newBoard[y])
      res.push(newBoard); // 빈 자리에 1..9를 넣은 행을 넣은 보드를 res에 다시 담기. (3차원 배열)
      //    console.log("res")
      //    console.log(res)
    }
  }
  //    console.log("res")
  //    console.log(res)
  return res;
}
// 첫 번째 빈 자리에 대한 i(y) j(x) 좌표 가져오기)
function findEmptySquare(board) {
  console.log('call findEmptySquare');
  for (let i = 0; i < 9; i++) {
    for (let j = 0; j < 9; j++) {
      if (board[i][j] == 0) {
        return [i, j];
      }
    }
  }
}
// 목록에서 유효한 보드만 담고 잘못된 보드를 모두 필터링.
function keepOnlyValid(boards) {
  console.log('call keepOnlyValid');
  let res = [];
  for (let i = 0; i < boards.length; i++) {
    //    console.log("boards[i]")
    //    console.log(boards[i])
    if (validBoard(boards[i])) {
      res.push(boards[i]);
      //    console.log("res")
      //    console.log(res)
    }
  }
  //    console.log("res")
  //    console.log(res)
  return res;
}
// 주어진 보드가 유효한지 확인
function validBoard(board) {
  console.log('call validBoard');
  return rowsCheck(board) && columnsCheck(board) && boxesCheck(board);
}
// 각 행(가로줄)에 반복되는 숫자가 없는지 검사
function rowsCheck(board) {
  for (let i = 0; i < 9; i++) {
    let cur = [];
    for (let j = 0; j < 9; j++) {
      if (cur.includes(board[i][j])) {
        return false;
      } else if (board[i][j] != 0) {
        cur.push(board[i][j]);
      }
    }
  }
  return true;
}
// 각 열(세로줄)에 반복되는 숫자가 없는지 검사
function columnsCheck(board) {
  for (let i = 0; i < 9; i++) {
    let cur = [];
    for (let j = 0; j < 9; j++) {
      if (cur.includes(board[j][i])) {
        return false;
      } else if (board[j][i] != 0) {
        cur.push(board[j][i]);
      }
    }
  }
  return true;
}
// 각 박스(3x3)에 반복되는 숫자가 없는지 검사
function boxesCheck(board) {
  const boxCoordinates = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2],
  ];
  for (let y = 0; y < 9; y += 3) {
    for (let x = 0; x < 9; x += 3) {
      // 순회는 각 상자를 검사해야 한다.
      let cur = [];
      for (let i = 0; i < 9; i++) {
        let coordinates = [...boxCoordinates[i]];
        coordinates[0] += y;
        coordinates[1] += x;
        if (cur.includes(board[coordinates[0]][coordinates[1]])) {
          return false;
        } else if (board[coordinates[0]][coordinates[1]] != 0) {
          cur.push(board[coordinates[0]][coordinates[1]]);
        }
      }
    }
  }
  return true;
}
// let board = [
//   [0, 3, 0, 2, 6, 0, 7, 0, 1],
//   [6, 8, 0, 0, 7, 0, 0, 9, 0],
//   [1, 9, 0, 0, 0, 4, 5, 0, 0],
//   [8, 2, 0, 1, 0, 0, 0, 4, 0],
//   [0, 0, 4, 6, 0, 2, 9, 0, 0],
//   [0, 5, 0, 0, 0, 3, 0, 2, 8],
//   [0, 0, 9, 3, 0, 0, 0, 7, 4],
//   [0, 4, 0, 0, 5, 0, 0, 3, 6],
//   [7, 0, 3, 0, 1, 8, 0, 0, 0],
// ];

let board = [
  [4, 3, 5, 2, 6, 9, 7, 8, 1],
  [6, 8, 2, 5, 7, 1, 4, 9, 3],
  [1, 9, 7, 8, 3, 4, 5, 6, 2],
  [8, 2, 6, 1, 9, 5, 3, 4, 7],
  [3, 7, 4, 6, 8, 2, 9, 1, 5],
  [9, 5, 0, 0, 0, 0, 0, 2, 8],
  [5, 1, 9, 3, 2, 6, 8, 7, 4],
  [2, 4, 8, 9, 5, 7, 1, 3, 6],
  [7, 6, 3, 4, 1, 8, 2, 5, 9],
];
let output = solve(board);
console.log(output);
