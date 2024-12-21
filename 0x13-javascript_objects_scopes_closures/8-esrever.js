#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
	for (let o = list.length - 1; o >= 0; o--) {
		reversedList.push(list[o]);
		}
  return reversedList;
};
