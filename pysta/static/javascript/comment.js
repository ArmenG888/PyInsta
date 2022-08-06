function comment(id)
  {
    var comment = document.getElementById("comment_input").value;
    $.ajax({
        type:'POST',
        url : "/ajax/comment/"+id,
        data : comment,
        success: function(response){
          
        },
        error: function(response)
        {
            console.log("b");
        }
    });
  }