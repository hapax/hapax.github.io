---
title: Gube Blodger Harmonic Metaplanning
layout: plain
---

<div id="sketch-holder"></div>

Tickle the delicate gube blodgers, and listen to their sorrowful song.
Then you may begin the Metaplanning.

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let t = 0; // time variable
let osc, fft;

 osc = new p5.TriOsc(); // set frequency and type
  osc.amp(0.5);

  fft = new p5.FFT();
  osc.start();

function setup() {
  createCanvas(600, 600);
  noStroke();
}

function draw() {
  background(10, 10); // translucent background (creates trails)

  // make a x and y grid of ellipses
  for (let x = 0; x <= width; x = x + 60) {
    for (let y = 0; y <= height; y = y + 10) {
      // starting point of each circle depends on mouse position
      const xAngle = map(mouseX, 0, width, -4 * PI, 4 * PI, true);
      const yAngle = map(mouseY, 0, height, -4 * PI, 4 * PI, true);
      // and also varies based on the particle's location
      const angle = xAngle * (x / width) + yAngle * (y / height);

      // each particle moves in a circle
      const myX = x + 10 * cos(2 * PI * t + angle);
      const myY = y + 10 * sin(2 * PI * t + angle);

      fill((x+y)*(256/(height+width)), x*(256/width), mouseY*(256/width));
      
      ellipse(myX, myY, 30); // draw particle
    }
  }

  t = t + 0.01; // update time

  // change oscillator frequency based on mouseX
  let freq = map(mouseY, 0, width, 40, 880);
  osc.freq(freq);

  let amp = 1;
  osc.amp(amp);
}

</script>
</head>
</html>
