---
layout: page
title: Fun
permalink: /fun/
---

In the tradition of dorky, maximalist websites, here are some things I
do when I'm not sciencing or encouraging other people to science.

#### Writing

I like writing sci-fi. Some recent flash fiction:

- ["Arrest"]({{hapax.github.io}}/assets/arrest.pdf) (2019). Telekinetic
zombies, science gone mad, and the psychology of time. Winner of the
[2019 Ubyssey sci-fi competition](https://www.ubyssey.ca/science/arrestee-sci-fi-winner-2019/).
- ["A post-quantum fantasia"]({{hapax.github.io}}/assets/pqf.pdf)
(2020). A farcical "what if" about quantum computers.

In a prior life I earned a philosophy degree, and still take language
on holiday from time to time. Some rambling discursions:

- *Language, cognition and alien math*
  [[1](https://hapax.github.io/philosophy/alien-maths-1/)]] (2020,
  blog post). Is it possible to get inside the head of a bat?
- [*From solipsism to emergent time*](https://hapax.github.io/physics/philosophy/emergent-time/)
  (2020, blog post). What makes time different from space, and what
  would a physical explanation of this fact look like?
- [*The endless present*](https://hapax.github.io/philosophy/physics/psychology-time/)
  (2019, blog post). A four-dimensionalist account of the psychology
  of time, concluding with a radical version of eternal recurrence.
<!-- - [*Cigarettes, hard labour, and a box full of money*](https://hapax.github.io/philosophy/prisoners/)
(2017, blog post). How decision problems, from the Prisoner's Dilemma
to smoking to betting against the Oracle of Delphi, are secretly
  related.
<!-- What nuclear war, smoking, and the Oracle of Delphi have in -->
<!-- common. -->

#### Art

I put my digital art on [tumblr](https://caedrix.tumblr.com/)
(yes, it still exists) and photos of urban decay, chance Cornellian
arrangements of rubbish, symmetry, patterns, and so forth, on
[Instagram](https://www.instagram.com/dr__abe/).

#### Programming

<!-- I code for fun and occasionally profit in [Python](https://www.python.org/)
(it's quick), [Haskell](https://www.haskell.org/) (it's beautiful) and
[Processing](https://processing.org/) (it's visual). -->
I code for fun and occasionally profit. A few small projects:

- [*University of Melbourne course planner*](https://students.unimelb.edu.au/your-course/manage-your-course/planning-your-course-and-subjects/faculty-course-planning-resources/course-planning-tools). I
  designed the prototype version of the university's course
  planner. I've linked the snazzy beta version by the folks at [Eliiza](https://eliiza.com.au/about/).
- [*Genesim*](https://github.com/hapax/genesim). Simulate the random
distribution of genetic code around a family tree.
- [*Partitions*](https://github.com/hapax/haskell-partitions). Experimental
  number theory in Haskell, now with [blog post](https://hapax.github.io/mathematics/programming/haskell-partition/)!

Here is a list of
[Processing](https://processing.org/)/[p5js](https://p5js.org/)
sketches:

- [*Gothic window simulator*](https://www.openprocessing.org/sketch/571835). Program for drawing gothic window tracery.
- [*Pong mania*](https://www.openprocessing.org/sketch/590092). A buggy but addictive implementation of Pong. <!-- of which I am
  inordinately proud.-->

<figure>
 <div style="text-align:center"><img src ="/images/x64.png" />
 <figcaption><i>This little robot is very keen.</i></figcaption>
 	 </div>
  </figure>

<!-- <figure>
 <div style="text-align:center"><img src ="/images/gothic-2.png" />
 <figcaption><i>The gothic window simulator.</i></figcaption>
 	 </div>
  </figure> -->

<div id="sketch-holder"></div>

Rub the chromaline eggs.

<html>
<head>

<script src="https://cdn.jsdelivr.net/npm/p5@1.1.9/lib/p5.js"></script>
<script>

int paddleLx;
int paddleLy;
int paddleRx;
int paddleRy;
float ballX;
float ballY;
float ballVx;
float ballVy;
int ballSize = 20;
int paddleWidth = 20;
int paddleHeight = 60;
int bigWidth = (ballSize + paddleWidth)/2;
int bigHeight = (ballSize + paddleHeight)/2;
int gameOn = 0;
int ticker = 0;
int LScore = 0;
int RScore = 0;

void restart() {
  paddleLx = 20;
  paddleLy = 200;
  paddleRx = 380;
  paddleRy = 200;
  ballX = paddleLx + ballSize;
  ballY = paddleRy;
  ballVx = 0;
  ballVy = 0;
  paddleLx = 20;
  paddleLy = 200;
  paddleRx = 380;
  paddleRy = 200;
}

void setup() {
  size(400, 400);
  background(0);
  restart();
  textSize(60);
  fill(255);
  text("PONG", 100, 160);
  text("MANIA", 120, 240);
  fill(0,0,255);
  text("PONG", 100+3, 160+3);
  text("MANIA", 120+3, 240+3);
}

void mousePressed() {
  if (gameOn == 0) {
    gameOn = 1;
    ballVx = 5;
  }
  else {
    restart();
    gameOn = 0;
  }
}

void update() {
  background(0);
  fill(255, 100);
  textSize(32);
  text(LScore, 10, 30);
  text(RScore, 360, 30);
    
  paddleLy = mouseY;
  ballX += ballVx;
  ballY += ballVy;
  
  ++ticker;
  
  paddleRy = int(ballY + 50*sin(sin((ballY + ticker)/30)));
  
  if (ballY < 0 || ballY > 400) {
    ballVy *= -1;
  }
  else if ((paddleLx - bigWidth < ballX) && (ballX < paddleLx + bigWidth) && (paddleLy - bigHeight < ballY) && (ballY < paddleLy + bigHeight)) {
    ballVy = ((ballY - paddleLy)/float(bigHeight))*4;
    ballVx *= -1;
    ballX += 1;
  }
  else if ((paddleRx - bigWidth < ballX) && (ballX < paddleRx + bigWidth) && (paddleRy - bigHeight < ballY) && (ballY < paddleRy + bigHeight)) {
    ballVy = ((ballY - paddleRy)/float(bigHeight))*4;
    ballVx *= -1;
    ballX -= 1;
  }
  else if (ballX < -2) {
    ballVx = ballVy = 0;
    textSize(32);
    text("You lose!", 200, 200);
    ++RScore;
    gameOn = 0;
    restart();
  }
  else if (ballX > 402) {
    ballVx = ballVy = 0;
    textSize(32);
    text("You win!", 200, 200);
    ++LScore;
    gameOn = 0;
    restart();
  }
}

void draw() {
  if (gameOn == 1) {
    update();
  }
  fill(255);
  rect(paddleLx-(paddleWidth/2), paddleLy-(paddleHeight/2), paddleWidth, paddleHeight);
  rect(paddleRx-(paddleWidth/2), paddleRy-(paddleHeight/2), paddleWidth, paddleHeight);
  ellipse(int(ballX), int(ballY), ballSize, ballSize);
}
</script>
</head>
</html>
