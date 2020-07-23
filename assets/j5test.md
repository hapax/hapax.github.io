---
title: Chubbier Gargle Demon
layout: plain
---

<div id="sketch-holder"></div>

Tickle the delicate gargle demons.

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.sound.js"></script>
<script>
let t = 0;
let mic;

  mic = new p5.AudioIn();
  mic.start();

function setup() {
  createCanvas(600, 600);
  noStroke();
}

function draw() {
  background(10, 10);

let vol = mic.getLevel();

  for (let x = -10; x <= width+10; x = x + 60) {
    for (let y = -10; y <= height+10; y = y + 10) {
      const xAngle = map(mouseX, 0, width, -4 * PI, 4 * PI, true);
      const yAngle = map(mouseY, 0, height, -4 * PI, 4 * PI, true);
      const angle = xAngle * (x / width) + yAngle * (y / height);

      const myX = x + 15 * cos(2 * PI * t + angle);
      const myY = y + 15 * sin(2 * PI * t + angle);

      fill(vol*256, x*(256/width), mouseY*(256/width));
      
      ellipse(myX, myY, 30); // draw particle
    }
  }

t = t + 0.01; // update time
}

function mouseClicked() {
	let s = 'https://www.when2meet.com/?9417123-MPoci';
    fill(50);
    text(s, 10, 10, 70, 80);
  }
</script>
</head>
</html>
