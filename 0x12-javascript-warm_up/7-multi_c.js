#!/usr/bin/node

const arg = process.argv[2];
const x = parseInt(arg);

if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  let j = 0;
  while (j < x) {
    console.log('C is fun');
    j++;
  }
}
