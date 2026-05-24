# DK's Puzzles

Here I solve puzzles (to test out new languages and for dayjob interviews, etc.)

## Fizzbuzz

Print numbers from 1 to n.
For multiples of 3 print "Fizz", for multiples of 5 print "Buzz", and for multiples of both 3 and 5 print "FizzBuzz".

**Solutions:** [Python](fizzbuzz/fizzbuzz.py) | [Clojure](fizzbuzz/fizzbuzz.clj)

## Fibonacci

Generate the Fibonacci sequence. Each number is the sum of the two preceding ones: 0, 1, 1, 2, 3, 5, 8, 13, ...
Given a number n, print the first n Fibonacci numbers.

**Solutions:** [Python](fibonacci/fibonacci.py) | [Clojure](fibonacci/fibonacci.clj)

## Bubble Sort

Sort a list of numbers using the bubble sort algorithm. Repeatedly step through the list, compare adjacent elements, and swap them if they are in the wrong order. The pass through the list is repeated until the list is sorted. Time complexity: O(n^2).

**Solutions:** [Python](bubblesort/bubblesort.py) | [Clojure](bubblesort/bubblesort.clj)

## Collatz Conjecture

Start with any positive integer n. If n is even, divide by 2. If n is odd, multiply by 3 and add 1. Repeat until you reach 1. Print the sequence and count the steps. The conjecture states that this always reaches 1, but nobody has proven it.

**Solutions:** [Python](collatz/collatz.py) | [Clojure](collatz/collatz.clj)

## Euclidean Distance

Calculate the straight-line distance between two points in 2D space using the Pythagorean formula: d = sqrt((x2-x1)^2 + (y2-y1)^2). Can be extended to 3D.

**Solutions:** [Python](distance/distance.py) | [Clojure](distance/distance.clj)

## Pi Approximation (Monte Carlo)

Estimate Pi using the Monte Carlo method. Generate random points in a unit square [0,1] x [0,1]. Count how many fall inside the unit circle (x^2 + y^2 <= 1). The ratio of points inside the circle to total points approximates Pi/4, so Pi ≈ 4 * (inside / total).

**Solutions:** [Python](pi/pi.py) | [Clojure](pi/pi.clj)
