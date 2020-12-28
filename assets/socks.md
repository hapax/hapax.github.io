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

```python
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
repeats = 10000
for n in range(20):
  results = []
  for rep in range(repeats):
    results.append(randsocks(n))
	av = sum(results)/float(len(results))
	averages.append(av)
```
