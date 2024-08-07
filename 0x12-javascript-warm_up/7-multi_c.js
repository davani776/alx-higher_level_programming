#!/usr/bin/node
let arg = process.argv[2];
let i = 0; 
if (arg === undefined || isNaN(parseInt(arg))) {
	console.log('Missing number of occurrences');
}
else {
	while (i < arg) {
		console.log('C is fun');
		i++;
	}
}
