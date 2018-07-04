var title = document.title;
var href = window.location.href;
var userAgent = window.navigator.userAgent;
console.log(title);
console.log(href);
console.log(userAgent);

window.alert('Some Useless alert');
var reply = confirm('Yes no?');

console.log('Simple Log');
console.error('Error Log');
console.info('Information log');
console.warn('Warning Log');

var img = document.getElementById("asd");
// getElementById
// getElementByClassName
console.log(img);

// getAttribute
// setAttribute
// innerHTML

img.setAttribute('src', 'data:image/png;base64, iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg==');
console.log(paragraphs[0].getAttribute('style'));
