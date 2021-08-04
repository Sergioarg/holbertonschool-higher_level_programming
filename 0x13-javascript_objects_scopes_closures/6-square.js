#!/usr/bin/node
const parentSquare = require('./5-square');

class Square extends parentSquare {
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      for (let i = 0; i < this.with; i++) {
        console.log(c.repeat(this.with));
      }
    }
  }
}

module.exports = Square;
