const robotPath2 = function (room, src, sDir, dst, dDir) {
  const n = room[0].length;
  const m = room.length;
  const dx = [0, 0, 1, 0, -1];
  const dy = [0, -1, 0, 1, 0];
  let result = 0;

  room = room.map(el => el.map(el => el==1?-1:el));

  const queue = [];
  queue.push([src[0], src[1], sDir]);

  while (queue.length) {
    const [y,x,dir] = queue.shift()

    if (y === dst[0] && x === dst[1]) {
      result = room[y][x] + (Math.abs(dir-dDir)===3 ? 1 : Math.abs(dir-dDir))
      break;
    }

    for (let i = 1; i < 5; i++) {
      let k = 0;
      while (true) {
        k += 1;
        let ny = y + k * dy[i];
        let nx = x + k * dx[i];
        console.log('k =',k,'ny =', ny, 'nx =', nx)
        if (nx < 0 || nx >= n || ny < 0 || ny >= m)
          break;
        if (room[ny][nx] !== 0 ||  (ny === src[0] && nx === src[1])) break;

        room[ny][nx] = room[y][x] + (Math.abs(dir-i)===3 ? 1 : Math.abs(dir-i)) + 1;
        queue.push([ny, nx, i]);
        console.group(["이해 안되는 곳"])
        console.log(room)
        console.log(queue)
        console.groupEnd()
      }
    }
  }
  console.log(room)
  return result;
}; 


const room = [
  [0, 0, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1, 0, 1],
  [0, 0, 1, 0, 0, 0, 1],
  [0, 0, 1, 0, 1, 1, 1],
  [0, 0, 1, 0, 1, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
];
const src = [0, 4];
const sDir = 1;
const dst = [7, 2];
const dDir = 2;
let output = robotPath2(room, src, sDir, dst, dDir);
console.log(output) // --> 9
