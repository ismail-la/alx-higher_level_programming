#!/usr/bin/node
/* Script that prints the number of movies where the character
 */

const request = require('request');
const url = process.argv[2];
const characterId = '18';
let Character_count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(characterId)) {
          Character_count += 1;
        }
      });
    });
    console.log(Character_count);
  }
});
