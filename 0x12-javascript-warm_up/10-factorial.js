#!/usr/bin/node
function factorial (number) {
  if (isNaN(number) || !number || number <= 0) {
    return (1);
  }
  return (number * factorial(number - 1));
}
const argv = parseInt(process.argv[2]);

console.log(factorial(argv[2]));
