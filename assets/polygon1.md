---
layout: plain
title:  "Polygonal basis elements"
date:  2020-11-26
---

<div id="sketch-holder"></div>

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let rad = 180;
let input1, button1, input2, button2, greeting1, greeting2;

function setup() {
  createCanvas(400, 400);
  
  input1 = createInput();
  input1.position(30, 50);
  input1.size(50);
  
  input2 = createInput();
  input2.position(30, 70);
  input2.size(50);
  
  greeting1 = createElement('h3', 'd=');
  greeting1.position(8, 31);
  
  greeting2 = createElement('h3', 's=');
  greeting2.position(10, 51);
}

function draw() {
  background(255);
  
  strokeWeight(1);
  stroke(100);
  circle(height/2, width/2, 2*rad);
  
  strokeWeight(2);
  stroke(0);
  polygon(height/2, width/2, rad, input1.value(), input2.value());

  strokeWeight(10); // Make the points 10 pixels in size
  point(width/2+rad, height/2);
  stroke(255);
  strokeWeight(6);
  point(width/2+rad, height/2);
}

function polygon(x, y, radius, d, s) {
  let angle = s * TWO_PI / d;
  beginShape();
  for (let a = 0; a < d; a++) {
    let sx = x + cos(a*angle) * radius;
    let sy = y + sin(a*angle) * radius;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}

</script>
</head>
</html>
