#!/usr/bin/node
/* Script that reads and prints the content of a file
The first argument is the file path
The content of the file must be read in utf-8
If an error occurred during the reading, print the error object
*/

// Include built in module
const fs = require('fs');

// Get first argument
const file_name = process.argv[2];

// Read file
fs.readFile(filePath, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
