/*
LEARNING JAVA SCRIPT

lessoon (lol garlic) from freecodecamp.org
url: https://youtu.be/PkZNo7MFNFg
coded on codepen.io
*/


"use strict"; // sets compiler to strictly check for incorrect/bad code

console.log('Beginning Javascript self-study'); // in-line comment, console.log in JS == print() in python
/* 
1. Statements should end with ';'

*/

var pogchamp = 'DJT'; // var can be used and changed throughout the program
let poggers = 'DJTJ'; // let can only be used and changed in the current scope
const poggina = 'Ivanka'; // constant can never be changed after being declared

console.log(pogchamp);
pogchamp = 'maga';
console.log(pogchamp);

var donald; // unlike python, even if I don't assign a var I must declare it id I want to use it

console.log(poggers.length); // find length of string with just the length attribute of a string

var astring = "boom boom";
//astring[0] = 'c'; // results in error
console.log(astring); // strings are immutable in JS unlike Python, cannot change an indivudual character, need to alter the whole string again
astring = 'coom boom';
console.log(astring);
console.log(astring[astring.length-1]);


/* Functions */
function get_len(arg1){
  return arg1.length;
}

/* Arrays */
var arr = [1,2,3,'shark', 'pog'];
console.log(get_len(arr));
arr[0] = 'Donald Trump is our lord and savior, QAnon is love QAnon is life, muh freedums, hilary\'s emails'; // Unlike strings, arrays are mutable
console.log(arr);
arr[2] = [1,2,3,'arrayception'];
console.log(arr[2][3]);
console.log(arr);
// Python list append == JS array push, adds an element at the end
// arr.pop() will remove an alement from the end
// arr.shift() will remove an element from the front
// arr.unshift() will add an element at the front

// What is Math library in JS
// What is JSON.stringify?

/* if else statement */
function check_condition(x){
  if (x >= 10){
    return "value greater than or equal to 10";
  } else if (x >= 5){
    return "value greater than/equal to 5 and less than 10";
  }
  return "value less than 5";
}
// Equal to is checked as ===

console.log(check_condition(2));
console.log(check_condition(7));
console.log(check_condition(15));



// JS has switch case statements unlike python
// break in JS == break in python



/* Var object with properties 
   This is like struct in c++,
   Like a dict in python
*/
function checkprop(prop, obj){
  if (obj.hasOwnProperty(prop)){
    return obj[prop];
  } else {
    console.log("object does not have this property");
  }
}


var myself = {
  "first_name": "Deborshi",
  "last_name": "Goswami",
  "age": 25
}

console.log(checkprop("age", myself));
console.log(myself.first_name);
console.log(myself['last_name']);
delete myself.age; // delete an object property /
checkprop("age", myself);
  


/* while loops */
var arr = [];
var i = 0;
while(i < 10){
  arr.push(i);
  i++;
}
console.log(arr);



/* for loop */
var arr = [];
for(var i = 5; i < 15; i ++){
  arr.push(i);
}
console.log(arr);

for(var i=0; i < arr.length; i++){
  arr[i] += 7;
}
console.log(arr);


// do while loop exists and is similar to most other languages

console.log(5 * parseInt("6")); // convert string to integer using parseInt


// try - catch in JS == try - except in python
try{
  console.log("can do this");
} catch ( ex ){
  console.log(ex);
}

// to prevent object from mutation, use: Object.freeze(object_name);


// Anonymous functions
var anon = (arg1) => arg1 * 2;
console.log (anon(2));

// concatenate one array on another
var conc = (a1, a2) => a1.concat(a2);// use array.concat()
console.log (conc([0,1],[2,3]));



/* Map, Filter*/
arr = [1,-1,2,-2,3.5,-6.7,9.6];

// Filter and Map
// Filter elements in an array based on a condition
// Map elements to new value based on a calculation
console.log(arr.filter(element => Number.isInteger(element) && element > 0 ).map(element => element * element));


// Use spread operator to copy contents of one array to another
var arr2 = [...arr];
arr = []
console.log(arr)
console.log(arr2)

/*
  Template Listerals: https://youtu.be/PkZNo7MFNFg?t=11200
  At 3:10:15, instructor explains how to print html code dynamically using the output of JS scripts
  This is fundamentally important for development (I believe)
*/

// Instantiate a new object given an object constructor function using new
// If we are using class then simply declare the function as 'constructor'

class admin{
  constructor(name){
    this.name = name + ' administration';
  }
  get admin_name() {
    return this.name;
  }
  get admin_date() {
    return this.date;
  }
  set admin_date(date){
    this.data = date;
  }
}
console.log(new admin('Biden'));

var new_admin = new admin('Cortez');
console.log(new_admin.admin_name);
new_admin.date = 2024;
console.log(new_admin.date);

/*
  import, export, require: https://youtu.be/PkZNo7MFNFg?t=12026
*/
