#!/usr/bin/node
const args = process.argv[2];
if (args === undefined || isNaN(parseInt(args))) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < args) {
    let row = '';
    let j = 0;
    while (j < args) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
