$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url : "/ajax/",
            success: function(response){
              if (response.recent_messages != "none")
              {
                console.log(response.recent_messages[0].text);
              }
            },
            error: function(response)
            {
                console.log("b");
            }
        });
    },1000);
});