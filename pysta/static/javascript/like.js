function like(id)
  {
    $.ajax({
        type:'GET',
        url : "/ajax/"+id,
        success: function(response){
          //console.log("startsIn{{ race.id }}");
          document.getElementById("likes"+id).innerText = response['likes'] + " likes";
          if (response['liked'] == true)
          {
            document.getElementById("like"+id).src = "/static/images/heart-red.png";
          }
          else{
            document.getElementById("like"+id).src = "/static/images/heart-"+response['theme']+".png";
          }
          
        },
        error: function(response)
        {
            console.log("b");
        }
    });
  }