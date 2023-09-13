#!/usr/bin/node

exports.converter = function (base) {
  function Converter (num) {
    return num.toString(base);
  }
  return Converter;
};
