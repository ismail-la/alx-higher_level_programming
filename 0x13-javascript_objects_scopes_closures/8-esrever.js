#!/usr/bin/node
exports.esrever = function (list) {
  const reversed_List = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed_List.push(list[i]);
  }

  return (reversed_List);
};
