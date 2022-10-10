# Suited For
Software Engineer 1, Software Engineer 2 and Senior Software Engineer

## Difficulty Level
Medium

### Given Problem statement:

Given a Natural number N > 0 find all its factors that are prime numbers

#### Definition
1. Divisors:
  - Any number that divides another number.
      eg: Divisors of 12 are [1,2,3,4,6,12]
2. Prime numbers:
  - A prime number is a whole number greater than 1 whose only factors are 1 and itself. Numbers with exact two factors are prime numbers
      eg: Divisors of 11 are [1,11]
3. Whole numbers are all natural numbers including 0 e.g. 0, 1, 2, 3, 4


```js

Input:
        70
Output:
        prime divisors of 70 : [2,5,7]

Input:
        13
Output:
        prime divisors of 12 : [13]

Input:
        1
Output:
        prime divisors of 1 : []

```

### Approach:
The above problem can be solved by
```js
1. if n is even then loop and do n=n/2 until n is no longer divisible by 2. add 2 to the resultset.
2. loop "int i" from 3 to squareRoot(N) with step size = 2 .if n is divisible by "i" then loop and do n=n/"i" until n is no longer divisible by "i". add "i" to the resultset.
3. if the final value of n!=1 , it means n is another prime divisors of original input. add n to the resultset.
```

### Sample Solution:
```js
// Java program to print a given matrix in spiral form
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

class PrimeDivisorExample{

    // A function to print all prime factors
    // of a given number n
    public static Set<Integer>  getPrimeDivisors(int n)
    {
        Set<Integer> primeDivisors = new HashSet<>();
        // Eliminate all even divisors in one go
        while (n % 2 == 0) {
            primeDivisors.add(2);
            n /= 2;
        }

        // n must be odd at this point.  So we can
        // skip one element (Note i = i +2)
        for (int i = 3; i <= Math.sqrt(n); i += 2) {
            // Eliminate all divisors that are multiples of i
            while (n % i == 0) {
                primeDivisors.add(i);
                n = n/i;
            }
        }

        // This condition is to handle the case when
        // n is a prime number 
        if (n != 1)
            primeDivisors.add(n);
        return primeDivisors;
    }

    public static void printPrimeDivisors(int n)
    {
        System.out.println(String.format("prime factors or %s: %s",n, getPrimeDivisors(n)));
    }


    // Driver Code
    public static void main(String[] args) {
        // Initilaize scanner object to capture user input argument
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        printPrimeDivisors(n);;

    }
}

```

### Time Complexity:
Time complexity of the above solution is O(n^1/2).

### Alternate Recursive Approach:

brute force approach looping from 1 to n/2 and when a divisor is found, pass it to another method isPrime to check before populating the resultset.
Time complexity O(n) to find divisor and O(n) or O(n^1/2) to check if a number is prime.

If pre-computation is allowed, the above problem can be solved by leveraging Sieve of Eratosthenes and Least prime factor of numbers till n.
It will result in O(n) space and O(log n) time complexity


### Variation/Similar problems

Print all divisors of a given numbers
Print all factors of a given number
Print sum of all prime divisors of a natural number
Print sum of all divisors of a collection of natural number

### Solving Time
A strong SWE2 candidate should be able to converge on the brute force solution within 20 minutes and show progress towards optimal solution with hints.
A strong SSE candidate should be able to converge on the optimal solution with some handholding within 30 minutes.
A strong Staff candidate should be able to converge on the optimal solution within 15 minutes with no hints.

### Reference:
https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
https://www.geeksforgeeks.org/sieve-of-eratosthenes/
https://www.geeksforgeeks.org/least-prime-factor-of-numbers-till-n/
https://www.geeksforgeeks.org/prime-factorization-using-sieve-olog-n-multiple-queries/
