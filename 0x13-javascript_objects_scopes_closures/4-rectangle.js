#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';

    for (let i = 0; i < this.height; i++) {
      for (let i = 0; i < this.width; i++) {
        str += 'X';
      }

      if (i !== this.height - 1) {
        str += '\n';
      }
    }
    if (str !== '') {
      console.log(str);
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    [this.width, this.height] = [this.width * 2, this.height * 2];
  }
}

module.exports = Rectangle;
