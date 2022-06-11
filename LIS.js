// const LIS = function (arr) {
//   //TODO: 여기에 코드를 작성합니다.
//   const n = arr.length;
//   const lis = Array(n).fill(1);

//   for (let i = 1; i < n; i++) {
//     // console.log('i = ', i);
//     for (let j = 0; j < i; j++) {
//       // console.log('j = ', j);
//       // console.log('arr = ', arr);
//       // console.log('lis = ', lis);
//       // console.log(`arr[${i}] = `, arr[i], `arr[${j}] = `, arr[j]);
//       // console.log(`lis[${i}] = `, lis[i], `lis[${j}] + 1 = `, lis[j] + 1);
//       if (arr[i] > arr[j] && lis[i] < lis[j] + 1) {
//         lis[i] = lis[j] + 1;
//         // console.log('lis = ', lis);
//       }
//     }
//   }
//   let maximum = 0;
//   for (let i = 0; i < n; i++) {
//     maximum = Math.max(maximum, lis[i]);
//     // if (isMaxChange !== maximum) {
//     //   result.push(arr[i - 1]);
//     //   isMaxChange = maximum;
//     // }
//   }

//   // result.push(arr[lis.lastIndexOf(maximum)]);
//   console.log('lis = ', lis);
//   return maximum;
// };


/* 수도코드 

1. 1번째 인덱스부터 시작, 앞에것들보다 크면 1을 더한다. 
2. 앞에것들과 비교하며 더크면 앞에것들중 가장 큰 원소의 lis 값을 더해준다.

*/

const LIS = function (arr) {
  const n = arr.length
  const lis = Array(n).fill(1)

  for (let i=1; i<n; i++){
    let max = 0
    for (let j=0; j<i; j++){
      if(arr[j] < arr[i] && max < lis[j]){
        max = lis[j]
      }
    }
    lis[i] += max
  }
  return Math.max(...lis)
}

let output = LIS([3, 2]);
console.log(output); // --> 1 (3 or 2)

 output = LIS([3, 10, 2, 1, 20]); //[1, 2, 1, 1, 3]
console.log(output); // --> 3 (3, 10, 20)

 output = LIS([10, 20, 40, 25, 30, 50, 32, 70, 85]); //[1, 2, 3, 3, 4, 5, 5, 6, 7]
console.log(output); // --> 7

 output = LIS([7, 2, 6, 4, 5, 1, 3]); 
console.log(output); // --> 3

 output = LIS([7, 2, 5, 3, 4, 9, 1, 10, 2]);
console.log(output); // --> 5

 output = LIS([2, 5, 3, 7, 11, 8, 10, 13, 6]);
console.log(output); // --> 6



