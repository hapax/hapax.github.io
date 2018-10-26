---
layout: post
mathjax: true
comments: true
title:  "Partition identities in Haskell"
categories: [Mathematics, Programming]
date:   2018-09-30
---

**September 30, 2018.** *With a little experimental mathematics, you
  too can arrive at the insights as Ramanujan! A simple program in
  Haskell for discovering partition identities.*

### Introduction

<i>Prerequisites: basic number theory, some exposure to Haskell.</i>

The
[*Rogers-Ramanujan identities*](https://en.wikipedia.org/wiki/Rogers%E2%80%93Ramanujan_identities)
relate different ways of splitting natural numbers into smaller
parts. I will state a precise version below, but before that, I'll
introduce some basic notions. The purpose of this post will not be to
prove these identities, but rather, to arrive at them *experimentally*
using Haskell. The associated GitHub page is [here](https://github.com/hapax/haskell-partitions).

A *partition* of a natural number $n \in \mathbb{N}$ is a way of writing $n$ as a sum of smaller natural numbers, or *blocks*, ignoring the order in which we add the blocks. For instance, there are $5$ ways to partition the number $4$:

$$
4 = 3 + 1 = 2 + 2 = 2 + 1 + 1 = 1 + 1 + 1 + 1.
$$

A partition $\sigma$ can be thought of a *multiset* of natural numbers $\sigma = [\sigma_1, \ldots, \sigma_k] = [\sigma_i]$, where $\sigma_i \in \mathbb{N}$.
The variable $k$ will stand for the number of blocks in a partition, and we typically order the blocks in increasing size, so that $\sigma_1 \leq \sigma_2 \leq \cdots \ldots \sigma_k$.
This means we can talk about blocks being next to each other, or *adjacent*, in a partition.

We can consider partitions where the blocks have certain properties, conveniently encoded by a test which takes a partition and spits out "true" or "false" according to whether the partition has the property.
Let's denote the number of partitions of $n$ satisfying a predicate
$Q$ by $p_Q(n)$.
This is a modification of the usual notation $p(n)$ for the number of
partitions without any constraints.
Note that $p_Q(n) \leq p(n)$.
Predicates can be combined using propositional connectives like "not" ($\neg$), "and" ($\wedge$), and "or" ($\vee$).

Here are some specific predicates:
- Adjacent elements of $\sigma$ differ by at least $2$, or $\sigma_{i+1}-\sigma_i \geq 2$ for all $0 \leq i \leq k$. We call this predicate $A$.
- The smallest element of $\sigma$ is at least $2$, or $\sigma_1 \geq 2$. Label this predicate $B$.
- Elements of $\sigma$ are congruent to $1$ or $4$ modulo $5$. Call this $C$.
- Elements of $\sigma$ are congruent to $2$ or $3$ modulo $5$. Call this $D$.

We can now state the Rogers-Ramanujan identities. For all $n \in \mathbb{N}$,

$$
p_A(n) = p_C(n), \qquad p_{A\wedge B}(n) = p_D(n).
$$

We're going to build some Haskell code for experimentally seeing this result, and other similar partition identities.
To follow along, you will need to have [Haskell](https://www.haskell.org) installed on your system, and understand the basics of the language.
(For an introduction, I recommend [Learn You a Haskell for Great Good](http://learnyouahaskell.com).) This little project is, in part, a rather belated tribute to the surprisingly good Ramanujan biopic, *The Man who Knew Infinity* (2015).

### Generating partitions

To begin with, we're going to be manipulating some lists, so we will import ```Data.List```:

```haskell
import Data.List
```

We now need some way to generate ordinary partitions (with the trivial predicate). Let's do it recursively! Basically, to get partitions of $n$, we take the partitions of $n-1$ and either (a) add an extra block $1$, or (b) increase one of the blocks by $1$:

```haskell
indexedAdd :: ([Int], Int) -> [Int]
indexedAdd (x:xs, 1) = (x+1):xs
indexedAdd (x:xs, n) = x:(indexedAdd (xs, (n-1)))

addOne :: [Int] -> [[Int]]
addOne ls = map indexedAdd zipped
           where numCopies = length ls
                 copyLs    = replicate numCopies ls
                 zipped    = zip copyLs [1..numCopies]

partitions :: Int -> [[Int]]
partitions 0 = [[]]
partitions n = nub $ biggerParts ++ newParts
           where recurParts  = partitions (n-1)
                 newParts    = [ [1] ++ part | part <- recurParts ]
                 biggerParts = map sort $ concat $ map addOne recurParts
```

This automatically produces partitions with blocks in ascending
size. This method is highly inefficient, so in the future, I hope to
optimise this.

### Predicate builders

To find $p_Q(n)$, we need to filter the partitions of $n$ using the predicate $Q$. Before showing how to do this, let's build up a stock of predicates. Even better, using currying, we can build objects which build predicates! Examples of flexible predicate builders are *supersets*, *forbidden numbers* and *given remainders*. I'll go through these in turn.

A superset predicate just checks if all the blocks lie in some set $N \subseteq \mathbb{N}$ of natural numbers:

```haskell
supersetOf :: [Int] -> [Int] -> Bool
supersetOf sup = foldl (\t x -> and [x `elem` sup, t]) True
```

Forbidden numbers are actually the same as supersets, but it's easier sometimes to specify the complement of $N$ than $N$ itself:

```haskell
forbiddenNums :: [Int] -> [Int] -> Bool
forbiddenNums forbidList = foldl (\t x -> and [not $ x `elem` forbidList, t]) True
```

An alternative way to forbid numbers is to negate the superset predicate, which I'll discuss below. Finally, we have remainders, e.g. $\equiv 1 \pmod 4$:

```haskell
remainders :: Int -> [Int] -> [Int]
remainders b [] = [1..]
remainders b rs = filter correctRem [1..]
           where correctRem num = (rem num b) `elem` rs
```
		   
These will obviously be important for the Rogers-Ramanujan identities. I'll list a few more predicate builders that I decided would be useful:

```haskell
differsBy :: Int -> [Int] -> Bool
differsBy _ []   = True
differsBy n ls = all (>=n) diffs
          where diffs  = zipWith (-) (tail ls) ls

biggerThan :: Int -> [Int] -> Bool
biggerThan n = all (>n)

lessThan :: Int -> [Int] -> Bool
lessThan n = all (<n)

limitReps :: Int -> [Int] -> Bool
limitReps n ls = all (<=n) repLengths
          where repLengths = map length $ group ls

noConsecMult :: Int -> Int -> [Int] -> Bool
noConsecMult b rs ls = all test pairDiffs
          where diffs     = zipWith (-) (tail ls) ls
                pairDiffs = zip diffs $ tail ls
                test      = \(x, y) -> or [ x /= b, not $ (rem y b) `elem` rs]

predGaps :: Int -> Int -> Int -> [Int] -> Bool
predGaps b rs gap ls = all test pairDiffs
          where diffs     = zipWith (-) (tail ls) ls
                pairDiffs = zip diffs $ tail ls
                test      = \(x, y) -> or [ x > gap, not $ (rem y b) `elem` rs]
```

Briefly, ```differsBy``` checks that adjacent blocks differ by more
than some specified minimum. The builders ```biggerThan``` and
```lessThan``` impose upper and lower limits on block size. Finally, ```limitReps```, ```noConsecMult``` and ```predGaps``` respectively limit repeated blocks, forbid consecutive blocks with given remainders modulo a base, and forbid given remainders between consecutive blocks whose difference is less than some gap.

We can combine predicates using logical connectives.
The connectives ```and``` and ```not``` are nice because they are associative: we can hit a big list of predicates with them!
We implement these for lists of predicates:

```haskell
andPreds :: [[Int] -> Bool] -> [Int] -> Bool
andPreds predLs part = and $ map ($ part) predLs

orPreds :: [[Int] -> Bool] -> [Int] -> Bool
orPreds predLs part = or $ map ($ part) predLs
```

We can also negate a predicate using Haskell's built-in ```not``` operators.
These operators are sufficient to create any truth-functional combination of predicates.

### Building sets

The tools so far allow us to test partition partitions like the Rogers-Ramanujan identities.
It is much cooler to *discover* these, however, so we will describe and implement a method for taking a given predicate $Q$, and trying to construct a superset predicate $S_Q$ which gives equivalent answers, in the sense that

$$
p_Q(n) = p_{S_Q}(n).
$$

The basic idea is to iteratively build $S_Q$, assuming it exists.
We start by looking at $p_Q(1)$.
If $p_Q(1) = 0$, then $1 \notin S_Q$; if $p_Q(1) = 1$, then we must
have $1 \in S_Q$, corresponding to the trivial partition $1 = 1$.
Since $p_Q(1) \leq p(1) = 1$, these are the only possibilities.
Now $p(2) = 2$, we must have $p_Q(2) \in \{0, 1, 2\}$.
Rather than go through all possibilities, let's assume that $p_Q(1) =
1$ and $p_Q(2) = 1$.
Then $2 \notin S_Q$, since then we would have $p_Q(2)  = 2$.

More generally, suppose we have constructed a set $S_{(k-1)}$ which
produces the same answers as $p_Q$ for $n \leq k-1$:

$$
p_Q(n) = p_{S_{(k-1)}}(n), \quad \forall n \leq k-1.
$$

We construct $S_{(k)}$ as follows:

$$
S_{(k)} =
\begin{cases} S_{(k-1)} \cup \{k\} & p_{Q}(k) = p_{S_{(k-1)}\cup \{k\}}(k) \\
S_{(k-1)} & p_{Q}(k) = p_{S_{(k-1)}}(k) \\
\text{no $S_Q$ exists} & \text{else}.
\end{cases}
$$

Note that if the last leg occurs, we have a constructive proof that no
set $S_Q$ exists.
(More generally, I'm not sure if there is a characterisation of the
predicates $Q$ for $S_Q$ exists.)
Here is the Haskell implementation for building $S_{(k)}$, where in
```buildSet``` below we label $k$ as ```maxNumber```:

```haskell
numPartsPred :: ([Int] -> Bool) -> Int -> Int
numPartsPred partPred n = length $ filter partPred $ partitions n

buildSetStep :: ([Int] -> Bool) -> [Int] -> Int -> [Int]
buildSetStep partPred setSoFar current
                      | numPartsPred partPred current == numPartsPred setSoFarPred current = setSoFar
                      | numPartsPred partPred current == numPartsPred setAddPred current   = setAdd
                      | otherwise                                                          = error "no set"
                      where setAdd       = setSoFar ++ [current]
                            setSoFarPred = supersetOf setSoFar
                            setAddPred   = supersetOf setAdd

buildSet :: ([Int] -> Bool) -> Int -> [Int]
buildSet partPred maxNumber = foldl step [] [1..maxNumber]
         where step = buildSetStep partPred
```

### Discovering partition identities

Let's briefly present some examples and illustrate usage.
Open a shell, navigate to the folder you've stored ```HaskPart.hs```,
and boot up ```ghci```.
Now load the file:

```
Prelude> :load HaskPart.hs
[1 of 1] Compiling HaskPart         ( HaskPart.hs, interpreted )
Ok, one module loaded.
```

Let's start with a simple identity due to Euler.
We let $Q$ be the predicate that the blocks in the partition are
distinct.
This corresponds to the predicate ```differsBy 1```, since this
ensures that adjacent blocks are at least $1$ apart.
We plug this predicate into the ```buildSet``` function, setting $k = 20$:

```
*HaskPart> buildSet (differsBy 1) 20
[1,3,5,7,9,11,13,15,17,19]
```

This definitely looks like the set of odd numbers!
Indeed, Leonhard Euler proved that the number of partitions into odd numbers,
and into distinct blocks, are the same.
This theorem, called *Euler's partition identity*, was historically
the first result on partitions.

Let's now discover the Rogers-Ramanujan identities.
For the first, the predicate $Q$ requires adjacent blocks to differ by
$2$:

```
*HaskPart> buildSet (differsBy 2) 20
[1,4,6,9,11,14,16,19]
```

This looks like the numbers equal to $1, 4$ modulo $5$, as the first
Rogers-Ramanujan identity claims. We can guess the second identity
similarly, now using ```andPreds``` to combine the predicate
```differsBy 2``` (which requires adjacent blocks to differ by at
least $2$) and ```biggerThan 1``` (which requires the smallest block
to be at least $2$):

```
*HaskPart> buildSet (andPreds [differsBy 2, biggerThan 1]) 20
[2,3,7,8,12,13,17,18]
```

These are the numbers $\leq 20$ which have residues $2, 3$ modulo $5$.

Proving these results is considerably harder, but the basic tool is
*generating functions*, discussed in Chapters 13-14 of Andrews, or
[my earlier blog post](https://hapax.github.io/mathematics/partitions/)
on partitions.
But we don't need to know any of this to discover the identities!
This is the big advantage of experimental mathematics, particularly on
a computer: with simple numerical evidence, our conjectures can very
quickly outstrip our theorems.

### Exercises

Here are some exercises lifted directly from Andrews.
Determine $S_Q$ (if it exists) for the following predicates:
1. Blocks differ by at least $2$ and no consecutive even numbers
   appear as summands.
2. Blocks differ by at least $2$ and no consecutive odd numbers
   appear as summands.
3. (1) and blocks are $\geq 3$.
4. (2) and blocks are $\geq 3$.
5. No block appears more than twice.
6. Blocks are $\geq 2$, and the difference between any odd block and
any smaller block is at least $3$.
7. No part appears more than twice, and if $m$ appears twice, $m \pm
   1$ are not blocks.
8. All blocks differ by at last $6$, neither $1$ nor $3$ appears as a
   block, and if $m$ and $m+6$ appear as blocks, then $m \neq 0, 1, 3$
   mod $6$.
9. Odd blocks are not repeated.
10. No block appears more than $3$ times, and if it appears more than
   once, $m+1$ appears at most once.
11. No block is $\leq 2$, blocks appear at most twice, and no blocks
    are consecutive.
12. No block is $\leq 2$, and no blocks are consecutive.
13. No block repeats, and no blocks are multiples of $3$.

### References

- [*Number theory*](https://archive.org/details/NumberTheory_862/page/n157)
  (1971), George Andrews.
