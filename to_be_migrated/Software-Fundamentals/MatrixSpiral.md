# Suited For
Software Engineer 1, Software Engineer 2 and Senior Software Engineer

## Difficulty Level
Medium

### Given Problem statement:

Given a 2D array, print it in spiral form


```js
Input:
        1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output:
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10


Input:
        1   2   3   4  5   6
        7   8   9  10  11  12
        13  14  15 16  17  18
Output:
1 2 3 4 5 6 12 18 17 16 15 14 13 7 8 9 10 11
```

### Approach:
The above problem can be solved using four for loops which prints all the elements. Every for loop defines a single direction movement along with the matrix. The first for loop represents the movement from left to right, whereas the second crawl represents the movement from top to bottom, the third represents the movement from the right to left, and the fourth represents the movement from bottom to up.


### Sample Solution:

```js
// Java program to print a given matrix in spiral form
import java.io.*;

class GFG {
    // Function print matrix in spiral form
    static void spiralPrint(int m, int n, int a[][])
    {
        int i, k = 0, l = 0;
        /*  k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator
        */

        while (k < m && l < n) {
            // Print the first row from the remaining rows
            for (i = l; i < n; ++i) {
                System.out.print(a[k][i] + " ");
            }
            k++;

            // Print the last column from the remaining columns
            for (i = k; i < m; ++i) {
                System.out.print(a[i][n - 1] + " ");
            }
            n--;

            // Print the last row from the remaining rows */
            if (k < m) {
                for (i = n - 1; i >= l; --i) {
                    System.out.print(a[m - 1][i] + " ");
                }
                m--;
            }

            // Print the first column from the remaining columns */
            if (l < n) {
                for (i = m - 1; i >= k; --i) {
                    System.out.print(a[i][l] + " ");
                }
                l++;
            }
        }
    }

    // driver program
    public static void main(String[] args)
    {
        int R = 3;
        int C = 6;
        int a[][] = { { 1, 2, 3, 4, 5, 6 },
                      { 7, 8, 9, 10, 11, 12 },
                      { 13, 14, 15, 16, 17, 18 } };
        spiralPrint(R, C, a);
    }
}
```

### Time Complexity:
Time complexity of the above solution is O(mn).

### Alternate Recursive Approach:

The above problem can be solved by printing the boundary of the Matrix recursively. In each recursive call, we decrease the dimensions of the matrix.


### Variation/Similar problems

Print K'th element in spiral form of matrix
Print a matrix in a spiral form starting from a point
Print a given matrix in counter-clock wise spiral form
Print a given matrix in zigzag form
Print all the diagonals in a N X N matrix from left to right.

### Solving Time
Approx 30 - 45 mins

### Reference:
https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/

