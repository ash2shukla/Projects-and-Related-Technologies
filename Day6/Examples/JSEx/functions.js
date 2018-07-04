function someother_function(one, two ) {
	console.log('The first argument was ',one);
	console.log(two('hello'));
}

someother_function(1, function (var1) {console.log(var1);});