var slider_content = document.getElementById('box');
var image = ['img1','img2'];

var i = image.length;


// function for next slide 

function nextImage(){
  if (i<image.length) {
      i= i+1;
  }else{
      i = 1;
  }
    slider_content.innerHTML = "<img src="+image[i+1]+"img2.jpg>";
}


// function for prev slide

function prevImage(){

  if (i<image.length+1 && i>1) {
      i= i-1;
  }else{
      i = image.length;
  }
    slider_content.innerHTML = "<img src="+image[i-1]+".jpg>";

}

setInterval(nextImage , 4000);
