#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const File_Path = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(File_Path, body, 'utf8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
