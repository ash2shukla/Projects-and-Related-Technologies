var title = document.title;
var href = window.location.href;
var userAgent = window.navigator.userAgent;
console.log(title);
console.log(href);
console.log(userAgent);

window.alert('Some Useless alert');
var reply = confirm('Yes no?');
console.log(reply);
var value = prompt('Give some value?');
console.log(value);

console.log('Simple Log');
console.error('Error Log');
console.info('Information log');
console.warn('Warning Log');

var paragraphs = document.getElementsByTagName("p");
// getElementById
// getElementByClassName
console.log(paragraphs);

// getAttribute
// setAttribute
// innerHTML
paragraphs[0].innerHTML = 'Changed Content';

paragraphs[0].setAttribute('style', 'font-size:20px');
console.log(paragraphs[0].getAttribute('style'));
