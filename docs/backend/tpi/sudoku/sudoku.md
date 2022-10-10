# Sudoku Puzzle Solver

## Tags

Difficulty Options: `hard` 

Interview Type Options: `phonescreen` , `onsite`

Level Options: `swe2` `sse` `staff`  

Role Category Options: `backend` `frontend` `data` `fullstack`

## Share with Candidate - Public

### Description
Given a partially filled 9×9 2D array ‘grid[9][9]’, the goal is to assign digits (from 1 to 9) to the empty cells so that every row, column, and subgrid of size 3×3 contains exactly one instance of the digits from 1 to 9.

**Input:**
```
{
    {3, 0, 6, 5, 0, 8, 4, 0, 0},
    {5, 2, 0, 0, 0, 0, 0, 0, 0},
    {0, 8, 7, 0, 0, 0, 0, 3, 1},
    {0, 0, 3, 0, 1, 0, 0, 8, 0},
    {9, 0, 0, 8, 6, 3, 0, 0, 5},
    {0, 5, 0, 0, 9, 0, 6, 0, 0},
    {1, 3, 0, 0, 0, 0, 2, 5, 0},
    {0, 0, 0, 0, 0, 0, 0, 7, 4},
    {0, 0, 5, 2, 0, 6, 3, 0, 0}
 };
```
**Output:**
```
  3 1 6 5 7 8 4 9 2
  5 2 9 1 3 4 7 6 8
  4 8 7 6 2 9 5 3 1
  2 6 3 4 1 5 9 8 7
  9 7 4 8 6 3 1 2 5
  8 5 1 7 9 2 6 4 3
  1 3 8 9 4 7 2 5 6
  6 9 2 3 5 1 8 7 4
  7 4 5 2 8 6 3 1 9
```

### Preparation Instructions to be Shared in Advance
* You can use any programming language & online IDE of your choice


## Intuit Internal ONLY Do Not Share with Candidate
Estimated time to complete: 60 minutes

#### Common Clarification Questions/FAQ
`Any expected clarification questions from candidate for this interview`

**Good question as a good candidate, to discuss and think outloud approach to solve the puzzle prior to start implementation. List ways on how to identify and enter valid data in blank cell.**

### Solution

#### Approach
##### Naive Algorithm
 The Naive Algorithm is to generate all possible configurations of numbers from 1 to 9 to fill the empty cells. Try every configuration one by one until the correct configuration is found.

##### Backtracking Algorithm
 Like all other Backtracking problems, we can solve Sudoku by one by one assigning numbers to empty cells. Before assigning a number, we check whether it is safe to assign. We basically check that the same number is not present in the current row, current column and current 3X3 subgrid. After checking for safety, we assign the number, and recursively check whether this assignment leads to a solution or not. If the assignment doesn’t lead to a solution, then we try the next number for the current empty cell. And if none of the number (1 to 9) leads to a solution, we return false.

  Find row, col of an unassigned cell
  If there is none, return true
  For digits from 1 to 9
    a) If there is no conflict for digit at row, col
        assign digit to row, col and recursively try fill in rest of grid
    b) If recursion successful, return true
    c) Else, remove digit and try another
  If all digits have been tried and nothing worked, return false

#### Sample Solution

```js
/* A Backtracking program in
Java to solve Sudoku problem */
class Solution
{
   public static boolean isSafe(int[][] board,
                                int row, int col,
                                int num)
   {
       // row has the unique (row-clash)
       for (int d = 0; d < board.length; d++)
       {
           // if the number we are trying to
           // place is already present in
           // that row, return false;
           if (board[row][d] == num)
           {
               return false;
           }
       }
   
       // column has the unique numbers (column-clash)
       for (int r = 0; r < board.length; r++)
       {
           // if the number we are trying to
           // place is already present in
           // that column, return false;
   
           if (board[r][col] == num)
           {
               return false;
           }
       }
   
       // corresponding square has
       // unique number (box-clash)
       int sqrt = (int) Math.sqrt(board.length);
       int boxRowStart = row - row % sqrt;
       int boxColStart = col - col % sqrt;
   
       for (int r = boxRowStart;
                r < boxRowStart + sqrt; r++)
       {
           for (int d = boxColStart;
                    d < boxColStart + sqrt; d++)
           {
               if (board[r][d] == num)
               {
                   return false;
               }
           }
       }
   
           // if there is no clash, it's safe
       return true;
   }
   
   public static boolean solveSudoku(int[][] board, int n)
   {
       int row = -1;
       int col = -1;
       boolean isEmpty = true;
       for (int i = 0; i < n; i++)
       {
           for (int j = 0; j < n; j++)
           {
               if (board[i][j] == 0)
               {
                   row = i;
                   col = j;
   
                   // we still have some remaining
                   // missing values in Sudoku
                   isEmpty = false;
                   break;
               }
           }
           if (!isEmpty)
           {
               break;
           }
       }
   
       // no empty space left
       if (isEmpty)
       {
           return true;
       }
   
       // else for each-row backtrack
       for (int num = 1; num <= n; num++)
       {
           if (isSafe(board, row, col, num))
           {
               board[row][col] = num;
               if (solveSudoku(board, n))
               {
                   // print(board, n);
                   return true;
               }
               else
               {
                   board[row][col] = 0; // replace it
               }
           }
       }
       return false;
   }
   
   public static void print(int[][] board, int N)
   {
       // we got the answer, just print it
       for (int r = 0; r < N; r++)
       {
           for (int d = 0; d < N; d++)
           {
               System.out.print(board[r][d]);
               System.out.print(" ");
           }
           System.out.print("\n");
   
           if ((r + 1) % (int) Math.sqrt(N) == 0)
           {
               System.out.print("");
           }
       }
   }
   
   // Driver Code
   public static void main(String args[])
   {
       int[][] board = new int[][]
       {
               {3, 0, 6, 5, 0, 8, 4, 0, 0},
               {5, 2, 0, 0, 0, 0, 0, 0, 0},
               {0, 8, 7, 0, 0, 0, 0, 3, 1},
               {0, 0, 3, 0, 1, 0, 0, 8, 0},
               {9, 0, 0, 8, 6, 3, 0, 0, 5},
               {0, 5, 0, 0, 9, 0, 6, 0, 0},
               {1, 3, 0, 0, 0, 0, 2, 5, 0},
               {0, 0, 0, 0, 0, 0, 0, 7, 4},
               {0, 0, 5, 2, 0, 6, 3, 0, 0}
       };
       int N = board.length;
   
       if (solveSudoku(board, N))
       {
           print(board, N); // print solution
       }
       else
       {
           System.out.println("No solution");
       }
   }          
}
```

#### Time Complexity
O(n ^ m) where n is the number of possibilities for each square (i.e., 9 in classic Sudoku) and m is the number of spaces that are blank.

This can be seen by working backwards from only a single blank. If there is only one blank, then you have n possibilities that you must work through in the worst case. If there are two blanks, then you must work through n possibilities for the first blank and n possibilities for the second blank for each of the possibilities for the first blank. If there are three blanks, then you must work through n possibilities for the first blank. Each of those possibilities will yield a puzzle with two blanks that has n^2 possibilities.

This algorithm performs a depth-first search through the possible solutions. Each level of the graph represents the choices for a single square. The depth of the graph is the number of squares that need to be filled. With a branching factor of n and a depth of m, finding a solution in the graph has a worst-case performance of O(n ^ m).

### How to Assess Candidate / Expected Answer by Level
`Provide guidance in minutes / answer expectation for different roles`


Example: 
```
A strong SWE2 candidate should be able to converge on the brute force solution within 20 minutes and show progress towards optimal solution with hints.
A strong SSE candidate should be able to converge on the optimal solution with some handholding within 30 minutes.
A strong Staff candidate should be able to converge on the optimal solution within 15 minutes with no hints.

Also, questions that we would like the candidate to ask are also useful.
Edge cases identified, etc.
```

### Repeat above more approaches if there are alternatives

### Variation/Similar problems
* Program for Sudoku Generator
* Check if given Sudoku board configuration is valid or not

`Document other variations or similar problems, and the differences in expected solutions`

### References
- [Exhaustive recursion and backtracking](http://see.stanford.edu/materials/icspacs106b/H19-RecBacktrackExamples.pdf)
- [Sudoku Backtracking](https://www.geeksforgeeks.org/sudoku-backtracking-7/)
- [Sudoku Algorithm Complexity](https://stackoverflow.com/questions/15327376/algorithm-complexity-big-o-of-sudoku-solver)