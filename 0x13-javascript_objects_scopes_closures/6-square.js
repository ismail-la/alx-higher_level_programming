#!/usr/bin/node
/**
 * Class Square that defines a square and inherits from Square of 5-square.js:
 *    You must use the class notation for defining your class and extends
 *    Create an instance method called charPrint(c) that prints the rectangle using the character c
 *    If c is undefined, use the character X
 */

const SquarePrev = require('./5-square');

class Square extends SquarePrev {
  charPrint (c) {
    const Char = c === undefined ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      let Var = '';
      let y = 0;
      while (y < this.width) {
        Var += Char;
        y++;
      }

      console.log(Var);
    }
  }
}

module.exports = Square;
