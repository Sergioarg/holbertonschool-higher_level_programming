#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonBody = (JSON.parse(body));
    let count = 0;
    for (const i of jsonBody.results) {
      for (const j of i.characters) {
        if (j.search(18) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
