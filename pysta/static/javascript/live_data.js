$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            type:'GET',
            url : "/ajax/",
            success: function(response){
              if (response.recent_messages != "none")
              {
                console.log(response.recent_messages[0])
                var x = document.getElementById("snackbar");
                x.className = "show";
                x.innerHTML = response.recent_messages[0].text;
                setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
              }
            },
            error: function(response)
            {
                console.log("b");
            }
        });
    },1000);
});