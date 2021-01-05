---
Layout: post
mathjax: true
comments: true
title:  "Sublets: a road trip game"
categories: [Mathematics, Programming]
date:  2021-01-05
---

**January 5, 2021.** *Sublets is a fun game for road trips. Take
  letters from the license plates of passing cars, and find words of
  which the license plate letters form a subsequence. I explain the
  game in more detail and provide code for finding solutions. I also
  explore how the difficulty of the game varies with license plate length.*

#### Introduction

*Sublets* (standing for "subsequence of letters") is a game that, to
the best of my knowledge, my family collectively invented on a car
trip to South Australia in the noughties.
In my home state of Victoria, Australia,
license plates used to be alphanumeric strings consisting of three
letters and three numbers.
The game was simply to find a word those three letters occurred, in
that order.
In mathematical parlance, the license plate letters are a subsequence
of the word.
Here is an example:

$$
\mathbf{spf} \to \mathbf{sp}\text{oo}\mathbf{f}.
$$

The first person to find a valid word wins the round.
The way we played it, if a tie breaker was needed, shorter and/or
simpler words were preferred, so "**sp**oo**f**" beat "**s**o**p**ori**f**ic".

#### A solver

I've written a little solver to find solutions.
It's based on the Natural Language ToolKit (NLTK) package for Python,
and in particular, the `words` corpus, consisting of $\sim 250,000$
English words.
It also uses an iterator trick from the `itertools` library, so we
start by invoking these two packages:

```python
from nltk.corpus import words
import itertools
```

Our next step is to define a helper function which checks if `str2` is
a subsequence of `str1`.
It defines an iterator `it` over the letters in `str2`, and then
returns `True` if each letter of the iterator is in `str2`.
The ordering comes for free from the iterator:

```python
def subseq(str1, str2):
  it = iter(str2)
  return all(x in it for x in str1)
```

Finally, for a given license plate string, we simply search the whole
corpus `words.words()` and look for supersequences:

```python
def regfull(str):
    return [word for word in words.words()
		if subseq(str, word)]
```

Note that the `words` corpus is in lowercase.
As an example, we can list words of seven letters or less for which
"spf" is a subsequence:

```python
>>> [word for word in regfull('spf') if len(word) < 8]
	['sapful', 'scupful', 'shipful', 'shopful', 'skepful', 
		'specify', 'spiff', 'spiffed', 'spiffy', 'spitful', 
		'spoffle', 'spoffy', 'spoof', 'spoofer', 'spuffle', 'stupefy']
```

Incidentally, this shows that "spoof" is the equal shortest word.
In general, to find the shortest word, we can do two passes through
the whole list: one to find the minimum length, and a second to pluck
out all the words of that length.

```python
def regshort(str):
    words = regfull(str)
    minlength = min([len(word) for word in words])
    return [word for word in words if len(word) == minlength]
```

An example:

```python
>>> regshort("pwm")
	['pewdom']
```

Apparently, "pewdom" refers to the "system or prevalence of pews in a
church". English is a funny language.

#### Difficulty scaling

Not infrequently, it's hard to find a word, but with three letters
there seems to be a good chance that eventually you will hit on
something.
At some point, license plates in Victoria shifted to four letters, and
it became much, much harder to play.
The odds seem much worse, and the game is dramatically less fun.
