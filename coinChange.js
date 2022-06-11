// const coinChange = function (S, m, n){

//   // table[i]는 값 i에 대한 솔루션의 수를 저장
//   // 상향식(bottom-up)으로 구성되므로 n+1개의 행이 필요
//   let table = Array(n+1).fill(0)

//   // Base case (주어진 값이 0인 경우)
//   table[0] = 1;

//   // 모든 코인을 하나씩 선택하고 선택된 코인의 값보다 크거나 같은 인덱스 뒤에 table[] 값을 업데이트
//   for(let i = 0; i < m; i++) {
//     // console.log("i : ", i)
//     for(let j = S[i]; j <= n; j++){
//       // console.log("j : ", j)
//       table[j] += table[j - S[i]];
//       // console.log(table);
//       // console.log(table[j - S[i]]);
//     }
//   }
//   return table[n];
// }


const coinChange = function (S, m, n) {
  // memo[i][j]는 i만큼의 금액을 S[j]부터 ~ S[m - 1]까지 사용하여 만들 수 있는 경우의 수를 저장
  const memo = [];
  for (let i = 0; i < n + 1; i++) memo.push(Array(m).fill(-1));

  const makeChageFrom = (left, idx) => {

    // 0을 만드는 방법은 1가지이다. 아니면 목표 금액을 만들었다고 생각해도 된다.
    if (left === 0) return 1;
    // 금액이 마이너스가 되는 경우는 불가능하므로 0을 리턴
    if (left < 0) return 0;
    // 동전을 전부 검토해서, 남아있는 새로운 동전은 없는데 목표 금액을 만들지 못한 경우 (실패)
    if (idx >= m && left > 0) return 0;
    // 이미 해결한 적이 있는 문제는 다시 풀지 않는다.
    if (memo[left][idx] !== -1) return memo[left][idx];

    // left만큼의 금액을 S[idx]부터 사용하여 만들 수 있는 경우의 수는
    //  1) S[idx]는 그만 사용하고, 다음 동전으로 넘어가거나 (목표 금액은 그대로이고, idx가 증가한다.)
    //  2)) S[idx]를 한번 더 사용한다. S[idx]를 또 사용할 수 있으므로, idx는 그대로이고, 목표 금액은 S[i]만큼 줄어든다.
    memo[left][idx] =
      makeChageFrom(left, idx + 1) + makeChageFrom(left - S[idx], idx);
    return memo[left][idx];
  };
  return makeChageFrom(n, 0);
};

// const n = 10;
// const S = [6, 5, 3, 2];
// output = coinChange(S, S.length, n);
// console.log(output); // -> 5


const n = 256;
const S = [100, 5, 1, 50, 10, 500];
output = coinChange(S, S.length, n);
console.log(output); // -> 2104