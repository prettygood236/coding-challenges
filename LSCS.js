const LSCS = function (arr) {
  //TODO: 여기에 코드를 작성합니다.
  let sum = 0
  let sumArr = []
  for (let i=0; i<arr.length; i++){
    sum = sum + arr[i]
    console.log(`sum=${sum}`)
    sumArr.push(sum)
    console.table(sumArr)
    if (sumArr[i]<0){
      sum = 0
    }
  }
  return Math.max(...sumArr)
};


// let output = LSCS([1, 2, 3]);
// console.log(output); // --> 6

// output = LSCS([1, 2, 3, -4]);
// console.log(output); // --> 6 ([1, 2, 3])


// let output = LSCS([1, 2, 3, -4, 5]);
// console.log(output); // --> 7 ([1, 2, 3, -4, 5])

// let output = LSCS([10, -11, 11]);
// console.log(output); // --> 11 ([11])

// let output = LSCS([-7, -6, -9])
// console.log(output); // --> -6 ([-6])

let output = LSCS([1, 2, 3, -6, 4, 5, 6])
console.log(output); // --> 15 ([1,2,3,-6,4,5,6])

// LSCS([1, 2, 3, -5, 4, 5, 6])
// console.log(output); // --> 16 ([1,2,3,-5,4,5,6])

// LSCS([1, 2, 3, -4, 5, -4, 5, -4, -4, -1]);
// console.log(output); // --> 8 ([1, 2, 3, -4, 5, -4, 5])
