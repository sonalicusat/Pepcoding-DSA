"""
1. You've to check whether a given number is prime or not.
2. Take a number "t" as input representing count of input numbers to be tested.
3. Take a number "n" as input "t" number of times.
4. For each input value of n, print "prime" if the number is prime and "not prime" otherwise.

Constraints
1 <= t <= 10000
2 <= n < 10^9

Format
Input
A number t
A number n
A number n
.. t number of times

Output
prime
not prime
not prime
.. t number of times

Example
Sample Input

5
13
2
3
4
5

Sample Output
prime
prime
prime
not prime
prime
"""

t=int(input())
for i in range(t):
    n = int(input())
    j = 2
    count = 0
    while j*j <= n:
        if n%j == 0:
            count +=1
        j += 1
    if count == 0:
        print("prime")
    else:
        print("not prime")
