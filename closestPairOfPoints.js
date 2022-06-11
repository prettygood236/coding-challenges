// // 좌표평면 위의 두 점 사이의 거리를 계산하는 함수입니다.
function calculateDistance(p1, p2) {
  const yDiff = p2[0] - p1[0];
  const xDiff = p2[1] - p1[1];
  return Math.round(100 * Math.sqrt(Math.pow(yDiff, 2) + Math.pow(xDiff, 2)));
}

const closestPairOfPoints = function (points) {
  // TODO: 여기에 코드를 작성합니다.
  const getCombinations = function (arr, selectNumber) {
    const results = [];
    if (selectNumber === 1) return arr.map((el) => [el]);

    arr.forEach((fixed, index, origin) => {
      const rest = origin.slice(index + 1);
      const combinations = getCombinations(rest, selectNumber - 1);
      const attached = combinations.map((el) => [fixed, ...el]);
      results.push(...attached);
    });
    return results
  }
  const combinations = getCombinations(points, 2)

  const result = combinations.map(value => {
    return calculateDistance(value[0], value[1])
  })
  const min = Math.min(...result)
  return result
};
// let points = [
//   [0, 0],
//   [1, 3],
//   [2, 2],
// ];
// let output = closestPairOfPoints(points);
// console.log(output); // --> 141 ([1, 3], [2, 2])
/*
3 |  x
2 |     x
1 |       
0 | x 
------------
    0 1 2 3 
*/

// let points = [
//   [0, 0],
//   [0, 1],
//   [0, 3],
//   [0, 5],
// ];
// output = closestPairOfPoints(points);
// console.log(output); // --> 100 ([0, 0], [0, 1])
/*
5 | x
4 | 
3 | x
2 |     
1 | x     
0 | x 
------------
    0 1 2 3 
*/

// const points = [
//   [0, 2],
//   [6, 67],
//   [42, 81],
//   [39, 101],
//   [189, 140],
// ];
// output = closestPairOfPoints(points);
// console.log(output); // --> 2022

// const points = [
//   [0, 100],
//   [3, 4],
//   [58, 34],
//   [22, 65],
//   [121, 132],
//   [140, 153],
// ];
// output = closestPairOfPoints(points);
// console.log(output); // --> 2832

const points = Array(2).fill(1)
for (let i = 0; i < 300; i++) {
  points.push(Array(i).fill(1));
}
output = closestPairOfPoints(points);
console.log(output);