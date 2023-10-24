#!/usr/bin/node
/* Script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name by line
You must use the Star wars API
You must use the module request
*/

const request = require('request');
const movie_Id = process.argv[2];
const url = `https://swapi.dev/api/films/${movie_Id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const characters = data.characters;
  for (const character of characters) {
    request(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const character_Data = JSON.parse(body);
      console.log(character_Data.name);
    });
  }
});
