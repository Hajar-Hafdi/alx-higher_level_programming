#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const ag1 = process.argv[2];
const ag2 = process.argv[3];

const int1 = parseInt(ag1);
const int2 = parseInt(ag2);

if (isNaN(int1) || isNaN(int2)) {
  console.log('NaN');
} else {
  console.log(add(int1, int2));
}
