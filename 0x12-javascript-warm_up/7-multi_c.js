#!/usr/bin/node
const args = process.argv.slice(2);
let asInt = parseInt(args[0], 10);

if (isNaN(asInt)) {
  console.log('Missing number of occurences');
} else {
  while (asInt > 0) {
    console.log('C is fun');
    asInt--;
  }
}
