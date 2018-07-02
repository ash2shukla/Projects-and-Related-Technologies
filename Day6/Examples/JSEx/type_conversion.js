// to Number
console.log(Number("10"));         // a => 10
console.log(Number(false));        // b =>  0
console.log(parseInt("10", 10));   // c => 10
console.log(parseInt(10.2));       // d => 10
console.log(parseFloat("10.2"));   // e => 10.2


// to String
console.log(String(false));        // a => "false"
console.log(String(10));           // b => "10"
console.log(String(10.2));         // c => "10.2"
console.log((10).toString());      // d => "10"

// to Boolean
console.log(Boolean(10));          // a => true
console.log(Boolean(0));           // b => false
console.log(Boolean(0.3));         // c => true
console.log(Boolean("true"));      // d => true
console.log(Boolean(""));
console.log(Boolean(undefined));