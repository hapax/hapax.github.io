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
let mx = [], my = [], rotx = [], roty = [], Mx = [], My = [];
let input1, linkageToggle = 0, polyToggle = 0, valToggle=0;

function setup() {
  createCanvas(400, 400);
  
  input = createInput();
  input.position(35, 87);
  input.size(50);
  }

function draw() {
  background(255);
  
  strokeWeight(2);
  stroke(200);
  circle(height/2, width/2, 2*rad);
  strokeWeight(12);
  point(height/2, width/2);
  
  let len = mx.length;
  textSize(18);
  text('d= ' + str(mx.length), 7, 25);
  text('s= ', 8, 47)
  
  if (linkageToggle === 0) {
    if (polyToggle === 1) {
      for (let i = 0; i < len-1; i++) {
        strokeWeight(1);
        stroke(130);
        line(mx[i], my[i], mx[i+1], my[i+1]);
		fill(130);
		push();
		translate(mx[i+1], my[i+1]);
		let angle = atan2(my[i+1] - my[i], mx[i+1] - mx[i]) + PI/2;
		rotate(angle);
		triangle(0, 0, 4, 10, -4, 10);
		pop();
		fill(255);
      }
      line(mx[len-1], my[len-1], mx[0], my[0]);
    }
    for (let i = 0; i < len; i++) {
      strokeWeight(2);
      stroke(0, 200, 200);
      line(width/2, height/2, mx[i], my[i]);
      if (i === 0) {
      stroke(0);
	  } else {  }
      strokeWeight(firstRad*(5/3));
      point(mx[i], my[i]);
      stroke(255);
      strokeWeight(firstRad);
      point(mx[i], my[i]);
    }
  } else if (linkageToggle === 1) {
    for (let i = 0; i < len; i++) {
      let sumx = 0, sumy = 0;
      let angle = -valToggle * input.value() * TWO_PI / len;
      rotx[i] = (mx[i]-width/2) * cos(i * angle) - (my[i]-height/2) * sin(i * angle);
      roty[i] = (mx[i]-width/2) * sin(i * angle) + (my[i]-height/2) * cos(i * angle);
      for (let j = 0; j < i+1; j++) {
        sumx = sumx + rotx[j];
        sumy = sumy + roty[j];
      }
      Mx[i] = sumx + width/2;
      My[i] = sumy + height/2;
    }
    strokeWeight(2);
    stroke(0, 200, 200); 
    line(width/2, height/2,Mx[0],My[0]);
    for (let i = 0; i < len-1; i++) {
      line(Mx[i],My[i],Mx[i+1],My[i+1]);
    }
    
    if (valToggle === 1) {
      strokeWeight(2);
      stroke(200, 0, 200);
      line(width/2, height/2, Mx[len-1],My[len-1]);
    }
    strokeWeight(firstRad*(5/3));
    point(Mx[len-1],My[len-1]);
    stroke(255);
    strokeWeight(firstRad);
    point(Mx[len-1],My[len-1]);
  }
}

function mousePressed() {
  if ((mouseX > 60) && (mouseY > 60)) {
    mx.push(mouseX);
    my.push(mouseY);
  }
}

function keyPressed() {
  if (keyCode == 76) {
    if (linkageToggle === 0) {
      linkageToggle = 1;
    } else { 
      linkageToggle = 0;
    }  
  } else if (keyCode == 80) {
    if (polyToggle === 0) {
      polyToggle = 1;
    } else { 
      polyToggle = 0;
    }  
  } else if (keyCode == 86) {
    if (valToggle === 0) {
      valToggle = 1;
    } else { 
      valToggle = 0;
    }  
  }
}

</script>
</head>
</html>
