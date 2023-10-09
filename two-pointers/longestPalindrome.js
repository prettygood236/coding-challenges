// ---
// title: Longest Palindrome
// tags: [CodingChallenges, JavaScript, TwoPointers, Palindrome]
// created: '2022-07-11'
// ---

// ## Problem Description

// A palindrome is a word, number, phrase, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization). Write a function that finds the longest palindromic substring in a given string.

// ## Solution

// This problem can be solved using two pointers approach. The idea is to expand around each character and find longest palindrome. We keep track of maximum length palindrome seen so far.

// ```javascript
function longestPalindrome(str) {
  let n = str.length; // calculating size of string
  if (n < 2) return n; // if string is empty then size will be 0.
  // if n==1 then, answer will be 1(single
  // character will always palindrome)

  let maxLength = 1,
    start = 0;
  let low, high;
  for (let i = 0; i < n; i++) {
    low = i - 1;
    high = i + 1;
    while (
      high < n &&
      str[high] == str[i] //increment 'high'
    )
      high++;

    while (
      low >= 0 &&
      str[low] == str[i] // decrement 'low'
    )
      low--;

    while (low >= 0 && high < n && str[low] == str[high]) {
      low--;
      high++;
    }

    let length = high - low - 1;
    if (maxLength < length) {
      maxLength = length;
      start = low + 1;
    }
  }

  return maxLength;
}
let str = 'My dad is a racecar athlete';
let result = longestPalindrome(str);
console.log(result); // --> 11 ('a racecar a')

str = ' dad ';
result = longestPalindrome(str);
console.log(result); // --> 5 (' dad ')
