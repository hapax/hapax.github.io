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
let tipWidth = 3, tipHeight = 8, firstRad = 9;
let myTextInputs, myInputs;
let copyToggle = 0, factorToggle = 0;

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
  let myTextInputs = split(input1.value(), ',');
  let myInputs = int(myTextInputs);
  len = myInputs.length;
  s = input2.value()
  if (copyToggle === 0) {
    for (let i = 0; i < len; i++) {
      myCol = 255*(1-(i+1)/len);
      stroke(myCol);
      polygon(height/2, width/2, rad, myInputs[i], s, myCol);
      s = s/myInputs[i];
    } 
  } else {
    let prod = 1;
    for (let i = 0; i < len; i++) {
      prod = prod*myInputs[i];
    }
    stroke(0);
    polygon(height/2, width/2, rad, prod, s, 0);
  }

  strokeWeight(firstRad*(5/3));
  point(width/2+rad, height/2);
  stroke(255);
  strokeWeight(firstRad);
  point(width/2+rad, height/2);
}

function polygon(x, y, radius, d, s, color) {
  let angle = s * TWO_PI / d;
  beginShape();
  for (let a = 0; a < d; a++) {
    let sx = x + cos(a*angle) * radius;
    let sy = y - sin(a*angle) * radius;
    vertex(sx, sy);
  }
  endShape(CLOSE);

  let compAngle = PI - TWO_PI / d;
  for (let a = 1; a < d; a++) {
    let sx = x + cos((a)*angle) * radius;
    let sy = y - sin((a)*angle) * radius;
    fill(color);
    push();
    translate(sx, sy);
    rotate(-(a-1/2)*angle);
    triangle(0, 0, tipWidth, tipHeight, -tipWidth, tipHeight);
    pop();
    noFill();
  }
}

function keyPressed() {
  if (keyCode == 67) {
    if (copyToggle === 0) {
      copyToggle = 1;
    } else { 
      copyToggle = 0;
    }  
  } else if (keyCode == 70) {
    if (factorToggle === 0) {
      factorToggle = 1;
    } else { 
      factorToggle = 0;
    }  
  } else if (keyCode == 76) {
      if (tipWidth === 3) {
      tipWidth = 0;
      tipHeight = 0;
      firstRad = 0;
    } else {
      tipWidth = 3;
      tipHeight = 8;
      firstRad = 6;
    }
  }
}

</script>
</head>
</html>
