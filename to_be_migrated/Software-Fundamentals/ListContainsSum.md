# List Contains Sum
### Write an algorithm for determining if a list contains a target sum



Estimated time to complete: 30 minutes

Tags: medium phonescreen sse backend java

## Description
Given a list of unsorted positive integers without duplicates 
return true if the list of integers contains 2 integers which 
when added together equal a target sum return false otherwise.

Show a few unit test cases to demonstrate your solution.

Please also create an interface and implementation for
your work and define the public api of your interface type
using javadoc. 

Bonus points if you drive the design of your interface 
from your tests, that is demonstrate Test Driven Design (TDD)
practices.

```
Example Test Case 1 

Inputs 
    List=[2,5,4] 
    TargetSum=6 

Result
    true  

Example Test Case 2

Inputs 
    List=[2,5,4] 
    TargetSum=7 

Result
    true

Example Test Case 3 

Inputs 
    List=[2,5,4] 
    TargetSum=3 

Result
    false
```

### Approach:

There are 3 standard solutions to the problem:
- brute force
- binary search
- hashset / hashtable

#### Brute Force

The brute force approach involves looping over the input list
considering each element the left operand and then for each
element of the list looping over the list again to obtain the
right operand. If the sum of the outer loop's left operand
plus the inner loop's right operand equal the target sum,
then the boolean result true can be returned. Otherwise,
once all elements have been considered the boolean result false
can be returned.  

#### Binary Search

First sort the input list, then iterate over the elements in the list
considering each element the left operand. Subtract the sum from
the candidate left operand to determine the target right operand
that needs to exist in the list to return true. Implement the binary
search algorithm and use it to determine if target right operand is
in the list, if it is, return true, otherwise if all elements 
are considered as a candidate left operand and no target right
operand can be found, then return false. 

#### Hashset / Hashtable

First add all elements of the list into an empty hashset.
Then iterate over each element of the list considering it as
a candidate left operand. Subtract the candidate left operand
from the target sum to get the target right operand. Check
if the target right operand exists in the seeded hashset,
if it does return true, otherwise after exhausting the list
of candidate left operands return false.

#### Note about TDD and unit testing

Part of this problem involves evaluating the candidate's understanding
of TDD, coding to an interface / api and understanding the difference
between an interface and an implementation. The ideal candidate
will start from the unit test method and materialize an appropriate
interface needed to solve the problem. Then they will create one of the above
solutions as an implementation of their interface. 

### Sample Solution:

```java
import java.io.*;
import java.util.*;
import java.util.stream.*;
import org.junit.*;
import org.junit.runner.*;


public class Solution {

  public interface SumFinder {
    
    /**
     * Checks if {@code targetSum} is in {@code unsortedList}. Unsorted list
     * may not be null or contain null elements. List consists only of positive integers
     * and may not contain duplicates. 
     */
    boolean listContainsSum(List<Integer> unsortedList, int targetSum);
  }
  
  private static final class BruteForceSumFinder implements SumFinder {
    
    /**
     * Checks if {@code targetSum} is in {@code unsortedList} in O(n^2) time.
     */    
    @Override
    public boolean listContainsSum(final List<Integer> unsortedList, final int targetSum) {
      
      for(int i = 0; i < unsortedList.size(); i++) {
        
        final int leftOperand = unsortedList.get(i);
        
        for(int j = 0; j < unsortedList.size(); j++) {
          
          if(i == j) {
            continue;
          }
          
          final int rightOperand = unsortedList.get(j);
          
          if((leftOperand + rightOperand) == targetSum) {
            return true;
          }
          
        }
      }
      
      return false;      
    }
    
  }
  
  private static final class BinarySearchSumFinder implements SumFinder {
    
    /**
     * Checks if {@code targetSum} is in {@code unsortedList} in O(n log n) time.
     */
    @Override
    public boolean listContainsSum(final List<Integer> unsortedList, final int targetSum) {
      
      final List<Integer> sortedList = unsortedList
        .stream()
        .filter(n -> n < targetSum)
        .sorted()
        .collect(Collectors.toList());
      
      for(final int leftOperand : sortedList) {
        final int targetRightOperand = targetSum - leftOperand;
        if(leftOperand == targetRightOperand) {
          continue;
        }
        if(binarySearch(sortedList, targetRightOperand)) {
          return true;
        }
      }          
      
      return false;      
    }
    
    private static boolean binarySearch(final List<Integer> sortedList, final int target) {
      int left = 0;
      int right = sortedList.size()-1;
      while(left <= right) {
        final int middle = left + ((right -1) / 2);
        final int elementToCheck = sortedList.get(middle);
        if(elementToCheck == target) {
          return true;
        }
        if(elementToCheck < target) {
          left = middle+1;
        } else {
          right = middle-1;
        }        
      }
      return false;
    }    
  }
  
  private static final class HashSetSumFinder implements SumFinder {
    
    /**
     * Checks if {@code targetSum} is in {@code unsortedList} in O(n) time.
     */
    @Override
    public boolean listContainsSum(final List<Integer> unsortedList, final int targetSum) {
      
      final Set<Integer> operands = new HashSet<>(unsortedList);
      for(final int leftOperand : operands) {
        final int rightOperand = targetSum - leftOperand;
        if(leftOperand == rightOperand) {
          continue;
        }
        if(operands.contains(rightOperand)) {
          return true;
        }
      }   
      
      return false;      
    }
    
  }  
  
  
  @Test
  public void testListContainsSum() {  
    // Ideally candidate would demonstrate testing against
    // the interface and substituting various implementations
    final SumFinder sumFinder = new HashSetSumFinder();
    final List<Integer> inputList = List.of(2,5,4);    
    
    Assert.assertTrue(sumFinder.listContainsSum(inputList, 6));
    Assert.assertTrue(sumFinder.listContainsSum(inputList, 7));
    Assert.assertFalse(sumFinder.listContainsSum(inputList, 3));
  }
  
  // Boilerplate main method if using Coderpad
  public static void main(String[] args) {
    JUnitCore.main("Solution");        
  }  
}
```

### Time Complexity:

#### Brute Force Solution
Time Complexity: O(n^2)

#### Binary Search Solution
Time Complexity: O(n log n)

#### Hashset Solution
Time Complexity: O(n)
 

### Alternate Approach:

Discussed above


### Variation/Similar problems

- Union and Intersection of two Linked Lists
- Intersection of two Sorted Linked Lists
- First common element in two linked lists

## Rubric / How to Assess Candidate

This problem assesses for the following:

- Ability to solve 3 implementations of the problem: brute force, binary search and hashset based
- Proper understanding of the distinction between interfaces and concrete implementations 
- Coding and testing to interfaces / public apis
- Proper understanding of unit test framework basics--ability to define assertions and model test cases / test inputs 
and expected results
- Javadoc with big O time cost complexity identified for each algorithm implementation

Ideal Candidate:
 
 - Starts with the design of the unit test and the test case declaration
 - Creates the interface to abstract the algorithm implementations
 - Can code 2-3 of the implementations and can correctly identify its time cost complexity
 
Above Average Candidate:

 - Knows how to write unit tests but perhaps doesn't demonstrate TDD
 - May initially skip the interface definition but with a bit of guidance knows how to define and implement the interface
 - Can get code the brute force solution and with some hints can arrive at a solution for either the hashset or binary
 tree solution
 
Average Candidate:

 - Typically able to code the brute force solution as a function, no attempt at an interface or class implementation
 - Usually needs some coaching on how to structure the unit test and make assertions

### Expected Solving Time

- Brute force solution should be solved in about 10-15 mins with unit tests and interface / impl class. 
- Additional 10-15 mins to tackle either the binary search or hashset approach. 

### Reference:
https://coderpad.io/PHDHKKAZ/playback#1920

