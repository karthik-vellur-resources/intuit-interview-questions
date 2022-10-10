# Suited For
Software Engineer 1, Software Engineer 2 and Senior Software Engineer

## Difficulty Level
Low-Medium

### Given Problem statement:

Shuffle a deck of cards (generalization of "shuffle a given array")

#### Definition
Given an ordered or unordered array of numbers from 0 to 51, return an array with the same size, where the numbers are in a random order. This algorithm is expected to produce a different result with every run.

```js

Input:
        int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 
                   9, 10, 11, 12, 13, 14, 15, 
                   16, 17, 18, 19, 20, 21, 22, 
                   23, 24, 25, 26, 27, 28, 29, 
                   30, 31, 32, 33, 34, 35, 36, 
                   37, 38, 39, 40, 41, 42, 43, 
                   44, 45, 46, 47, 48, 49, 50,  
                   51};
Output:
        29 27 20 23 26 21 35 51 15 18 46 32 33 19 
        24 30 3 45 40 34 16 11 36 50 17 10 7 5 4 
        39 6 47 38 28 13 44 49 1 8 42 43 48 0 12 
        37 41 25 2 31 14 22
```

### Approach:
The above problem can be solved by
```js
1. First, fill the array with the values in order.
2. Go through the array and exchange each element 
   with the randomly chosen element in the range 
   from itself to the end.
```

### Sample Solution:
```js
// Java Code for Shuffle a deck of cards 
import java.util.Random; 
  
class Solution { 
      
    // Function which shuffle and print the array 
    public static void shuffle(int card[], int n) 
    { 
          
        Random rand = new Random(); 
          
        for (int i = 0; i < n; i++) 
        { 
            // Random for remaining positions. 
            int r = i + rand.nextInt(52 - i); 
              
             //swapping the elements 
             int temp = card[r]; 
             card[r] = card[i]; 
             card[i] = temp; 
               
        } 
    } 
       
    // Driver code 
    public static void main(String[] args)  
    { 
        // Array from 0 to 51 
        int a[] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 
                   9, 10, 11, 12, 13, 14, 15, 
                   16, 17, 18, 19, 20, 21, 22, 
                   23, 24, 25, 26, 27, 28, 29, 
                   30, 31, 32, 33, 34, 35, 36, 
                   37, 38, 39, 40, 41, 42, 43, 
                   44, 45, 46, 47, 48, 49, 50,  
                   51}; 
       
        shuffle(a, 52); 
       
        // Printing all shuffled elements of cards 
        for (int i = 0; i < 52; i ++) 
           System.out.print(a[i]+" "); 
          
    } 
} 
```

### Time Complexity:
Time complexity of the above solution is O(n).

### Alternate Approach:

It is possible to use directly the java.util.Collections.shuffle() method in Java. This would require converting the array to Java list and back to an array.

### Variation/Similar problems

Shuffle a given array using Fisher–Yates shuffle Algorithm
Shuffle or Randomize a list in Java

### Solving Time
A strong SWE1 or SWE2 candidate should be able to converge on a solution within 30 minutes with some hints.
A strong SSE candidate should be able to converge on the optimal solution within 15 minutes with no hints.

### Reference:

https://www.geeksforgeeks.org/shuffle-a-deck-of-cards-3/
https://www.geeksforgeeks.org/shuffle-a-given-array-using-fisher-yates-shuffle-algorithm/
https://www.geeksforgeeks.org/shuffle-or-randomize-a-list-in-java/
