#!/usr/bin/node
/* Display the status code of a GET request. */
const argv = process.argv;
const request = require("request");

request(argv[2], function (error, response) {
  if (error) {
    return console.log(error);
  } else {
    console.log("code: ", response && response.statusCode);
  }
});
