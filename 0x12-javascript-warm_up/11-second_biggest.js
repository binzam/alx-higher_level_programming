#!/usr/bin/node
const argumentsList = process.argv.slice(2);
const numArguments = argumentsList.length;

if (numArguments === 0 || numArguments === 1) {
  console.log(0);
} else {
  const sortedArguments = argumentsList.map(Number).sort((a, b) => b - a);
  console.log(sortedArguments[1]);
}
