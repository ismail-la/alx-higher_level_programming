#!/usr/bin/node

const dict = require('./101-data.js').dict;

const new_Dict = {};
Object.getOwnPropertyNames(dict).forEach(occurences => {
  if (new_Dict[dict[occurences]] === undefined) {
    new_Dict[dict[occurences]] = [occurences];
  } else {
    new_Dict[dict[occurences]].push(occurences);
  }
});

console.log(new_Dict);
