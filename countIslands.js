// const countIslands = function (grid) {
//   // TODO: 여기에 코드를 작성합니다.
//   // 빈 배열을 입력받은 경우, 0을 리턴한다.
//   if (grid.flat().length == 0) return 0;
//   // n은 가로(x) m은 세로(y) 이다.
//   const m = grid.length;
//   const n = grid[0].length;
//   // 이동할 네 가지 방향을 정의한다. (위쪽(0), 오른쪽(1), 아래쪽(2), 왼쪽(3) 순)
//   const dy = [-1, 0, 1, 0];
//   const dx = [0, 1, 0, -1];
//   let count = 1;
//   let result = 0;

//   // BFS를 구현할 큐를 만들고 왼쪽 맨 위에서 출발한다.
//   const queue = [];
//   queue.push([0, 0]);

//   // grid를 직접 바꾸어 답을 도출할 것이므로 값을 다루기 편한 숫자형으로 바꾸어준다.
//   grid = grid.map((el) => el.map((el) => (el == '0' ? -1 : 0)));
//   // 0,0이 땅이라면 1을 미리 할당해준다.
//   grid[0][0] = grid[0][0] == 0 ? 1 : -1;

//   // BFS를 수행한다. (큐가 바닥날 때까지 수행하면 된다.)
//   while (queue.length) {
//     // 반복할 떄 마다 큐에서 원소를 꺼내고,
//     console.log('queue : ', queue);
//     const [y, x] = queue.shift();
//     console.log('y : ', y, ' x : ', x);
//     // 현재 위치에서 4가지 방향으로 한번씩 방문한다.
//     for (let i = 0; i < 4; i++) {
//       // 방문기록을 남기는 것은 필수이다!
//       while (true) {
//         let ny = y + dy[i];
//         let nx = x + dx[i];
//         console.log('ny : ', ny, ' nx : ', nx);
//         // 다음 땅이 공간을 벗어난 경우 이 반복을 탈출한다.
//         if (nx < 0 || nx >= n || ny < 0 || ny >= m) break;
//         // 다음 땅이 연결되어 있으나 이전 땅보다 큰 값이라면 다시 초기화 해준다.
//         if (grid[ny][nx] > 0 && grid[y][x] > 0) {
//           grid[ny][nx] = Math.min(grid[ny][nx], grid[y][x]);
//           count = grid[ny][nx] + 1;
//         }
//         // 다음 땅이 이미 방문한적 있다면 이 반복을 탈출한다.
//         if (grid[ny][nx] > 0 || grid[ny][nx] == -2) break;
//         // 다음 땅이 물이라면 방문체크를 하고 다음 땅으로 가기위해 큐에 좌표만 넣어주고 이 반복을 탈출한다.
//         if (grid[ny][nx] == -1) {
//           grid[ny][nx] = -2;
//           queue.push([ny, nx]);
//           break;
//         }
//         // 다음 땅이 땅이고 땅에서 땅으로 이동하면 섬의 개수는 동일한 것이다.
//         if (grid[ny][nx] == 0 && grid[y][x] > 0) {
//           grid[ny][nx] = grid[y][x];
//         }
//         // 다음 땅이 땅이고 땅에서 물에서 땅으로 이동했을 때만 섬의 개수를 세어준다.
//         if (grid[ny][nx] == 0 && grid[y][x] < 0) {
//           grid[ny][nx] = count;
//           count += 1;
//         }
//         console.log(grid);
//         console.log(Math.max(...grid.flat()));
//         // 방문 노드의 좌표를 큐에 넣는다.
//         queue.push([ny, nx]);
//       }
//     }
//   }
//   result = Math.max(...grid.flat());
//   return result;
// };

const countIslands = function (grid) {
  // dfs solution
  const HEIGHT = grid.length;
  const WIDTH = HEIGHT && grid[0].length;
  let count = 0;

  for (let row = 0; row < HEIGHT; row++) {
    for (let col = 0; col < WIDTH; col++) {
      if (grid[row][col] === '0') continue;
      count++;
      searchIsland(row, col);
    }
  }

  function searchIsland(row, col) {
    if (row < 0 || col < 0 || row >= HEIGHT || col >= WIDTH) return;
    if (grid[row][col] === '0') return;

    grid[row][col] = '0';
    searchIsland(row - 1, col);
    searchIsland(row + 1, col);
    searchIsland(row, col - 1);
    searchIsland(row, col + 1);
  }

  return count;
};

let grid = [
  ['0', '1', '0', '1', '0', '1'],
  ['1', '0', '1', '0', '1', '0'],
  ['0', '1', '0', '1', '0', '1'],
  ['1', '0', '1', '0', '1', '0'],
  ['0', '1', '0', '1', '0', '1'],
];
result = countIslands(grid);
console.log(result); // --> 15
