#!/usr/bin/node
const args = process.argv.slice(2);
const asInt = parseInt(args[0], 10);

if (!isNaN(asInt)) {
  console.log(`My number: ${asInt}`);
} else {
  console.log('Not a number');
}
