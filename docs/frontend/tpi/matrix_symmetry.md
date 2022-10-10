# SWE 2 Check horizontal and vertical symmetry in binary matrix - Share with Candidate - Public

## Description

Given a 2D binary matrix of N rows and M columns. 

* The task is to check whether the matrix is horizontal symmetric, vertical symmetric, or both.
* The matrix is said to be horizontal symmetric if the first row is the same as the last row, the second row is the same as the second last row, and so on.
* The matrix is said to be vertical symmetric if the first column is the same as the last column, the second column is the same as the second last column, and so on. 
* Print “VERTICAL” if the matrix is vertically symmetric, “HORIZONTAL” if the matrix is vertically symmetric, “BOTH” if the matrix is vertical and horizontal symmetric, and “NOT SYMMETRIC” if not symmetric.


```
    Example:
    Input: N = 4 M = 4
    0 1 0 1
    0 0 0 0
    0 0 0 0
    0 1 0 1
    Output: Both

    In above example, First and fourth row are same and also second and third row , So it's Horizontal Symmetric.
    Similarly, First and fourth column are same and also second and third column are same, so its Vertical Symmetric as well.
      
    Input: 
    0 1 1
    0 0 1
    0 1 1    
    Output: HORIZONTAL                                   
```

## Preparation Instructions to be Shared in Advance

Use either codepen or glider.

Share with candidate:

# Intuit Internal ONLY Do Not Share with Candidate

Estimated time to complete: 15-20 minutes.

## Solution

### Approach:

There are different variants of solution depending on the approach the candidate takes. 

But here's one of the approaches:

The idea is to use pointers indicating two rows (or columns) and compare each cell of both the pointed rows (or columns). 

###  Solution
```
function checkHVSymmetry(arr, N, M) {

  // Initializing as both horizontal
  // and vertical symmetric.
  let horizontal = true;
  let vertical = true;

  // Checking for Horizontal Symmetry.
  // We compare first row with lasta
  // row, second row with second
  // last row and so on.
  for (let i = 0, k = N - 1; i < parseInt(N / 2, 10); i++, k--) {

    // Checking each cell of a column.
    for (let j = 0; j < M; j++) {
      // check if every cell is identical
      if (arr[i][j] != arr[k][j]) {
        horizontal = false;
        break;
      }
    }
  }

  // Checking for Vertical Symmetry. We compare
  // first column with last column, second xolumn
  // with second last column and so on.
  for (let i = 0, k = M - 1; i < parseInt(M / 2, 10); i++, k--) {

    // Checking each cell of a row.
    for (let j = 0; j < N; j++) {
      // check if every cell is identical
      if (arr[i][j] != arr[k][j]) {
        horizontal = false;
        break;
      }
    }
  }

  if (!horizontal && !vertical)
    return("NOT SYMMETRIC");

  else if (horizontal && !vertical)
    return("HORIZONTAL");

  else if (vertical && !horizontal)
   return("VERTICAL");

  else
    return("BOTH");
}

```
### Time complexity
O(N*M)
### How to Assess Candidate

Generally this problem should only be used for SWE2.

A strong candidate should be able to solve this relatively quickly, giving us indication of their logical thinking.

## Tags

`easy`, `phonescreen`, `swe2`, `frontend`
