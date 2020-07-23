---
title: Chubbier Gargle Demon
layout: plain
---

<div id="sketch-holder"></div>

Tickle the gargle demons.

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>
let t = 0;
function setup() {
  createCanvas(600, 600);
  noStroke();
}

function draw() {
  background(10, 10);

  for (let x = -50; x <= width+50; x = x + 60) {
    for (let y = -50; y <= height+50; y = y + 10) {
      const xAngle = map(mouseX, 0, width, -4 * PI, 4 * PI, true);
      const yAngle = map(mouseY, 0, height, -4 * PI, 4 * PI, true);
      const angle = xAngle * (x / width) + yAngle * (y / height);

      const myX = x + 15 * cos(2 * PI * t + angle);
      const myY = y + 15 * sin(2 * PI * t + angle);

      fill((x+y)*(256/(height+width)), x*(256/width), mouseY*(256/width));
      
      ellipse(myX, myY, 30);
    }
  }
    
t = t + 0.01;
}
</script>
<p>Click the button to display a string as a hyperlink.</p>

<button onclick="myFunction()">Sick of tickling?</button>

<p id="demo"></p>

<script>
function myFunction() {
  var str = "Plan with the chubby demons.";
  var result = str.link("https://www.when2meet.com/?9417123-MPoci");
  document.getElementById("demo").innerHTML = result;
}
</script>

</head>
</html>
