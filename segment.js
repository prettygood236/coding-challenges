let N = 100000;

let n; // array size

// Max size of tree
let tree = new Array(2 * N);
tree.fill(0);

// function to build the tree
function build(arr) {
  // insert leaf nodes in tree
  for (let i = 0; i < n; i++) tree[n + i] = arr[i];

  // build the tree by calculating
  // parents
  for (let i = n - 1; i > 0; --i) tree[i] = tree[i << 1] + tree[(i << 1) | 1];
}

// function to get sum on
// interval [l, r)
function query(l, r) {
  let res = 0;

  // loop to find the sum in the range
  for (l += n, r += n; l < r; l >>= 1, r >>= 1) {
    if ((l & 1) > 0) res += tree[l++];

    if ((r & 1) > 0) res += tree[--r];
  }

  return res;
}

let a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12];

// n is global
n = a.length;

// build tree
build(a);

console.log(a);

// print the sum in range(1,2)
// index-based
console.log(a.length);

console.log(query(11, 12));
