#!/usr/bin/node
function factorial (number) {
  if (number <= 0 || isNaN(number) || !number) {
    return (1);
  }
  return (number * factorial(number - 1));
}
const argv = parseInt(process.argv[2]);

console.log(factorial(argv[2]));
