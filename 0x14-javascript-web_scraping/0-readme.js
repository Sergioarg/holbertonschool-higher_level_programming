#!/usr/bin/node
/* Reads and prints the content of a file. */

const argc = process.argv;
const fs = require("fs");

fs.readFile(argc[2], "utf-8", function (error, output) {
  if (error) {
    console.log(error);
  } else {
    console.log(output);
  }
});
