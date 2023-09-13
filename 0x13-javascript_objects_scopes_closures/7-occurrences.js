#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let val = 0;
  for (let i = 0; i < list.length; i++) {
    val = (list[i] === searchElement ? val + 1 : val);
  }
  return val;
};
