# concert-planning


## Algorithmic exercise

Write a function that takes as input a list of integers L and an integer T,
and finds  if there exists a subset of L of size 3 such that the sum of
its elements is equal to the integer T.

## A variant

What if we want to find if there is any subset of size 1, 2, ..., size(L) that
sums to T ?

Answer:
* The case for size 1 is trivial.
* For size 2 we can check for each n in L if (T - n) is in L. This runs in O(N).
* For size 3, see the main problem definition above.
* For size 4, we can compute the sum of all pairs in L. Then check if each pair
is in this new hashset. Computing the pairs is O(N^2), there are N(N+1)/2 pairs.
  Looping through is then O(N^2). So this runs in O(N^2).
* For sizes 5 and up: I can't think of a tractable solution yet !