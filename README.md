# Kaprekar Constant

6174 is known as Kaprekar's constantafter the Indian mathematician D. R. Kaprekar. This number is notable for the following rule:

Take any four-digit number, using at least two different digits (leading zeros are allowed).
Arrange the digits in descending and then in ascending order to get two four-digit numbers, adding leading zeros if necessary.
Subtract the smaller number from the bigger number.
Go back to step 2 and repeat.
The above process, known as Kaprekar's routine, will always reach its fixed point, 6174, in at most 7 iterations.Once 6174 is reached, the process will continue yielding 7641 – 1467 = 6174. For example, choose 1495:

9541 – 1459 = 8082

8820 – 0288 = 8532

8532 – 2358 = 6174

7641 – 1467 = 6174

The only four-digit numbers for which Kaprekar's routine does not reach 6174 are repdigits such as 1111, which give the result 0000 after a single iteration. All other four-digit numbers eventually reach 6174 if leading zeros are used to keep the number of digits at 4.


The Math Behind the Fact:

Each number in the sequence uniquely determines the next number in the sequence. Since there are only finitely many possibilities, eventually the sequence must return to a number it hit before, leading to a cycle. So any starting number will give a sequence that eventually cycles. There can be many cycles; however, for length 4 strings in base 10, there happens to be 1 non-trivial cycle, and it has length 1 (involving the number 6174).

For more reference :

https://en.wikipedia.org/wiki/6174_(number)

https://youtu.be/0Hrmq6jkq0M
