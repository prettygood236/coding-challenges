const largestRectangularArea = function (histogram) {
  // TODO: 여기에 코드를 작성합니다.# title : 'LargestRectangularAreainaHistogram2.py'

  let stack = [];
  let max_area = 0;
  let index = 0;
  let top_of_stack = 0;
  let area = 0;

  while (index < histogram.length) {
    console.log("11111111111111111")
    console.log("stack = ", stack)
    console.log("index = ", index)
    if (stack.length === 0 || histogram[stack[stack.length - 1]] <= histogram[index]) {
      console.log("22222222222222222")
      stack.push(index);
      console.log("stack = ", stack)
      index += 1;
      console.log("index = ", index)
    } else {
      console.log("33333333333333333")
      top_of_stack = stack.pop();
      console.log("top_of_stack = ", top_of_stack)
      console.log("index = ", index)
      area =
        histogram[top_of_stack] *
        (stack.length > 0 ? index - stack[stack.length - 1] - 1 : index);
      console.log("area = ", area)
      max_area = Math.max(max_area, area);
      console.log("max_area = ", max_area)
    }
  }

  while (stack.length > 0) {
    console.log("444444444444444444")
    console.log("stack = ", stack)
    top_of_stack = stack.pop();
    console.log("top_of_stack = ", top_of_stack)
    console.log("index = ", index)
    area =
      histogram[top_of_stack] *
      (stack.length > 0 ? index - stack[stack.length - 1] - 1 : index);
      console.log("area = ", area)
    max_area = Math.max(max_area, area);
    console.log("max_area = ", max_area)
  }
  return max_area;
};

// let histogram = [2, 1, 4, 5, 1, 3, 3];
// let output = largestRectangularArea(histogram);
// console.log(output); // --> 8
/*
5 |       x     
4 |     O O     
3 |     O O   x x
2 | x   O O   x x
1 | x x O O x x x
------------------
    2 1 4 5 1 3 3 
*/

let histogram = [6, 2, 5, 4, 5, 1, 6];
let output = largestRectangularArea(histogram);
console.log(output); // --> 12
// /*
// 6 | x           x
// 5 | x   x   x   x
// 4 | x   O O O   x
// 3 | x   O O O   x
// 2 | x x O O O   x
// 1 | x x O O O x x
// ------------------
// */
