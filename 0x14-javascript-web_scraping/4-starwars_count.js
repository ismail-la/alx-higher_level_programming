#!/usr/bin/node
// Script that prints the number of movies
const request = require('request');
const url = process.argv[2];
const charId = '18';
let Count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
