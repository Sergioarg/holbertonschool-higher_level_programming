#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
const request = require('request');
const url = argv[2]; const filePath = argv[3];

request(url, function (error, response, body) {
  if (error) {
    return console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function error (err) {
      if (err) {
        return console.log(err);
      }
    });
  }
});
