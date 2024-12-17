#!/usr/bin/node

function callMeMoby (x, theFunction) {
  for (let o = 0; o < x; o++) {
    theFunction();
  }
}

module.exports.callMeMoby = callMeMoby;
