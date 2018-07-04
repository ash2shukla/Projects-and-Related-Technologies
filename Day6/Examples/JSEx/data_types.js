/*
There are three types of Numbers
*/

// 1. Integers
var int_num = 1;
console.log(typeof(int_num));

// 2. floats
var float_num = 1.1;
console.log(typeof(float_num));

// 3. special -> nan, inf
console.log(Math.sqrt(-1));
console.log(10/0);
console.log(-10/0);

/*
The strings can be declared using double or single quotes
Their important methods are - slice, substr, split, replace, match, search, indexOf
*/
var string = "I am a string";
console.log("The length of string is", string.length);
console.log("Slice->", string.slice(0,5));
console.log("Substr->", string.substr(0,5)); 
console.log("Split->", string.split(' '));
var regex = '[a-zA-Z ]+';
console.log("Match->", string.match(regex));
console.log("Search-> Provides index of the match only", string.search(regex));
console.log("indexOf->", string.indexOf('T'));

/*
Booleans like in any other language are true and false
mind that unlike python both are lower case
*/

/* undefined is not null
undefined means variable has not been defined yet only declared
whereas null means that the variable has been defined but has no value
*/
var x;
console.log(x);
x = null;
console.log(x);

/*
Although not a data type but arrays is extremely 
useful data structures to know they are just like lists 
*/

var a = [1, 2, 3];
console.log(typeof(a));

/* Arrays are mutable */

a[1] = 'JS';
console.log(a);

/* We can push and pop in arrays */
a.push(1);
console.log('After push', a);
console.log('The popped element is', a.pop());

/* Splice method adds and removes methods from an array and returns them */
a.splice(1, 3, "Element1", "Element2");

/* Array.splice(from_index, how_many, new_items_to_add) */
console.log(a);

