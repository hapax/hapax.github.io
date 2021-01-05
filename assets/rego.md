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
start by invoking these two packages.
We also download the corpus:

```python
import nltk
import itertools

nltk.download('words')
from nltk.corpus import words
```

Our next step is to define a helper function `subseq(str1, str2)`
which checks if `str2` is a subsequence of `str1`.
It defines an iterator `it` over the letters in `str2`, and then
returns `True` if each letter of the iterator is in `str2`.
The ordering comes for free from the iterator:

```python
def subseq(str1, str2):
  it = iter(str2)
  return all(x in it for x in str1)
```

Finally, for a given license plate string, `regfull(str)` simply
searches the whole corpus `words.words()` and looks for supersequences:

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
	'specify', 'spiff', 'spiffed', 'spiffy',
	'spitful',  'spoffle', 'spoffy', 'spoof',
	'spoofer', 'spuffle', 'stupefy']
```

Incidentally, this shows that "spoof" is the equal shortest word.
In general, we can find the shortest word with `regshort(str)`. It does two passes through
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

With three letters, the game is often hard, but the chances are very
good that a word would eventually be found, and the natural variation
of difficulty makes the game fun.
At some point, license plates in Victoria shifted to four letters, and
it became much, much harder to play.
This raises the question: how much harder is it to play?
The natural measure is simply how many combinations have answers.
(It would be even better if we could weight words by how common they
are, which we could easily check using concordance, but I can't be
bothered right now.)

To compute this, we're going to iterate over many combinations of
letters and many words.
We will need to be clever about how we do this in order to have
something that runs in a reasonable time.
To begin with, we don't need all the words in the list, just a check
if it is non-empty.
So we can write a function `requick(str)` which stops iterating over
the corpus and spits out `True` as soon as it finds a single supersequence:

```python
def regquick(str):
    outcome = False
    wordnum = len(words.words())
    i = 0
    while outcome == False & i < wordnum:
        outcome = subseq(str, words.words()[i])
        i = i + 1
    return outcome
```

We can use this to build a function `goodreg(n)` which returns the
list of strings of length `n` which have valid supersequences.
Rather than iterate over combinations and then words, it iterates over
words, adding all the subsequences of length $n$ once again using `itertools`:

```python
def goodreg(n):
    goodreg = set()
    for word in words.words():
        lower = [combos for combos in
			list(itertools.combinations(word, n)) if
			all(x.islower() for x in list(combos))]
        goodreg.update(set(lower))
    return goodreg
```

Assuming license plates are random strings of length `n`, then the
chance of success is given by the proportion of good strings to the
total number:

```python
def regprop(n):
    return len(goodreg(n))/float(26**n)
```

So, let's check how hard it is!
I did up to six letters before my CPU got sore:

```python
>>> regprop(2)
1.0
>>> regprop(3)
0.9442
>>> regprop(4)
0.6683
>>> regprop(5)
0.2902
>>> regprop(6)
0.0711
```

About 94\% of three letter sequences have an answer, but only two
thirds of four letter sequences.
This is more than I expected, and that is of course because the corpus
includes ridiculous words like "spoffle" and "pewdom".
