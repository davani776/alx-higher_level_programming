#!/usr/bin/node
const args = process.argv;
if (args.length <=3) {
  console.log('0');
} else {
  let second = parseInt(args[2]);
  let high = parseInt(args[3]);
  for (let i = 2; i < args.length; i++) {
    const current = parseInt(args[1]);
    if (current > high) {
      second = high;
      high = current;
    } else if (current > second && current < high) {
      second = current;
    }
  }
  console.log(second);
}
