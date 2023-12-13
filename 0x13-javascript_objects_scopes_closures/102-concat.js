#!/usr/bin/node
const fs = require("fs");

const fileA = fs.readFileSync(process.argv[2]).toString();
const fileB = fs.readFileSync(process.argv[3]).toString();
const fileC = process.argv[4];

fs.writeFileSync(fileC, fileA + fileB);
