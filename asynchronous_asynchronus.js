function task1(a, b, callback) {
  setTimeout(() => {
    const res = a + b;
    callback(res)
  }, 3000)
}

function task2(n, callback) {
  setTimeout(() => {
    const res = n * 2;
    callback(res)
  }, 2000)
}

function task3(n, callback) {
  setTimeout(() => {
    const res = n - 2;
    callback(res)
  }, 1000)
}

task1(6, 2, (a_res) => {
  console.log("1 RESULT : ", a_res);
  task2(a_res, (b_res) => {
    console.log("2 RESULT : ", b_res);
    task3(b_res, (c_res) => {
      console.log("3 RESULT : ", c_res)
    })
  })
})

console.log("START")