/*
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
*/

import java.util.*;
  
  public class Main{
  
  public static void main(String[] args) {
      Scanner scn = new Scanner(System.in);
      int t = scn.nextInt();
      for (int k = 1; k <= t; k++){
  
       int n = scn.nextInt();
       boolean isprime = true;
       for(int j=2; j*j <= n; j++){
           if(n%j==0){
               isprime=false;
               break;
           }
       }
       if(isprime==true){
           System.out.println("prime");
       }
       else {
           System.out.println("not prime");
       }
      }
   }
  }
