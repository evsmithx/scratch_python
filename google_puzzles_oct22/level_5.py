"""
 Write a function solution(str_n) which, given the string representation of an integer n, returns the sum of
 (floor(1*sqrt(2)) + floor(2*sqrt(2)) + ... + floor(n*sqrt(2))) as a string. That is, for every number i in the range
  1 to n, it adds up all of the integer portions of i*sqrt(2).

For example, if str_n was "5", the solution would be calculated as
floor(1*sqrt(2)) +
floor(2*sqrt(2)) +
floor(3*sqrt(2)) +
floor(4*sqrt(2)) +
floor(5*sqrt(2))
= 1+2+4+5+7 = 19
so the function would return "19".

str_n will be a positive integer between 1 and 10^100, inclusive. Since n can be very large (up to 101 digits!), using
just sqrt(2) and a loop won't work. Sometimes, it's easier to take a step back and concentrate not on what you have in
front of you, but on what you don't.


hmmm, okay
doing the multiplication and then throwing away part of the result is wasteful
expand out the sqrt and then see which bits are required...
1.4142135623730951
n * sqrt(2)
= n * 1 + n * 0.4 + n * 0.01 etc.
also we're summing over all n
sum of first term is n * (n+1) / 2
hmm, the above is misleading and might cause extra wholes
also I can't ignore terms just because they're below one - 0.9 + 0.9 gives me... oh but it's 0.9 + 0.09 for example,
that's fine

I have a vague feeling this would be easier in binary

If i can just express sqrt 2 as a series of fractions this would be fine
No, except that as above, I can't just not add terms that are less than 1

1.4142135623730951
2.8284271247461903
4.242640687119286  # 3 * 1 + 3 * 0.4
5.656854249492381  # 4 * 1 + 4 * 0.4 + 4 * 0.01
7.0710678118654755
8.485281374238571
9.899494936611665
11.313708498984761
12.727922061357857

str_n will be a positive integer between 1 and 10^100
so about 300 binary digits
this doesn't help. I still can't ignore the smallest decimal places
But I can in some cases?
100 * 3.123
100 * 3.124
are the same int
but 3 * 0.333 is not the same as 3 * 0.334
binary does help because it makes everything like multiplying by 10
101 * 1111
==    1 1 1 1
  1 1 1 1 0 0
1 0 0 1 0 1 1
but no, there's stil an adding step, sigh, that can create a chain of carrying that messes everything up

Most expansions are problematic, because they give a guarantee like "will be with epsilon of correct value". But for
my purposes int+epsilon and int-epsilon are meaningfully different

very roughly the answer is (n*(n-1)/2) * sqrt(2)
hmm, no less than that
because int() throws away stuff but never adds it
how much does it throw away?
maybe calculating i*sqrt(2) % 1 is easier
yes... this is promising
because if anything is too big you can definitely throw it away

100 * sqrt(2) mod 1, how to calculate
1.4142135623730951
can ignore 1.41, it's 0.421 etc
for 10 it would be 0.1421
for 1 it's 0.414
now binary would help...



"""
from math import sqrt

sqrt2 = sqrt(2)


def solution(s):
    s = int(s)
    total = sum((int(i * sqrt2) for i in range(s + 1)))  # correct, inefficient
    return str(total)


def solution2(s):
    s = int(s)
    total = sum((int(i * sqrt2) for i in range(s + 1)))  # correct, inefficient
    full_sum = (s * (s + 1) / 2) * sqrt2
    correct_excess = sum(((i * sqrt2) % 1 for i in range(s + 1)))

    extra2 = (s * (s + 1) / 2) * (sqrt2 % 1)  # too big
    test1 = (s * (s + 1) / 2) * (sqrt2 / 10 - 1)

    print("\t".join([str(x) for x in [s, total, full_sum, correct_excess, extra2, test1]]))
    return str(full_sum - correct_excess)


if __name__ == "__main__":
    import time

    small_tests = list(range(1, 20))
    test_cases = small_tests + ["77"]

    for tc in test_cases:
        tic = time.perf_counter()
        soln = solution(tc)
        toc = time.perf_counter()
        soln2 = solution2(tc)
        tac = time.perf_counter()
        # print(soln, toc - tic, soln2, tac - toc)

    for i in range(21):
        print(i, i * sqrt(2), (i * sqrt2) % 1)

"""
how to break this down?
for each multiple of sqrt2 we have a bit of extra residual
10res = 10 times the 1 residual minus 4
the 11 residual is 10 times the 1 residual (minus 4) plus the one residual.
does something like this help?
so the sum for 15 is 6 * 10 residual + 2 * 1 residual + 2 * 2 residual ... + 2 * 5 res + 1 * 6 res + ... 1 * 9res
in the numbers from 1-15 there are 6 tens, 2 ones, 2 twos... 1 nine
and the 20s?
20res is 2res * 10 - 8

Okay, so I can have a big lookup table and then a sum
size of table: 9 * number of digits, so 909.
That's not terrible...

Ugh I'm still going to overcount. Because xy is the x0 residual plus the y residual but this could go over 1.

Maybe dividing it by ten helps... I have a vague feeling this keeps everything to the right of the decimal point?

n * sqrt2 and n*(sqrt2 % 1) have the same figures after the decimal point, different before it
This seems helpful?
It's expected because the first can be broken down into n*(sqrt2 // 1) + n * (sqrt2 % 1), and obviously the first term
doesn't have a decimal part.

Maybe express it as 2 - (2 - sqrt2)?

I'm integrating a weird stepped function
1 1
2 2
3 4
4 5
How many times do we add an extra integer?
int(n * sqrt2) - n. not very helpful...

Mostly when n goes up by one then f goes up by one, about 1/sqrt2 of the time - could divide total by this?



"""
