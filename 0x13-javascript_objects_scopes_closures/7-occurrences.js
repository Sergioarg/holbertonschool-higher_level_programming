#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const value in list) {
    if (list[value] === searchElement) {
      count++;
    }
  }
  return (count);
};
