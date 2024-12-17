#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  let firstMax = -Infinity;
  let secondMax = -Infinity;

  for (const ber of numbers) {
    if (ber > firstMax) {
      secondMax = firstMax;
      firstMax = ber;
    } else if (ber > secondMax && ber < firstMax) {
      secondMax = ber;
    }
  }

  console.log(secondMax);
}
