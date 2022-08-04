function like(user_id, follow_id)
{
    $.ajax({
        type:'GET',
        url : "/ajax/follow/"+user_id+"/"+follow_id,
        success: function(response){
          //console.log("startsIn{{ race.id }}");
          //document.getElementById("likes"+id).innerText = response['likes'] + " likes";
          
          
        },
        error: function(response)
        {
            console.log("b");
        }
    });
}