#!/usr/bin/node
const number = parseInt(Number(process.argv[2]));
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My nomber: ${number}`);
}
