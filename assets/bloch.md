---
layout: plain
title:  "Noise on the Bloch sphere"
date:  2020-11-20
---

<div id="sketch-holder"></div>

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let phase, bit, phaseBit, depol, depolFactor, phaseRad, bitRad, phaseBitRad;
let rad0=100;

function setup() {
  createCanvas(400, 400, WEBGL);
  phase = createSlider(1,24, 1);
  phase.position(5+5, 10+190);
  phase.style('width', '80px');
  bit = createSlider(1,24, 1);
  bit.position(5+85+5,10+190);
  bit.style('width', '80px');
  phaseBit = createSlider(1,24, 1);
  bit.position(5+85+85+5,10+190);
  phaseBit.style('width', '80px');
  depol = createSlider(1,24, 1);
  depol.position(5+85+85+85+5,10+190);
  depol.style('width', '80px');
}

function draw() {
  background(205, 105, 94);
  fill(255);
  directionalLight(250, 250, 250, 0.8, 0.5, -1);
  
  strokeWeight(0);
  depolFactor = (24-depol.value())/24+0.0;
  rad = depolFactor*rad0;
  phaseRad = depolFactor*4*(phase.value()-2);
  bitRad = depolFactor*4*(bit.value()-2);
  phaseBitRad = depolFactor*4*(phaseBit.value()-2);
  
  ellipsoid(rad-phaseRad-phaseBitRad,rad-bitRad-phaseBitRad,rad-bitRad-phaseRad,24,24);
  strokeWeight(1);
  noFill();
  stroke(255);
  circle(0,0,2*rad0+10);
  strokeWeight(5);
  point(0,-rad0-10);
  rotateX(PI/2);
  strokeWeight(1);
  stroke(100,140,20);
  circle(0,0,2*rad0+10);
  rotateX(-PI/2);
  rotateY(PI/2);
  stroke(100,40,200);
  strokeWeight(1);
  circle(0,0,2*rad0+10);
  stroke(0);
  strokeWeight(5);
  point(0,rad0+10);
  rotateY(-PI/2);
  rotateZ(PI/2);
  stroke(100,140,20);
  strokeWeight(5);
  point(0,-rad0-10);
  
  orbitControl(3,3,3);
}
</script>
</head>
</html>

The sketch below represents the effect of different single-qubit noise
channels on the Bloch sphere.
The white circle lies on the *y-z* plane, while green lies on
*x-y*, and purple on *x-z*.
The white point represents |0⟩, the black point |1⟩,
and the green point |+⟩.
The sliders, in order, representing the strength of various noise channels:

- phase flip channel;
- bit flip channel;
- bit/phase flip channel;
- depolarization.

There are various bugs I will fix at some point. I might also add
amplitude damping.

---
