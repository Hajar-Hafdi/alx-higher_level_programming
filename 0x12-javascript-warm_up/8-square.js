#!/usr/bin/node

const arg = process.argv[2];
const size = parseInt(arg);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  let row = '';
  for (let o = 0; o < size; o++) {
    row += 'X';
  }
  for (let k = 0; k < size; k++) {
    console.log(row);
  }
}
