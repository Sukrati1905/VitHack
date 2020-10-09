var image=null;
var canvas=null;

//Upload image
function uploadImage(){
  var file=document.getElementById("finput");
  canvas=document.getElementById("can");
  image=new SimpleImage(file);
  image.drawTo(canvas);
}

//Apply Rainbow Filter
function applyRainbow(){
  notLoaded();
  var rainbowImage=new SimpleImage(image);
  for(var pixel of rainbowImage.values()){
    var h=rainbowImage.getHeight();
    var y=pixel.getY();
    var avg=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    if(y>=0 && y<h/7){
      if(avg < 128){
      pixel.setRed(2*avg);
      pixel.setGreen(0);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(255);
      pixel.setGreen(2*avg-255);
      pixel.setBlue(2*avg-255);
    } }
    else if(y>=h/7 && y<(2*h)/7){
      if(avg < 128){
      pixel.setRed(2*avg);
      pixel.setGreen(0.8*avg);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(255);
      pixel.setGreen(1.2*avg-51);
      pixel.setBlue(2*avg-255);
    } 
    }
    else if(y>=(2*h)/7 && y<(3*h)/7){
      if(avg < 128){
      pixel.setRed(2*avg);
      pixel.setGreen(2*avg);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(255);
      pixel.setGreen(255);
      pixel.setBlue(2*avg-255);
    } 
    }
    else if(y>=(3*h)/7 && y<(4*h)/7){
      if(avg < 128){
      pixel.setRed(0);
      pixel.setGreen(2*avg);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(2*avg-255);
      pixel.setGreen(255);
      pixel.setBlue(2*avg-255);
    } 
    }
    else if(y>=(4*h)/7 && y<(5*h)/7){
      if(avg < 128){
      pixel.setRed(0);
      pixel.setGreen(0);
      pixel.setBlue(2*avg);
    }
    else if(avg >128){
      pixel.setRed(2*avg-255);
      pixel.setGreen(2*avg-255);
      pixel.setBlue(255);
    } 
    }
    else if(y>=(5*h)/7 && y<(6*h)/7){
      if(avg < 128){
      pixel.setRed(0.8*avg);
      pixel.setGreen(0);
      pixel.setBlue(2*avg);
    }
    else if(avg >128){
      pixel.setRed(1.2*avg-51);
      pixel.setGreen(2*avg-255);
      pixel.setBlue(255);
    } 
    }
    else if(y>=(6*h)/7 && y<h){
      if(avg < 128){
      pixel.setRed(1.6*avg);
      pixel.setGreen(0);
      pixel.setBlue(1.6*avg);
    }
    else if(avg >128){
      pixel.setRed(0.4*avg+153);
      pixel.setGreen(2*avg-255);
      pixel.setBlue(0.4*avg+153);
    } }
  }
  rainbowImage.drawTo(canvas);
}

//Apply Sunshine Filter
function applySunshine(){
  notLoaded();
  var sunshineImage=new SimpleImage(image);
  for(var pixel of sunshineImage.values()){
     var avg=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    if(avg < 128){
      pixel.setRed(2*avg);
      pixel.setGreen(2*avg);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(255);
      pixel.setGreen(255);
      pixel.setBlue(2*avg-255);
    }
  }
  sunshineImage.drawTo(canvas);
}

//Apply Red Filter
function applyRed(){
  notLoaded();
  var redImage=new SimpleImage(image);
  for(var pixel of redImage.values()){
    var avg=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
    if(avg < 128){
      pixel.setRed(2*avg);
      pixel.setGreen(0);
      pixel.setBlue(0);
    }
    else if(avg >128){
      pixel.setRed(255);
      pixel.setGreen(2*avg-255);
      pixel.setBlue(2*avg-255);
    }
  }
  redImage.drawTo(canvas);
}

//Apply Gray Filter
function applyGray(){
  notLoaded();
  var grayImage=new SimpleImage(image);
  for(var pixel of grayImage.values()){
        var avg=(pixel.getRed()+pixel.getGreen()+pixel.getBlue())/3;
        pixel.setRed(avg);
        pixel.setGreen(avg);
        pixel.setBlue(avg);
    }
  grayImage.drawTo(canvas);
}

//Apply Window Pane Filter
function makeWindow(){
  notLoaded();
  var windowImage=new SimpleImage(image);
  var w=windowImage.getWidth();
  var h=windowImage.getHeight();
  for(var pixel of windowImage.values()){
    var x=pixel.getX();
    var y=pixel.getY();
    if((x>=0 && x<=5) || (x>=(w/4)+1 && x<=(w/4)+3) || (x>=(w/2)-1 && x<=(w/2)+1) || (x>=(3*w/4)-3 && x<=(3*w/4)-1) || (x>=w-5 && x<=w) || (y>=0 && y<=5) || (y>=h-5 && y<=h) || (y>=(h/2)-1 && y<=(h/2)+1)){
      pixel.setRed(255);
      pixel.setGreen(195);
      pixel.setBlue(77);
    }
  }
  windowImage.drawTo(canvas);
}

function ensureInImage (coordinate, size) {
    if (coordinate < 0) {
        return 0;
    }
    if (coordinate >= size) {
        return size - 1;
    }
    return coordinate;
}

//Apply Blur Filter
function makeBlur(){
  notLoaded();
  var blurImage=new SimpleImage(image.getWidth(),image.getHeight());
  for(var pixel of image.values()){
    var x=pixel.getX();
    var y=pixel.getY();
    if(Math.random()>0.5){
      var dx=Math.random()*10-5;
      var dy=Math.random()*10-5;
      var nx=ensureInImage(x+dx,image.getWidth());
      var ny=ensureInImage(y+dy,image.getHeight());             blurImage.setPixel(x,y,image.getPixel(nx,ny));
    }
    else{
      blurImage.setPixel(x,y,pixel);
    }
  }
  blurImage.drawTo(canvas);
}

//Reset Original Image
function resetImage(){
  notLoaded();
  image.drawTo(canvas);
}

function notLoaded(){
  if(image==null || !image.complete()){
    alert("Image not loaded");
    return;
  }
}