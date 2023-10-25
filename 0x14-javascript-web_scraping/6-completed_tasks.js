#!/usr/bin/node

// Import modules
const request = require('request');

// Get command arguments
const url = process.argv[2];

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const User_tasksCompleted = {};

  body.forEach((todo) => {
    if (todo.completed) {
      if (!User_tasksCompleted[todo.userId]) {
        User_tasksCompleted[todo.userId] = 1;
      } else {
        User_tasksCompleted[todo.userId] += 1;
      }
    }
  });
  console.log(User_tasksCompleted);
});
