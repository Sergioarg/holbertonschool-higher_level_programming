#!/usr/bin/node
const request = require('request');
const argv = process.argv;
const id = argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
