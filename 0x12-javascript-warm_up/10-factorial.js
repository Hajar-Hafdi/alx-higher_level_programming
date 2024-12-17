#!/usr/bin/node

function factorial (v) {
  if (isNaN(v) || v <= 1) {
    return 1;
  }
  return v * factorial(v - 1);
}

const ag = process.argv[2];
const ber = parseInt(ag);

console.log(factorial(ber));
