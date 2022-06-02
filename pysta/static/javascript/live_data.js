$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url : "{% url 'live_data' %}",
            success: function(response){
                console.log(response);
            },
            error: function(response)
            {
                console.log("b");
            }
        });
    },1000);
});
