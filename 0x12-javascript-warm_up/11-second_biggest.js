#!/usr/bin/node

const length = process.argv.slice(2).length;
// const number = parseInt(Number(process.argv[2]));
if (length === 0 || length === 1) {
  console.log('0');
} else {
  console.log('Arguments found');
}
