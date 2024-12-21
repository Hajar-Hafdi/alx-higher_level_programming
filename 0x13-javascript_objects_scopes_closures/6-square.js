#!/usr/bin/node
const BaseSquare = require('./5-square');

class Square extends BaseSquare {
  charPrint (c = 'X') {
	  for (let o = 0; o < this.height; o++) {
		  console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
