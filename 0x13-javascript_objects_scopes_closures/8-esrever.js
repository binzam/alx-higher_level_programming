#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  const len = list.length - 1;
  for (let i = len; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return reversedList;
};
