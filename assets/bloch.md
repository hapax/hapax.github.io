---
title: Noise on the Bloch sphere
layout: plain
---

<div id="sketch-holder"></div>

Bloch sphere things

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let phase, bit, phaseBit, depol, depolFactor, phaseRad, bitRad, phaseBitRad;
let rad0=100;

function setup() {
  createCanvas(400, 400, WEBGL);
  phase = createSlider(1,24, 1);
  phase.position(5, 10+70);
  phase.style('width', '80px');
  bit = createSlider(1,24, 1);
  bit.position(width-85,10+70);
  bit.style('width', '80px');
  phaseBit = createSlider(1,24, 1);
  phaseBit.position(5,height-25+70);
  phaseBit.style('width', '80px');
  depol = createSlider(1,24, 1);
  depol.position(width-85, height-25+70);
  depol.style('width', '80px');
}

function draw() {
  background(205, 105, 94);
  fill(255);
  directionalLight(250, 250, 250, 0.8, 0.5, -1);
  strokeWeight(0);
  
  depolFactor = (24-depol.value())/24;
  rad = depolFactor*rad0;
  phaseRad = depolFactor*phase.value();
  bitRad = depolFactor*bit.value();
  phaseBitRad = depolFactor*phaseBit.value();
  
  ellipsoid(rad-phaseRad-phaseBitRad,rad-bitRad-phaseBitRad,rad-bitRad-phaseRad,24,24);
  strokeWeight(1);
  stroke(255);
  noFill();
  circle(0,0,2*rad0-1)
}

</script>
</head>
</html>
