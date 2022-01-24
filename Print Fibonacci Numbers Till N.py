"""
1. You've to print first n fibonacci numbers.
2. Take as input "n", the count of fibonacci numbers to print.
3. Print first n fibonacci numbers.

Constraints
1 <= n < 40

Format
Input
n

Output
0
1
1
2
3
5
8
.. first n fibonaccis

Example
Sample Input

10

Sample Output
0
1
1
2
3
5
8
13
21
34
"""


n=int(input())
#write your code here
a = 0
b = 1
for i in range(n):
  print(a)
  c = a + b
  a = b
  b = c
  
