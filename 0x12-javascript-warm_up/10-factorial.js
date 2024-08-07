#!/usr/bin/node
let fact = parseInt(process.argv[2]);
if (isNaN(fact)) {
  fact = 1;
}
function factorial (n) {
  if (n === 0) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
console.log(factorial(fact));
