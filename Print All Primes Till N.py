"""
1. You've to print all prime numbers between a range. 
2. Take as input "low", the lower limit of range.
3. Take as input "high", the higher limit of range.
4. For the range print all the primes numbers between low and high (both included).

Constraints
2 <= low < high < 10 ^ 6

Format
Input
low 
high

Output
n1
n2
.. all primes between low and high (both included)

Example
Sample Input

6 
24

Sample Output
7
11
13
17
19
23
"""

low=int(input())
high=int(input())
#write your code here
for i in range(low,high+1):
    j = 2
    count = 1
    while j*j <= i:
        if i%j == 0:
            count= 0
            break
        j+=1
    if count == 1:
        print(i)
    
