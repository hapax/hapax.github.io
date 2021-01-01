---
layout: plain
title:  "Trammel"
date:  2020-11-26
---

<div id="sketch-holder"></div>

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

let d = 170;
let b = 100;
let x = b;
let y = b;

function setup() {
  createCanvas(400 + 2*b, 400 + 2*b);
}

function draw() {
  background(200);
  noSmooth();

  strokeWeight(0);
  fill(200, 160, 45);
  square(b, b, 400)
  fill(153, 15, 35);
  square(b, b, d);
  square(width - b - d, b, d);
  square(b, height - b - d, d);
  square(width - b - d, height - b - d, d);
  
  fill(15, 153, 35);
  rect(mouseX, b + d, 100, (400-2*d));
  rect(b + d, mouseY, (400-2*d), 100);
}
