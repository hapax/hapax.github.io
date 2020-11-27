---
layout: plain
title:  "Linkages and inner products"
date:  2020-11-26
---

<div id="sketch-holder"></div>

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let firstRad = 6, rad = 180;
let mx = [], my = [], Mx = [], My = [];
let input1, greeting, sumToggle = 0;

function setup() {
  createCanvas(400, 400);
  
  input = createInput();
  input.position(30, 50);
  input.size(50);
  
  greeting1 = createElement('h3', 's=');
  greeting1.position(8, 31);
  }

function draw() {
  background(255);
  
  strokeWeight(2);
  stroke(200);
  circle(height/2, width/2, 2*rad);
  strokeWeight(6);
  point(height/2, width/2);
  
  let len = mx.length;
  if (sumToggle === 0) {
    for (let i = 0; i < len; i++) {
      strokeWeight(2);
      stroke(200, 0, 0);      
      line(width/2, height/2, mx[i], my[i]);
      strokeWeight(firstRad*(5/3));
      point(mx[i], my[i]);
      stroke(255);
      strokeWeight(firstRad);
      point(mx[i], my[i]);
    }
  }
}

function mousePressed() {
  mx.push(mouseX);
  my.push(mouseY);
}

function keyPressed() {
  if (keyCode == 83) {
    if (sumToggle === 0) {
      sumToggle = 1;
    } else { 
      sumToggle = 0;
    }  
  }
}

</script>
</head>
</html>
