#!/usr/bin/node

const z = Math.floor(Number(process.argv[2]));
if (isNaN(z)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < z; i++) {
    console.log('C is fun');
  }
}
