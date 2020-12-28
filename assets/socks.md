---
Layout: post
mathjax: true
comments: true
title:  "The sock problem"
categories: [Maths, Everyday]
date:  2020-12-27
---

**December 27, 2020.** *How many socks do you need to grab before you
  get a pair? The answer turns out to be surprisingly tricky.*

#### Analytics

#### Simulations

<figure>
    <div style="text-align:center"><img src
    ="/images/posts/sockssim.png"/>
	</div>
	</figure>

```python
import numpy as np
import scipy.special as sc
import matplotlib.pyplot as plt

def randsocks(n):
  socks0 = [[i, 0] for i in range(n)]
  socks1 = [[i, 1] for i in range(n)]
  rand = np.random.permutation(socks0+socks1)
  firstrand = [i for [i, j] in rand]
  k = 0
  while len(firstrand[:k]) == len(list(set(firstrand[:k]))):
    k = k + 1
  return k

averages = []
repeats = 1000
for n in range(1,21):
  results = []
  for rep in range(repeats):
    results.append(randsocks(n))
  av = sum(results)/float(len(results))
  averages.append(av)

hyper = []
for n in range(1, 21):
  hyper.append(sc.hyp2f1(1, -n, -2*n, 2))

fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(range(1,21), averages,color='r')
ax.scatter(range(1,21), hyper,color='b')
plt.show()
```
