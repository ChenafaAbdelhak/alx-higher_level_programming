#!/usr/bin/node
const args = process.argv.slice(2);
let asInt = parseInt(args[0], 10);
let str = '';

if (isNaN(asInt)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < asInt; i++) {
    for (let i = 0; i < asInt; i++) {
      str += 'X'
    }
    if (i != asInt - 1) {
      str += '\n';
    }
  }
  if (str != '') {
    console.log(str);
  }
}
