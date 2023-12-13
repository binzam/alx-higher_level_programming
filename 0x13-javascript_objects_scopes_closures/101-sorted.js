#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const value in dict) {
  const key = dict[value];

  if (key in newDict) {
    newDict[key].push(value);
  } else {
    newDict[key] = [value];
  }
}
console.log(newDict);
