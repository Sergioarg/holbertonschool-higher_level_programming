#!/usr/bin/node
const request = require("request");
const argv = process.argv;
const url = argv[2];
const dict = {};

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const json_body = JSON.parse(body);

    for (const tasks of json_body) {
      if (tasks.completed) {
        if (dict[tasks.userId]) {
          dict[tasks.userId]++;
        } else {
          dict[tasks.userId] = 1;
        }
      }
    }
    console.log(dict);
  }
});
