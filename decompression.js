const decompression = function (image) {
  // TODO: 여기에 코드를 작성합니다.
  let str = '';

  const recurForDecomp = function (str, image) {
    console.log('call decomp');
    const zero = [];
    const one = [];
    let n = image.length;
    for (let i = 0; i < n; i++) {
      zero.push(Array(n).fill(0));
      one.push(Array(n).fill(1));
    }
    switch (JSON.stringify(image)) {
      case JSON.stringify(zero):
        str += '0';
        console.log('P1', str);
        return str;
      case JSON.stringify(one):
        str += '1';
        console.log('P2', str);
        return str;
      default:
        str += 'X';
        let arr = [];
        for (let i = 0; i < image.length / 2; i++) {
          arr.push(image[i].slice(0, image.length / 2));
        }
        console.log('P3', str);
        str = recurForDecomp(str, arr);
        arr = [];
        for (let i = 0; i < image.length / 2; i++) {
          arr.push(image[i].slice(image.length / 2, image.length));
        }
        console.log('P4', str);
        str = recurForDecomp(str, arr);
        arr = [];
        for (let i = image.length / 2; i < image.length; i++) {
          arr.push(image[i].slice(0, image.length / 2));
        }
        console.log('P5', str);
        str = recurForDecomp(str, arr);
        arr = [];
        for (let i = image.length / 2; i < image.length; i++) {
          arr.push(image[i].slice(image.length / 2, image.length));
        }
        console.log('P6', str);
        str = recurForDecomp(str, arr);
    }
    console.log('P7', str);
    return str;
  };
  return recurForDecomp(str, image);
};

let image = [
  [1, 0, 1, 1],
  [0, 1, 1, 1],
  [0, 0, 1, 1],
  [0, 0, 0, 0],
];
let result = decompression(image);
console.log(result); // --> 'XX100110X1100​'

image = [
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [0, 0, 0, 0, 1, 1, 1, 0],
  [1, 1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 0, 0],
  [1, 1, 1, 1, 1, 0, 1, 1],
  [1, 1, 1, 1, 0, 1, 1, 1],
];
result = decompression(image);
console.log(result); // --> 'X0X101X10101X00X10011'

image = [
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
  [0, 1, 0, 1, 0, 1, 0, 1],
];
result = decompression(image);
console.log(result); // --> 'XXX0101X0101X0101X0101XX0101X0101X0101X0101XX0101X0101X0101X0101XX0101X0101X0101X0101'
