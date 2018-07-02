// $ stands for JQuery selector
function handleResponse(response){
	console.log(response);
}

$(document).ready(function(){
	var initial = false;
	 setInterval(function(){ initial? $("p").hide(): $("p").show(); initial = !initial }, 200);
	 $.ajax({
      url: "http://api.jquery.com/jquery.ajax/",
      type: "GET",
      dataType: "html",
      // data: data, data should  not be sent with GET
      success: handleResponse,
    });
});

