$( document ).ready(function() {
    console.log("jquery ready");

    $("#button1").click(function (){
        alert("the next image you click will be an example of a new  class");
        $.ajax({url: "/setstatus/newlabel", success: function(result){    
        }});
    });

    $("#button2").click(function(){
        $.ajax({url: "/setstatus/reset", success: function(result){}});
    });   
});