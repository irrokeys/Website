function myFunction() {
    var x = document.getElementById("links");
    if (x.classList.contains('animation')) {

     
      x.classList.remove('animation');
      console.log('hey');
    } else {
      x.classList.add('animation');
      
    }
  }

function close_menu () {
  document.getElementById('links').classList.remove('animation');
}

