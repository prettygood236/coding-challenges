// ---
// title: Longest Increasing Subsequence (LIS)
// tags: [CodingChallenges, JavaScript, DynamicProgramming, LIS]
// # created: '2022-11-07'
// ---

// ## Problem Description

// Given an array of integers, find the length of the longest increasing subsequence (LIS). An increasing subsequence is a subsequence where all the elements are in sorted order, lowest to highest.

// ## Solution

// The solution uses dynamic programming to keep track of the longest increasing subsequences ending at each index. For each element in the array, we iterate through all previous elements and if current element is greater than any previous one and maximum length at that previous index is more than current maximum length then update current maximum length.

// Pseudocode:
// 1. Start from first index.
// 2. If current element is larger than its preceding elements, add 1.
// 3. When comparing with preceding elements and if current element is larger, add the largest LIS value among those preceding elements.

// Here's how this looks in JavaScript:

// ```javascript
const LIS = function (arr) {
  const n = arr.length;
  const lis = Array(n).fill(1);

  for (let i = 1; i < n; i++) {
    let max = 0;
    for (let j = 0; j < i; j++) {
      if (arr[j] < arr[i] && max < lis[j]) {
        max = lis[j];
      }
    }
    lis[i] += max;
  }

  return Math.max(...lis);
};

let output = LIS([3, 2]);
console.log(output); // --> 1

output = LIS([3, 10, 2, 1, 20]);
console.log(output); // --> 3

output = LIS([10, 20, '40', 25, '30', '50', 32, '70', 85]);
console.log(output); // -->7

output = LIS(['7', '2', '6', '4', '5', '1', '3']);
console.log(output); // -->3

output = LIS(['7', '2', '5', '3', '4', '9', '1', '10', '2']);
console.log(output); //-->5

output = LIS(['2', '5', '3', '7', '11', '8', '10', '13', '6']);
console.log(output); //-->6
