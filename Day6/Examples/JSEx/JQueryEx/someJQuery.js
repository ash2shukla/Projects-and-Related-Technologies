// $ stands for JQuery selector
function handleResponse(response){
	console.log(response);
}

$(document).ready(function(){
	var initial = false;
	 setInterval(function(){ initial? $("p").hide(): $("p").show(); initial = !initial }, 200);
	 $.ajax({
      url: "https://jsonplaceholder.typicode.com/posts/1",
      type: "GET",
      dataType: "html",
      // data: data, data should  not be sent with GET
      success: handleResponse,
    });
});

