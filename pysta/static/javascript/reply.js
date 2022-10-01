function showReply(id) {
    var x = document.getElementById("replys"+id);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }