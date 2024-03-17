#!/usr/bin/node

exports.nbOccurences = function nbOccurences (list, searchElement) {
  let count = 0;

  for (const ele of list) {
    if (ele === searchElement) {
      count++;
    }
  }
  return count;
};
