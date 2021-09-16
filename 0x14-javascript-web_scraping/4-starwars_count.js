#!/usr/bin/node
/* Wedge Antilles is character ID 18 */

const request = require('request');
const argv = process.argv;
const url = argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {

    const json_body = (JSON.parse(body));
    let count = 0;
    for (const i of json_body.results) {
        for (const j of i.characters) {
            if (j.search(18) > 0) {
                count++;
            }
        }
    }
    console.log(count);
  }
});
